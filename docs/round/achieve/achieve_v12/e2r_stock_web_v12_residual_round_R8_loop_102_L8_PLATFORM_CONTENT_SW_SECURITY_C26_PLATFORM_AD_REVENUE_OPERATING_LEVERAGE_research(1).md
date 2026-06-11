# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
schema_family = v12_sector_archetype_residual
selected_round = R8
selected_loop = 102
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id = PLATFORM_AD_RECOVERY_OPERATING_LEVERAGE_BRIDGE_VS_AD_RECOVERY_LABEL_AND_MEDIA_AGENCY_FALSE_POSITIVE
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | local_4b_guard | canonical_archetype_compression
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Current Calibrated Profile Assumption

Current proxy profile is `e2r_2_1_stock_web_calibrated_proxy` under the v12 prompt. The already-applied global axes are treated as baseline, not re-proposed globally:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This loop tests whether C26 should require a more explicit **platform/ad monetization → operating leverage → revision or margin bridge** before a generic advertising recovery or platform traffic label is allowed to become Stage2-Actionable. The problem is like listening to a busy marketplace from outside: crowd noise says there is traffic, but it does not prove merchants are converting traffic into margin.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R8 |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY |
| canonical_archetype_id | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE |
| fine_archetype_id | PLATFORM_AD_RECOVERY_OPERATING_LEVERAGE_BRIDGE_VS_AD_RECOVERY_LABEL_AND_MEDIA_AGENCY_FALSE_POSITIVE |
| scope logic | C26 belongs to R8/L8. Scope consistency passes. |

## 3. Previous Coverage / Duplicate Avoidance Check

The current NO-REPEAT index marks C26 as Priority 0 with 3 rows and 27 needed to reach the 30-row floor. Conversation-local generated ledger already added an earlier C26 loop using `067160`, `089600`, and `216050`. This loop therefore avoids those names and also avoids index top-covered C26 symbols such as `035420`, `042000`, and `237820`.

Selected new symbols:

| symbol | name at trigger date | novelty |
|---:|---|---|
| 035760 | CJ ENM | new C26-adjacent platform/content commerce and ad-recovery monetization case |
| 035720 | 카카오 | new C26 platform ad/commerce false-positive case, not using NAVER-covered symbol |
| 030000 | 제일기획 | new C26 advertising agency counterexample; ad recovery label without return acceleration |
| 214320 | 이노션 | new C26 advertising agency positive/mixed case; steadier operating leverage bridge |

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row intentionally repeats existing C26 symbol-trigger keys from the index or this conversation's C26 output.

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| manifest | atlas/manifest.json |
| calibration shard root | atlas/ohlcv_tradable_by_symbol_year |
| price basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| manifest_max_date | 2026-02-20 |
| validation rule | Every trigger below has 30D / 90D / 180D MFE and MAE from actual 1D OHLC rows. |

Source shard/profile paths checked:

| symbol | profile path | price shard path | profile caveat |
|---:|---|---|---|
| 035760 | atlas/symbol_profiles/035/035760.json | atlas/ohlcv_tradable_by_symbol_year/035/035760/2024.csv | old corporate-action windows blocked; 2024 trigger window used outside listed candidate dates |
| 035720 | atlas/symbol_profiles/035/035720.json | atlas/ohlcv_tradable_by_symbol_year/035/035720/2024.csv | old corporate-action windows blocked; 2024 trigger window used outside listed candidate dates |
| 030000 | atlas/symbol_profiles/030/030000.json | atlas/ohlcv_tradable_by_symbol_year/030/030000/2024.csv | old corporate-action windows blocked; 2024 trigger window used outside listed candidate dates |
| 214320 | atlas/symbol_profiles/214/214320.json | atlas/ohlcv_tradable_by_symbol_year/214/214320/2024.csv | 2023 corporate-action candidate dates only; 2024 trigger window used |

## 5. OHLC Anchor Rows Used

Selected anchor rows are quoted as compact row facts rather than full CSV dumps.

| symbol | entry anchor | confirming/peak/low anchors used |
|---:|---|---|
| 035760 | 2024-01-23 close 69,900 | 2024-02-08 high 89,300; 2024-05-27 high 94,900 / close 91,100; 2024-07-04 low 68,400 |
| 035720 | 2024-01-11 close 60,800 | 2024-01-11 high 61,900; 2024-02-01 low 51,500; 2024-05-24 low 44,400; 2024-09-09 low 32,900 |
| 030000 | 2024-04-01 close 19,280 | 2024-05-10 high 19,570; 2024-07-18 low 17,750; 2024-08-07 low 16,700 |
| 214320 | 2024-01-25 close 21,200 | 2024-02-26 high 22,800; 2024-05-03 high 24,300; 2024-07-23 low 19,630 |

## 6. Research Thesis

C26 is not a generic "advertising got better" bucket. It is specifically a monetization and operating leverage bucket. The useful signal is not the headline itself but the bridge:

```text
traffic / ad spend / inventory demand
    -> monetization yield, ARPU, take-rate, booking or agency margin
    -> operating leverage, EPS revision, cash-flow conversion
```

When the bridge exists, the price path can support Stage2-Actionable. When the bridge is only implied by vocabulary, the path often becomes a low-MFE / high-MAE false positive.

## 7. Case Classification

| case_id | symbol | thesis class | classification | reason |
|---|---:|---|---|---|
| C26_R8L102_035760_20240123 | 035760 | content/commerce platform + media ad recovery | positive + later 4B watch | price path rewarded monetization/recovery bridge, then needed peak-risk overlay |
| C26_R8L102_035720_20240111 | 035720 | platform ad/commerce recovery vocabulary | counterexample | platform label alone had almost no MFE and very large MAE |
| C26_R8L102_030000_20240401 | 030000 | ad agency recovery | counterexample | stable agency quality did not convert to strong return without revision/OPM acceleration |
| C26_R8L102_214320_20240125 | 214320 | ad agency operating leverage | positive/mixed | modest but cleaner MFE with controlled MAE before later sector fade |

## 8. Aggregate Summary

| metric | value |
|---|---:|
| new_independent_case_count | 4 |
| reused_case_count | 0 |
| same_archetype_new_symbol_count | 4 |
| same_archetype_new_trigger_family_count | 5 |
| calibration_usable_case_count | 4 |
| calibration_usable_trigger_count | 5 |
| positive_case_count | 2 |
| counterexample_count | 2 |
| local_4b_watch_count | 1 |
| current_profile_error_count | 4 |
| do_not_propose_new_weight_delta | false |
| auto_selected_coverage_gap | C26 rows 6 -> 10 if accepted; still Priority 0, need 20 to 30 |

## 9. Evidence Source Map

| case_id | evidence family | evidence source status | evidence interpretation |
|---|---|---|---|
| C26_R8L102_035760_20240123 | media/content commerce ad recovery, platform monetization, margin recovery | source_proxy_only / evidence_url_pending | positive only if non-price evidence proves monetization and operating leverage, not just content headline |
| C26_R8L102_035720_20240111 | platform ad/commerce recovery, AI/commerce headline, ecosystem traffic | source_proxy_only / evidence_url_pending | traffic/platform vocabulary alone should not be Stage2-Actionable |
| C26_R8L102_030000_20240401 | ad agency rebound, advertiser budget normalization | source_proxy_only / evidence_url_pending | agency rebound needs OPM/revision confirmation; otherwise low MFE persists |
| C26_R8L102_214320_20240125 | ad agency captive/global client margin normalization | source_proxy_only / evidence_url_pending | cleaner but still moderate positive; allow Stage2 but require operating leverage bridge for Green |

## 10. Trigger Grid

| trigger_id | trigger_type | entry | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | verdict |
|---|---|---|---:|---:|---:|---|
| T_C26_035760_STAGE2A_20240123 | Stage2-Actionable | 2024-01-23 / 69,900 | 27.75 / -5.72 | 35.77 / -5.72 | 35.77 / -5.72 | valid C26 positive if monetization bridge exists |
| T_C26_035760_STAGE4B_20240527 | Stage4B | 2024-05-27 / 91,100 | 4.17 / -24.92 | 4.17 / -24.92 | 4.17 / -24.92 | local/full 4B overlay useful after rerating |
| T_C26_035720_STAGE2_20240111 | Stage2 | 2024-01-11 / 60,800 | 1.81 / -15.30 | 1.81 / -26.97 | 1.81 / -45.89 | platform ad label false positive |
| T_C26_030000_STAGE2_20240401 | Stage2 | 2024-04-01 / 19,280 | 1.50 / -4.30 | 1.50 / -7.94 | 1.50 / -13.38 | ad agency label without revision was too weak |
| T_C26_214320_STAGE2A_20240125 | Stage2-Actionable | 2024-01-25 / 21,200 | 7.55 / -2.59 | 14.62 / -2.59 | 14.62 / -7.41 | moderate positive; bridge required before Green |

## 11. Trigger-Level OHLC Backtest Table

| symbol | trigger_type | entry_price | peak_date | peak_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | drawdown_after_peak_pct |
|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 035760 | Stage2-Actionable | 69900 | 2024-05-27 | 94900 | 27.75 | 35.77 | 35.77 | -5.72 | -5.72 | -5.72 | -27.92 |
| 035760 | Stage4B | 91100 | 2024-05-27 | 94900 | 4.17 | 4.17 | 4.17 | -24.92 | -24.92 | -24.92 | -27.92 |
| 035720 | Stage2 | 60800 | 2024-01-11 | 61900 | 1.81 | 1.81 | 1.81 | -15.30 | -26.97 | -45.89 | -46.85 |
| 030000 | Stage2 | 19280 | 2024-05-10 | 19570 | 1.50 | 1.50 | 1.50 | -4.30 | -7.94 | -13.38 | -14.66 |
| 214320 | Stage2-Actionable | 21200 | 2024-05-03 | 24300 | 7.55 | 14.62 | 14.62 | -2.59 | -2.59 | -7.41 | -19.22 |

## 12. Current Calibrated Profile Stress Test

| case_id | current calibrated profile likely verdict | actual price path alignment | residual error |
|---|---|---|---|
| C26_R8L102_035760_20240123 | Stage2-Actionable allowed if monetization bridge is visible | MFE180 +35.77 with contained initial MAE, then local 4B risk | current_profile_ok_but_needs_4B_overlay |
| C26_R8L102_035720_20240111 | Stage2 if platform/ad recovery language is over-credited | MFE capped at +1.81 while MAE180 reached -45.89 | current_profile_false_positive |
| C26_R8L102_030000_20240401 | Stage2 if ad agency recovery is over-credited | MFE capped at +1.50 while MAE180 reached -13.38 | current_profile_false_positive |
| C26_R8L102_214320_20240125 | Stage2-Actionable allowed, Green withheld | MFE180 +14.62 with manageable MAE; not enough for Green | current_profile_stage_cap_ok |

Existing axis assessment:

```text
stage2_actionable_evidence_bonus = existing_axis_kept
stage3_yellow_total_min = existing_axis_kept
stage3_green_total_min = existing_axis_kept
stage3_green_revision_min = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 13. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is created in this loop. C26 should not be Green-unlocked by platform traffic, ad-spend recovery, or media-agency label alone.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

Interpretation:

- CJ ENM-style content/commerce recovery can be Stage2-Actionable if monetization and operating leverage evidence are already visible.
- Kakao-style platform vocabulary without confirmed monetization bridge should be capped, because platform scale can be a large room with the lights on but the cash register quiet.
- Ad agency names need advertiser budget recovery plus OPM/revision visibility. The label alone is weak.

## 14. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_evidence_type | local peak proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| T_C26_035760_STAGE4B_20240527 | rerating_peak, content/ad recovery positioning, post-MFE exhaustion | 0.94 | 0.88 | good_local_4B_timing |

4B remains an overlay, not a standalone short/sell rule. The useful rule is that a C26 positive case reaching peak-window proximity after rerating should move into 4B-watch when non-price valuation/positioning evidence is also present.

## 15. 4C Protection Audit

No hard Stage4C trigger is emitted in this loop.

```text
four_c_protection_label = thesis_break_watch_only
```

C26 4C should be reserved for thesis breaks such as confirmed traffic decline, advertiser demand cut, platform policy break, monetization failure, accounting/trust break, or repeated margin disappointment.

## 16. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
sector_specific_rule_candidate = true
candidate = L8 platform/ad Stage2 bridge should require monetization or operating leverage evidence, not theme vocabulary alone.
```

L8 is heterogeneous. C26 specifically asks whether traffic or ad inventory becomes money. Without ARPU, take-rate, ad yield, OPM, or EPS revision, the trigger should not receive Stage2-Actionable credit.

## 17. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_rule_candidate = true
candidate = C26_platform_ad_operating_leverage_bridge_required
```

Proposed C26 rule:

```text
If C26 has traffic/platform/ad recovery + monetization evidence + OPM/EPS/revision bridge:
    allow Stage2-Actionable.
If C26 has only ad-spend recovery, platform traffic, agency label, or price momentum:
    cap at Stage2 watch or counterexample audit.
If C26 rerates near local/full-window peak after a valid Stage2 bridge:
    allow Stage4B overlay only when non-price valuation/positioning evidence exists.
Do not grant Stage3-Green unless monetization bridge has already become measurable revision or cash-flow evidence.
```

## 18. Before / After Backtest Comparison

| profile | hypothesis | eligible representative triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false-positive rate | score-return alignment |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current calibrated baseline | 4 | 13.43 | -10.81 | 13.43 | -18.53 | 0.50 | mixed; over-credits platform/ad label if bridge absent |
| P0b e2r_2_0_baseline_reference | pre-calibrated reference | 4 | 13.43 | -10.81 | 13.43 | -18.53 | 0.50 | too loose on headline/platform vocabulary |
| P1 sector_specific_candidate_profile | L8 requires monetization/retention bridge | 3 | 17.30 | -5.42 | 17.30 | -8.50 | 0.33 | better precision |
| P2 canonical_archetype_candidate_profile | C26 requires ARPU/OPM/revision bridge | 2 | 25.20 | -4.16 | 25.20 | -6.56 | 0.00 | best alignment |
| P3 counterexample_guard_profile | ad agency/platform label without margin bridge capped | 2 | 25.20 | -4.16 | 25.20 | -6.56 | 0.00 | improves false-positive control |

## 19. Score-Return Alignment Matrix

| case_id | raw component interpretation | before score / stage | proposed score / stage | alignment verdict |
|---|---|---|---|---|
| C26_R8L102_035760_20240123 | traffic/content/ad recovery + monetization path | 77 / Stage2-Actionable | 79 / Stage2-Actionable plus 4B-watch after rerating | aligned if 4B overlay retained |
| C26_R8L102_035720_20240111 | platform/ad label but weak operating leverage bridge | 74 / Stage2 | 67 / capped Stage2-watch | better; blocks false positive |
| C26_R8L102_030000_20240401 | ad agency normalization but no strong revision | 72 / Stage2 | 66 / capped Stage2-watch | better; low MFE path |
| C26_R8L102_214320_20240125 | ad agency operating leverage bridge partly visible | 75 / Stage2-Actionable | 75 / Stage2-Actionable but Green blocked | aligned |

## 20. Raw Component Score Breakdown

| case_id | EPS/revision | visibility | bottleneck/platform | misinformation/label risk | valuation | capital/FCF | info quality | total proxy |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| C26_R8L102_035760_20240123 | 16 | 16 | 13 | 10 | 10 | 6 | 8 | 79 |
| C26_R8L102_035720_20240111 | 10 | 12 | 16 | 16 | 8 | 3 | 2 | 67 |
| C26_R8L102_030000_20240401 | 9 | 14 | 8 | 15 | 10 | 7 | 3 | 66 |
| C26_R8L102_214320_20240125 | 14 | 16 | 9 | 11 | 12 | 8 | 5 | 75 |

## 21. Machine-Readable Rows

```jsonl
{"row_type":"trigger","schema_version":"v12","case_id":"C26_R8L102_035760_20240123","trigger_id":"T_C26_035760_STAGE2A_20240123","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PLATFORM_AD_RECOVERY_OPERATING_LEVERAGE_BRIDGE_VS_AD_RECOVERY_LABEL_AND_MEDIA_AGENCY_FALSE_POSITIVE","symbol":"035760","name":"CJ ENM","trigger_type":"Stage2-Actionable","entry_date":"2024-01-23","entry_price":69900,"mfe_30d_pct":27.75,"mae_30d_pct":-5.72,"mfe_90d_pct":35.77,"mae_90d_pct":-5.72,"mfe_180d_pct":35.77,"mae_180d_pct":-5.72,"peak_date":"2024-05-27","peak_price":94900,"drawdown_after_peak_pct":-27.92,"case_outcome":"positive","current_profile_error":"none_but_needs_4b_overlay","evidence_source_status":"source_proxy_only","evidence_url_pending":true}
{"row_type":"trigger","schema_version":"v12","case_id":"C26_R8L102_035760_20240123","trigger_id":"T_C26_035760_STAGE4B_20240527","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PLATFORM_AD_RECOVERY_OPERATING_LEVERAGE_BRIDGE_VS_AD_RECOVERY_LABEL_AND_MEDIA_AGENCY_FALSE_POSITIVE","symbol":"035760","name":"CJ ENM","trigger_type":"Stage4B","entry_date":"2024-05-27","entry_price":91100,"mfe_30d_pct":4.17,"mae_30d_pct":-24.92,"mfe_90d_pct":4.17,"mae_90d_pct":-24.92,"mfe_180d_pct":4.17,"mae_180d_pct":-24.92,"peak_date":"2024-05-27","peak_price":94900,"drawdown_after_peak_pct":-27.92,"case_outcome":"local_4b_watch","current_profile_error":"needs_local_4b_overlay","evidence_source_status":"source_proxy_only","evidence_url_pending":true}
{"row_type":"trigger","schema_version":"v12","case_id":"C26_R8L102_035720_20240111","trigger_id":"T_C26_035720_STAGE2_20240111","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PLATFORM_AD_RECOVERY_OPERATING_LEVERAGE_BRIDGE_VS_AD_RECOVERY_LABEL_AND_MEDIA_AGENCY_FALSE_POSITIVE","symbol":"035720","name":"카카오","trigger_type":"Stage2","entry_date":"2024-01-11","entry_price":60800,"mfe_30d_pct":1.81,"mae_30d_pct":-15.30,"mfe_90d_pct":1.81,"mae_90d_pct":-26.97,"mfe_180d_pct":1.81,"mae_180d_pct":-45.89,"peak_date":"2024-01-11","peak_price":61900,"drawdown_after_peak_pct":-46.85,"case_outcome":"counterexample","current_profile_error":"false_positive_if_platform_label_overcredited","evidence_source_status":"source_proxy_only","evidence_url_pending":true}
{"row_type":"trigger","schema_version":"v12","case_id":"C26_R8L102_030000_20240401","trigger_id":"T_C26_030000_STAGE2_20240401","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PLATFORM_AD_RECOVERY_OPERATING_LEVERAGE_BRIDGE_VS_AD_RECOVERY_LABEL_AND_MEDIA_AGENCY_FALSE_POSITIVE","symbol":"030000","name":"제일기획","trigger_type":"Stage2","entry_date":"2024-04-01","entry_price":19280,"mfe_30d_pct":1.50,"mae_30d_pct":-4.30,"mfe_90d_pct":1.50,"mae_90d_pct":-7.94,"mfe_180d_pct":1.50,"mae_180d_pct":-13.38,"peak_date":"2024-05-10","peak_price":19570,"drawdown_after_peak_pct":-14.66,"case_outcome":"counterexample","current_profile_error":"low_mfe_ad_agency_label_false_positive","evidence_source_status":"source_proxy_only","evidence_url_pending":true}
{"row_type":"trigger","schema_version":"v12","case_id":"C26_R8L102_214320_20240125","trigger_id":"T_C26_214320_STAGE2A_20240125","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PLATFORM_AD_RECOVERY_OPERATING_LEVERAGE_BRIDGE_VS_AD_RECOVERY_LABEL_AND_MEDIA_AGENCY_FALSE_POSITIVE","symbol":"214320","name":"이노션","trigger_type":"Stage2-Actionable","entry_date":"2024-01-25","entry_price":21200,"mfe_30d_pct":7.55,"mae_30d_pct":-2.59,"mfe_90d_pct":14.62,"mae_90d_pct":-2.59,"mfe_180d_pct":14.62,"mae_180d_pct":-7.41,"peak_date":"2024-05-03","peak_price":24300,"drawdown_after_peak_pct":-19.22,"case_outcome":"positive_mixed","current_profile_error":"stage_cap_ok_green_block_required","evidence_source_status":"source_proxy_only","evidence_url_pending":true}
{"row_type":"aggregate","schema_version":"v12","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","selected_round":"R8","selected_loop":102,"case_count":4,"trigger_count":5,"positive_case_count":2,"counterexample_count":2,"local_4b_watch_count":1,"avg_mfe_90d_pct":13.43,"avg_mae_90d_pct":-10.81,"avg_mfe_180d_pct":13.43,"avg_mae_180d_pct":-18.53,"false_positive_rate":0.50,"shadow_rule_candidate":"C26_platform_ad_operating_leverage_bridge_required"}
{"row_type":"shadow_weight","schema_version":"v12","scope":"canonical_archetype_specific","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","proposed_axis":"C26_platform_ad_operating_leverage_bridge_required","direction":"add_guardrail_not_global_weight_change","effect":"cap platform/ad recovery labels unless ARPU, take-rate, ad yield, OPM, EPS revision, or cash conversion bridge exists"}
{"row_type":"residual_contribution","schema_version":"v12","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","loop_contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":"C26_platform_ad_operating_leverage_bridge_required","existing_axis_strengthened":"price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail","existing_axis_weakened":null}
```

## 22. Residual Contribution Summary

```text
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = C26_platform_ad_operating_leverage_bridge_required
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail
existing_axis_weakened = null
```

This loop contributes four new C26 symbols and five trigger rows. The new axis is not a global scoring rewrite. It is a C26-specific bridge requirement that separates actual platform/ad operating leverage from the surface glitter of ad recovery vocabulary.

## 23. Deferred Coding Agent Handoff Prompt

Do not execute in this research session.

```text
You are the later coding agent for Songdaiki/stock_agent. Read this Markdown as one v12 residual research artifact. Do not treat the rows as production code by themselves. Batch-ingest the machine-readable rows only after parser validation. If accepted, map the proposed canonical shadow rule candidate into the C26 rule registry:

- canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
- proposed_axis: C26_platform_ad_operating_leverage_bridge_required
- action: add guardrail/cap logic, not global weight rewrite
- expected behavior:
  1. If C26 evidence has traffic/ad recovery but lacks ARPU, take-rate, ad yield, OPM, EPS revision, or cash-flow conversion, cap at Stage2-watch.
  2. If C26 evidence has monetization bridge and operating leverage, allow Stage2-Actionable.
  3. Keep Stage3-Green blocked until measurable revision/cash conversion exists.
  4. Preserve local/full-window 4B overlay for post-rerating peaks.

Validate all trigger rows for complete 30D/90D/180D MFE/MAE before ingestion.
```

## 24. Final Notes

This MD is a standalone historical calibration artifact. It does not change production scoring and does not scan live candidates. All price-path claims are based on Songdaiki/stock-web 1D OHLCV shards. Non-price event evidence remains `source_proxy_only / evidence_url_pending=true`, so implementation should use it as a low-trust research row until source URLs are attached in a later batch.
