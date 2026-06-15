# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
selected_round: R13
selected_loop: 175
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: R13_special_cross_archetype_quality_review_after_false_positive_and_high_mae_passes
round_schedule_status: coverage_index_selected_not_sequential
round_sector_consistency: pass
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
fine_archetype_id: mixed_accounting_violation_trading_halt_regulatory_trust_price_validation_leaf_set
loop_objective: 4C_thesis_break_timing_test|4B_non_price_requirement_stress_test|counterexample_mining|holdout_validation|price_source_validation
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Current Calibrated Profile Assumption

```text
before_profile_id: e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id: e2r_2_0_baseline_reference
existing_axis_tested: hard_4c_thesis_break_routes_to_4c|full_4b_requires_non_price_evidence|price_only_blowoff_blocks_positive_stage
new_axis_proposed: r13_accounting_trust_reviewable_vs_irreversible_event_gate
```

이번 loop는 개별 Cxx 섹터를 다시 키우는 작업이 아니라, 회계·신뢰·거래정지·규제 신뢰 이벤트를 cross-archetype checkpoint로 묶는다. 핵심 질문은 하나다. **회계/신뢰 이벤트가 나오면 무조건 hard 4C인가, 아니면 거래재개·법원·감독결론·사업지속성·가격 reset을 확인한 뒤 staged watch로 내려야 하는가?**

## 2. Round / Large Sector / Canonical Archetype Scope

- R13은 L10 전용 cross-archetype checkpoint다.
- 허용 scope 중 이번 선택은 `R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION`이다.
- source canonical은 C23/C24/C25/C27/C30/C32에서 왔지만, 파일명과 metadata는 R13/L10만 사용한다.

## 3. Previous Coverage / Duplicate Avoidance Check

```text
previous_session_context: loop173 R13_STAGE2_FALSE_POSITIVE_REVIEW, loop174 R13_HIGH_MAE_GUARDRAIL completed
this_loop_scope: accounting_trust_price_validation
hard_duplicate_policy: canonical_archetype_id + symbol + trigger_type + entry_date 반복 금지
same_archetype_new_symbol_count: 8
same_archetype_new_trigger_family_count: 8
reused_case_count: 0
narrative_only_blocked_case_count: 1
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source: Songdaiki/stock-web
price_data_repo: https://github.com/Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
stock_web_manifest_max_date: 2026-02-20
```

Stock-Web manifest 기준 max_date 이후 가격은 만들지 않았다. 모든 정규 trigger row는 entry 이후 180 trading rows가 있고, SillaJen은 프로필상 entry date와 corporate-action candidate가 겹쳐 narrative-only로 내렸다.

## 5. Historical Eligibility Gate

| check | result |
|---|---:|
| calibration usable trigger rows | 8 |
| rows with required 30/90/180 MFE·MAE | 8 |
| rows with clean 180D corporate-action window | 8 |
| narrative-only / blocked | 1 |
| rows missing entry date or price | 0 |

## 6. Canonical Archetype Compression Map

| source canonical | source event type | R13 compression |
|---|---|---|
| C23/C24/C25 | bio approval/trial/device regulatory trust | accounting_or_regulatory_trust_break vs event-cap rebound |
| C27 | token/platform disclosure trust | disclosure trust break with rebound risk |
| C30 | construction safety/license trust | irreversible safety trust break |
| C32 | governance/control premium cleanup | event premium cap after legal gate |

## 7. Case Selection Summary

|symbol|company|source_Cxx|trigger_type|trigger_date|entry_date|entry_price|MFE90|MAE90|MFE180|MAE180|role|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|207940|삼성바이오로직스|C23|Stage4C|2018-11-14|2018-12-11|394000|6.6|-20.56|6.6|-38.71|counterexample|current_profile_correct|
|068270|셀트리온|C23|Stage2-Actionable|2022-03-11|2022-03-14|180500|6.93|-22.99|19.11|-22.99|positive|current_profile_4C_too_early|
|048260|오스템임플란트|C25|Stage2-Actionable|2022-04-27|2022-04-28|112000|29.37|-19.02|29.37|-19.02|positive|current_profile_4C_too_early|
|112040|위메이드|C27|Stage4C|2022-11-24|2022-11-25|39400|62.94|-27.41|62.94|-27.41|counterexample|current_profile_4C_too_late|
|294870|HDC현대산업개발|C30|Stage4C|2022-01-17|2022-01-17|18750|5.6|-29.87|5.6|-45.33|counterexample|current_profile_correct|
|086900|메디톡스|C25|Stage4C|2020-04-17|2020-04-20|133700|108.23|-24.38|108.23|-24.38|positive|current_profile_4C_too_early|
|102940|코오롱생명과학|C24|Stage4C|2019-05-29|2019-05-29|20000|53.0|-34.25|72.5|-34.25|positive|current_profile_4C_too_early|
|003920|남양유업|C32|Stage2|2024-01-04|2024-01-05|605000|6.61|-22.64|6.61|-23.14|counterexample|current_profile_false_positive|


## 8. Positive vs Counterexample Balance

```text
positive_case_count: 4
counterexample_count: 4
4B_watch_or_overlay_count: 5
4C_case_count: 4
current_profile_error_count: 6
```

Positive here means the new R13 guard improves classification versus a blunt hard-4C interpretation. Counterexample means the trust break or event-premium cap should remain dangerous and not be diluted into a generic Stage2 narrative.

## 9. Evidence Source Map

| symbol | event | evidence source |
|---|---|---|
| 207940 | Samsung BioLogics accounting ruling / trading halt / delisting review | FSC SFC final ruling; Yonhap KRX continued listing |
| 068270 | Celltrion SFC audit conclusion / limited sanctions | Celltrion notice; Yonhap FSC fine report |
| 048260 | Osstem embezzlement review and trading resumption | Yonhap KRX resumption report |
| 112040 | WEMIX exchange delisting and disclosure dispute | Asiae DAXA report; Korea JoongAng court-delisting report |
| 294870 | HDC collapse, chairman resignation, license/safety trust risk | Reuters; Korea JoongAng license suspension report |
| 086900 | Medytox MFDS action and court optionality | Yonhap; Korea Times court ban report |
| 102940 | Kolon Life Science Invossa mislabel/license cancellation | Yonhap; Korea Times Invossa price/trust report |
| 003920 | Namyang ownership dispute resolution | Yonhap; Pulse/MK legal dispute background |
| 215600 | SillaJen long-halt resumption | Yonhap; blocked by stock-web profile candidate date |

## 10. Price Data Source Map

| symbol | shard | profile | profile CA overlap judgment |
|---|---|---|---|
| 207940 | atlas/ohlcv_tradable_by_symbol_year/207/207940/2018.csv | atlas/symbol_profiles/207/207940.json | clean_180D_window; profile candidates ['2025-11-24'] do not overlap entry~D180 |
| 068270 | atlas/ohlcv_tradable_by_symbol_year/068/068270/2022.csv | atlas/symbol_profiles/068/068270.json | clean_180D_window; profile candidates ['2006-10-13', '2008-06-10', '2008-09-24', '2012-06-29', '2013-03-22', '2024-01-12'] do not overlap entry~D180 |
| 048260 | atlas/ohlcv_tradable_by_symbol_year/048/048260/2022.csv | atlas/symbol_profiles/048/048260.json | clean_180D_window; profile candidates ['2023-08-03'] do not overlap entry~D180 |
| 112040 | atlas/ohlcv_tradable_by_symbol_year/112/112040/2022.csv | atlas/symbol_profiles/112/112040.json | clean_180D_window; profile candidates ['2012-05-23', '2012-06-14', '2021-09-13', '2021-10-06'] do not overlap entry~D180 |
| 294870 | atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv | atlas/symbol_profiles/294/294870.json | clean_180D_window; profile candidates ['2020-03-26'] do not overlap entry~D180 |
| 086900 | atlas/ohlcv_tradable_by_symbol_year/086/086900/2020.csv | atlas/symbol_profiles/086/086900.json | clean_180D_window; profile candidates [] do not overlap entry~D180 |
| 102940 | atlas/ohlcv_tradable_by_symbol_year/102/102940/2019.csv | atlas/symbol_profiles/102/102940.json | clean_180D_window; profile candidates ['2018-01-25'] do not overlap entry~D180 |
| 003920 | atlas/ohlcv_tradable_by_symbol_year/003/003920/2024.csv | atlas/symbol_profiles/003/003920.json | clean_180D_window; profile candidates ['2024-11-20'] do not overlap entry~D180 |
| 215600 | atlas/ohlcv_tradable_by_symbol_year/215/215600/2022.csv | atlas/symbol_profiles/215/215600.json | blocked: candidate date 2022-10-13 overlaps entry |

## 11. Case-by-Case Trigger Grid

|case_id|symbol|company|trigger_outcome_label|current_profile_verdict|notes|
|---|---|---|---|---|---|
|r13acct175_207940_sbio_fsc_halt|207940|삼성바이오로직스|intentional_accounting_violation_trading_halt_drawdown_success|current_profile_correct|FSC intentional accounting violation ruling and KRX review/trading halt; post-resumption D180 MAE stayed deep while MFE stayed capped.|
|r13acct175_068270_celltrion_sfc_limited_sanction|068270|셀트리온|accounting_audit_conclusion_limited_sanction_uncertainty_clearance|current_profile_4C_too_early|SFC decision ended a long audit overhang; sanction existed, but no prosecution/referral-like hard thesis break, so hard 4C should be delayed.|
|r13acct175_048260_osstem_resume_after_embezzlement|048260|오스템임플란트|trading_resume_after_embezzlement_business_maintenance_positive|current_profile_4C_too_early|KRX allowed trading to resume after embezzlement review, implying business continuity; price path showed usable upside despite trust scar.|
|r13acct175_112040_wemade_wemix_delisting|112040|위메이드|token_circulation_disclosure_trust_break_delisting_high_volatility|current_profile_4C_too_late|DAXA delisting decision and court denial centered on token circulation disclosure/trust; large rebound did not erase initial trust-break MAE.|
|r13acct175_294870_hdc_collapse_license_trust|294870|HDC현대산업개발|fatal_collapse_safety_license_trust_break_persistent_drawdown|current_profile_correct|Fatal collapse and license-risk path produced low MFE and deep MAE; this is a real trust-break 4C, not merely price-only fear.|
|r13acct175_086900_medytox_mfds_event_cap|086900|메디톡스|mfds_license_suspension_event_cap_court_optionality_false_hard_4c|current_profile_4C_too_early|Regulatory trust break existed, but injunction/litigation optionality made immediate hard 4C too blunt after the first gap-down.|
|r13acct175_102940_kolon_invossa_mislabel|102940|코오롱생명과학|invossa_mislabel_license_cancellation_price_reset_rebound|current_profile_4C_too_early|Invossa mislabeling was a true trust break, but after heavy pre-event repricing, the 180D path showed event-cap rebound and high-MAE coexistence.|
|r13acct175_003920_namyang_control_cleanup_cap|003920|남양유업|supreme_court_control_change_cleanup_but_event_premium_cap|current_profile_false_positive|Governance cleanup resolved ownership uncertainty, but the control premium was largely event-capped and did not create durable Stage2 upside.|


## 12. Trigger-Level OHLC Backtest Tables

|trigger_id|entry_date|entry_price|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|peak_date|peak_price|drawdown_after_peak_pct|
|---|---|---|---|---|---|---|---|---|---|---|---|
|tr_r13acct175_01_207940|2018-12-11|394000|6.6|-14.85|6.6|-20.56|6.6|-38.71|2018-12-11|420000|-42.5|
|tr_r13acct175_02_068270|2022-03-14|180500|4.99|-13.85|6.93|-22.99|19.11|-22.99|2022-08-11|215000|-24.65|
|tr_r13acct175_03_048260|2022-04-28|112000|17.77|-15.18|29.37|-19.02|29.37|-19.02|2022-09-06|144900|-30.99|
|tr_r13acct175_04_112040|2022-11-25|39400|13.2|-27.41|62.94|-27.41|62.94|-27.41|2023-02-22|64200|-46.42|
|tr_r13acct175_05_294870|2022-01-17|18750|5.6|-28.0|5.6|-29.87|5.6|-45.33|2022-01-17|19800|-48.23|
|tr_r13acct175_06_086900|2020-04-20|133700|42.11|-24.38|108.23|-24.38|108.23|-24.38|2020-08-19|278400|-44.86|
|tr_r13acct175_07_102940|2019-05-29|20000|53.0|-6.25|53.0|-34.25|72.5|-34.25|2019-10-15|34500|-55.07|
|tr_r13acct175_08_003920|2024-01-05|605000|6.61|-9.09|6.61|-22.64|6.61|-23.14|2024-01-05|645000|-27.91|


## 13. Current Calibrated Profile Stress Test

1. Blunt hard 4C is correct for irreversible trust breaks like HDC safety/license damage and Samsung BioLogics post-halt drawdown.
2. Blunt hard 4C is too early for reviewable or event-capped trust breaks where legal review, trade resumption, product court optionality, or heavy pre-event repricing changes the price path.
3. Stage2 is false-positive for governance cleanup when the control premium is already capped and operating/FCF bridge is absent.
4. Price validation matters: SillaJen looks interesting but the profile candidate date overlaps entry, so the row is narrative-only.

## 14. Stage2 / Yellow / Green Comparison

Stage3-Green lateness is not the primary target in this R13 loop. The test is earlier in the pipeline: whether a trust event should be Stage4C, Stage4B-watch, or Stage2 reviewable reset. `green_lateness_ratio = not_applicable_r13_cross_check` is therefore used in trigger rows.

## 15. 4B Local vs Full-window Timing Audit

4B is used here as an event-cap overlay rather than a full exit signal. Namyang and Wemade illustrate event-premium caps; Osstem and Medytox show cases where a local trust shock did not erase full-window upside.

## 16. 4C Protection Audit

| class | symbols | interpretation |
|---|---|---|
| hard_4c_success | 207940, 294870 | trust break was not merely a cheap-entry opportunity; MFE stayed capped and MAE deepened |
| false_break / too early | 068270, 048260, 086900, 102940 | event review, court optionality, or pre-event reset made immediate hard 4C too blunt |
| thesis_break_watch_only | 112040, 003920 | token disclosure/governance event needed event-cap handling, not automatic positive rerating |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate: L10_ACCOUNTING_TRUST_PRICE_VALIDATION_GATE_V1
rule_scope: cross_archetype_r13
rule_logic:
  - If a trust event is irreversible and directly impairs license/order/safety/business continuity, allow hard 4C.
  - If the event is reviewable, already price-reset, or followed by trading-resumption/business-continuity validation, use Stage4B-watch or staged-entry rather than hard 4C.
  - If the event is governance cleanup/control transfer, require operating or cash-flow bridge before Stage2-Actionable.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: R13_ACCOUNTING_TRUST_PRICE_VALIDATION_GATE_V1
new_axis_proposed: r13_accounting_trust_reviewable_vs_irreversible_event_gate
```

## 19. Before / After Backtest Comparison

|profile_key|profile_id|hypothesis|changed_axes|eligible_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|verdict|
|---|---|---|---|---|---|---|---|---|---|
|P0|e2r_2_1_stock_web_calibrated_proxy|current global calibrated profile|none|8|34.91|-25.14|38.87|-29.4|mixed; hard 4C too blunt for reviewable trust events|
|P0b|e2r_2_0_baseline_reference|older baseline; more price/story sensitive|none|8|34.91|-25.14|38.87|-29.4|too many event-premium false positives|
|P1|cross_archetype_trust_event_cap_profile|adds reviewable-vs-irreversible trust event split|+trust_event_review_gate|8|34.91|-25.14|38.87|-29.4|improves false-hard-4C on Medytox/Kolon/Osstem|
|P2|accounting_trust_price_validation_profile|requires post-halt clean tradable entry and profile clean window|+price_validation_halt_gate|8|34.91|-25.14|38.87|-29.4|blocks SillaJen-type contaminated entry rows|
|P3|counterexample_guard_profile|hard blocks irreversible safety/disclosure trust breaks|+irreversible_trust_break_guard|8|34.91|-25.14|38.87|-29.4|keeps HDC/SamsungBio/Wemade as hard risk controls|


## 20. Score-Return Alignment Matrix

|symbol|MFE90|MAE90|MFE180|MAE180|profile verdict|alignment|
|---|---|---|---|---|---|---|
|207940|6.6|-20.56|6.6|-38.71|current_profile_correct|aligned|
|068270|6.93|-22.99|19.11|-22.99|current_profile_4C_too_early|residual_error|
|048260|29.37|-19.02|29.37|-19.02|current_profile_4C_too_early|residual_error|
|112040|62.94|-27.41|62.94|-27.41|current_profile_4C_too_late|residual_error|
|294870|5.6|-29.87|5.6|-45.33|current_profile_correct|aligned|
|086900|108.23|-24.38|108.23|-24.38|current_profile_4C_too_early|residual_error|
|102940|53.0|-34.25|72.5|-34.25|current_profile_4C_too_early|residual_error|
|003920|6.61|-22.64|6.61|-23.14|current_profile_false_positive|residual_error|


## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L10_POLICY_EVENT_CROSS_REDTEAM_MISC|R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|mixed_accounting_violation_trading_halt_regulatory_trust_price_validation_leaf_set|4|4|5|4|8|0|8|8|6|R13_ACCOUNTING_TRUST_PRICE_VALIDATION_GATE_V1|R13_ACCOUNTING_TRUST_PRICE_VALIDATION_GATE_V1|R13 accounting/trust scope now has dedicated loop175 rows; no Cxx sector row count mutation claimed|


## 22. Residual Contribution Summary

```text
new_independent_case_count: 8
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 8
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 8
tested_existing_calibrated_axes: hard_4c_thesis_break_routes_to_4c|full_4b_requires_non_price_evidence|price_only_blowoff_blocks_positive_stage
residual_error_types_found: hard_4c_too_early_after_reviewable_trust_event|hard_4c_too_late_for_irreversible_safety_or_disclosure_break|event_premium_stage2_false_positive|profile_candidate_price_contamination_block
new_axis_proposed: r13_accounting_trust_reviewable_vs_irreversible_event_gate
existing_axis_strengthened: hard_4c_thesis_break_routes_to_4c|full_4b_requires_non_price_evidence
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c_should_not_fire_before_review_gate_or_clean_trade_resumption_validation
existing_axis_kept: price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: L10_ACCOUNTING_TRUST_PRICE_VALIDATION_GATE_V1
canonical_archetype_rule_candidate: R13_ACCOUNTING_TRUST_PRICE_VALIDATION_GATE_V1
no_new_signal_reason: null
loop_contribution_label: residual_error_found
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated: 8 clean stock-web trigger rows with complete 30/90/180D MFE·MAE.
Non-validated: SillaJen is evidence-useful but blocked as narrative-only because the stock-web symbol profile flags a corporate-action candidate on the resumption/entry date.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,r13_accounting_trust_reviewable_vs_irreversible_event_gate,cross_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION,0,1,+1,"separates irreversible trust break from reviewable/event-capped trust shock","reduced false-hard-4C on Medytox/Kolon/Osstem while keeping HDC/SamsungBio hard risk","tr_r13acct175_01_207940|tr_r13acct175_02_068270|tr_r13acct175_03_048260|tr_r13acct175_04_112040|tr_r13acct175_05_294870|tr_r13acct175_06_086900|tr_r13acct175_07_102940|tr_r13acct175_08_003920",8,8,4,medium,r13_shadow_only,"not production; post-calibrated residual"
shadow_weight,profile_candidate_price_contamination_block,cross_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION,0,1,+1,"blocks trigger rows when profile corporate-action candidate overlaps entry window","SillaJen moved to narrative_only despite complete price path",tr_r13acct175_narr_215600,0,0,1,high,validation_shadow_only,"not production; row validation guard"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"r13acct175_207940_sbio_fsc_halt","symbol":"207940","company_name":"삼성바이오로직스","round":"R13","loop":"175","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"mixed_accounting_violation_trading_halt_regulatory_trust_price_validation_leaf_set","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"intentional_accounting_violation_trading_halt_drawdown_success","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_correct","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"FSC intentional accounting violation ruling and KRX review/trading halt; post-resumption D180 MAE stayed deep while MFE stayed capped."}
{"row_type":"trigger","trigger_id":"tr_r13acct175_01_207940","case_id":"r13acct175_207940_sbio_fsc_halt","symbol":"207940","company_name":"삼성바이오로직스","round":"R13","loop":"175","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"mixed_accounting_violation_trading_halt_regulatory_trust_price_validation_leaf_set","sector":"bio_c23_accounting_trust","primary_archetype":"C23","loop_objective":"4C_thesis_break_timing_test|4B_non_price_requirement_stress_test|counterexample_mining|holdout_validation|price_source_validation","trigger_type":"Stage4C","trigger_date":"2018-11-14","entry_date":"2018-12-11","entry_price":394000,"evidence_available_at_that_date":"public source available by trigger date or next-trading-day entry rule","evidence_source":"https://www.fsc.go.kr/eng/pr010101/22194?curPage=4&srchBeginDt=&srchCtgry=4&srchEndDt=&srchKey=&srchText= | https://en.yna.co.kr/view/AEN20181210010500320","stage2_evidence_fields":["none"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block","positioning_overheat"],"stage4c_evidence_fields":["accounting_or_trust_break","regulatory_rejection"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/207/207940/2018.csv","profile_path":"atlas/symbol_profiles/207/207940.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.6,"MFE_90D_pct":6.6,"MFE_180D_pct":6.6,"MFE_1Y_pct":6.6,"MFE_2Y_pct":null,"MAE_30D_pct":-14.85,"MAE_90D_pct":-20.56,"MAE_180D_pct":-38.71,"MAE_1Y_pct":-38.71,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2018-12-11","peak_price":420000,"drawdown_after_peak_pct":-42.5,"green_lateness_ratio":"not_applicable_r13_cross_check","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_or_accounting_trust_event_cap_audit","four_b_evidence_type":["legal_or_regulatory_block","positioning_overheat"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"intentional_accounting_violation_trading_halt_drawdown_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"seg_r13acct175_207940_2018-12-11","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"r13acct175_207940_sbio_fsc_halt","trigger_id":"tr_r13acct175_01_207940","symbol":"207940","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":65},"weighted_score_before":47.2,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":75},"weighted_score_after":44.8,"stage_label_after":"Stage4B","changed_components":["accounting_trust_risk_score","legal_or_contract_risk_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"R13 accounting/trust guard separates irreversible trust break from reviewable/event-capped trust overhang and validates post-halt entry using stock-web OHLC.","MFE_90D_pct":6.6,"MAE_90D_pct":-20.56,"score_return_alignment_label":"current_profile_correct","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"r13acct175_068270_celltrion_sfc_limited_sanction","symbol":"068270","company_name":"셀트리온","round":"R13","loop":"175","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"mixed_accounting_violation_trading_halt_regulatory_trust_price_validation_leaf_set","case_type":"false_break","positive_or_counterexample":"positive","best_trigger":"accounting_audit_conclusion_limited_sanction_uncertainty_clearance","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_4C_too_early","current_profile_verdict":"current_profile_4C_too_early","price_source":"Songdaiki/stock-web","notes":"SFC decision ended a long audit overhang; sanction existed, but no prosecution/referral-like hard thesis break, so hard 4C should be delayed."}
{"row_type":"trigger","trigger_id":"tr_r13acct175_02_068270","case_id":"r13acct175_068270_celltrion_sfc_limited_sanction","symbol":"068270","company_name":"셀트리온","round":"R13","loop":"175","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"mixed_accounting_violation_trading_halt_regulatory_trust_price_validation_leaf_set","sector":"bio_c23_accounting_resolution","primary_archetype":"C23","loop_objective":"4C_thesis_break_timing_test|4B_non_price_requirement_stress_test|counterexample_mining|holdout_validation|price_source_validation","trigger_type":"Stage2-Actionable","trigger_date":"2022-03-11","entry_date":"2022-03-14","entry_price":180500,"evidence_available_at_that_date":"public source available by trigger date or next-trading-day entry rule","evidence_source":"https://www.celltrion.com/en-us/company/notice/932 | https://en.yna.co.kr/view/AEN20220316010300320","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["legal_or_regulatory_block"],"stage4c_evidence_fields":["accounting_or_trust_break"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/068/068270/2022.csv","profile_path":"atlas/symbol_profiles/068/068270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.99,"MFE_90D_pct":6.93,"MFE_180D_pct":19.11,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-13.85,"MAE_90D_pct":-22.99,"MAE_180D_pct":-22.99,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-08-11","peak_price":215000,"drawdown_after_peak_pct":-24.65,"green_lateness_ratio":"not_applicable_r13_cross_check","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_or_accounting_trust_event_cap_audit","four_b_evidence_type":["legal_or_regulatory_block"],"four_c_protection_label":"false_break","trigger_outcome_label":"accounting_audit_conclusion_limited_sanction_uncertainty_clearance","current_profile_verdict":"current_profile_4C_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"seg_r13acct175_068270_2022-03-14","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"r13acct175_068270_celltrion_sfc_limited_sanction","trigger_id":"tr_r13acct175_02_068270","symbol":"068270","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":20,"execution_risk_score":35,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":65},"weighted_score_before":44.6,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":35,"execution_risk_score":35,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":0,"accounting_trust_risk_score":30},"weighted_score_after":48.2,"stage_label_after":"Stage4B","changed_components":["accounting_trust_risk_score","legal_or_contract_risk_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"R13 accounting/trust guard separates irreversible trust break from reviewable/event-capped trust overhang and validates post-halt entry using stock-web OHLC.","MFE_90D_pct":6.93,"MAE_90D_pct":-22.99,"score_return_alignment_label":"current_profile_4C_too_early","current_profile_verdict":"current_profile_4C_too_early"}
{"row_type":"case","case_id":"r13acct175_048260_osstem_resume_after_embezzlement","symbol":"048260","company_name":"오스템임플란트","round":"R13","loop":"175","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"mixed_accounting_violation_trading_halt_regulatory_trust_price_validation_leaf_set","case_type":"false_break","positive_or_counterexample":"positive","best_trigger":"trading_resume_after_embezzlement_business_maintenance_positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_4C_too_early","current_profile_verdict":"current_profile_4C_too_early","price_source":"Songdaiki/stock-web","notes":"KRX allowed trading to resume after embezzlement review, implying business continuity; price path showed usable upside despite trust scar."}
{"row_type":"trigger","trigger_id":"tr_r13acct175_03_048260","case_id":"r13acct175_048260_osstem_resume_after_embezzlement","symbol":"048260","company_name":"오스템임플란트","round":"R13","loop":"175","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"mixed_accounting_violation_trading_halt_regulatory_trust_price_validation_leaf_set","sector":"medical_c25_embezzlement_resumption","primary_archetype":"C25","loop_objective":"4C_thesis_break_timing_test|4B_non_price_requirement_stress_test|counterexample_mining|holdout_validation|price_source_validation","trigger_type":"Stage2-Actionable","trigger_date":"2022-04-27","entry_date":"2022-04-28","entry_price":112000,"evidence_available_at_that_date":"public source available by trigger date or next-trading-day entry rule","evidence_source":"https://en.yna.co.kr/view/AEN20220427003900320","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":["financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":["accounting_or_trust_break","capital_raise_or_overhang"],"stage4c_evidence_fields":["accounting_or_trust_break"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/048/048260/2022.csv","profile_path":"atlas/symbol_profiles/048/048260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.77,"MFE_90D_pct":29.37,"MFE_180D_pct":29.37,"MFE_1Y_pct":69.82,"MFE_2Y_pct":null,"MAE_30D_pct":-15.18,"MAE_90D_pct":-19.02,"MAE_180D_pct":-19.02,"MAE_1Y_pct":-19.02,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-09-06","peak_price":144900,"drawdown_after_peak_pct":-30.99,"green_lateness_ratio":"not_applicable_r13_cross_check","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_or_accounting_trust_event_cap_audit","four_b_evidence_type":["accounting_or_trust_break","capital_raise_or_overhang"],"four_c_protection_label":"false_break","trigger_outcome_label":"trading_resume_after_embezzlement_business_maintenance_positive","current_profile_verdict":"current_profile_4C_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"seg_r13acct175_048260_2022-04-28","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"r13acct175_048260_osstem_resume_after_embezzlement","trigger_id":"tr_r13acct175_03_048260","symbol":"048260","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":20,"execution_risk_score":35,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":65},"weighted_score_before":44.6,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":35,"execution_risk_score":35,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":0,"accounting_trust_risk_score":30},"weighted_score_after":48.2,"stage_label_after":"Stage4B","changed_components":["accounting_trust_risk_score","legal_or_contract_risk_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"R13 accounting/trust guard separates irreversible trust break from reviewable/event-capped trust overhang and validates post-halt entry using stock-web OHLC.","MFE_90D_pct":29.37,"MAE_90D_pct":-19.02,"score_return_alignment_label":"current_profile_4C_too_early","current_profile_verdict":"current_profile_4C_too_early"}
{"row_type":"case","case_id":"r13acct175_112040_wemade_wemix_delisting","symbol":"112040","company_name":"위메이드","round":"R13","loop":"175","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"mixed_accounting_violation_trading_halt_regulatory_trust_price_validation_leaf_set","case_type":"4C_late","positive_or_counterexample":"counterexample","best_trigger":"token_circulation_disclosure_trust_break_delisting_high_volatility","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_4C_too_late","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"DAXA delisting decision and court denial centered on token circulation disclosure/trust; large rebound did not erase initial trust-break MAE."}
{"row_type":"trigger","trigger_id":"tr_r13acct175_04_112040","case_id":"r13acct175_112040_wemade_wemix_delisting","symbol":"112040","company_name":"위메이드","round":"R13","loop":"175","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"mixed_accounting_violation_trading_halt_regulatory_trust_price_validation_leaf_set","sector":"platform_c27_token_disclosure_trust","primary_archetype":"C27","loop_objective":"4C_thesis_break_timing_test|4B_non_price_requirement_stress_test|counterexample_mining|holdout_validation|price_source_validation","trigger_type":"Stage4C","trigger_date":"2022-11-24","entry_date":"2022-11-25","entry_price":39400,"evidence_available_at_that_date":"public source available by trigger date or next-trading-day entry rule","evidence_source":"https://www.asiae.co.kr/en/article/2022112510445705836 | https://koreajoongangdaily.joins.com/2022/12/08/business/tech/Korea-Wemade-Wemix/20221208183614019.html","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","legal_or_regulatory_block"],"stage4c_evidence_fields":["accounting_or_trust_break","regulatory_rejection","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/112/112040/2022.csv","profile_path":"atlas/symbol_profiles/112/112040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.2,"MFE_90D_pct":62.94,"MFE_180D_pct":62.94,"MFE_1Y_pct":62.94,"MFE_2Y_pct":null,"MAE_30D_pct":-27.41,"MAE_90D_pct":-27.41,"MAE_180D_pct":-27.41,"MAE_1Y_pct":-27.41,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-02-22","peak_price":64200,"drawdown_after_peak_pct":-46.42,"green_lateness_ratio":"not_applicable_r13_cross_check","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_or_accounting_trust_event_cap_audit","four_b_evidence_type":["valuation_blowoff","legal_or_regulatory_block"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"token_circulation_disclosure_trust_break_delisting_high_volatility","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"seg_r13acct175_112040_2022-11-25","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"r13acct175_112040_wemade_wemix_delisting","trigger_id":"tr_r13acct175_04_112040","symbol":"112040","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":70,"legal_or_contract_risk_score":70,"dilution_cb_risk_score":0,"accounting_trust_risk_score":65},"weighted_score_before":30.4,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":80,"legal_or_contract_risk_score":70,"dilution_cb_risk_score":0,"accounting_trust_risk_score":75},"weighted_score_after":28.0,"stage_label_after":"Stage4C","changed_components":["accounting_trust_risk_score","legal_or_contract_risk_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"R13 accounting/trust guard separates irreversible trust break from reviewable/event-capped trust overhang and validates post-halt entry using stock-web OHLC.","MFE_90D_pct":62.94,"MAE_90D_pct":-27.41,"score_return_alignment_label":"current_profile_4C_too_late","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"case","case_id":"r13acct175_294870_hdc_collapse_license_trust","symbol":"294870","company_name":"HDC현대산업개발","round":"R13","loop":"175","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"mixed_accounting_violation_trading_halt_regulatory_trust_price_validation_leaf_set","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"fatal_collapse_safety_license_trust_break_persistent_drawdown","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_correct","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Fatal collapse and license-risk path produced low MFE and deep MAE; this is a real trust-break 4C, not merely price-only fear."}
{"row_type":"trigger","trigger_id":"tr_r13acct175_05_294870","case_id":"r13acct175_294870_hdc_collapse_license_trust","symbol":"294870","company_name":"HDC현대산업개발","round":"R13","loop":"175","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"mixed_accounting_violation_trading_halt_regulatory_trust_price_validation_leaf_set","sector":"construction_c30_safety_license_trust","primary_archetype":"C30","loop_objective":"4C_thesis_break_timing_test|4B_non_price_requirement_stress_test|counterexample_mining|holdout_validation|price_source_validation","trigger_type":"Stage4C","trigger_date":"2022-01-17","entry_date":"2022-01-17","entry_price":18750,"evidence_available_at_that_date":"public source available by trigger date or next-trading-day entry rule","evidence_source":"https://www.reuters.com/world/asia-pacific/skorea-builder-hdcs-chairman-steps-down-after-apartment-complex-collapse-2022-01-17/ | https://koreajoongangdaily.joins.com/2022/03/30/business/industry/HDC-Building-collapse-Gwangju/20220330162503613.html","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["accounting_or_trust_break","forced_liquidation_or_crash","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv","profile_path":"atlas/symbol_profiles/294/294870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.6,"MFE_90D_pct":5.6,"MFE_180D_pct":5.6,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-28.0,"MAE_90D_pct":-29.87,"MAE_180D_pct":-45.33,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-01-17","peak_price":19800,"drawdown_after_peak_pct":-48.23,"green_lateness_ratio":"not_applicable_r13_cross_check","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_or_accounting_trust_event_cap_audit","four_b_evidence_type":["legal_or_regulatory_block","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"fatal_collapse_safety_license_trust_break_persistent_drawdown","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"seg_r13acct175_294870_2022-01-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"r13acct175_294870_hdc_collapse_license_trust","trigger_id":"tr_r13acct175_05_294870","symbol":"294870","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":45,"valuation_repricing_score":0,"execution_risk_score":70,"legal_or_contract_risk_score":70,"dilution_cb_risk_score":0,"accounting_trust_risk_score":65},"weighted_score_before":34.0,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":45,"valuation_repricing_score":0,"execution_risk_score":80,"legal_or_contract_risk_score":70,"dilution_cb_risk_score":0,"accounting_trust_risk_score":75},"weighted_score_after":31.6,"stage_label_after":"Stage4B","changed_components":["accounting_trust_risk_score","legal_or_contract_risk_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"R13 accounting/trust guard separates irreversible trust break from reviewable/event-capped trust overhang and validates post-halt entry using stock-web OHLC.","MFE_90D_pct":5.6,"MAE_90D_pct":-29.87,"score_return_alignment_label":"current_profile_correct","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"r13acct175_086900_medytox_mfds_event_cap","symbol":"086900","company_name":"메디톡스","round":"R13","loop":"175","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"mixed_accounting_violation_trading_halt_regulatory_trust_price_validation_leaf_set","case_type":"false_break","positive_or_counterexample":"positive","best_trigger":"mfds_license_suspension_event_cap_court_optionality_false_hard_4c","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_4C_too_early","current_profile_verdict":"current_profile_4C_too_early","price_source":"Songdaiki/stock-web","notes":"Regulatory trust break existed, but injunction/litigation optionality made immediate hard 4C too blunt after the first gap-down."}
{"row_type":"trigger","trigger_id":"tr_r13acct175_06_086900","case_id":"r13acct175_086900_medytox_mfds_event_cap","symbol":"086900","company_name":"메디톡스","round":"R13","loop":"175","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"mixed_accounting_violation_trading_halt_regulatory_trust_price_validation_leaf_set","sector":"bio_c25_regulatory_trust_event_cap","primary_archetype":"C25","loop_objective":"4C_thesis_break_timing_test|4B_non_price_requirement_stress_test|counterexample_mining|holdout_validation|price_source_validation","trigger_type":"Stage4C","trigger_date":"2020-04-17","entry_date":"2020-04-20","entry_price":133700,"evidence_available_at_that_date":"public source available by trigger date or next-trading-day entry rule","evidence_source":"https://en.yna.co.kr/view/AEN20200618001053320 | https://www.koreatimes.co.kr/southkorea/health/20200522/court-lifts-sales-ban-on-meditoxin","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block"],"stage4c_evidence_fields":["regulatory_rejection","accounting_or_trust_break"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086900/2020.csv","profile_path":"atlas/symbol_profiles/086/086900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":42.11,"MFE_90D_pct":108.23,"MFE_180D_pct":108.23,"MFE_1Y_pct":108.23,"MFE_2Y_pct":null,"MAE_30D_pct":-24.38,"MAE_90D_pct":-24.38,"MAE_180D_pct":-24.38,"MAE_1Y_pct":-24.38,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-08-19","peak_price":278400,"drawdown_after_peak_pct":-44.86,"green_lateness_ratio":"not_applicable_r13_cross_check","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_or_accounting_trust_event_cap_audit","four_b_evidence_type":["legal_or_regulatory_block"],"four_c_protection_label":"false_break","trigger_outcome_label":"mfds_license_suspension_event_cap_court_optionality_false_hard_4c","current_profile_verdict":"current_profile_4C_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"seg_r13acct175_086900_2020-04-20","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"r13acct175_086900_medytox_mfds_event_cap","trigger_id":"tr_r13acct175_06_086900","symbol":"086900","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":45,"valuation_repricing_score":20,"execution_risk_score":35,"legal_or_contract_risk_score":60,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":48.8,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":45,"valuation_repricing_score":35,"execution_risk_score":35,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":0,"accounting_trust_risk_score":20},"weighted_score_after":50.6,"stage_label_after":"Stage4B","changed_components":["accounting_trust_risk_score","legal_or_contract_risk_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"R13 accounting/trust guard separates irreversible trust break from reviewable/event-capped trust overhang and validates post-halt entry using stock-web OHLC.","MFE_90D_pct":108.23,"MAE_90D_pct":-24.38,"score_return_alignment_label":"current_profile_4C_too_early","current_profile_verdict":"current_profile_4C_too_early"}
{"row_type":"case","case_id":"r13acct175_102940_kolon_invossa_mislabel","symbol":"102940","company_name":"코오롱생명과학","round":"R13","loop":"175","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"mixed_accounting_violation_trading_halt_regulatory_trust_price_validation_leaf_set","case_type":"false_break","positive_or_counterexample":"positive","best_trigger":"invossa_mislabel_license_cancellation_price_reset_rebound","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_4C_too_early","current_profile_verdict":"current_profile_4C_too_early","price_source":"Songdaiki/stock-web","notes":"Invossa mislabeling was a true trust break, but after heavy pre-event repricing, the 180D path showed event-cap rebound and high-MAE coexistence."}
{"row_type":"trigger","trigger_id":"tr_r13acct175_07_102940","case_id":"r13acct175_102940_kolon_invossa_mislabel","symbol":"102940","company_name":"코오롱생명과학","round":"R13","loop":"175","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"mixed_accounting_violation_trading_halt_regulatory_trust_price_validation_leaf_set","sector":"bio_c24_mislabel_trial_regulatory_trust","primary_archetype":"C24","loop_objective":"4C_thesis_break_timing_test|4B_non_price_requirement_stress_test|counterexample_mining|holdout_validation|price_source_validation","trigger_type":"Stage4C","trigger_date":"2019-05-29","entry_date":"2019-05-29","entry_price":20000,"evidence_available_at_that_date":"public source available by trigger date or next-trading-day entry rule","evidence_source":"https://en.yna.co.kr/view/AEN20190826008300320 | https://www.koreatimes.co.kr/business/companies/20190507/shares-of-kolon-life-science-plunge-60-on-invossa-fiasco","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block","positioning_overheat"],"stage4c_evidence_fields":["regulatory_rejection","safety_or_trial_failure","accounting_or_trust_break"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/102/102940/2019.csv","profile_path":"atlas/symbol_profiles/102/102940.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":53.0,"MFE_90D_pct":53.0,"MFE_180D_pct":72.5,"MFE_1Y_pct":160.0,"MFE_2Y_pct":null,"MAE_30D_pct":-6.25,"MAE_90D_pct":-34.25,"MAE_180D_pct":-34.25,"MAE_1Y_pct":-45.0,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2019-10-15","peak_price":34500,"drawdown_after_peak_pct":-55.07,"green_lateness_ratio":"not_applicable_r13_cross_check","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_or_accounting_trust_event_cap_audit","four_b_evidence_type":["legal_or_regulatory_block","positioning_overheat"],"four_c_protection_label":"false_break","trigger_outcome_label":"invossa_mislabel_license_cancellation_price_reset_rebound","current_profile_verdict":"current_profile_4C_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"seg_r13acct175_102940_2019-05-29","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"r13acct175_102940_kolon_invossa_mislabel","trigger_id":"tr_r13acct175_07_102940","symbol":"102940","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":45,"valuation_repricing_score":20,"execution_risk_score":35,"legal_or_contract_risk_score":60,"dilution_cb_risk_score":0,"accounting_trust_risk_score":65},"weighted_score_before":41.0,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":45,"valuation_repricing_score":35,"execution_risk_score":35,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":0,"accounting_trust_risk_score":30},"weighted_score_after":49.4,"stage_label_after":"Stage4B","changed_components":["accounting_trust_risk_score","legal_or_contract_risk_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"R13 accounting/trust guard separates irreversible trust break from reviewable/event-capped trust overhang and validates post-halt entry using stock-web OHLC.","MFE_90D_pct":53.0,"MAE_90D_pct":-34.25,"score_return_alignment_label":"current_profile_4C_too_early","current_profile_verdict":"current_profile_4C_too_early"}
{"row_type":"case","case_id":"r13acct175_003920_namyang_control_cleanup_cap","symbol":"003920","company_name":"남양유업","round":"R13","loop":"175","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"mixed_accounting_violation_trading_halt_regulatory_trust_price_validation_leaf_set","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"supreme_court_control_change_cleanup_but_event_premium_cap","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Governance cleanup resolved ownership uncertainty, but the control premium was largely event-capped and did not create durable Stage2 upside."}
{"row_type":"trigger","trigger_id":"tr_r13acct175_08_003920","case_id":"r13acct175_003920_namyang_control_cleanup_cap","symbol":"003920","company_name":"남양유업","round":"R13","loop":"175","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"mixed_accounting_violation_trading_halt_regulatory_trust_price_validation_leaf_set","sector":"governance_c32_control_premium_cleanup","primary_archetype":"C32","loop_objective":"4C_thesis_break_timing_test|4B_non_price_requirement_stress_test|counterexample_mining|holdout_validation|price_source_validation","trigger_type":"Stage2","trigger_date":"2024-01-04","entry_date":"2024-01-05","entry_price":605000,"evidence_available_at_that_date":"public source available by trigger date or next-trading-day entry rule","evidence_source":"https://en.yna.co.kr/view/AEN20240104007400320 | https://pulse.mk.co.kr/news/english/10660553","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":["low_red_team_risk"],"stage4b_evidence_fields":["explicit_event_cap","control_premium_or_event_premium"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003920/2024.csv","profile_path":"atlas/symbol_profiles/003/003920.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.61,"MFE_90D_pct":6.61,"MFE_180D_pct":6.61,"MFE_1Y_pct":19.01,"MFE_2Y_pct":null,"MAE_30D_pct":-9.09,"MAE_90D_pct":-22.64,"MAE_180D_pct":-23.14,"MAE_1Y_pct":-90.69,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-05","peak_price":645000,"drawdown_after_peak_pct":-27.91,"green_lateness_ratio":"not_applicable_r13_cross_check","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_or_accounting_trust_event_cap_audit","four_b_evidence_type":["explicit_event_cap","control_premium_or_event_premium"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"supreme_court_control_change_cleanup_but_event_premium_cap","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"seg_r13acct175_003920_2024-01-05","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"r13acct175_003920_namyang_control_cleanup_cap","trigger_id":"tr_r13acct175_08_003920","symbol":"003920","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":30,"valuation_repricing_score":45,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":61.0,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":30,"valuation_repricing_score":45,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_after":58.6,"stage_label_after":"Stage2","changed_components":["accounting_trust_risk_score","legal_or_contract_risk_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"R13 accounting/trust guard separates irreversible trust break from reviewable/event-capped trust overhang and validates post-halt entry using stock-web OHLC.","MFE_90D_pct":6.61,"MAE_90D_pct":-22.64,"score_return_alignment_label":"current_profile_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"narrative_only","case_id":"r13acct175_215600_sillajen_resumption_profile_blocked","symbol":"215600","company_name":"신라젠","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"trading_resumption_after_long_halt_profile_candidate_block","reason":"profile_corporate_action_candidate_dates_include_entry_date_2022-10-13; do not emit trigger row despite useful R13 accounting/trust evidence","price_source":"Songdaiki/stock-web","profile_path":"atlas/symbol_profiles/215/215600.json","usage":"not_weight_calibration","evidence_source":"https://en.yna.co.kr/view/AEN20221013003851320","MFE_30D_pct":52.53,"MAE_30D_pct":-22.76,"MFE_90D_pct":52.53,"MAE_90D_pct":-44.7,"MFE_180D_pct":52.53,"MAE_180D_pct":-54.79}
{"row_type":"residual_contribution","round":"R13","loop":"175","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","new_independent_case_count":8,"reused_case_count":0,"new_symbol_count":8,"new_trigger_family_count":8,"tested_existing_calibrated_axes":["hard_4c_thesis_break_routes_to_4c","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["hard_4c_too_early_after_reviewable_trust_event","hard_4c_too_late_for_irreversible_safety_or_disclosure_break","event_premium_stage2_false_positive","profile_candidate_price_contamination_block"],"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<symbol>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<symbol>.json.

### Rules
- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks
1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output
- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R13
completed_loop = 175
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = R13_special_cross_archetype_quality_review_after_false_positive_and_high_mae_passes
next_recommended_archetypes = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|C18_CONSUMER_EXPORT_CHANNEL_REORDER|C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- No-repeat index: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- Event evidence URLs are embedded in each machine-readable trigger row.

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 8
calibration_usable_trigger_count: 8
representative_trigger_count: 8
new_weight_evidence_candidate_count: 8
guardrail_candidate_count: 8
narrative_only_or_rejected_count: 1
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
