# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata
```text
selected_round = R8
selected_loop = 156
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id = mixed_c27_game_liveops_console_hit_ott_kdrama_kpop_ip_leaf_set
loop_objective = coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
```

This loop adds 7 new independent C27 cases, 5 counterexamples, and 6 residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C27_CONTENT_IP_GLOBAL_MONETIZATION.

## 1. Current Calibrated Profile Assumption
```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
active_research_mode = post_calibrated_sector_archetype_residual_research
```

The current proxy already blocks price-only blowoff and requires non-price evidence. The remaining C27 problem is narrower: **a global hit is not always retained economics**. A launch chart, viral title, or global OTT ranking can be a bright flare; C27 needs to know whether that flare is attached to a fuel tank: liveops, repeat monetization, direct revenue capture, margin bridge, or contracted platform economics.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R8 |
| loop | 156 |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY |
| canonical_archetype_id | C27_CONTENT_IP_GLOBAL_MONETIZATION |
| fine/deep scope | game liveops, webtoon-IP game launch, China license launch, console one-hit risk, OTT K-drama platform rental, global drama hit margin conversion |
| invalid_round_sector_pair | false |

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index baseline places `C27_CONTENT_IP_GLOBAL_MONETIZATION` at 48 representative rows, 30 symbols, need-to-50 = 2. The session had already cleared C12, C05 and C23, so C27 is the remaining Priority 1 target to push above the 50-row practical calibration line.

Avoided visible top-covered C27 cluster: `293490`, `352820`, `035760`, `035900`, `036420`, `041510`. This pass uses `259960`, `251270`, `194480`, `112040`, `095660`, `253450`, `160550` with new trigger families.

## 4. Stock-Web OHLC Input / Price Source Validation

| item | value |
|---|---|
| source | Songdaiki/stock-web |
| manifest | atlas/manifest.json |
| schema | atlas/schema.json |
| calibration shard root | atlas/ohlcv_tradable_by_symbol_year |
| price basis | tradable_raw |
| price adjustment | raw_unadjusted_marcap |
| max date | 2026-02-20 |

MFE/MAE formula used:

```text
MFE_N_pct = (max high from entry_date through N trading days / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N trading days / entry_price - 1) * 100
entry_price = stock-web tradable row close c on entry_date
```

## 5. Historical Eligibility Gate

All representative trigger rows have:

```text
entry_date present = true
entry_price > 0 = true
forward_window_trading_days >= 180 = true
MFE_30D/90D/180D and MAE_30D/90D/180D present = true
corporate_action_window_status = clean_180D_window
calibration_usable = true
```

## 6. Canonical Archetype Compression Map

| fine/deep leaf | canonical compression | rule implication |
|---|---|---|
| C27_GAME_EVERGREEN_IP_LIVEOPS_GLOBAL_MONETIZATION | C27 | durable liveops + margin bridge can be Stage2-Actionable |
| C27_WEBTOON_IP_GAME_LAUNCH_SPIKE_WITH_RETENTION_RISK | C27 | launch success without retention bridge stays Stage2-Watch |
| C27_GAME_IP_CHINA_LICENSE_LAUNCH_HIGH_MAE_SUCCESS | C27 | regulatory/local partner launch can work but needs staged-entry guard |
| C27_GAME_GLOBAL_LAUNCH_TOKENIZED_MONETIZATION_DECAY | C27 | early sales spike can need 4B overlay |
| C27_CONSOLE_GAME_GLOBAL_SALES_ONE_HIT_RISK | C27 | paid console milestone is not the same as repeat monetization |
| C27_OTT_KDRAMA_GLOBAL_HIT_MARGIN_CONVERSION_GAP | C27 | global rankings need contract/margin capture evidence |
| C27_OTT_KDRAMA_SINGLE_TITLE_PLATFORM_RENTAL_RISK | C27 | single platform title hit is not retained listed-company economics |

## 7. Case Selection Summary

| symbol | company | trigger | trigger_date | entry_date | entry_price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | role | current profile verdict |
|---|---|---|---|---:|---:|---:|---:|---:|---|---|
| 259960 | 크래프톤 | Stage2-Actionable | 2024-05-14 | 2024-05-16 | 258500 | 15.67 / -6.96 | 37.33 / -6.96 | 50.87 / -6.96 | positive | current_profile_correct |
| 251270 | 넷마블 | Stage2 | 2024-05-08 | 2024-05-09 | 64800 | 11.73 / -19.14 | 11.73 / -19.14 | 11.73 / -34.65 | counterexample | current_profile_false_positive |
| 194480 | 데브시스터즈 | Stage2-Actionable | 2023-12-28 | 2024-01-02 | 44750 | 12.85 / -23.8 | 36.76 / -23.8 | 70.5 / -23.8 | positive | current_profile_too_early |
| 112040 | 위메이드 | Stage4B | 2024-03-14 | 2024-03-15 | 56200 | 43.24 / -19.22 | 43.24 / -35.94 | 43.24 / -48.04 | counterexample | current_profile_4B_too_late |
| 095660 | 네오위즈 | Stage2 | 2023-10-17 | 2023-10-18 | 26200 | 18.13 / -7.06 | 18.13 / -13.74 | 18.13 / -27.1 | counterexample | current_profile_false_positive |
| 253450 | 스튜디오드래곤 | Stage2 | 2024-07-08 | 2024-07-09 | 41400 | 1.21 / -20.29 | 12.2 / -20.29 | 26.57 / -20.29 | counterexample | current_profile_false_positive |
| 160550 | NEW | Stage2 | 2023-08-09 | 2023-08-10 | 6670 | 11.54 / -15.74 | 11.54 / -39.28 | 11.54 / -54.87 | counterexample | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 5
4B_watch_or_overlay_count = 6
4C_or_thesis_break_watch_count = 1
current_profile_error_count = 6
```

Positive cases are concentrated where C27 has repeat monetization or hard commercial conversion. Counterexamples are concentrated where a title became culturally visible but the listed company did not retain enough economics, margin, or repeat sales power.

## 9. Evidence Source Map

| case_id | evidence source | evidence family |
|---|---|---|
| C27_R8_L156_259960_KRAFTON_PUBG_BGMI_RECORD_Q1 | https://www.businesswire.com/news/home/20240514074924/en/KRAFTON-Achieves-Record-high-Sales-of-665.9-billion-KRW-in-1Q24 | 1Q24 record quarterly sales and OP; PUBG/BGMI live-service monetization and India/mobile recovery gave repeat monetization evidence. |
| C27_R8_L156_251270_NETMARBLE_SOLO_LEVELING_LAUNCH | https://ch.netmarble.com/Eng/Newsroom/Detail?bbs_code=1020&post_seq=4808 | Solo Leveling: ARISE global launch had strong IP pull and preregistration, but the trigger lacked durable retention, margin and earnings bridge. |
| C27_R8_L156_194480_DEVSISTERS_COOKIE_RUN_CHINA | https://www.businesskorea.co.kr/news/articleView.html?idxno=208789 | Cookie Run: Kingdom China release created real IP localization/partner conversion, but entry timing had severe early MAE before later upside. |
| C27_R8_L156_112040_WEMADE_NIGHT_CROWS_GLOBAL | https://www.wemix.com/news/wemades-night-crows-surpasses-10-million-in-global-sales-within-three-days-after-launch-5a0da7a44044 | Night Crows global exceeded $10m in three days, but the price path showed launch-spike exhaustion and high-MAE decay risk. |
| C27_R8_L156_095660_NEOWIZ_LIES_OF_P_1M | https://www.businesswire.com/news/home/20231016032202/en/Acclaimed-Souls-like-Lies-of-P-Reaches-1-Million-Units-Sold-Less-Than-a-Month-After-Launch | Lies of P reached one million global sales within a month, but paid console success lacked liveops/repeat monetization bridge at the trigger. |
| C27_R8_L156_253450_STUDIO_DRAGON_QOT | https://www.studiodragon.net/en/pr/news/studio-dragon-gains-continuous-success-globally-3-global-ott-topranked-series-in-the-first-half-of-2024/ | Queen of Tears and other series ranked globally, but the trigger still needed production-volume, margin and contract economics bridge. |
| C27_R8_L156_160550_NEW_MOVING_DISNEY | https://en.yna.co.kr/view/AEN20230922004400315 | Moving became a major Disney+/Hulu global/APAC Korean original, but a single platform-commissioned title did not equal retained listed-parent economics. |


## 10. Price Data Source Map

| symbol | entry date | price shard | profile path | corp-action window |
|---|---|---|---|---|
| 259960 | 2024-05-16 | atlas/ohlcv_tradable_by_symbol_year/259/259960/2024.csv | atlas/symbol_profiles/259/259960.json | clean_180D_window |
| 251270 | 2024-05-09 | atlas/ohlcv_tradable_by_symbol_year/251/251270/2024.csv | atlas/symbol_profiles/251/251270.json | clean_180D_window |
| 194480 | 2024-01-02 | atlas/ohlcv_tradable_by_symbol_year/194/194480/2024.csv | atlas/symbol_profiles/194/194480.json | clean_180D_window |
| 112040 | 2024-03-15 | atlas/ohlcv_tradable_by_symbol_year/112/112040/2024.csv | atlas/symbol_profiles/112/112040.json | clean_180D_window |
| 095660 | 2023-10-18 | atlas/ohlcv_tradable_by_symbol_year/095/095660/2023.csv | atlas/symbol_profiles/095/095660.json | clean_180D_window |
| 253450 | 2024-07-09 | atlas/ohlcv_tradable_by_symbol_year/253/253450/2024.csv | atlas/symbol_profiles/253/253450.json | clean_180D_window |
| 160550 | 2023-08-10 | atlas/ohlcv_tradable_by_symbol_year/160/160550/2023.csv | atlas/symbol_profiles/160/160550.json | clean_180D_window |


## 11. Case-by-Case Trigger Grid

### C27-1. 크래프톤 / PUBG-BGMI evergreen liveops
- Verdict: structural_success.
- Mechanism: global IP is not a one-time box-office print; PUBG/BGMI is a live-service cash register. The trigger had sales, OP, and repeat monetization bridge.
- Stress test: current profile mostly correct; C27 gate should preserve this as Stage2-Actionable or Yellow candidate.

### C27-2. 넷마블 / Solo Leveling launch spike
- Verdict: failed_rerating.
- Mechanism: webtoon IP created a visible launch flare, but retention, margin and post-launch revenue bridge were not confirmed at trigger.
- Stress test: current generic content-IP enthusiasm can be too early.

### C27-3. 데브시스터즈 / CookieRun China
- Verdict: high_mae_success.
- Mechanism: China partner launch was real commercialization, but early entry suffered severe MAE before the later 180D MFE. This is not a simple false positive; it is a staged-entry case.

### C27-4. 위메이드 / Night Crows global
- Verdict: 4B_overlay_success.
- Mechanism: sales spike was real, but the listed equity behaved like a launch-heat trade rather than a clean retained-economics rerating.

### C27-5. 네오위즈 / Lies of P one-million milestone
- Verdict: failed_rerating.
- Mechanism: global console success proved product quality, but paid console sales lacked liveops/repeat monetization at trigger.

### C27-6. 스튜디오드래곤 / Queen of Tears global hit
- Verdict: failed_rerating with delayed partial recovery.
- Mechanism: rankings and views were strong, but the conversion problem was contract economics, production volume and margin bridge.

### C27-7. NEW / Moving Disney+ hit
- Verdict: failed_rerating.
- Mechanism: platform hit and cultural impact did not equal retained economics for the listed parent. C27 must separate audience share from shareholder capture.

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | DD after peak |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| TRG_C27_R8_L156_01_259960_STAGE2ACTIONABLE | 259960 | 2024-05-16 | 258500 | 15.67 | -6.96 | 37.33 | -6.96 | 50.87 | -6.96 | 2025-02-10 | 390000 | -19.23 |
| TRG_C27_R8_L156_02_251270_STAGE2 | 251270 | 2024-05-09 | 64800 | 11.73 | -19.14 | 11.73 | -19.14 | 11.73 | -34.65 | 2024-05-10 | 72400 | -41.51 |
| TRG_C27_R8_L156_03_194480_STAGE2ACTIONABLE | 194480 | 2024-01-02 | 44750 | 12.85 | -23.8 | 36.76 | -23.8 | 70.5 | -23.8 | 2024-06-26 | 76300 | -52.75 |
| TRG_C27_R8_L156_04_112040_STAGE4B | 112040 | 2024-03-15 | 56200 | 43.24 | -19.22 | 43.24 | -35.94 | 43.24 | -48.04 | 2024-03-20 | 80500 | -63.73 |
| TRG_C27_R8_L156_05_095660_STAGE2 | 095660 | 2023-10-18 | 26200 | 18.13 | -7.06 | 18.13 | -13.74 | 18.13 | -27.1 | 2023-11-10 | 30950 | -38.29 |
| TRG_C27_R8_L156_06_253450_STAGE2 | 253450 | 2024-07-09 | 41400 | 1.21 | -20.29 | 12.2 | -20.29 | 26.57 | -20.29 | 2025-02-28 | 52400 | -13.17 |
| TRG_C27_R8_L156_07_160550_STAGE2 | 160550 | 2023-08-10 | 6670 | 11.54 | -15.74 | 11.54 | -39.28 | 11.54 | -54.87 | 2023-08-31 | 7440 | -59.54 |


## 13. Current Calibrated Profile Stress Test

| case | expected current-profile behavior | actual path verdict | stress result |
|---|---|---|---|
| KRAFTON | promote because sales/OP bridge exists | high MFE, shallow MAE | current_profile_correct |
| Netmarble | may promote launch IP too early | low MFE, deep 180D MAE | current_profile_false_positive |
| Devsisters | promote but with no timing guard | high MFE after -23.8 MAE | current_profile_too_early |
| Wemade | should add 4B quickly after launch heat | 30D spike then -48.04 MAE | current_profile_4B_too_late |
| Neowiz | may overrate milestone sales | capped MFE, later drawdown | current_profile_false_positive |
| Studio Dragon | may overrate global ranking | drawdown first, delayed recovery | current_profile_false_positive |
| NEW | may overrate title hit | severe 180D drawdown | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is written in this loop. Green would have been too aggressive for all cases except KRAFTON, and even KRAFTON is safer as Stage3-Yellow unless the revision bridge is confirmed. C27 should therefore use:

```text
Stage2-Watch: global launch / chart / platform ranking only
Stage2-Actionable: retained economics + repeat monetization/liveops/contract capture
Stage3-Yellow: verified revenue + OP/revision bridge
Stage3-Green: rare; requires durable repeat monetization and low red-team risk
```

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B evidence | verdict |
|---|---|---|
| 112040 | launch spike, positioning, valuation heat | good local 4B overlay; full-window thesis decayed |
| 251270 | day-after launch peak then persistent drawdown | launch-only Stage2 should be capped; not full 4B without margin evidence |
| 194480 | severe early MAE before later upside | 4B too early would miss later MFE; use staged entry instead |
| 095660 | milestone event cap | one-hit sales milestone should cap promotion |
| 160550 | platform/title event cap | listed-parent economics not retained enough; 4B/4C watch valid |

## 16. 4C Protection Audit

No row is emitted as a hard Stage4C representative. NEW has thesis-break-watch characteristics because the Disney+ hit did not create retained listed-parent economics, but this loop keeps it as Stage2 false-positive / 4C-watch rather than hard 4C. C27 hard 4C should require evidence such as contract cancellation, production slate collapse, license non-renewal, or monetization failure, not merely a stock drawdown.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
sector_specific_rule_candidate = L8_CONTENT_IP_RETAINED_ECONOMICS_AND_LIVEOPS_GATE_V1
```

L8 content/IP should not treat global buzz as equivalent to revenue capture. The sector gate should require at least one hard bridge:

```text
- liveops repeat monetization
- direct publisher revenue / margin bridge
- retained IP economics or royalty participation
- contracted platform economics with visible margin
- launch-to-retention evidence beyond first-week chart rank
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = C27_RETAINED_ECONOMICS_REPEAT_MONETIZATION_AND_ONE_HIT_DECAY_GATE_V1
```

C27 should promote KRAFTON-like evergreen monetization and carefully staged Devsisters-like China IP conversion, while down-routing Netmarble/Neowiz/StudioDragon/NEW-type one-title or launch-only cases until retained economics are visible.

## 19. Before / After Backtest Comparison

| profile | profile_id | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive rate | verdict |
|---|---|---:|---:|---:|---:|---:|---|---|
| P0 | e2r_2_1_stock_web_calibrated_proxy | 7 | 24.42 | -22.74 | 33.23 | -30.82 | 5/7 | weak: many launch-hit false positives remain |
| P0b | e2r_2_0_baseline_reference | 7 | 24.42 | -22.74 | 33.23 | -30.82 | 5/7 | worse: stronger one-hit promotion risk |
| P1 | L8_sector_specific_candidate | 3 | 28.76 | -17.02 | 49.31 | -17.02 | 1/3 | improved but still allows StudioDragon high-MAE watch |
| P2 | C27_canonical_candidate | 2 | 37.05 | -15.38 | 60.69 | -15.38 | 0/2 | best alignment: two real conversion cases only |
| P3 | counterexample_guard_profile | 2 | 37.05 | -15.38 | 60.69 | -15.38 | 0/2 | best risk control; may miss early speculative upside |

## 20. Score-Return Alignment Matrix

| symbol | before stage | after stage | alignment |
|---|---|---|---|
| 259960 | Stage2-Actionable / 80 | Stage3-Yellow / 84 | evergreen_pubg_bgmi_liveops_op_bridge_positive |
| 251270 | Stage2-Actionable / 73 | Stage2-Watch / 58 | global_webtoon_ip_launch_spike_without_durable_margin_bridge |
| 194480 | Stage2-Actionable / 76 | Stage2-Actionable_with_staged_entry_guard / 72 | china_launch_real_ip_conversion_but_requires_staged_entry |
| 112040 | Stage2-Actionable / 77 | Stage4B-Watch / 61 | global_launch_sales_spike_followed_by_monetization_decay_and_high_mae |
| 095660 | Stage2 / 70 | Stage2-Watch / 55 | console_sales_milestone_one_hit_without_liveops_retention |
| 253450 | Stage2 / 69 | Stage2-Watch / 56 | global_ott_hit_without_equity_margin_conversion_at_trigger |
| 160550 | Stage2 / 68 | Stage4B/4C-Watch / 48 | single_title_disney_hit_does_not_equal_retained_ip_economics |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C27_CONTENT_IP_GLOBAL_MONETIZATION | mixed_c27_game_liveops_console_hit_ott_kdrama_kpop_ip_leaf_set | 2 | 5 | 6 | 1 | 7 | 0 | 7 | 7 | 6 | L8_CONTENT_IP_RETAINED_ECONOMICS_AND_LIVEOPS_GATE_V1 | C27_RETAINED_ECONOMICS_REPEAT_MONETIZATION_AND_ONE_HIT_DECAY_GATE_V1 | index baseline 48 -> 55; need_to_50 = 0 |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 7
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 7
new_canonical_archetype_count: 0
new_fine_archetype_count: 7
new_trigger_family_count: 7
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus|price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence|hard_4c_thesis_break_routes_to_4c
residual_error_types_found: ip_launch_false_positive|single_title_no_retained_economics|liveops_margin_bridge_missed|post_launch_high_mae|ott_hit_margin_conversion_gap
new_axis_proposed: c27_retained_economics_repeat_monetization_and_one_hit_decay_gate
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c_should_not_fire_on_single_title_drawdown_alone
existing_axis_kept: stage2_actionable_evidence_bonus|stage3_yellow_total_min|stage3_green_total_min|stage3_green_revision_min
sector_specific_rule_candidate: L8_CONTENT_IP_RETAINED_ECONOMICS_AND_LIVEOPS_GATE_V1
canonical_archetype_rule_candidate: C27_RETAINED_ECONOMICS_REPEAT_MONETIZATION_AND_ONE_HIT_DECAY_GATE_V1
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- historical trigger-level calibration only
- stock-web actual 1D OHLCV only
- 30D/90D/180D MFE/MAE only
- canonical C27 shadow rule candidate only
```

Non-validation scope:

```text
- no live stock recommendation
- no production scoring patch
- no brokerage/API connection
- no non-stock-web price route substitution
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,retained_economics_required,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"one-title/global-rank launch cases produced 5 residual false positives","false positives reduce from 5/7 to 0/2 under strict C27 gate","TRG_C27_R8_L156_01_259960_STAGE2ACTIONABLE|TRG_C27_R8_L156_02_251270_STAGE2|TRG_C27_R8_L156_03_194480_STAGE2ACTIONABLE|TRG_C27_R8_L156_04_112040_STAGE4B|TRG_C27_R8_L156_05_095660_STAGE2|TRG_C27_R8_L156_06_253450_STAGE2|TRG_C27_R8_L156_07_160550_STAGE2",7,7,5,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,liveops_or_repeat_monetization_bonus,sector_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"KRAFTON and Devsisters show better MFE path when repeat monetization/commercial conversion exists","positive cases avg MFE180 60.69 vs all cases avg MFE180 33.23","TRG_C27_R8_L156_01_259960_STAGE2ACTIONABLE|TRG_C27_R8_L156_03_194480_STAGE2ACTIONABLE",2,2,0,medium,sector_shadow_only,"not production; L8/C27 only"
shadow_weight,one_hit_decay_risk_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"console/OTT/single-launch hits had high 180D MAE when retained economics was absent","counterexamples avg MAE180 -36.99","TRG_C27_R8_L156_02_251270_STAGE2|TRG_C27_R8_L156_04_112040_STAGE4B|TRG_C27_R8_L156_05_095660_STAGE2|TRG_C27_R8_L156_06_253450_STAGE2|TRG_C27_R8_L156_07_160550_STAGE2",5,5,5,medium,canonical_shadow_only,"not production; guards Stage2-Actionable"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C27_R8_L156_259960_KRAFTON_PUBG_BGMI_RECORD_Q1","symbol":"259960","company_name":"크래프톤","round":"R8","loop":"156","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_GAME_EVERGREEN_IP_LIVEOPS_GLOBAL_MONETIZATION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"evergreen_pubg_bgmi_liveops_op_bridge_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"1Q24 record quarterly sales and OP; PUBG/BGMI live-service monetization and India/mobile recovery gave repeat monetization evidence."}
{"row_type":"trigger","trigger_id":"TRG_C27_R8_L156_01_259960_STAGE2ACTIONABLE","case_id":"C27_R8_L156_259960_KRAFTON_PUBG_BGMI_RECORD_Q1","symbol":"259960","company_name":"크래프톤","round":"R8","loop":"156","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_GAME_EVERGREEN_IP_LIVEOPS_GLOBAL_MONETIZATION","sector":"platform_content_sw_security","primary_archetype":"content_ip_global_monetization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-14","entry_date":"2024-05-16","entry_price":258500.0,"evidence_available_at_that_date":"1Q24 record quarterly sales and OP; PUBG/BGMI live-service monetization and India/mobile recovery gave repeat monetization evidence.","evidence_source":"https://www.businesswire.com/news/home/20240514074924/en/KRAFTON-Achieves-Record-high-Sales-of-665.9-billion-KRW-in-1Q24","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/259/259960/2024.csv","profile_path":"atlas/symbol_profiles/259/259960.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.67,"MFE_90D_pct":37.33,"MFE_180D_pct":50.87,"MFE_1Y_pct":52.03,"MFE_2Y_pct":null,"MAE_30D_pct":-6.96,"MAE_90D_pct":-6.96,"MAE_180D_pct":-6.96,"MAE_1Y_pct":-6.96,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-10","peak_price":390000.0,"drawdown_after_peak_pct":-19.23,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"overlay_only_or_not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"evergreen_pubg_bgmi_liveops_op_bridge_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION|259960|Stage2-Actionable|2024-05-16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"C27_CONTENT_IP_RETAINED_ECONOMICS_GATE_V1","case_id":"C27_R8_L156_259960_KRAFTON_PUBG_BGMI_RECORD_Q1","trigger_id":"TRG_C27_R8_L156_01_259960_STAGE2ACTIONABLE","symbol":"259960","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":82,"revision_score":78,"relative_strength_score":78,"customer_quality_score":70,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":25,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":85,"retention_or_repeat_monetization_score":88,"platform_revenue_capture_score":80,"one_hit_decay_risk_score":10,"positioning_overheat_score":20},"weighted_score_before":80,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":82,"revision_score":78,"relative_strength_score":78,"customer_quality_score":70,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":25,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":85,"retention_or_repeat_monetization_score":92,"platform_revenue_capture_score":80,"one_hit_decay_risk_score":10,"positioning_overheat_score":20},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow","changed_components":["retention_or_repeat_monetization_score","platform_revenue_capture_score","one_hit_decay_risk_score","positioning_overheat_score"],"component_delta_explanation":"C27 gate requires retained economics/liveops/repeat monetization or direct platform revenue capture before Stage2-Actionable; one-title launch spikes are down-routed to watch/4B.","MFE_90D_pct":37.33,"MAE_90D_pct":-6.96,"score_return_alignment_label":"evergreen_pubg_bgmi_liveops_op_bridge_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C27_R8_L156_251270_NETMARBLE_SOLO_LEVELING_LAUNCH","symbol":"251270","company_name":"넷마블","round":"R8","loop":"156","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_WEBTOON_IP_GAME_LAUNCH_SPIKE_WITH_RETENTION_RISK","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"global_webtoon_ip_launch_spike_without_durable_margin_bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Solo Leveling: ARISE global launch had strong IP pull and preregistration, but the trigger lacked durable retention, margin and earnings bridge."}
{"row_type":"trigger","trigger_id":"TRG_C27_R8_L156_02_251270_STAGE2","case_id":"C27_R8_L156_251270_NETMARBLE_SOLO_LEVELING_LAUNCH","symbol":"251270","company_name":"넷마블","round":"R8","loop":"156","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_WEBTOON_IP_GAME_LAUNCH_SPIKE_WITH_RETENTION_RISK","sector":"platform_content_sw_security","primary_archetype":"content_ip_global_monetization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2024-05-08","entry_date":"2024-05-09","entry_price":64800.0,"evidence_available_at_that_date":"Solo Leveling: ARISE global launch had strong IP pull and preregistration, but the trigger lacked durable retention, margin and earnings bridge.","evidence_source":"https://ch.netmarble.com/Eng/Newsroom/Detail?bbs_code=1020&post_seq=4808","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","price_only_local_peak","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/251/251270/2024.csv","profile_path":"atlas/symbol_profiles/251/251270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.73,"MFE_90D_pct":11.73,"MFE_180D_pct":11.73,"MFE_1Y_pct":11.73,"MFE_2Y_pct":null,"MAE_30D_pct":-19.14,"MAE_90D_pct":-19.14,"MAE_180D_pct":-34.65,"MAE_1Y_pct":-42.13,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-10","peak_price":72400.0,"drawdown_after_peak_pct":-41.51,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"overlay_only_or_not_applicable","four_b_evidence_type":["positioning_overheat","price_only_local_peak","margin_or_backlog_slowdown"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"global_webtoon_ip_launch_spike_without_durable_margin_bridge","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION|251270|Stage2|2024-05-09","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"C27_CONTENT_IP_RETAINED_ECONOMICS_GATE_V1","case_id":"C27_R8_L156_251270_NETMARBLE_SOLO_LEVELING_LAUNCH","trigger_id":"TRG_C27_R8_L156_02_251270_STAGE2","symbol":"251270","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":74,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":68,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":70,"retention_or_repeat_monetization_score":35,"platform_revenue_capture_score":48,"one_hit_decay_risk_score":70,"positioning_overheat_score":74},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":74,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":76,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":70,"retention_or_repeat_monetization_score":35,"platform_revenue_capture_score":48,"one_hit_decay_risk_score":80,"positioning_overheat_score":74},"weighted_score_after":58,"stage_label_after":"Stage2-Watch","changed_components":["retention_or_repeat_monetization_score","platform_revenue_capture_score","one_hit_decay_risk_score","positioning_overheat_score"],"component_delta_explanation":"C27 gate requires retained economics/liveops/repeat monetization or direct platform revenue capture before Stage2-Actionable; one-title launch spikes are down-routed to watch/4B.","MFE_90D_pct":11.73,"MAE_90D_pct":-19.14,"score_return_alignment_label":"global_webtoon_ip_launch_spike_without_durable_margin_bridge","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C27_R8_L156_194480_DEVSISTERS_COOKIE_RUN_CHINA","symbol":"194480","company_name":"데브시스터즈","round":"R8","loop":"156","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_GAME_IP_CHINA_LICENSE_LAUNCH_HIGH_MAE_SUCCESS","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"china_launch_real_ip_conversion_but_requires_staged_entry","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"Cookie Run: Kingdom China release created real IP localization/partner conversion, but entry timing had severe early MAE before later upside."}
{"row_type":"trigger","trigger_id":"TRG_C27_R8_L156_03_194480_STAGE2ACTIONABLE","case_id":"C27_R8_L156_194480_DEVSISTERS_COOKIE_RUN_CHINA","symbol":"194480","company_name":"데브시스터즈","round":"R8","loop":"156","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_GAME_IP_CHINA_LICENSE_LAUNCH_HIGH_MAE_SUCCESS","sector":"platform_content_sw_security","primary_archetype":"content_ip_global_monetization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-12-28","entry_date":"2024-01-02","entry_price":44750.0,"evidence_available_at_that_date":"Cookie Run: Kingdom China release created real IP localization/partner conversion, but entry timing had severe early MAE before later upside.","evidence_source":"https://www.businesskorea.co.kr/news/articleView.html?idxno=208789","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources","repeat_order_or_conversion"],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/194/194480/2024.csv","profile_path":"atlas/symbol_profiles/194/194480.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.85,"MFE_90D_pct":36.76,"MFE_180D_pct":70.5,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-23.8,"MAE_90D_pct":-23.8,"MAE_180D_pct":-23.8,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-26","peak_price":76300.0,"drawdown_after_peak_pct":-52.75,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"overlay_only_or_not_applicable","four_b_evidence_type":["positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"china_launch_real_ip_conversion_but_requires_staged_entry","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION|194480|Stage2-Actionable|2024-01-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"C27_CONTENT_IP_RETAINED_ECONOMICS_GATE_V1","case_id":"C27_R8_L156_194480_DEVSISTERS_COOKIE_RUN_CHINA","trigger_id":"TRG_C27_R8_L156_03_194480_STAGE2ACTIONABLE","symbol":"194480","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":70,"customer_quality_score":70,"policy_or_regulatory_score":65,"valuation_repricing_score":0,"execution_risk_score":55,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":76,"retention_or_repeat_monetization_score":58,"platform_revenue_capture_score":60,"one_hit_decay_risk_score":45,"positioning_overheat_score":55},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":70,"customer_quality_score":70,"policy_or_regulatory_score":65,"valuation_repricing_score":0,"execution_risk_score":55,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":76,"retention_or_repeat_monetization_score":62,"platform_revenue_capture_score":60,"one_hit_decay_risk_score":45,"positioning_overheat_score":55},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable_with_staged_entry_guard","changed_components":["retention_or_repeat_monetization_score","platform_revenue_capture_score","one_hit_decay_risk_score","positioning_overheat_score"],"component_delta_explanation":"C27 gate requires retained economics/liveops/repeat monetization or direct platform revenue capture before Stage2-Actionable; one-title launch spikes are down-routed to watch/4B.","MFE_90D_pct":36.76,"MAE_90D_pct":-23.8,"score_return_alignment_label":"china_launch_real_ip_conversion_but_requires_staged_entry","current_profile_verdict":"current_profile_too_early"}
{"row_type":"case","case_id":"C27_R8_L156_112040_WEMADE_NIGHT_CROWS_GLOBAL","symbol":"112040","company_name":"위메이드","round":"R8","loop":"156","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_GAME_GLOBAL_LAUNCH_TOKENIZED_MONETIZATION_DECAY","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"global_launch_sales_spike_followed_by_monetization_decay_and_high_mae","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Night Crows global exceeded $10m in three days, but the price path showed launch-spike exhaustion and high-MAE decay risk."}
{"row_type":"trigger","trigger_id":"TRG_C27_R8_L156_04_112040_STAGE4B","case_id":"C27_R8_L156_112040_WEMADE_NIGHT_CROWS_GLOBAL","symbol":"112040","company_name":"위메이드","round":"R8","loop":"156","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_GAME_GLOBAL_LAUNCH_TOKENIZED_MONETIZATION_DECAY","sector":"platform_content_sw_security","primary_archetype":"content_ip_global_monetization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-03-14","entry_date":"2024-03-15","entry_price":56200.0,"evidence_available_at_that_date":"Night Crows global exceeded $10m in three days, but the price path showed launch-spike exhaustion and high-MAE decay risk.","evidence_source":"https://www.wemix.com/news/wemades-night-crows-surpasses-10-million-in-global-sales-within-three-days-after-launch-5a0da7a44044","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","valuation_blowoff","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/112/112040/2024.csv","profile_path":"atlas/symbol_profiles/112/112040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":43.24,"MFE_90D_pct":43.24,"MFE_180D_pct":43.24,"MFE_1Y_pct":43.24,"MFE_2Y_pct":null,"MAE_30D_pct":-19.22,"MAE_90D_pct":-35.94,"MAE_180D_pct":-48.04,"MAE_1Y_pct":-49.02,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-20","peak_price":80500.0,"drawdown_after_peak_pct":-63.73,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"overlay_only_or_not_applicable","four_b_evidence_type":["positioning_overheat","valuation_blowoff","price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"global_launch_sales_spike_followed_by_monetization_decay_and_high_mae","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION|112040|Stage4B|2024-03-15","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"C27_CONTENT_IP_RETAINED_ECONOMICS_GATE_V1","case_id":"C27_R8_L156_112040_WEMADE_NIGHT_CROWS_GLOBAL","trigger_id":"TRG_C27_R8_L156_04_112040_STAGE4B","symbol":"112040","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":82,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":75,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":75,"retention_or_repeat_monetization_score":42,"platform_revenue_capture_score":55,"one_hit_decay_risk_score":78,"positioning_overheat_score":85},"weighted_score_before":77,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":82,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":83,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":75,"retention_or_repeat_monetization_score":42,"platform_revenue_capture_score":55,"one_hit_decay_risk_score":88,"positioning_overheat_score":85},"weighted_score_after":61,"stage_label_after":"Stage4B-Watch","changed_components":["retention_or_repeat_monetization_score","platform_revenue_capture_score","one_hit_decay_risk_score","positioning_overheat_score"],"component_delta_explanation":"C27 gate requires retained economics/liveops/repeat monetization or direct platform revenue capture before Stage2-Actionable; one-title launch spikes are down-routed to watch/4B.","MFE_90D_pct":43.24,"MAE_90D_pct":-35.94,"score_return_alignment_label":"global_launch_sales_spike_followed_by_monetization_decay_and_high_mae","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"case","case_id":"C27_R8_L156_095660_NEOWIZ_LIES_OF_P_1M","symbol":"095660","company_name":"네오위즈","round":"R8","loop":"156","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_CONSOLE_GAME_GLOBAL_SALES_ONE_HIT_RISK","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"console_sales_milestone_one_hit_without_liveops_retention","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Lies of P reached one million global sales within a month, but paid console success lacked liveops/repeat monetization bridge at the trigger."}
{"row_type":"trigger","trigger_id":"TRG_C27_R8_L156_05_095660_STAGE2","case_id":"C27_R8_L156_095660_NEOWIZ_LIES_OF_P_1M","symbol":"095660","company_name":"네오위즈","round":"R8","loop":"156","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_CONSOLE_GAME_GLOBAL_SALES_ONE_HIT_RISK","sector":"platform_content_sw_security","primary_archetype":"content_ip_global_monetization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2023-10-17","entry_date":"2023-10-18","entry_price":26200.0,"evidence_available_at_that_date":"Lies of P reached one million global sales within a month, but paid console success lacked liveops/repeat monetization bridge at the trigger.","evidence_source":"https://www.businesswire.com/news/home/20231016032202/en/Acclaimed-Souls-like-Lies-of-P-Reaches-1-Million-Units-Sold-Less-Than-a-Month-After-Launch","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["event_cap","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095660/2023.csv","profile_path":"atlas/symbol_profiles/095/095660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.13,"MFE_90D_pct":18.13,"MFE_180D_pct":18.13,"MFE_1Y_pct":18.13,"MFE_2Y_pct":null,"MAE_30D_pct":-7.06,"MAE_90D_pct":-13.74,"MAE_180D_pct":-27.1,"MAE_1Y_pct":-33.02,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-11-10","peak_price":30950.0,"drawdown_after_peak_pct":-38.29,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"overlay_only_or_not_applicable","four_b_evidence_type":["event_cap","margin_or_backlog_slowdown"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"console_sales_milestone_one_hit_without_liveops_retention","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION|095660|Stage2|2023-10-18","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"C27_CONTENT_IP_RETAINED_ECONOMICS_GATE_V1","case_id":"C27_R8_L156_095660_NEOWIZ_LIES_OF_P_1M","trigger_id":"TRG_C27_R8_L156_05_095660_STAGE2","symbol":"095660","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":66,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":65,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":62,"retention_or_repeat_monetization_score":30,"platform_revenue_capture_score":45,"one_hit_decay_risk_score":72,"positioning_overheat_score":52},"weighted_score_before":70,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":66,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":73,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":62,"retention_or_repeat_monetization_score":30,"platform_revenue_capture_score":45,"one_hit_decay_risk_score":82,"positioning_overheat_score":52},"weighted_score_after":55,"stage_label_after":"Stage2-Watch","changed_components":["retention_or_repeat_monetization_score","platform_revenue_capture_score","one_hit_decay_risk_score","positioning_overheat_score"],"component_delta_explanation":"C27 gate requires retained economics/liveops/repeat monetization or direct platform revenue capture before Stage2-Actionable; one-title launch spikes are down-routed to watch/4B.","MFE_90D_pct":18.13,"MAE_90D_pct":-13.74,"score_return_alignment_label":"console_sales_milestone_one_hit_without_liveops_retention","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C27_R8_L156_253450_STUDIO_DRAGON_QOT","symbol":"253450","company_name":"스튜디오드래곤","round":"R8","loop":"156","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_OTT_KDRAMA_GLOBAL_HIT_MARGIN_CONVERSION_GAP","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"global_ott_hit_without_equity_margin_conversion_at_trigger","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Queen of Tears and other series ranked globally, but the trigger still needed production-volume, margin and contract economics bridge."}
{"row_type":"trigger","trigger_id":"TRG_C27_R8_L156_06_253450_STAGE2","case_id":"C27_R8_L156_253450_STUDIO_DRAGON_QOT","symbol":"253450","company_name":"스튜디오드래곤","round":"R8","loop":"156","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_OTT_KDRAMA_GLOBAL_HIT_MARGIN_CONVERSION_GAP","sector":"platform_content_sw_security","primary_archetype":"content_ip_global_monetization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2024-07-08","entry_date":"2024-07-09","entry_price":41400.0,"evidence_available_at_that_date":"Queen of Tears and other series ranked globally, but the trigger still needed production-volume, margin and contract economics bridge.","evidence_source":"https://www.studiodragon.net/en/pr/news/studio-dragon-gains-continuous-success-globally-3-global-ott-topranked-series-in-the-first-half-of-2024/","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/253/253450/2024.csv","profile_path":"atlas/symbol_profiles/253/253450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.21,"MFE_90D_pct":12.2,"MFE_180D_pct":26.57,"MFE_1Y_pct":37.68,"MFE_2Y_pct":null,"MAE_30D_pct":-20.29,"MAE_90D_pct":-20.29,"MAE_180D_pct":-20.29,"MAE_1Y_pct":-20.29,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-28","peak_price":52400.0,"drawdown_after_peak_pct":-13.17,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"overlay_only_or_not_applicable","four_b_evidence_type":["margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"global_ott_hit_without_equity_margin_conversion_at_trigger","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION|253450|Stage2|2024-07-09","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"C27_CONTENT_IP_RETAINED_ECONOMICS_GATE_V1","case_id":"C27_R8_L156_253450_STUDIO_DRAGON_QOT","trigger_id":"TRG_C27_R8_L156_06_253450_STAGE2","symbol":"253450","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":25,"revision_score":0,"relative_strength_score":62,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":63,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":65,"retention_or_repeat_monetization_score":44,"platform_revenue_capture_score":38,"one_hit_decay_risk_score":58,"positioning_overheat_score":48},"weighted_score_before":69,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":25,"revision_score":0,"relative_strength_score":62,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":71,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":65,"retention_or_repeat_monetization_score":44,"platform_revenue_capture_score":38,"one_hit_decay_risk_score":68,"positioning_overheat_score":48},"weighted_score_after":56,"stage_label_after":"Stage2-Watch","changed_components":["retention_or_repeat_monetization_score","platform_revenue_capture_score","one_hit_decay_risk_score","positioning_overheat_score"],"component_delta_explanation":"C27 gate requires retained economics/liveops/repeat monetization or direct platform revenue capture before Stage2-Actionable; one-title launch spikes are down-routed to watch/4B.","MFE_90D_pct":12.2,"MAE_90D_pct":-20.29,"score_return_alignment_label":"global_ott_hit_without_equity_margin_conversion_at_trigger","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C27_R8_L156_160550_NEW_MOVING_DISNEY","symbol":"160550","company_name":"NEW","round":"R8","loop":"156","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_OTT_KDRAMA_SINGLE_TITLE_PLATFORM_RENTAL_RISK","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"single_title_disney_hit_does_not_equal_retained_ip_economics","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Moving became a major Disney+/Hulu global/APAC Korean original, but a single platform-commissioned title did not equal retained listed-parent economics."}
{"row_type":"trigger","trigger_id":"TRG_C27_R8_L156_07_160550_STAGE2","case_id":"C27_R8_L156_160550_NEW_MOVING_DISNEY","symbol":"160550","company_name":"NEW","round":"R8","loop":"156","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_OTT_KDRAMA_SINGLE_TITLE_PLATFORM_RENTAL_RISK","sector":"platform_content_sw_security","primary_archetype":"content_ip_global_monetization","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2023-08-09","entry_date":"2023-08-10","entry_price":6670.0,"evidence_available_at_that_date":"Moving became a major Disney+/Hulu global/APAC Korean original, but a single platform-commissioned title did not equal retained listed-parent economics.","evidence_source":"https://en.yna.co.kr/view/AEN20230922004400315","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["event_cap","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/160/160550/2023.csv","profile_path":"atlas/symbol_profiles/160/160550.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.54,"MFE_90D_pct":11.54,"MFE_180D_pct":11.54,"MFE_1Y_pct":11.54,"MFE_2Y_pct":null,"MAE_30D_pct":-15.74,"MAE_90D_pct":-39.28,"MAE_180D_pct":-54.87,"MAE_1Y_pct":-66.27,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-31","peak_price":7440.0,"drawdown_after_peak_pct":-59.54,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"overlay_only_or_not_applicable","four_b_evidence_type":["event_cap","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"single_title_disney_hit_does_not_equal_retained_ip_economics","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION|160550|Stage2|2023-08-10","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"C27_CONTENT_IP_RETAINED_ECONOMICS_GATE_V1","case_id":"C27_R8_L156_160550_NEW_MOVING_DISNEY","trigger_id":"TRG_C27_R8_L156_07_160550_STAGE2","symbol":"160550","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":15,"revision_score":0,"relative_strength_score":68,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":80,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":60,"retention_or_repeat_monetization_score":22,"platform_revenue_capture_score":30,"one_hit_decay_risk_score":85,"positioning_overheat_score":55},"weighted_score_before":68,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":15,"revision_score":0,"relative_strength_score":68,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":88,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"commercialization_score":60,"retention_or_repeat_monetization_score":22,"platform_revenue_capture_score":30,"one_hit_decay_risk_score":95,"positioning_overheat_score":55},"weighted_score_after":48,"stage_label_after":"Stage4B/4C-Watch","changed_components":["retention_or_repeat_monetization_score","platform_revenue_capture_score","one_hit_decay_risk_score","positioning_overheat_score"],"component_delta_explanation":"C27 gate requires retained economics/liveops/repeat monetization or direct platform revenue capture before Stage2-Actionable; one-title launch spikes are down-routed to watch/4B.","MFE_90D_pct":11.54,"MAE_90D_pct":-39.28,"score_return_alignment_label":"single_title_disney_hit_does_not_equal_retained_ip_economics","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R8","loop":"156","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","new_independent_case_count":7,"reused_case_count":0,"new_symbol_count":7,"new_trigger_family_count":7,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["ip_launch_false_positive","single_title_no_retained_economics","liveops_margin_bridge_missed","post_launch_high_mae","ott_hit_margin_conversion_gap"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 7
new_weight_evidence_candidate_count: 7
guardrail_candidate_count: 5
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/{prefix}/{ticker}/{year}.csv.
- Symbol profile pattern: atlas/symbol_profiles/{prefix}/{ticker}.json.

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
completed_round = R8
completed_loop = 156
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
next_recommended_archetypes = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|C01_ORDER_BACKLOG_MARGIN_BRIDGE|C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|C06_HBM_MEMORY_CUSTOMER_CAPACITY
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- No-Repeat Index: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- Stock-web schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
