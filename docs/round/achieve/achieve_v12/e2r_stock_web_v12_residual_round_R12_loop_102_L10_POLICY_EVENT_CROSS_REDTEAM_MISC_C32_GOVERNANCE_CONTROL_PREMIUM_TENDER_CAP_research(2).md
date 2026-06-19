# E2R Stock-Web v12 Residual Research — R12 / C32 Governance Control Premium Tender Cap Loop 102

## 0. Research metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R12_loop_102_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
completed_round: R12
completed_loop: 102
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 2 quality_repair_after_local_priority0_priority1_fill
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: C32_CONTROL_RIGHTS_RESTRUCTURING_WITHDRAWAL_AND_RECOVERY_EXCEPTION_FILTER_V3
deep_sub_archetype_id: C32_DEEP_KOREA_ZINC_HYBE_DOOSAN_SK_TWAY_CONTROL_RIGHTS_RECOVERY_VS_SPIKE_FADE
primary_price_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
stock_agent_code_accessed: false
stock_agent_code_patch_written: false
```

## 1. Selection rationale

The execution prompt requires `coverage_index_first`, not mechanical R1→R13 rotation. Published C32 coverage is already above the minimum band, so this run is a Priority 2 quality-repair loop rather than a minimum-fill loop. The local sequence has already produced C32 loop100 and loop101, then R13 and C31 checks. This loop returns to C32 with a **new trigger-family/date set** focused on post-announcement recovery exceptions versus governance-label spike fade.

Prior C32 loops covered Korea Zinc tender/counteroffer, SM/Kakao tender, Hankook & Company tender, Hanmi-OCI vote, Namyang control transfer, Hanjin KAL proxy, DB HiTek activism, KT&G activism, Doosan initial restructuring, SK merger approval, and T'way initial management-rights push. This loop uses a second-order event frame:

```text
Korea Zinc share-sale withdrawal after tender battle
Doosan revised restructuring / post-shock recovery
HYBE-ADOR management-rights dispute
SK Innovation merger effective date follow-through
Kakao founder arrest / SM takeover trust-break comparator
```

Research question:

> In C32, should the engine promote a governance/restructuring/control-rights headline, or should it ask whether the event creates a verified control-premium, vote, transaction, cash-flow, or post-shock recovery bridge?

## 2. Stock-Web price source confirmation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
```

All trigger rows use actual local Stock-Web 1D OHLCV shards already present in the working session. Each row includes 30D/90D/180D MFE and MAE. Entry date is the trigger date or the next tradable close. All entry windows have at least 180 tradable rows before the stock-web manifest max date.

## 3. Public event frame

| symbol | event source | use |
|---:|---|---|
| 010130 | https://www.reuters.com/markets/commodities/korea-zinc-withdraws-plan-issue-18-bln-new-shares-2024-11-13/ | Korea Zinc withdrew a planned new-share issue after investor/regulatory backlash during the MBK/Young Poong control battle; this is a verified control-premium recovery exception, not a generic governance label. |
| 241560 | https://www.kedglobal.com/corporate-restructuring/newsView/ked202410210006 | Doosan resumed the Bobcat-Robotics restructuring with a revised ratio after minority-holder criticism; Bobcat became a post-shock recovery control. |
| 000150 | https://www.kedglobal.com/corporate-restructuring/newsView/ked202410210006 | Doosan holdco repriced after revised restructuring terms; the verified bridge is group-control simplification after valuation-transfer backlash. |
| 034020 | https://www.kedglobal.com/corporate-restructuring/newsView/ked202410210006 | Doosan Enerbility’s revised restructuring terms created a recovery exception versus the initial share-exchange discount. |
| 352820 | https://www.reuters.com/lifestyle/record-giant-hybe-audits-newjeans-label-infighting-returns-k-pop-2024-04-24/ | HYBE audit/ADOR breakaway dispute was a true management-rights event but lacked a positive control-premium bridge for HYBE shareholders at the trigger. |
| 454910 | https://www.kedglobal.com/corporate-restructuring/newsView/ked202410210006 | Even after revised ratio, Doosan Robotics remained the high-valuation receiving asset; the governance headline needed local 4B watch rather than positive C32 rerating. |
| 096770 | https://www.reuters.com/markets/deals/sk-innovation-shareholders-approve-merger-plan-with-sk-es-yonhap-reports-2024-08-27/ | SK Innovation-SK E&S merger was approved/effective, but SK On/battery-loss and restructuring execution risk still capped near-term rerating. |
| 035720 | https://www.reuters.com/technology/south-korean-court-approves-arrest-warrant-kakao-founder-2024-07-22/ | Kakao founder arrest in the SM takeover stock-manipulation case was a governance/trust-control event, but the issuer bridge remained weak and the row is a local 4B/trust-break watch rather than positive C32 rerating. |


## 4. Novelty / no-repeat check

```text
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
local_previous_C32_loops = R12_loop_100, R12_loop_101
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
hard_duplicate_count = 0
new_trigger_family_count = 8
same_archetype_new_symbol_count = 1
reused_symbol_with_new_trigger_family_count = 7
minimum_new_independent_case_ratio = pass
```

This loop intentionally reuses some C32 universe names because governance-control events are episodic, but no row repeats the prior C32 exact `symbol + trigger_type + entry_date + evidence_family` key. HYBE is a new C32 symbol in the local C32 set; Korea Zinc, Doosan, SK, and T'way names are reused only with later trigger families and new entry dates.

## 5. Case selection summary

| case_id | symbol | company | role | trigger_type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | current_profile_verdict |
|---|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| C32-L102-01-010130-20241113 | 010130 | 고려아연 | positive | Stage3-Yellow | 2024-11-13 | 981000.0 | 145.36 | -8.87 | 145.36 | -29.05 | 145.36 | -34.45 | current_profile_missed_recovery_exception |
| C32-L102-02-241560-20241021 | 241560 | 두산밥캣 | positive | Stage2-Actionable | 2024-10-21 | 43550.0 | 1.49 | -17.11 | 22.62 | -17.11 | 69.69 | -17.11 | current_profile_missed_recovery_exception |
| C32-L102-03-000150-20241021 | 000150 | 두산 | positive | Stage3-Yellow | 2024-10-21 | 207000.0 | 18.36 | -10.48 | 86.47 | -10.48 | 237.92 | -10.48 | current_profile_missed_recovery_exception |
| C32-L102-04-034020-20241021 | 034020 | 두산에너빌리티 | positive | Stage2-Actionable | 2024-10-21 | 20650.0 | 10.41 | -6.30 | 49.64 | -18.11 | 249.64 | -18.11 | current_profile_missed_recovery_exception |
| C32-L102-05-352820-20240424 | 352820 | HYBE | counterexample | Stage4B | 2024-04-24 | 211000.0 | 2.84 | -11.99 | 2.84 | -24.17 | 7.35 | -25.26 | current_profile_false_positive_or_4B_too_late |
| C32-L102-06-454910-20241021 | 454910 | 두산로보틱스 | counterexample | Stage4B | 2024-10-21 | 71600.0 | 9.22 | -15.36 | 9.22 | -30.38 | 9.22 | -44.76 | current_profile_false_positive_or_4B_too_late |
| C32-L102-07-096770-20241101 | 096770 | SK이노베이션 | counterexample | Stage4B | 2024-11-01 | 121800.0 | 1.81 | -24.63 | 15.11 | -24.63 | 15.11 | -33.66 | current_profile_false_positive_or_4B_too_late |
| C32-L102-08-035720-20240723 | 035720 | 카카오 | counterexample | Stage4B | 2024-07-23 | 38850.0 | 6.69 | -9.01 | 21.24 | -16.22 | 21.24 | -16.22 | current_profile_false_positive_or_4B_too_late |


## 6. Aggregate / score-return alignment

```json
{
  "row_type": "aggregate_summary",
  "selected_round": "R12",
  "selected_loop": 102,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
  "fine_archetype_id": "C32_CONTROL_RIGHTS_RESTRUCTURING_WITHDRAWAL_AND_RECOVERY_EXCEPTION_FILTER_V3",
  "new_independent_case_count": 8,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 1,
  "same_archetype_new_trigger_family_count": 8,
  "new_trigger_family_count": 8,
  "calibration_usable_trigger_count": 8,
  "representative_trigger_count": 8,
  "positive_case_count": 4,
  "counterexample_count": 4,
  "stage4b_case_count": 4,
  "stage4c_case_count": 0,
  "current_profile_error_count": 7,
  "source_proxy_only_count": 0,
  "evidence_url_pending_count": 0,
  "pos_avg_MFE90": 76.0224,
  "pos_avg_MAE90": -18.6883,
  "pos_avg_MFE180": 175.6529,
  "pos_avg_MAE180": -20.039,
  "counter_avg_MFE90": 12.1009,
  "counter_avg_MAE90": -23.8486,
  "counter_avg_MFE180": 13.2265,
  "counter_avg_MAE180": -29.9753,
  "do_not_propose_new_weight_delta": false,
  "sector_specific_rule_candidate": true,
  "canonical_archetype_rule_candidate": true,
  "loop_contribution_label": "canonical_archetype_rule_candidate"
}
```

Interpretation:

- Positive controls have avg MFE90 / MAE90 of `76.0224 / -18.6883` and avg MFE180 / MAE180 of `175.6529 / -20.039`.
- Counterexamples have avg MFE90 / MAE90 of `12.1009 / -23.8486` and avg MFE180 / MAE180 of `13.2265 / -29.9753`.
- The split is not “governance event good vs bad.” It is **bridge-aware**. Korea Zinc and Doosan post-shock entries had a concrete recovery/control-premium bridge. HYBE, Doosan Robotics, SK Innovation, and Kakao had management/control/restructuring/trust-break labels but weaker issuer-level bridge or deep high-MAE path.

## 7. Price data source map

| symbol | shard path | profile path |
|---:|---|---|
| 010130 | `atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv` | `atlas/symbol_profiles/010/010130.json` |
| 241560 | `atlas/ohlcv_tradable_by_symbol_year/241/241560/2024.csv` | `atlas/symbol_profiles/241/241560.json` |
| 000150 | `atlas/ohlcv_tradable_by_symbol_year/000/000150/2024.csv` | `atlas/symbol_profiles/000/000150.json` |
| 034020 | `atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv` | `atlas/symbol_profiles/034/034020.json` |
| 352820 | `atlas/ohlcv_tradable_by_symbol_year/352/352820/2024.csv` | `atlas/symbol_profiles/352/352820.json` |
| 454910 | `atlas/ohlcv_tradable_by_symbol_year/454/454910/2024.csv` | `atlas/symbol_profiles/454/454910.json` |
| 096770 | `atlas/ohlcv_tradable_by_symbol_year/096/096770/2024.csv` | `atlas/symbol_profiles/096/096770.json` |
| 035720 | `atlas/ohlcv_tradable_by_symbol_year/035/035720/2024.csv` | `atlas/symbol_profiles/035/035720.json` |


## 8. Machine-readable trigger rows JSONL

```jsonl
{"MAE_180D_pct": -34.4546, "MAE_30D_pct": -8.8685, "MAE_90D_pct": -29.052, "MFE_180D_pct": 145.3619, "MFE_30D_pct": 145.3619, "MFE_90D_pct": 145.3619, "aggregate_group_role": "representative", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32-L102-01-010130-20241113", "classification": "positive", "company": "고려아연", "component_score_breakdown": {"control_premium_specificity": 78, "high_MAE_overlay": true, "information_quality": 70, "issuer_level_bridge": 75, "minority_holder_risk": 35, "price_path_alignment": 72, "shareholder_vote_or_transaction_clarity": 68, "valuation_transfer_risk": 38}, "corporate_action_window_status": "not_contaminated_in_30_90_180D_calibration_window_by_this_loop_check", "current_profile_error": true, "current_profile_verdict": "current_profile_missed_recovery_exception", "dedupe_for_aggregate": "representative_candidate", "deep_sub_archetype_id": "C32_DEEP_KOREA_ZINC_HYBE_DOOSAN_SK_TWAY_CONTROL_RIGHTS_RECOVERY_VS_SPIKE_FADE", "do_not_count_as_new_case": false, "entry_date": "2024-11-13", "entry_price": 981000.0, "entry_rule": "target_trigger_date_or_next_tradable_close", "evidence_family": "korea_zinc_share_sale_withdrawal_after_tender_battle_recovery_exception", "evidence_timing": "Korea Zinc withdrew a planned new-share issue after investor/regulatory backlash during the MBK/Young Poong control battle; this is a verified control-premium recovery exception, not a generic governance label.", "evidence_url": "https://www.reuters.com/markets/commodities/korea-zinc-withdraws-plan-issue-18-bln-new-shares-2024-11-13/", "evidence_url_pending": false, "fine_archetype_id": "C32_CONTROL_RIGHTS_RESTRUCTURING_WITHDRAWAL_AND_RECOVERY_EXCEPTION_FILTER_V3", "independent_evidence_weight": 0.5, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "peak_180D_date": "2024-12-06", "peak_30D_date": "2024-12-06", "peak_90D_date": "2024-12-06", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "promotion_blocked_until_url_repair": false, "representative_for_aggregate": true, "research_session": "post_calibrated_sector_archetype_residual_research", "reuse_reason": "same C32 universe allowed because trigger_family and entry_date are new versus prior local C32 loop100/101 where applicable", "role": "positive", "row_type": "trigger", "same_entry_group_id": "C32|010130|Stage3-Yellow|2024-11-13|korea_zinc_share_sale_withdrawal_after_tender_battle_recovery_exception", "source_proxy_only": false, "symbol": "010130", "trigger_date": "2024-11-13", "trigger_family": "korea_zinc_share_sale_withdrawal_after_tender_battle_recovery_exception", "trigger_type": "Stage3-Yellow", "trough_180D_date": "2025-04-09", "trough_30D_date": "2024-11-26", "trough_90D_date": "2025-03-07", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -17.1068, "MAE_30D_pct": -17.1068, "MAE_90D_pct": -17.1068, "MFE_180D_pct": 69.69, "MFE_30D_pct": 1.4925, "MFE_90D_pct": 22.6177, "aggregate_group_role": "representative", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32-L102-02-241560-20241021", "classification": "positive", "company": "두산밥캣", "component_score_breakdown": {"control_premium_specificity": 78, "high_MAE_overlay": false, "information_quality": 70, "issuer_level_bridge": 75, "minority_holder_risk": 35, "price_path_alignment": 72, "shareholder_vote_or_transaction_clarity": 68, "valuation_transfer_risk": 38}, "corporate_action_window_status": "not_contaminated_in_30_90_180D_calibration_window_by_this_loop_check", "current_profile_error": false, "current_profile_verdict": "current_profile_missed_recovery_exception", "dedupe_for_aggregate": "representative_candidate", "deep_sub_archetype_id": "C32_DEEP_KOREA_ZINC_HYBE_DOOSAN_SK_TWAY_CONTROL_RIGHTS_RECOVERY_VS_SPIKE_FADE", "do_not_count_as_new_case": false, "entry_date": "2024-10-21", "entry_price": 43550.0, "entry_rule": "target_trigger_date_or_next_tradable_close", "evidence_family": "doosan_bobcat_revised_share_exchange_ratio_recovery_bridge", "evidence_timing": "Doosan resumed the Bobcat-Robotics restructuring with a revised ratio after minority-holder criticism; Bobcat became a post-shock recovery control.", "evidence_url": "https://www.kedglobal.com/corporate-restructuring/newsView/ked202410210006", "evidence_url_pending": false, "fine_archetype_id": "C32_CONTROL_RIGHTS_RESTRUCTURING_WITHDRAWAL_AND_RECOVERY_EXCEPTION_FILTER_V3", "independent_evidence_weight": 0.5, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "peak_180D_date": "2025-06-24", "peak_30D_date": "2024-10-21", "peak_90D_date": "2025-01-24", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "promotion_blocked_until_url_repair": false, "representative_for_aggregate": true, "research_session": "post_calibrated_sector_archetype_residual_research", "reuse_reason": "same C32 universe allowed because trigger_family and entry_date are new versus prior local C32 loop100/101 where applicable", "role": "positive", "row_type": "trigger", "same_entry_group_id": "C32|241560|Stage2-Actionable|2024-10-21|doosan_bobcat_revised_share_exchange_ratio_recovery_bridge", "source_proxy_only": false, "symbol": "241560", "trigger_date": "2024-10-21", "trigger_family": "doosan_bobcat_revised_share_exchange_ratio_recovery_bridge", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2024-10-29", "trough_30D_date": "2024-10-29", "trough_90D_date": "2024-10-29", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -10.4831, "MAE_30D_pct": -10.4831, "MAE_90D_pct": -10.4831, "MFE_180D_pct": 237.9227, "MFE_30D_pct": 18.3575, "MFE_90D_pct": 86.4734, "aggregate_group_role": "representative", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32-L102-03-000150-20241021", "classification": "positive", "company": "두산", "component_score_breakdown": {"control_premium_specificity": 78, "high_MAE_overlay": false, "information_quality": 70, "issuer_level_bridge": 75, "minority_holder_risk": 35, "price_path_alignment": 72, "shareholder_vote_or_transaction_clarity": 68, "valuation_transfer_risk": 38}, "corporate_action_window_status": "not_contaminated_in_30_90_180D_calibration_window_by_this_loop_check", "current_profile_error": true, "current_profile_verdict": "current_profile_missed_recovery_exception", "dedupe_for_aggregate": "representative_candidate", "deep_sub_archetype_id": "C32_DEEP_KOREA_ZINC_HYBE_DOOSAN_SK_TWAY_CONTROL_RIGHTS_RECOVERY_VS_SPIKE_FADE", "do_not_count_as_new_case": false, "entry_date": "2024-10-21", "entry_price": 207000.0, "entry_rule": "target_trigger_date_or_next_tradable_close", "evidence_family": "doosan_holdco_revised_restructuring_control_premium_bridge", "evidence_timing": "Doosan holdco repriced after revised restructuring terms; the verified bridge is group-control simplification after valuation-transfer backlash.", "evidence_url": "https://www.kedglobal.com/corporate-restructuring/newsView/ked202410210006", "evidence_url_pending": false, "fine_archetype_id": "C32_CONTROL_RIGHTS_RESTRUCTURING_WITHDRAWAL_AND_RECOVERY_EXCEPTION_FILTER_V3", "independent_evidence_weight": 0.5, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "peak_180D_date": "2025-06-30", "peak_30D_date": "2024-11-14", "peak_90D_date": "2025-02-26", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "promotion_blocked_until_url_repair": false, "representative_for_aggregate": true, "research_session": "post_calibrated_sector_archetype_residual_research", "reuse_reason": "same C32 universe allowed because trigger_family and entry_date are new versus prior local C32 loop100/101 where applicable", "role": "positive", "row_type": "trigger", "same_entry_group_id": "C32|000150|Stage3-Yellow|2024-10-21|doosan_holdco_revised_restructuring_control_premium_bridge", "source_proxy_only": false, "symbol": "000150", "trigger_date": "2024-10-21", "trigger_family": "doosan_holdco_revised_restructuring_control_premium_bridge", "trigger_type": "Stage3-Yellow", "trough_180D_date": "2024-11-01", "trough_30D_date": "2024-11-01", "trough_90D_date": "2024-11-01", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -18.1114, "MAE_30D_pct": -6.2954, "MAE_90D_pct": -18.1114, "MFE_180D_pct": 249.6368, "MFE_30D_pct": 10.4116, "MFE_90D_pct": 49.6368, "aggregate_group_role": "representative", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32-L102-04-034020-20241021", "classification": "positive", "company": "두산에너빌리티", "component_score_breakdown": {"control_premium_specificity": 78, "high_MAE_overlay": false, "information_quality": 70, "issuer_level_bridge": 75, "minority_holder_risk": 35, "price_path_alignment": 72, "shareholder_vote_or_transaction_clarity": 68, "valuation_transfer_risk": 38}, "corporate_action_window_status": "not_contaminated_in_30_90_180D_calibration_window_by_this_loop_check", "current_profile_error": true, "current_profile_verdict": "current_profile_missed_recovery_exception", "dedupe_for_aggregate": "representative_candidate", "deep_sub_archetype_id": "C32_DEEP_KOREA_ZINC_HYBE_DOOSAN_SK_TWAY_CONTROL_RIGHTS_RECOVERY_VS_SPIKE_FADE", "do_not_count_as_new_case": false, "entry_date": "2024-10-21", "entry_price": 20650.0, "entry_rule": "target_trigger_date_or_next_tradable_close", "evidence_family": "doosan_enerbility_revised_spin_merger_recovery_bridge", "evidence_timing": "Doosan Enerbility’s revised restructuring terms created a recovery exception versus the initial share-exchange discount.", "evidence_url": "https://www.kedglobal.com/corporate-restructuring/newsView/ked202410210006", "evidence_url_pending": false, "fine_archetype_id": "C32_CONTROL_RIGHTS_RESTRUCTURING_WITHDRAWAL_AND_RECOVERY_EXCEPTION_FILTER_V3", "independent_evidence_weight": 0.5, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "peak_180D_date": "2025-06-30", "peak_30D_date": "2024-11-19", "peak_90D_date": "2025-02-19", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "promotion_blocked_until_url_repair": false, "representative_for_aggregate": true, "research_session": "post_calibrated_sector_archetype_residual_research", "reuse_reason": "same C32 universe allowed because trigger_family and entry_date are new versus prior local C32 loop100/101 where applicable", "role": "positive", "row_type": "trigger", "same_entry_group_id": "C32|034020|Stage2-Actionable|2024-10-21|doosan_enerbility_revised_spin_merger_recovery_bridge", "source_proxy_only": false, "symbol": "034020", "trigger_date": "2024-10-21", "trigger_family": "doosan_enerbility_revised_spin_merger_recovery_bridge", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2024-12-10", "trough_30D_date": "2024-11-04", "trough_90D_date": "2024-12-10", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -25.2607, "MAE_30D_pct": -11.9905, "MAE_90D_pct": -24.1706, "MFE_180D_pct": 7.346, "MFE_30D_pct": 2.8436, "MFE_90D_pct": 2.8436, "aggregate_group_role": "representative", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32-L102-05-352820-20240424", "classification": "counterexample", "company": "HYBE", "component_score_breakdown": {"control_premium_specificity": 58, "high_MAE_overlay": false, "information_quality": 70, "issuer_level_bridge": 42, "minority_holder_risk": 78, "price_path_alignment": 34, "shareholder_vote_or_transaction_clarity": 45, "valuation_transfer_risk": 82}, "corporate_action_window_status": "not_contaminated_in_30_90_180D_calibration_window_by_this_loop_check", "current_profile_error": true, "current_profile_verdict": "current_profile_false_positive_or_4B_too_late", "dedupe_for_aggregate": "representative_candidate", "deep_sub_archetype_id": "C32_DEEP_KOREA_ZINC_HYBE_DOOSAN_SK_TWAY_CONTROL_RIGHTS_RECOVERY_VS_SPIKE_FADE", "do_not_count_as_new_case": false, "entry_date": "2024-04-24", "entry_price": 211000.0, "entry_rule": "target_trigger_date_or_next_tradable_close", "evidence_family": "hybe_ador_management_rights_dispute_label_spike_fade", "evidence_timing": "HYBE audit/ADOR breakaway dispute was a true management-rights event but lacked a positive control-premium bridge for HYBE shareholders at the trigger.", "evidence_url": "https://www.reuters.com/lifestyle/record-giant-hybe-audits-newjeans-label-infighting-returns-k-pop-2024-04-24/", "evidence_url_pending": false, "fine_archetype_id": "C32_CONTROL_RIGHTS_RESTRUCTURING_WITHDRAWAL_AND_RECOVERY_EXCEPTION_FILTER_V3", "independent_evidence_weight": 1.0, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "peak_180D_date": "2025-01-17", "peak_30D_date": "2024-04-25", "peak_90D_date": "2024-04-25", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "promotion_blocked_until_url_repair": false, "representative_for_aggregate": true, "research_session": "post_calibrated_sector_archetype_residual_research", "reuse_reason": "same C32 universe allowed because trigger_family and entry_date are new versus prior local C32 loop100/101 where applicable", "role": "counterexample", "row_type": "trigger", "same_entry_group_id": "C32|352820|Stage4B|2024-04-24|hybe_ador_management_rights_dispute_label_spike_fade", "source_proxy_only": false, "symbol": "352820", "trigger_date": "2024-04-24", "trigger_family": "hybe_ador_management_rights_dispute_label_spike_fade", "trigger_type": "Stage4B", "trough_180D_date": "2024-09-23", "trough_30D_date": "2024-05-23", "trough_90D_date": "2024-08-05", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -44.7626, "MAE_30D_pct": -15.3631, "MAE_90D_pct": -30.3771, "MFE_180D_pct": 9.2179, "MFE_30D_pct": 9.2179, "MFE_90D_pct": 9.2179, "aggregate_group_role": "representative", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32-L102-06-454910-20241021", "classification": "counterexample", "company": "두산로보틱스", "component_score_breakdown": {"control_premium_specificity": 58, "high_MAE_overlay": true, "information_quality": 70, "issuer_level_bridge": 42, "minority_holder_risk": 78, "price_path_alignment": 34, "shareholder_vote_or_transaction_clarity": 45, "valuation_transfer_risk": 82}, "corporate_action_window_status": "not_contaminated_in_30_90_180D_calibration_window_by_this_loop_check", "current_profile_error": true, "current_profile_verdict": "current_profile_false_positive_or_4B_too_late", "dedupe_for_aggregate": "representative_candidate", "deep_sub_archetype_id": "C32_DEEP_KOREA_ZINC_HYBE_DOOSAN_SK_TWAY_CONTROL_RIGHTS_RECOVERY_VS_SPIKE_FADE", "do_not_count_as_new_case": false, "entry_date": "2024-10-21", "entry_price": 71600.0, "entry_rule": "target_trigger_date_or_next_tradable_close", "evidence_family": "doosan_robotics_revised_merger_ratio_still_valuation_transfer_risk", "evidence_timing": "Even after revised ratio, Doosan Robotics remained the high-valuation receiving asset; the governance headline needed local 4B watch rather than positive C32 rerating.", "evidence_url": "https://www.kedglobal.com/corporate-restructuring/newsView/ked202410210006", "evidence_url_pending": false, "fine_archetype_id": "C32_CONTROL_RIGHTS_RESTRUCTURING_WITHDRAWAL_AND_RECOVERY_EXCEPTION_FILTER_V3", "independent_evidence_weight": 0.5, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "peak_180D_date": "2024-10-21", "peak_30D_date": "2024-10-21", "peak_90D_date": "2024-10-21", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "promotion_blocked_until_url_repair": false, "representative_for_aggregate": true, "research_session": "post_calibrated_sector_archetype_residual_research", "reuse_reason": "same C32 universe allowed because trigger_family and entry_date are new versus prior local C32 loop100/101 where applicable", "role": "counterexample", "row_type": "trigger", "same_entry_group_id": "C32|454910|Stage4B|2024-10-21|doosan_robotics_revised_merger_ratio_still_valuation_transfer_risk", "source_proxy_only": false, "symbol": "454910", "trigger_date": "2024-10-21", "trigger_family": "doosan_robotics_revised_merger_ratio_still_valuation_transfer_risk", "trigger_type": "Stage4B", "trough_180D_date": "2025-04-09", "trough_30D_date": "2024-11-14", "trough_90D_date": "2024-12-20", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -33.6617, "MAE_30D_pct": -24.6305, "MAE_90D_pct": -24.6305, "MFE_180D_pct": 15.1067, "MFE_30D_pct": 1.8062, "MFE_90D_pct": 15.1067, "aggregate_group_role": "representative", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32-L102-07-096770-20241101", "classification": "counterexample", "company": "SK이노베이션", "component_score_breakdown": {"control_premium_specificity": 58, "high_MAE_overlay": false, "information_quality": 70, "issuer_level_bridge": 42, "minority_holder_risk": 78, "price_path_alignment": 34, "shareholder_vote_or_transaction_clarity": 45, "valuation_transfer_risk": 82}, "corporate_action_window_status": "not_contaminated_in_30_90_180D_calibration_window_by_this_loop_check", "current_profile_error": true, "current_profile_verdict": "current_profile_false_positive_or_4B_too_late", "dedupe_for_aggregate": "representative_candidate", "deep_sub_archetype_id": "C32_DEEP_KOREA_ZINC_HYBE_DOOSAN_SK_TWAY_CONTROL_RIGHTS_RECOVERY_VS_SPIKE_FADE", "do_not_count_as_new_case": false, "entry_date": "2024-11-01", "entry_price": 121800.0, "entry_rule": "target_trigger_date_or_next_tradable_close", "evidence_family": "sk_innovation_merger_effective_restructuring_label_without_fast_profit_bridge", "evidence_timing": "SK Innovation-SK E&S merger was approved/effective, but SK On/battery-loss and restructuring execution risk still capped near-term rerating.", "evidence_url": "https://www.reuters.com/markets/deals/sk-innovation-shareholders-approve-merger-plan-with-sk-es-yonhap-reports-2024-08-27/", "evidence_url_pending": false, "fine_archetype_id": "C32_CONTROL_RIGHTS_RESTRUCTURING_WITHDRAWAL_AND_RECOVERY_EXCEPTION_FILTER_V3", "independent_evidence_weight": 0.5, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "peak_180D_date": "2025-03-13", "peak_30D_date": "2024-11-01", "peak_90D_date": "2025-03-13", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "promotion_blocked_until_url_repair": false, "representative_for_aggregate": true, "research_session": "post_calibrated_sector_archetype_residual_research", "reuse_reason": "same C32 universe allowed because trigger_family and entry_date are new versus prior local C32 loop100/101 where applicable", "role": "counterexample", "row_type": "trigger", "same_entry_group_id": "C32|096770|Stage4B|2024-11-01|sk_innovation_merger_effective_restructuring_label_without_fast_profit_bridge", "source_proxy_only": false, "symbol": "096770", "trigger_date": "2024-11-01", "trigger_family": "sk_innovation_merger_effective_restructuring_label_without_fast_profit_bridge", "trigger_type": "Stage4B", "trough_180D_date": "2025-05-23", "trough_30D_date": "2024-11-15", "trough_90D_date": "2024-11-15", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -16.2162, "MAE_30D_pct": -9.009, "MAE_90D_pct": -16.2162, "MFE_180D_pct": 21.2355, "MFE_30D_pct": 6.6924, "MFE_90D_pct": 21.2355, "aggregate_group_role": "representative", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32-L102-08-035720-20240723", "classification": "counterexample", "company": "카카오", "component_score_breakdown": {"control_premium_specificity": 58, "high_MAE_overlay": false, "information_quality": 70, "issuer_level_bridge": 42, "minority_holder_risk": 78, "price_path_alignment": 34, "shareholder_vote_or_transaction_clarity": 45, "valuation_transfer_risk": 82}, "corporate_action_window_status": "not_contaminated_in_30_90_180D_calibration_window_by_this_loop_check", "current_profile_error": true, "current_profile_verdict": "current_profile_false_positive_or_4B_too_late", "dedupe_for_aggregate": "representative_candidate", "deep_sub_archetype_id": "C32_DEEP_KOREA_ZINC_HYBE_DOOSAN_SK_TWAY_CONTROL_RIGHTS_RECOVERY_VS_SPIKE_FADE", "do_not_count_as_new_case": false, "entry_date": "2024-07-23", "entry_price": 38850.0, "entry_rule": "target_trigger_date_or_next_tradable_close", "evidence_family": "kakao_founder_arrest_sm_takeover_stock_manipulation_trust_break", "evidence_timing": "Kakao founder arrest in the SM takeover stock-manipulation case was a governance/trust-control event, but the issuer bridge remained weak and the row is a local 4B/trust-break watch rather than positive C32 rerating.", "evidence_url": "https://www.reuters.com/technology/south-korean-court-approves-arrest-warrant-kakao-founder-2024-07-22/", "evidence_url_pending": false, "fine_archetype_id": "C32_CONTROL_RIGHTS_RESTRUCTURING_WITHDRAWAL_AND_RECOVERY_EXCEPTION_FILTER_V3", "independent_evidence_weight": 0.5, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "peak_180D_date": "2024-12-04", "peak_30D_date": "2024-07-23", "peak_90D_date": "2024-12-04", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "promotion_blocked_until_url_repair": false, "representative_for_aggregate": true, "research_session": "post_calibrated_sector_archetype_residual_research", "reuse_reason": "same C32 universe allowed because trigger_family and entry_date are new versus prior local C32 loop100/101 where applicable", "role": "counterexample", "row_type": "trigger", "same_entry_group_id": "C32|035720|Stage4B|2024-07-23|kakao_founder_arrest_sm_takeover_stock_manipulation_trust_break", "source_proxy_only": false, "symbol": "035720", "trigger_date": "2024-07-23", "trigger_family": "kakao_founder_arrest_sm_takeover_stock_manipulation_trust_break", "trigger_type": "Stage4B", "trough_180D_date": "2024-11-14", "trough_30D_date": "2024-08-05", "trough_90D_date": "2024-11-14", "upstream_source": "FinanceData/marcap"}
```

## 9. Machine-readable score simulation rows JSONL

```jsonl
{"MAE_90D_pct": -29.052, "MFE_90D_pct": 145.3619, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32-L102-01-010130-20241113", "current_profile_proxy_score": 80, "profile_expected_stage_without_new_rule": "Stage3-Yellow", "row_type": "score_simulation", "rule_read": "C32 requires verified control-premium / vote / transaction / recovery bridge before Yellow; governance label spike alone routes to local 4B watch.", "suggested_shadow_stage_after_C32_rule": "Stage3-Yellow_or_Actionable_with_MAE_overlay", "symbol": "010130", "trigger_type": "Stage3-Yellow"}
{"MAE_90D_pct": -17.1068, "MFE_90D_pct": 22.6177, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32-L102-02-241560-20241021", "current_profile_proxy_score": 80, "profile_expected_stage_without_new_rule": "Stage3-Yellow", "row_type": "score_simulation", "rule_read": "C32 requires verified control-premium / vote / transaction / recovery bridge before Yellow; governance label spike alone routes to local 4B watch.", "suggested_shadow_stage_after_C32_rule": "Stage3-Yellow_or_Actionable_with_MAE_overlay", "symbol": "241560", "trigger_type": "Stage2-Actionable"}
{"MAE_90D_pct": -10.4831, "MFE_90D_pct": 86.4734, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32-L102-03-000150-20241021", "current_profile_proxy_score": 80, "profile_expected_stage_without_new_rule": "Stage3-Yellow", "row_type": "score_simulation", "rule_read": "C32 requires verified control-premium / vote / transaction / recovery bridge before Yellow; governance label spike alone routes to local 4B watch.", "suggested_shadow_stage_after_C32_rule": "Stage3-Yellow_or_Actionable_with_MAE_overlay", "symbol": "000150", "trigger_type": "Stage3-Yellow"}
{"MAE_90D_pct": -18.1114, "MFE_90D_pct": 49.6368, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32-L102-04-034020-20241021", "current_profile_proxy_score": 80, "profile_expected_stage_without_new_rule": "Stage3-Yellow", "row_type": "score_simulation", "rule_read": "C32 requires verified control-premium / vote / transaction / recovery bridge before Yellow; governance label spike alone routes to local 4B watch.", "suggested_shadow_stage_after_C32_rule": "Stage3-Yellow_or_Actionable_with_MAE_overlay", "symbol": "034020", "trigger_type": "Stage2-Actionable"}
{"MAE_90D_pct": -24.1706, "MFE_90D_pct": 2.8436, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32-L102-05-352820-20240424", "current_profile_proxy_score": 68, "profile_expected_stage_without_new_rule": "Stage2-Actionable_or_Yellow_false_positive", "row_type": "score_simulation", "rule_read": "C32 requires verified control-premium / vote / transaction / recovery bridge before Yellow; governance label spike alone routes to local 4B watch.", "suggested_shadow_stage_after_C32_rule": "Local-4B-Watch_or_Stage4B", "symbol": "352820", "trigger_type": "Stage4B"}
{"MAE_90D_pct": -30.3771, "MFE_90D_pct": 9.2179, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32-L102-06-454910-20241021", "current_profile_proxy_score": 68, "profile_expected_stage_without_new_rule": "Stage2-Actionable_or_Yellow_false_positive", "row_type": "score_simulation", "rule_read": "C32 requires verified control-premium / vote / transaction / recovery bridge before Yellow; governance label spike alone routes to local 4B watch.", "suggested_shadow_stage_after_C32_rule": "Local-4B-Watch_or_Stage4B", "symbol": "454910", "trigger_type": "Stage4B"}
{"MAE_90D_pct": -24.6305, "MFE_90D_pct": 15.1067, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32-L102-07-096770-20241101", "current_profile_proxy_score": 68, "profile_expected_stage_without_new_rule": "Stage2-Actionable_or_Yellow_false_positive", "row_type": "score_simulation", "rule_read": "C32 requires verified control-premium / vote / transaction / recovery bridge before Yellow; governance label spike alone routes to local 4B watch.", "suggested_shadow_stage_after_C32_rule": "Local-4B-Watch_or_Stage4B", "symbol": "096770", "trigger_type": "Stage4B"}
{"MAE_90D_pct": -16.2162, "MFE_90D_pct": 21.2355, "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "case_id": "C32-L102-08-035720-20240723", "current_profile_proxy_score": 68, "profile_expected_stage_without_new_rule": "Stage2-Actionable_or_Yellow_false_positive", "row_type": "score_simulation", "rule_read": "C32 requires verified control-premium / vote / transaction / recovery bridge before Yellow; governance label spike alone routes to local 4B watch.", "suggested_shadow_stage_after_C32_rule": "Local-4B-Watch_or_Stage4B", "symbol": "035720", "trigger_type": "Stage4B"}
```

## 10. Residual diagnosis

```text
current_profile_error_pattern_1 = C32 governance/control label can still create Stage2 or Yellow shell without verified control-premium/vote/transaction bridge.
current_profile_error_pattern_2 = post-shock recovery entries and announcement-spike entries must be separated.
current_profile_error_pattern_3 = Korea Zinc and Doosan positive controls still need high-MAE overlay where drawdown is deep; Green should not be loosened.
current_profile_error_pattern_4 = hard 4C should require failed vote, canceled transaction, trust break, value-transfer loss, or issuer-level break, not just generic governance disappointment.
```

## 11. Candidate shadow rule

```text
new_axis_proposed = C32_verified_control_premium_vote_transaction_or_post_shock_recovery_bridge_required_before_Yellow_or_Green_v3
existing_axis_strengthened = stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
existing_axis_weakened = hard_4c_thesis_break_routes_to_4c_when_only_generic_governance_or_restructuring_label_is_present
```

Proposed C32-specific shadow rule:

```text
If canonical_archetype_id == C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP:
  Yellow/Green requires one of:
    - verified tender/control premium price bridge,
    - shareholder vote / merger approval plus issuer-level value bridge,
    - post-shock recovery after valuation-transfer risk has been repriced,
    - rights-dispute resolution with visible control or cash-flow bridge.
  If evidence is only governance/restructuring/control-rights label and the price path is already locally spiked:
    route to local_4B_watch, not positive rerating.
  Hard 4C requires failed vote, canceled transaction, trust break, value-transfer loss, or issuer-level bridge break.
  If MFE90 is high but MAE90 <= -25%, keep high-MAE overlay and block Stage3-Green loosening.
```

## 12. Validation self-audit

```yaml
filename_matches_standard_v12_pattern: true
metadata_round_loop_matches_filename: true
row_type_trigger_rows_have_trigger_type: true
entry_date_present: true
entry_price_positive: true
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
forward_window_trading_days_gte_180: true
MFE_MAE_30_90_180_present: true
large_sector_id_present: true
canonical_archetype_id_present: true
corporate_action_window_status_not_contaminated: true
same_entry_group_id_present: true
dedupe_for_aggregate_present: true
aggregate_group_role_present: true
calibration_usable_present: true
```

## 13. Residual contribution summary

```yaml
loop_contribution_label: canonical_archetype_rule_candidate
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: false
new_independent_case_count: 8
reused_case_count: 0
new_symbol_count: 1
same_archetype_new_symbol_count: 1
same_archetype_new_trigger_family_count: 8
positive_case_count: 4
counterexample_count: 4
current_profile_error_count: 7
diversity_score_summary: HYBE is new to local C32; Korea Zinc/Doosan/SK/Kakao symbols are reused only with new trigger-family/date rows. Positive-counterexample balance is 4:4, and Stage4B path count is 4.
```

This loop adds `8` new C32 trigger-family/date cases, `4` counterexamples, and `7` residual errors for `R12/C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP`.

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not execute this now. Later coding agent should batch-ingest this MD with other V12 outputs.

Task:
- Parse trigger rows and score simulation rows from this MD.
- Treat C32_CONTROL_RIGHTS_RESTRUCTURING_WITHDRAWAL_AND_RECOVERY_EXCEPTION_FILTER_V3 as a C32 fine-archetype family.
- Do not globally loosen Stage3-Green.
- Candidate rule: C32 requires verified control-premium/vote/transaction/post-shock recovery bridge before Yellow or Green.
- Keep local 4B watch for governance-label spikes without issuer-level bridge.
- Keep high-MAE overlay if MAE90 <= -25 even when MFE90 is high.
```

## 15. Next research state

```text
completed_round = R12
completed_loop = 102
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality_repair_after_local_priority0_priority1_fill
next_recommended_archetypes = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE, R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL, C31_POLICY_SUBSIDY_LEGISLATION_EVENT, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
