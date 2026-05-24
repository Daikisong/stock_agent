# E2R Stock-Web Historical Calibration / Backtest Optimization Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough
round = R5
loop = 1
sector = 소비재·유통·브랜드
sector_slug = consumer_retail_brands
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
stock_agent_repo_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
output_format = one_standalone_markdown_file
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

이번 R5 Loop 1의 목적은 소비재·유통·브랜드 영역에서 **수출 반복수요, K-beauty/K-food 글로벌 채널 확장, 중국 소비재 회복 기대의 실패**가 실제 가격경로와 어떻게 맞았는지 점검하는 것이다. 이번 파일은 live 후보 탐색이 아니다. 모든 가격 검증은 `Songdaiki/stock-web`의 실제 1D OHLCV row를 기준으로 했다.

## 1. Round Scope

```text
R5 = 소비재·유통·브랜드
primary_focus = export recurring consumer demand / K-food / K-beauty / brand channel expansion / China recovery false-positive
case_count_target = 3_to_5
case_count_used = 3
calibration_usable_case_count = 3
calibration_usable_trigger_count = 9
```

R5의 핵심 질문은 다음과 같다.

```text
- 반복 소비 수요와 해외 채널 확장이 Stage2에서 이미 보였는가?
- Stage3-Green 확인을 기다리면 소비재 대시세의 대부분을 놓치는가?
- K-food/K-beauty처럼 viral/social/channel evidence가 빠르게 숫자로 닫히는 경우 Stage2-Actionable이 더 좋은가?
- 중국 소비 회복/브랜드 프리미엄 기대처럼 narrative가 크지만 숫자가 닫히지 않는 경우 false positive를 어떻게 막을 것인가?
- 4B는 단순 고평가가 아니라 positioning/valuation/expectation crowding이 붙은 overlay로 봐야 하는가?
```

## 2. Stock-Web OHLC Input / Price Source Validation

`Songdaiki/stock-web`에서 매 라운드 필수 파일을 확인했다.

| file | status | key fields checked |
|---|---:|---|
| `atlas/manifest.json` | checked | `source_name=FinanceData/marcap`, `max_date=2026-02-20`, `tradable_row_count=14354401`, `symbol_count=5414`, `calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year` |
| `atlas/schema.json` | checked | tradable columns `d,o,h,l,c,v,a,mc,s,m`, MFE/MAE formulas, corporate action blocking rule |
| `atlas/universe/all_symbols.csv` | checked | symbol/profile path mapping sanity check |
| `diagnostics/chatgpt_bundle.txt` | checked | stock-web smoke bundle and self-test rows |

Price-source validation row:

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 3. Historical Eligibility Gate

| rule | result |
|---|---:|
| trigger date is historical | pass |
| entry date exists in stock-web tradable shard | pass for 9 usable triggers |
| forward 180 trading days available | pass for 9 usable triggers; blocked for late-2025 4B rows |
| OHLCV positive and present | pass |
| corporate action contaminated 180D window | no overlap for selected usable windows |
| production scoring changed | false |

Important caveat: `raw_unadjusted_marcap` is not split-adjusted. The selected usable R5 windows do not overlap each case profile’s listed corporate-action candidate dates. APR has a corporate-action candidate on `2024-10-31`, so pre-2024-10-31 APR windows are not used for weight calibration. APR calibration therefore starts in 2025.

## 4. Canonical Archetypes Tested

| archetype | R5 meaning | tested case |
|---|---|---|
| `EXPORT_RECURRING_CONSUMER` | repeated overseas consumption demand, ASP/channel expansion, export-led OP revision | 삼양식품 / Buldak export cycle |
| `K_BEAUTY_DEVICE_SOCIAL_COMMERCE` | beauty device / DTC / social proof / US channel expansion | 에이피알 / Medicube device cycle |
| `BRAND_CHINA_RECOVERY_FALSE_POSITIVE` | China reopening or premium brand narrative without enough earnings confirmation | F&F / MLB China recovery expectation failure |

## 5. Case Selection Summary

| case_id | symbol | company | case_type | primary_archetype | best_actual_trigger | calibration_usable | score-price alignment |
|---|---:|---|---|---|---|---:|---|
| R5L1_C1_SAMYANG_BULDAK | 003230 | 삼양식품 | structural_success | EXPORT_RECURRING_CONSUMER | T2 Stage2-Actionable | true | score_low_return_high_missed_structural under baseline, corrected by early-evidence profile |
| R5L1_C2_APR_MEDICUBE | 278470 | 에이피알 | structural_success / success_candidate | K_BEAUTY_DEVICE_SOCIAL_COMMERCE | T2 Stage2-Actionable | true | score_mid_return_high_promote_candidate |
| R5L1_C3_FNF_CHINA_BRAND | 383220 | F&F | failed_rerating / false_positive_score | BRAND_CHINA_RECOVERY_FALSE_POSITIVE | no long entry; T6 risk trigger | true | score_high_return_low_false_positive under unguarded brand narrative |

## 6. Evidence Source Map

| case_id | trigger evidence type | evidence source class | evidence confidence | note |
|---|---|---|---:|---|
| R5L1_C1_SAMYANG_BULDAK | Buldak export acceleration, ASP/shipment expansion, operating-profit revision | public news / broker market talk / quarterly earnings / company disclosures | high | Later market talk explicitly tied strong 2Q estimates to exports, ASP, U.S./Europe shipments and capacity; the price path already rewarded earlier export-led evidence. |
| R5L1_C2_APR_MEDICUBE | Medicube beauty-device viral/social proof, overseas channel traction, rapid revenue scale-up | public news / IPO history / overseas K-beauty device articles | medium | 2025 public sources confirmed the mechanism, but early trigger evidence is partially social/channel data rather than a single clean DART-style earnings trigger. Use with guardrail. |
| R5L1_C3_FNF_CHINA_BRAND | China reopening / premium brand expectation without durable revision confirmation | public analyst narrative / price response / later price failure | medium-low | Used as a false-positive counterexample. It is not used to raise weights; it is used to demand numeric confirmation before brand narrative upgrades. |

## 7. Price Data Source Map

| symbol | profile_path | price_shards_used | corporate_action_window_status |
|---:|---|---|---|
| 003230 | `atlas/symbol_profiles/003/003230.json` | `atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv`, `2025.csv` | no 2024~2025 overlap with listed 2003 candidate |
| 278470 | `atlas/symbol_profiles/278/278470.json` | `atlas/ohlcv_tradable_by_symbol_year/278/278470/2025.csv`, `2026.csv` | 2024-10-31 candidate avoided; 2025 windows used |
| 383220 | `atlas/symbol_profiles/383/383220.json` | `atlas/ohlcv_tradable_by_symbol_year/383/383220/2023.csv` | no 2023 overlap with listed 2022 candidate |

## 8. Case-by-Case Trigger Grid

### R5L1_C1_SAMYANG_BULDAK — 삼양식품 / Buldak export rerating

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence available at that date | outcome |
|---|---|---:|---:|---:|---|---|
| R5L1_C1_T1 | Stage2 | 2024-03-04 | 2024-03-04 | 191000 | export momentum + early relative strength; price row confirms volume/price break | good_entry |
| R5L1_C1_T2 | Stage2-Actionable | 2024-03-25 | 2024-03-25 | 206500 | repeated export/ASP/capacity narrative and breakout continuation | excellent_entry |
| R5L1_C1_T4 | Stage3-Green | 2024-05-17 | 2024-05-17 | 446500 | quarterly earnings shock / export-driven OP rerating visible to market | late_but_valid_entry |
| R5L1_C1_T5 | Stage4B-watch | 2024-06-19 | 2024-06-19 | 673000 | parabolic move after export-rerating recognition | too_early_4b_watch |

### R5L1_C2_APR_MEDICUBE — 에이피알 / K-beauty device social-commerce rerating

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence available at that date | outcome |
|---|---|---:|---:|---:|---|---|
| R5L1_C2_T1 | Stage2 | 2025-02-27 | 2025-02-27 | 60100 | early high-volume break after K-beauty device/social proof narrative | good_entry |
| R5L1_C2_T2 | Stage2-Actionable | 2025-03-12 | 2025-03-12 | 67500 | second-leg RS confirmation plus recurring DTC/device demand signal | excellent_entry |
| R5L1_C2_T3 | Stage3-Yellow | 2025-05-08 | 2025-05-08 | 98400 | channel traction / social proof / high-volume reprice | good_entry |
| R5L1_C2_T4 | Stage3-Green | 2025-06-25 | 2025-06-25 | 151600 | multi-month confirmation of rerating thesis | late_entry |
| R5L1_C2_T5 | Stage4B-watch | 2025-11-04 | 2025-11-04 | 276000 | valuation/positioning crowding after multi-bagger | narrative_only_forward_180D_unavailable |

### R5L1_C3_FNF_CHINA_BRAND — F&F / brand-China false-positive

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence available at that date | outcome |
|---|---|---:|---:|---:|---|---|
| R5L1_C3_T1 | Stage2 | 2023-01-31 | 2023-01-31 | 151700 | China reopening / MLB premium-brand expectation, but earnings bridge not closed | bad_entry |
| R5L1_C3_T4 | Stage3-Green-proxy | 2023-04-18 | 2023-04-18 | 149400 | brand narrative persisted without enough durable OP/FCF confirmation | false_positive_score |
| R5L1_C3_T6 | Stage4C-watch | 2023-07-19 | 2023-07-19 | 105300 | price path broke trend; narrative failed to close into positive revision | hard_4c_late |

## 9. Trigger-Level OHLC Backtest Tables

Returns are percentage units. `unavailable` means the forward window is unavailable by stock-web manifest max date or blocked by the case rule.

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MFE_1Y_pct | MFE_2Y_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | MAE_1Y_pct | peak_date | peak_price | drawdown_after_peak_pct | usable |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| R5L1_C1_T1 | 003230 | Stage2 | 2024-03-04 | 191000 | 39.3 | 275.9 | 275.9 | 401.6 | unavailable | -3.7 | -3.7 | -3.7 | -3.7 | 2025-07-11 | 1535000 | -27.0 observed to 2025-12-30 | true |
| R5L1_C1_T2 | 003230 | Stage2-Actionable | 2024-03-25 | 206500 | 43.6 | 247.7 | 247.7 | 364.2 | unavailable | -6.3 | -6.3 | -6.3 | -6.3 | 2025-07-11 | 1535000 | -27.0 observed to 2025-12-30 | true |
| R5L1_C1_T4 | 003230 | Stage3-Green | 2024-05-17 | 446500 | 59.5 | 60.8 | 75.3 | 175.9 | unavailable | 0.0 | 0.0 | 0.0 | 0.0 | 2025-07-11 | 1535000 | -27.0 observed to 2025-12-30 | true |
| R5L1_C1_T5 | 003230 | Stage4B-watch | 2024-06-19 | 673000 | 2.8 | 1.9 | 18.8 | 94.4 | unavailable | -13.1 | -30.3 | -30.3 | -30.3 | 2025-07-11 | 1535000 | -27.0 observed to 2025-12-30 | true |
| R5L1_C2_T1 | 278470 | Stage2 | 2025-02-27 | 60100 | 13.5 | 173.7 | 364.9 | unavailable | unavailable | -4.2 | -4.2 | -4.2 | unavailable | 2026-02-04 | 306500 | -18.3 observed to 2026-02-20 | true |
| R5L1_C2_T2 | 278470 | Stage2-Actionable | 2025-03-12 | 67500 | 8.6 | 143.9 | 314.1 | unavailable | unavailable | -8.4 | -8.4 | -8.4 | unavailable | 2026-02-04 | 306500 | -18.3 observed to 2026-02-20 | true |
| R5L1_C2_T3 | 278470 | Stage3-Yellow | 2025-05-08 | 98400 | 22.7 | 127.6 | 184.0 | unavailable | unavailable | -20.5 | -20.5 | -20.5 | unavailable | 2026-02-04 | 306500 | -18.3 observed to 2026-02-20 | true |
| R5L1_C2_T4 | 278470 | Stage3-Green | 2025-06-25 | 151600 | 20.9 | 74.8 | 102.2 | unavailable | unavailable | -9.0 | -9.0 | -9.0 | unavailable | 2026-02-04 | 306500 | -18.3 observed to 2026-02-20 | true |
| R5L1_C3_T1 | 383220 | Stage2 | 2023-01-31 | 151700 | 2.6 | 2.6 | 2.6 | 2.6 | unavailable | -9.0 | -15.5 | -37.3 | -40.0 | 2023-02-01 | 155500 | -38.8 observed to 2023-07-26 | true |
| R5L1_C3_T4 | 383220 | Stage3-Green-proxy | 2023-04-18 | 149400 | 1.0 | 1.0 | 1.0 | unavailable | unavailable | -10.5 | -36.3 | -36.3 | unavailable | 2023-04-18 | 151500 | -37.2 observed to 2023-07-26 | true |
| R5L1_C3_T6 | 383220 | Stage4C-watch | 2023-07-19 | 105300 | 2.6 | unavailable | unavailable | unavailable | unavailable | -9.8 | unavailable | unavailable | unavailable | 2023-07-31 | 108000 | -11.8 observed to 2023-08-02 | true_for_4C_label_only |

## 10. 1D Price Path Summaries

### Samyang Foods — best Stage2-Actionable T2, entry 2024-03-25 at 206500

| point | date | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|---:|
| D+1 | 2024-03-26 | -0.2 | 2.9 | -1.9 |
| D+5 | 2024-04-01 | 5.6 | 7.5 | -1.9 |
| D+10 | 2024-04-08 | 4.8 | 8.5 | -1.9 |
| D+20 | 2024-04-22 | 41.9 | 41.9 | -1.9 |
| D+30 | 2024-05-03 | 46.7 | 50.4 | -1.9 |
| D+60 | 2024-06-19 | 226.0 | 247.7 | -1.9 |
| D+90 | 2024-07-31 | 198.8 | 247.7 | -1.9 |
| D+180 | 2024-12-13 | 232.7 | 247.7 | -1.9 |
| D+252 | 2025-03-31 | 316.5 | 364.2 | -1.9 |

### APR — best Stage2-Actionable T2, entry 2025-03-12 at 67500

| point | date | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|---:|
| D+1 | 2025-03-13 | 0.3 | 3.0 | -0.7 |
| D+5 | 2025-03-20 | 1.8 | 5.8 | -2.8 |
| D+10 | 2025-03-27 | 5.6 | 7.4 | -2.8 |
| D+20 | 2025-04-11 | 0.4 | 8.6 | -9.2 |
| D+30 | 2025-04-25 | 10.9 | 12.6 | -9.2 |
| D+60 | 2025-06-13 | 94.1 | 102.1 | -9.2 |
| D+90 | 2025-07-31 | 172.1 | 177.8 | -9.2 |
| D+180 | 2025-11-28 | 278.5 | 314.1 | -9.2 |
| D+252 | unavailable | unavailable | unavailable | unavailable |

### F&F — false-positive Stage2 T1, entry 2023-01-31 at 151700

| point | date | close_return_pct | high_to_date_return_pct | low_to_date_return_pct |
|---|---:|---:|---:|---:|
| D+1 | 2023-02-01 | -0.5 | 2.6 | -1.1 |
| D+5 | 2023-02-07 | -1.1 | 2.6 | -3.7 |
| D+10 | 2023-02-14 | 0.1 | 2.6 | -4.0 |
| D+20 | 2023-02-28 | -8.4 | 2.6 | -10.0 |
| D+30 | 2023-03-15 | -12.1 | 2.6 | -14.8 |
| D+60 | 2023-04-28 | -7.1 | 2.6 | -15.5 |
| D+90 | 2023-06-01 | -15.6 | 2.6 | -15.7 |
| D+180 | 2023-08-02 | -32.3 | 2.6 | -37.3 |

## 11. Case Trigger Comparison

| case_id | best_actual_trigger | baseline_selected_trigger | after_selected_trigger | verdict |
|---|---|---|---|---|
| R5L1_C1_SAMYANG_BULDAK | T2 Stage2-Actionable | T4 Stage3-Green | T2 Stage2-Actionable | Green was valid but much too late. Early export + relative strength should promote. |
| R5L1_C2_APR_MEDICUBE | T2 Stage2-Actionable | T4 Stage3-Green | T2 Stage2-Actionable | Social-commerce/device evidence plus RS beat late confirmation. Needs volatility guardrail. |
| R5L1_C3_FNF_CHINA_BRAND | no long entry / T6 risk | T4 Green-proxy | rejected by China-brand guardrail | Narrative-only China recovery should not become Green without OP/revision bridge. |

## 12. Stage2 → Stage4 Audit

1. **Stage2 trigger MFE was large?** Samyang and APR both produced very large Stage2/Stage2-Actionable MFE: Samyang T2 MFE90 247.7%, APR T2 MFE90 143.9%.
2. **Stage2 MAE tolerable?** Samyang T2 MAE90 -6.3%, APR T2 MAE90 -8.4%, both tolerable for early-stage consumer export winners.
3. **Stage2 better than Green?** Yes. Samyang Green entry at 446500 already consumed about 26.3% of the observed move from T2 entry to peak. APR Green entry at 151600 consumed about 42.2% of the observed move from T2 to observed peak.
4. **What made Stage2 good?** Evidence was not “brand is popular” alone. It was brand popularity plus repeated overseas demand, visible price relative strength, channel/ASP/volume bridge, and later operating-profit revision.
5. **Where Stage2 failed?** F&F showed that brand narrative without OP/revision/channel confirmation becomes a false-positive score. The price path quickly turned into deep MAE.

Shadow conclusion:

```text
old_gate_problem = Stage3_gate_too_late for export-recurring consumer winners
new_shadow_rule = promote_to_Stage2_Actionable_when_export_or_channel_evidence + RS + margin/OP bridge are present
counter_guardrail = reject China/brand recovery narrative without numerical OP/revision evidence
```

## 13. Stage3 Yellow / Green Lateness Audit

| case_id | Stage2_Actionable_entry | Stage3_Green_entry | observed_peak_after_stage2 | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| R5L1_C1_SAMYANG_BULDAK | 206500 | 446500 | 1535000 | 0.18 | Green not disastrous, but early-actionable captured much more upside. |
| R5L1_C2_APR_MEDICUBE | 67500 | 151600 | 306500 | 0.35 | Green materially late; Yellow/Actionable is more useful. |
| R5L1_C3_FNF_CHINA_BRAND | not valid | 149400 | 151500 | not_applicable | Green-proxy was false-positive; do not relax without guardrail. |

## 14. 4B Timing Audit

| case_id | 4B trigger | 4B entry | Stage2_Actionable entry | observed_peak | four_b_peak_proximity | verdict |
|---|---|---:|---:|---:|---:|---|
| R5L1_C1_SAMYANG_BULDAK | 2024-06-19 | 673000 | 206500 | 1535000 | 0.31 | Too early if used as exit. Should be Stage3 + 4B-watch only. |
| R5L1_C2_APR_MEDICUBE | 2025-11-04 | 276000 | 67500 | 306500 | 0.87 | Good 4B-watch timing, but forward 180D unavailable by manifest max date. |
| R5L1_C3_FNF_CHINA_BRAND | 2023-04-18 false Green | 149400 | not valid | 151500 | not_applicable | 4B not the issue; this was false-positive Green / 4C protection problem. |

4B rule implication: in viral consumer reratings, early overheat should not force full exit if the evidence bridge remains intact. It should create `Stage3 + 4B-watch`, not downgrade the core thesis.

## 15. 4C Protection Audit

| case_id | 4C candidate | protection label | note |
|---|---|---|---|
| R5L1_C1_SAMYANG_BULDAK | none confirmed | thesis_intact_through_test_window | Drawdown after peak exists but no confirmed thesis break in tested window. |
| R5L1_C2_APR_MEDICUBE | none confirmed | thesis_intact_but_valuation_watch | Late-2025/early-2026 valuation risk, not hard 4C. |
| R5L1_C3_FNF_CHINA_BRAND | 2023-07-19 | hard_4c_late | Price drawdown had already occurred. Earlier guardrail should have blocked Green-proxy before July. |

## 16. Baseline Score Simulation

Baseline current proxy assumptions:

```text
profile_id = baseline_current_proxy
profile_role = reference_only
production_scoring_changed = false
```

| case_id | baseline_selected_trigger | baseline_stage | baseline_entry | baseline_MFE90 | baseline_MAE90 | baseline failure mode |
|---|---|---|---:|---:|---:|---|
| R5L1_C1_SAMYANG_BULDAK | T4 | Stage3-Green | 446500 | 60.8 | 0.0 | late_green |
| R5L1_C2_APR_MEDICUBE | T4 | Stage3-Green | 151600 | 74.8 | -9.0 | late_green |
| R5L1_C3_FNF_CHINA_BRAND | T4 | Stage3-Green-proxy | 149400 | 1.0 | -36.3 | false_positive_score |

Baseline verdict: safe confirmation improves confidence but loses too much upside in structural export/viral consumer winners, while still failing to reject brand narrative without numerical confirmation.

## 17. Shadow Profile Optimization Loop

| profile_id | hypothesis | selected triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---|---:|---:|---:|---|
| P0_baseline_current_proxy | wait for Green confirmation | C1_T4, C2_T4, C3_T4 | 45.5 | -15.1 | 33.3% | reference only |
| P1_stage2_actionable_early_evidence_plus_with_channel_guardrail | promote early export/channel evidence + RS; reject narrative-only China/brand | C1_T2, C2_T2; reject C3 | 195.9 | -7.4 | 0.0% | best profile |
| P2_stage3_yellow_entry_relaxed | allow Yellow when OP/channel bridge partially closes | C1_T4, C2_T3; reject C3 | 94.2 | -10.3 | 0.0% | improved but less upside than P1 |
| P3_green_confirmation_timing_relaxed | move Green earlier once 2 evidence axes close | C1_T2/T4 hybrid, C2_T3, reject C3 | 124.9 | -9.1 | 0.0% | useful fallback |
| P4_four_b_peak_timing_tuned | avoid full-exit 4B before evidence deterioration | C1_T5 watch only, C2_T5 watch only | not_entry_profile | not_entry_profile | n/a | accepted for overlay logic |
| P5_four_c_thesis_break_earlier | block Green when brand narrative lacks revision bridge and MAE breaks trend | reject C3_T4 before 90D damage | avoided_bad_entry | avoided_bad_entry | 0.0% | accepted |

Best profile:

```text
best_shadow_profile = stage2_actionable_early_evidence_plus_with_recurring_export_and_channel_guardrail
```

## 18. Before / After Backtest Comparison

| case_id | best_actual_trigger | baseline_selected_trigger | after_selected_trigger | baseline_entry_price | after_entry_price | baseline_MFE90 | after_MFE90 | baseline_MAE90 | after_MAE90 | return_improvement_90D | risk_change_90D | reason_after_profile_selected |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| R5L1_C1_SAMYANG_BULDAK | C1_T2 | C1_T4 | C1_T2 | 446500 | 206500 | 60.8 | 247.7 | 0.0 | -6.3 | +186.9 | -6.3 | Export/channel evidence plus RS was already sufficient before Green. |
| R5L1_C2_APR_MEDICUBE | C2_T2 | C2_T4 | C2_T2 | 151600 | 67500 | 74.8 | 143.9 | -9.0 | -8.4 | +69.1 | +0.6 | Social-commerce/device evidence became actionable before full confirmation. |
| R5L1_C3_FNF_CHINA_BRAND | no long | C3_T4 | reject | 149400 | unavailable | 1.0 | avoided | -36.3 | avoided | avoided false positive | +36.3 | China-brand narrative lacked numeric OP/revision bridge. |

Natural-language interpretation: the adjustment works because it separates **repeatable consumer evidence** from **brand story**. Buldak and Medicube had demand/channel/RS mechanisms that behaved like a widening road before traffic was fully counted. F&F had a signboard saying “China recovery” but no reliable traffic count; the guardrail prevents the agent from treating a signboard as a highway.

## 19. Score-Return Alignment Matrix

| alignment_label | trigger_count | avg_weighted_score_before | avg_weighted_score_after | avg_MFE90 | avg_MAE90 | verdict |
|---|---:|---:|---:|---:|---:|---|
| score_mid_return_high_promote_candidate | 4 | 71 | 83 | 182.9 | -7.4 | Promote early evidence when channel/OP bridge exists. |
| score_high_return_high | 2 | 86 | 89 | 67.9 | -4.5 | Green remains useful but should not be the first entry tier. |
| score_high_return_low_false_positive | 1 | 84 | 58 | 1.0 | -36.3 | China-brand narrative must be downgraded without revision bridge. |
| score_mid_return_low_watch_only | 2 | 68 | 61 | 2.6 | -24.0 | Watch-only when evidence is narrative or recovery-beta. |

## 20. Weight Sensitivity Table

| axis | baseline | tested | delta | affected_trigger_ids | avg_MFE90_before | avg_MFE90_after | avg_MAE90_before | avg_MAE90_after | false_positive_before | false_positive_after | verdict |
|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---|
| recurring_export_channel_evidence | 0 | +2 | +2 | C1_T2,C2_T2 | 67.9 | 195.9 | -4.5 | -7.4 | 0 | 0 | accepted_positive_adjustment |
| relative_strength_with_volume_confirmation | 0 | +1 | +1 | C1_T2,C2_T2 | 67.9 | 195.9 | -4.5 | -7.4 | 0 | 0 | accepted_exploratory_adjustment |
| China_brand_recovery_without_revision_bridge | 0 | -3 | -3 | C3_T1,C3_T4 | 1.8 | rejected | -25.9 | avoided | 1 | 0 | accepted_guardrail |

## 21. Optimization Decision Log

```jsonl
{"row_type":"optimization_decision","decision_id":"R5L1_DECISION_001","hypothesis":"Export/channel recurring consumer evidence plus RS should promote Stage2-Actionable before full Green.","tested_cases":["R5L1_C1_SAMYANG_BULDAK","R5L1_C2_APR_MEDICUBE"],"tested_trigger_ids":["R5L1_C1_T2","R5L1_C2_T2"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus_with_recurring_export_and_channel_guardrail","backtest_result_summary":"After profile selected earlier triggers with avg MFE90 195.9% and avg MAE90 -7.4%, versus baseline avg MFE90 67.9% for the comparable Green entries.","accepted_or_rejected":"accepted","delta_magnitude":"+2","why_not_larger_delta":"Only two high-quality structural success cases in this R5 loop; broader consumer sub-archetype validation is still needed.","next_validation_needed":"Find more K-food, K-beauty, and export-brand counterexamples with complete evidence dates."}
{"row_type":"optimization_decision","decision_id":"R5L1_DECISION_002","hypothesis":"Brand/China recovery narrative without OP/revision bridge should not become Green.","tested_cases":["R5L1_C3_FNF_CHINA_BRAND"],"tested_trigger_ids":["R5L1_C3_T1","R5L1_C3_T4"],"baseline_profile":"baseline_current_proxy","selected_profile":"stage2_actionable_early_evidence_plus_with_recurring_export_and_channel_guardrail","backtest_result_summary":"F&F Green-proxy produced MFE90 1.0% and MAE90 -36.3%; after profile rejects it as watch-only/4C-watch.","accepted_or_rejected":"accepted","delta_magnitude":"-3","why_not_larger_delta":"Single failed case; use as guardrail, not universal penalty.","next_validation_needed":"Validate against additional China-consumer recovery cases."}
{"row_type":"optimization_decision","decision_id":"R5L1_DECISION_003","hypothesis":"Early 4B in viral consumer winners should be overlay-only unless evidence deterioration appears.","tested_cases":["R5L1_C1_SAMYANG_BULDAK","R5L1_C2_APR_MEDICUBE"],"tested_trigger_ids":["R5L1_C1_T5","R5L1_C2_T5"],"baseline_profile":"baseline_current_proxy","selected_profile":"four_b_peak_timing_tuned","backtest_result_summary":"Samyang 2024-06-19 4B-watch was too early: later observed peak was much higher. APR late-2025 4B-watch was closer to peak but forward 180D unavailable.","accepted_or_rejected":"accepted_as_overlay","delta_magnitude":"+1 threshold patience","why_not_larger_delta":"4B is timing-sensitive and one APR 4B row lacks 180D forward window.","next_validation_needed":"Require 4B validation with complete forward windows."}
```

## 22. Overfitting / Robustness Check

```text
usable_case_count = 3
usable_trigger_count = 9
structural_success_cases = 2
false_positive_counterexample_cases = 1
max_abs_delta_allowed = 2_or_3
selected_positive_delta = +2
selected_guardrail_delta = -3
production_scoring_changed = false
```

Robustness notes:

- Positive early-evidence promotion is accepted only at +2 because R5 Loop 1 has two structural success cases, not five or more.
- China-brand recovery penalty is -3 because the F&F false positive is severe, but it should be encoded as a guardrail rather than a broad consumer-sector penalty.
- APR’s 2024 corporate-action candidate date is avoided by using 2025 triggers only.
- APR 1Y/2Y fields are unavailable for 2025 entries where the stock-web manifest max date cannot provide the full forward window.

## 23. Cross-case Aggregate Metrics

### Trigger type aggregate

| trigger_type | usable_trigger_count | avg_MFE90 | median_MFE90 | avg_MAE90 | median_MAE90 | avg_MFE180 | avg_MAE180 | below_entry_90D_rate | avg_green_lateness_ratio | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Stage2 / Stage2-Actionable | 4 | 142.5 | 162.0 | -7.1 | -6.9 | 235.6 | -7.1 | 50.0% | n/a | Best entry tier when guarded. |
| Stage3-Yellow | 1 | 127.6 | 127.6 | -20.5 | -20.5 | 184.0 | -20.5 | 100.0% | n/a | Useful but volatile for APR. |
| Stage3-Green / Green-proxy | 3 | 45.5 | 60.8 | -15.1 | -9.0 | 58.8 | -15.1 | 33.3% | 0.265 structural-only | Too late for winners; false-positive for narrative. |
| Stage4B-watch | 1 usable + 1 narrative-only | 1.9 | 1.9 | -30.3 | -30.3 | 18.8 | -30.3 | 100.0% | n/a | Overlay-only, not automatic exit. |
| Stage4C-watch | 1 label-only | unavailable | unavailable | unavailable | unavailable | unavailable | unavailable | n/a | n/a | Useful as protection label after failed narrative. |

### Profile aggregate

| profile_id | case_count | selected_trigger_count | avg_MFE90 | median_MFE90 | avg_MAE90 | median_MAE90 | avg_MFE180 | avg_MAE180 | hit_rate_MFE90_gt_20 | bad_entry_rate_MAE90_lt_minus_15 | false_positive_rate | missed_structural_count | late_green_count | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| baseline_current_proxy | 3 | 3 | 45.5 | 60.8 | -15.1 | -9.0 | 58.8 | -15.1 | 66.7% | 33.3% | 33.3% | 2 | 2 | reference |
| stage2_actionable_early_evidence_plus_with_recurring_export_and_channel_guardrail | 3 | 2 | 195.9 | 195.9 | -7.4 | -7.4 | 157.4 | -7.4 | 100.0% | 0.0% | 0.0% | 0 | 0 | best |
| stage3_yellow_entry_relaxed | 3 | 2 | 94.2 | 94.2 | -10.3 | -10.3 | 129.7 | -10.3 | 100.0% | 50.0% | 0.0% | 0 | 1 | acceptable but more volatile |
| green_confirmation_timing_relaxed | 3 | 2 | 124.9 | 124.9 | -9.1 | -9.1 | 150.0 | -9.1 | 100.0% | 0.0% | 0.0% | 0 | 1 | accepted fallback |
| four_b_peak_timing_tuned | 2 | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | overlay-only |
| four_c_thesis_break_earlier | 1 | 0 | avoided | avoided | avoided | avoided | avoided | avoided | n/a | n/a | 0.0% | n/a | n/a | guardrail accepted |

## 24. Score-Price Alignment Verdict

```text
overall_verdict = early consumer export/channel evidence was underweighted by baseline proxy
winner_pattern = export/social/channel evidence + relative strength + later OP bridge
loser_pattern = brand or China recovery story without numeric revision bridge
production_scoring_changed = false
shadow_weight_only = true
```

The main calibration result is not simply “raise consumer stocks earlier.” It is narrower: **raise Stage2 evidence only when recurring export/channel demand and price relative strength are both present, and do not raise China-brand recovery narratives without OP/revision confirmation.**

## 25. Shadow Weight Calibration

```csv
row_type,axis,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,notes
shadow_weight,recurring_export_channel_evidence,0,2,+2,"Samyang and APR Stage2-Actionable triggers produced materially higher MFE than Green with tolerable MAE","Comparable selected-entry avg_MFE90 improved from 67.9 to 195.9 while avg_MAE90 moved from -4.5 to -7.4","R5L1_C1_T2|R5L1_C2_T2",2,"shadow-only; not production"
shadow_weight,relative_strength_with_volume_confirmation,0,1,+1,"Consumer export winners repriced before full earnings confirmation; volume/RS helped distinguish real demand from narrative","Improved early trigger selection in both structural success cases","R5L1_C1_T2|R5L1_C2_T2",2,"exploratory; require more cases"
shadow_weight,China_brand_recovery_without_revision_bridge,0,-3,-3,"F&F Green-proxy had MFE90 1.0 and MAE90 -36.3, showing narrative-only China recovery risk","Rejected bad entry and avoided false_positive_score","R5L1_C3_T1|R5L1_C3_T4",2,"guardrail; not broad consumer-sector penalty"
```

## 26. Machine-Readable Rows

### 26.1 Case rows JSONL

```jsonl
{"row_type":"case","case_id":"R5L1_C1_SAMYANG_BULDAK","symbol":"003230","company_name":"삼양식품","round":"R5","loop":"1","sector":"소비재·유통·브랜드","case_type":"structural_success","primary_archetype":"EXPORT_RECURRING_CONSUMER","best_trigger":"R5L1_C1_T2","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"score_low_return_high_missed_structural_under_baseline","price_source":"Songdaiki/stock-web","notes":"Buldak export/ASP/channel evidence became actionable before Green."}
{"row_type":"case","case_id":"R5L1_C2_APR_MEDICUBE","symbol":"278470","company_name":"에이피알","round":"R5","loop":"1","sector":"소비재·유통·브랜드","case_type":"structural_success_candidate","primary_archetype":"K_BEAUTY_DEVICE_SOCIAL_COMMERCE","best_trigger":"R5L1_C2_T2","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"score_mid_return_high_promote_candidate","price_source":"Songdaiki/stock-web","notes":"2025 triggers avoid 2024 corporate-action candidate window."}
{"row_type":"case","case_id":"R5L1_C3_FNF_CHINA_BRAND","symbol":"383220","company_name":"F&F","round":"R5","loop":"1","sector":"소비재·유통·브랜드","case_type":"failed_rerating_false_positive","primary_archetype":"BRAND_CHINA_RECOVERY_FALSE_POSITIVE","best_trigger":"none_long_entry","calibration_usable":true,"historical_window_status":"180D_available","score_price_alignment":"score_high_return_low_false_positive","price_source":"Songdaiki/stock-web","notes":"Brand narrative without OP/revision bridge produced deep MAE."}
```

### 26.2 Trigger rows JSONL

```jsonl
{"row_type":"trigger","trigger_id":"R5L1_C1_T2","case_id":"R5L1_C1_SAMYANG_BULDAK","symbol":"003230","company_name":"삼양식품","round":"R5","loop":"1","sector":"소비재·유통·브랜드","primary_archetype":"EXPORT_RECURRING_CONSUMER","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-25","entry_date":"2024-03-25","entry_price":206500,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv","profile_path":"atlas/symbol_profiles/003/003230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":43.6,"MFE_90D_pct":247.7,"MFE_180D_pct":247.7,"MFE_1Y_pct":364.2,"MFE_2Y_pct":"unavailable","MAE_30D_pct":-6.3,"MAE_90D_pct":-6.3,"MAE_180D_pct":-6.3,"MAE_1Y_pct":-6.3,"peak_date":"2025-07-11","peak_price":1535000,"drawdown_after_peak_pct":-27.0,"green_lateness_ratio":0.18,"four_b_peak_proximity":"not_applicable","trigger_outcome_label":"excellent_entry","calibration_usable":true,"forward_window_trading_days":252,"calibration_block_reasons":[]}
{"row_type":"trigger","trigger_id":"R5L1_C1_T4","case_id":"R5L1_C1_SAMYANG_BULDAK","symbol":"003230","trigger_type":"Stage3-Green","trigger_date":"2024-05-17","entry_date":"2024-05-17","entry_price":446500,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv","profile_path":"atlas/symbol_profiles/003/003230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_90D_pct":60.8,"MAE_90D_pct":0.0,"trigger_outcome_label":"late_but_valid_entry","calibration_usable":true,"forward_window_trading_days":252,"calibration_block_reasons":[]}
{"row_type":"trigger","trigger_id":"R5L1_C2_T2","case_id":"R5L1_C2_APR_MEDICUBE","symbol":"278470","company_name":"에이피알","round":"R5","loop":"1","sector":"소비재·유통·브랜드","primary_archetype":"K_BEAUTY_DEVICE_SOCIAL_COMMERCE","trigger_type":"Stage2-Actionable","trigger_date":"2025-03-12","entry_date":"2025-03-12","entry_price":67500,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/278/278470/2025.csv","profile_path":"atlas/symbol_profiles/278/278470.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":8.6,"MFE_90D_pct":143.9,"MFE_180D_pct":314.1,"MFE_1Y_pct":"unavailable","MFE_2Y_pct":"unavailable","MAE_30D_pct":-8.4,"MAE_90D_pct":-8.4,"MAE_180D_pct":-8.4,"MAE_1Y_pct":"unavailable","peak_date":"2026-02-04","peak_price":306500,"drawdown_after_peak_pct":-18.3,"green_lateness_ratio":0.35,"four_b_peak_proximity":"not_applicable","trigger_outcome_label":"excellent_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[]}
{"row_type":"trigger","trigger_id":"R5L1_C2_T4","case_id":"R5L1_C2_APR_MEDICUBE","symbol":"278470","trigger_type":"Stage3-Green","trigger_date":"2025-06-25","entry_date":"2025-06-25","entry_price":151600,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/278/278470/2025.csv","profile_path":"atlas/symbol_profiles/278/278470.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_90D_pct":74.8,"MAE_90D_pct":-9.0,"trigger_outcome_label":"late_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[]}
{"row_type":"trigger","trigger_id":"R5L1_C3_T4","case_id":"R5L1_C3_FNF_CHINA_BRAND","symbol":"383220","company_name":"F&F","round":"R5","loop":"1","sector":"소비재·유통·브랜드","primary_archetype":"BRAND_CHINA_RECOVERY_FALSE_POSITIVE","trigger_type":"Stage3-Green-proxy","trigger_date":"2023-04-18","entry_date":"2023-04-18","entry_price":149400,"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/383/383220/2023.csv","profile_path":"atlas/symbol_profiles/383/383220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_90D_pct":1.0,"MAE_90D_pct":-36.3,"MFE_180D_pct":1.0,"MAE_180D_pct":-36.3,"peak_date":"2023-04-18","peak_price":151500,"drawdown_after_peak_pct":-37.2,"trigger_outcome_label":"false_positive_score","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[]}
```

### 26.3 Score simulation rows JSONL

```jsonl
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R5L1_C1_SAMYANG_BULDAK","trigger_id":"R5L1_C1_T4","symbol":"003230","trigger_type":"Stage3-Green","weighted_score":86,"stage_label":"Stage3-Green","selected_by_profile":true,"MFE_90D_pct":60.8,"MAE_90D_pct":0.0,"score_return_alignment_label":"score_high_return_high_but_late"}
{"row_type":"score_simulation","profile_id":"stage2_actionable_early_evidence_plus_with_recurring_export_and_channel_guardrail","case_id":"R5L1_C1_SAMYANG_BULDAK","trigger_id":"R5L1_C1_T2","symbol":"003230","trigger_type":"Stage2-Actionable","weighted_score":83,"stage_label":"Stage2-Actionable","selected_by_profile":true,"MFE_90D_pct":247.7,"MAE_90D_pct":-6.3,"score_return_alignment_label":"score_mid_return_high_promote_candidate"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R5L1_C2_APR_MEDICUBE","trigger_id":"R5L1_C2_T4","symbol":"278470","trigger_type":"Stage3-Green","weighted_score":85,"stage_label":"Stage3-Green","selected_by_profile":true,"MFE_90D_pct":74.8,"MAE_90D_pct":-9.0,"score_return_alignment_label":"score_high_return_high_but_late"}
{"row_type":"score_simulation","profile_id":"stage2_actionable_early_evidence_plus_with_recurring_export_and_channel_guardrail","case_id":"R5L1_C2_APR_MEDICUBE","trigger_id":"R5L1_C2_T2","symbol":"278470","trigger_type":"Stage2-Actionable","weighted_score":81,"stage_label":"Stage2-Actionable","selected_by_profile":true,"MFE_90D_pct":143.9,"MAE_90D_pct":-8.4,"score_return_alignment_label":"score_mid_return_high_promote_candidate"}
{"row_type":"score_simulation","profile_id":"baseline_current_proxy","case_id":"R5L1_C3_FNF_CHINA_BRAND","trigger_id":"R5L1_C3_T4","symbol":"383220","trigger_type":"Stage3-Green-proxy","weighted_score":84,"stage_label":"Stage3-Green","selected_by_profile":true,"MFE_90D_pct":1.0,"MAE_90D_pct":-36.3,"score_return_alignment_label":"score_high_return_low_false_positive"}
{"row_type":"score_simulation","profile_id":"stage2_actionable_early_evidence_plus_with_recurring_export_and_channel_guardrail","case_id":"R5L1_C3_FNF_CHINA_BRAND","trigger_id":"R5L1_C3_T4","symbol":"383220","trigger_type":"Stage3-Green-proxy","weighted_score":58,"stage_label":"WatchOnly_or_Reject","selected_by_profile":false,"MFE_90D_pct":1.0,"MAE_90D_pct":-36.3,"score_return_alignment_label":"score_mid_return_low_watch_only"}
```

### 26.4 Profile comparison rows CSV

```csv
row_type,profile_id,case_count,selected_trigger_count,avg_MFE_90D_pct,avg_MAE_90D_pct,hit_rate_MFE90_gt_20pct,bad_entry_rate_MAE90_lt_minus_15pct,false_positive_rate,missed_structural_count,late_green_count,verdict
profile_comparison,baseline_current_proxy,3,3,45.5,-15.1,0.667,0.333,0.333,2,2,"reference; late and one false positive"
profile_comparison,stage2_actionable_early_evidence_plus_with_recurring_export_and_channel_guardrail,3,2,195.9,-7.4,1.0,0.0,0.0,0,0,"best; improved upside capture and avoided false positive"
profile_comparison,stage3_yellow_entry_relaxed,3,2,94.2,-10.3,1.0,0.5,0.0,0,1,"acceptable but volatile"
```

### 26.5 Narrative-only rows JSONL

```jsonl
{"row_type":"narrative_only","case_id":"R5L1_C2_APR_MEDICUBE","symbol":"278470","trigger_id":"R5L1_C2_T5","reason":"4B-watch trigger on 2025-11-04 lacks forward 180D by stock-web manifest max_date 2026-02-20","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 27. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are standalone E2R historical calibration and backtest optimization outputs produced using the Songdaiki/stock-web OHLC atlas. Do not redo market research unless a row is internally inconsistent. Ingest the machine-readable rows and update the repository in batch.

These MD files are not live candidate research. They are historical calibration and shadow optimization research. Use them to improve trigger-level backtesting, Stage2-Actionable / Stage3-Yellow gates, 4B timing, 4C protection logic, score-return alignment evaluation, and shadow score profiles.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.
- Manifest and schema were used to validate max_date, column mapping, and calibration rules.

### Rules
- Use only rows with calibration_usable=true for weight calibration.
- Reject narrative-only rows for score changes.
- Reject rows without OHLC-derived MFE/MAE.
- Reject rows without at least 180 trading days forward window.
- Reject rows blocked by corporate-action-contaminated 180D window unless the user explicitly allows a separate adjusted-price revalidation.
- Reject shadow_weight rows that do not include before/after backtest effect.
- Preserve shadow-only calibration separately from production rules.
- Keep Stage2-Actionable as a shadow trigger type unless already supported.
- Do not hardcode historical company names into scoring logic.
- Production scoring must not change unless the user explicitly approves applying the shadow profile.

### Repository tasks
1. Parse case / trigger / score_simulation / profile_comparison / optimization_decision / shadow weight / aggregate rows.
2. Validate price_source_validation rows.
3. Validate MFE / MAE / peak / drawdown values.
4. Validate green_lateness_ratio.
5. Validate four_b_peak_proximity.
6. Validate 4C protection labels.
7. Validate calibration_usable filtering.
8. Validate before/after profile comparison rows.
9. Validate score-return alignment labels.
10. Append valid case rows to abstract case library.
11. Append valid trigger rows to trigger calibration dataset.
12. Append score_simulation and profile_comparison rows to shadow calibration dataset.
13. Append shadow weight rows to shadow calibration profile only if before/after backtest effect exists.
14. Add tests that narrative-only, non-OHLC, insufficient-forward-window, and corporate-action-contaminated rows cannot change weights.
15. Add tests for optimization decision validation.
16. Produce checkpoint summary.

### Expected output
- Concise implementation summary.
- Files changed.
- Tests run.
- Rows accepted.
- Rows rejected and why.
- Shadow profile rows accepted.
- Shadow weight rows accepted.
- Shadow weight rows rejected.
- No investment recommendation language.

## 28. Next Round State

```text
current_round = R5 Loop 1
next_round = R6 Loop 1
next_sector = 금융·자본배분·디지털금융
production_scoring_changed = false
shadow_weight_only = true
```

## 29. Source Notes

- Stock-web manifest checked: `atlas/manifest.json`.
- Stock-web schema checked: `atlas/schema.json`.
- Stock-web universe checked: `atlas/universe/all_symbols.csv`.
- Stock-web optional smoke bundle checked: `diagnostics/chatgpt_bundle.txt`.
- Price shards checked: `003/003230/2024.csv`, `003/003230/2025.csv`, `278/278470/2025.csv`, `278/278470/2026.csv`, `383/383220/2023.csv`.
- Symbol profiles checked: `003230`, `278470`, `383220`.
- Web evidence used as contextual support only: Samyang export/ASP/capacity market-talk source; APR K-beauty device / Medicube public articles. F&F is treated as a price-path false-positive counterexample and not as positive weight evidence.
- No stock_agent repository files were opened or patched during this research run.
