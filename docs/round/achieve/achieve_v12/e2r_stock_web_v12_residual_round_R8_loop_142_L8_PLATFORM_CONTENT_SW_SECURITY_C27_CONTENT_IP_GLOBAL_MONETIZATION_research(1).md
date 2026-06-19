# E2R v12 Residual Research — R8 / C27_CONTENT_IP_GLOBAL_MONETIZATION

```text
output_file = e2r_stock_web_v12_residual_round_R8_loop_142_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
selected_round = R8
selected_loop = 142
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0/1 quality repair — C27 content/IP global monetization, source-proxy repair, 4B/4C taxonomy repair, repeat monetization bridge
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id = CONTENT_IP_GLOBAL_PLATFORM_RECURRING_MONETIZATION_GATE
loop_objective = sector_specific_rule_discovery; canonical_archetype_rule_candidate; counterexample_mining; positive_case_balance; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; complete_30_90_180_MFE_MAE
research_session = post_calibrated_sector_archetype_residual_research
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection rationale

This run intentionally moves away from the immediately prior C26 platform/ad operating-leverage study and selects the adjacent but mechanically different R8/L8 C27 scope.  C27 is already well-covered in raw count, so this is not a quantity-fill loop.  It is a quality-repair loop: C27 still needs cleaner separation between **global hit visibility** and **listed-company monetization**, plus sharper 4B/4C treatment for artist-contract concentration, platform losses, single-title spikes, and high-MAE positives.

The cumulative No-Repeat snapshot reports C27 at 248 representative rows, 40 symbols, 33 positive / 46 counterexample rows, and 42 / 12 4B/4C rows, with runtime weights `20/18/8/14/12/8/20`.  Therefore this loop emphasizes new trigger families rather than row-count completion.

## 2. Price atlas verification

Stock-Web manifest fields used:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Schema rule used:

```text
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
calibration_usable requires tradable_raw, positive OHLCV, entry row, 180 forward rows, complete MFE/MAE, and no 180D corporate-action contamination.
```

All selected rows use downloaded Stock-Web tradable shards under `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv`.

## 3. Novelty / duplicate gate

```text
new_independent_case_count = 8
reused_case_count = 0
same_archetype_new_symbol_count = 8
same_archetype_new_trigger_family_count = 8
calibration_usable_case_count = 8
calibration_usable_trigger_count = 8
positive_case_count = 3
counterexample_count = 5
stage4b_case_count = 2
stage4c_case_count = 3
source_proxy_only_count = 2
evidence_url_pending_count = 0
rows_missing_required_mfe_mae = 0
current_profile_error_count = 6
```

Hard duplicate check: no row reuses a same-session `C27_CONTENT_IP_GLOBAL_MONETIZATION + symbol + trigger_type + entry_date` key.  Same canonical reuse is allowed; same symbol/trigger/entry rematerialization is not used.

## 4. Case table

| case_id | symbol | name | trigger_type | trigger_date | entry_date | entry_price | MFE30/90/180 | MAE30/90/180 | outcome | evidence_family |
|---|---:|---|---|---|---|---:|---:|---:|---|---|
| C27-01 | 035900 | JYP Ent. | Stage3-Green | 2023-05-15 | 2023-05-15 | 95500 | 47.23/53.51/53.51 | -3.46/-3.46/-21.99 | positive | record_earnings_global_artist_monetization |
| C27-02 | 041510 | SM Entertainment | Stage4B | 2023-08-02 | 2023-08-03 | 132600 | 10.86/10.86/10.86 | -5.43/-37.78/-47.21 | counterexample | record_quarter_but_artist_cycle_valuation_drawdown |
| C27-03 | 263720 | D&C Media | Stage2-Actionable | 2024-01-08 | 2024-01-08 | 29850 | 29.31/29.31/29.31 | -19.26/-27.81/-46.37 | positive_with_4b_watch | single_ip_global_anime_launch |
| C27-04 | 376300 | DearU | Stage3-Yellow | 2024-05-16 | 2024-05-16 | 25600 | 7.23/9.77/67.19 | -12.30/-31.09/-31.09 | positive | subscription_fandom_platform_repeat_revenue |
| C27-05 | 253450 | Studio Dragon | Stage4C | 2023-03-13 | 2023-03-13 | 76000 | 2.89/2.89/2.89 | -11.58/-36.12/-39.47 | counterexample | hit_drama_without_company_level_monetization_bridge |
| C27-06 | 035760 | CJ ENM | Stage4C | 2023-05-04 | 2023-05-08 | 76900 | 4.55/4.55/4.68 | -6.50/-26.53/-35.63 | counterexample | content_pipeline_loss_break |
| C27-07 | 352820 | HYBE | Stage4B | 2024-04-26 | 2024-04-26 | 201500 | 3.47/3.47/12.41 | -7.84/-20.60/-21.74 | counterexample | artist_ip_key_person_label_dispute |
| C27-08 | 122870 | YG Entertainment | Stage4C | 2023-09-22 | 2023-09-22 | 66400 | 3.61/3.61/3.61 | -24.55/-39.61/-40.96 | counterexample | key_artist_contract_uncertainty |

## 5. Actual Stock-Web entry OHLC rows

| symbol | entry_date | o | h | l | c | volume | market | forward_rows_180 | corp_action_180D |
|---:|---|---:|---:|---:|---:|---:|---|---:|---|
| 035900 | 2023-05-15 | 94600 | 95500 | 92200 | 95500 | 601239 | KOSDAQ GLOBAL | 180 | false |
| 041510 | 2023-08-03 | 136100 | 142700 | 128300 | 132600 | 699620 | KOSDAQ | 180 | false |
| 263720 | 2024-01-08 | 25900 | 32150 | 25400 | 29850 | 2104638 | KOSDAQ | 180 | false |
| 376300 | 2024-05-16 | 25600 | 26150 | 25350 | 25600 | 39429 | KOSDAQ | 180 | false |
| 253450 | 2023-03-13 | 78100 | 78200 | 72400 | 76000 | 646149 | KOSDAQ | 180 | false |
| 035760 | 2023-05-08 | 78200 | 78600 | 76600 | 76900 | 106737 | KOSDAQ GLOBAL | 180 | false |
| 352820 | 2024-04-26 | 206000 | 207500 | 199800 | 201500 | 1122644 | KOSPI | 180 | false |
| 122870 | 2023-09-22 | 68000 | 68500 | 64300 | 66400 | 1150903 | KOSDAQ | 180 | false |

## 6. Forward price path — 30D / 90D / 180D MFE and MAE

| symbol | entry_price | 30D peak/date | 30D trough/date | 90D peak/date | 90D trough/date | 180D peak/date | 180D trough/date |
|---:|---:|---|---|---|---|---|---|
| 035900 | 95500 | 47.23% @ 140600 / 2023-06-21 | -3.46% @ 92200 / 2023-05-15 | 53.51% @ 146600 / 2023-07-25 | -3.46% @ 92200 / 2023-05-15 | 53.51% @ 146600 / 2023-07-25 | -21.99% @ 74500 / 2024-02-01 |
| 041510 | 132600 | 10.86% @ 147000 / 2023-08-29 | -5.43% @ 125400 / 2023-08-18 | 10.86% @ 147000 / 2023-08-29 | -37.78% @ 82500 / 2023-12-05 | 10.86% @ 147000 / 2023-08-29 | -47.21% @ 70000 / 2024-03-07 |
| 263720 | 29850 | 29.31% @ 38600 / 2024-01-24 | -19.26% @ 24100 / 2024-02-07 | 29.31% @ 38600 / 2024-01-24 | -27.81% @ 21550 / 2024-04-11 | 29.31% @ 38600 / 2024-01-24 | -46.37% @ 16010 / 2024-09-09 |
| 376300 | 25600 | 7.23% @ 27450 / 2024-05-27 | -12.30% @ 22450 / 2024-06-25 | 9.77% @ 28100 / 2024-07-12 | -31.09% @ 17640 / 2024-09-09 | 67.19% @ 42800 / 2025-02-12 | -31.09% @ 17640 / 2024-09-09 |
| 253450 | 76000 | 2.89% @ 78200 / 2023-03-13 | -11.58% @ 67200 / 2023-04-21 | 2.89% @ 78200 / 2023-03-13 | -36.12% @ 48550 / 2023-07-10 | 2.89% @ 78200 / 2023-03-13 | -39.47% @ 46000 / 2023-10-26 |
| 035760 | 76900 | 4.55% @ 80400 / 2023-05-25 | -6.50% @ 71900 / 2023-06-19 | 4.55% @ 80400 / 2023-05-25 | -26.53% @ 56500 / 2023-09-07 | 4.68% @ 80500 / 2023-12-04 | -35.63% @ 49500 / 2023-10-20 |
| 352820 | 201500 | 3.47% @ 208500 / 2024-05-27 | -7.84% @ 185700 / 2024-05-23 | 3.47% @ 208500 / 2024-05-27 | -20.60% @ 160000 / 2024-08-05 | 12.41% @ 226500 / 2025-01-17 | -21.74% @ 157700 / 2024-09-23 |
| 122870 | 66400 | 3.61% @ 68800 / 2023-09-25 | -24.55% @ 50100 / 2023-10-26 | 3.61% @ 68800 / 2023-09-25 | -39.61% @ 40100 / 2024-01-18 | 3.61% @ 68800 / 2023-09-25 | -40.96% @ 39200 / 2024-03-07 |

## 7. Case notes

### C27-01 — JYP Ent. / global artist monetization positive

JYP's 2023 Q1 earnings trigger combined revenue and operating-profit acceleration with global album, streaming, and tour monetization.  The entry path showed a clean 30D/90D right tail: +47.23% / +53.51% MFE with only -3.46% MAE through 90D.  The later 180D MAE of -21.99% is not a thesis break; it is a drawdown-aware Green confirmation warning after the initial rerating.

### C27-02 — SM Entertainment / record quarter but high-MAE cycle risk

SM's Q2 2023 operating profit beat and global concerts/album evidence were real, but the forward path peaked quickly and then produced -37.78% 90D MAE and -47.21% 180D MAE.  This is a C27 4B path: strong content/IP evidence can still be late-cycle if repeat monetization and margin durability are not confirmed beyond the release window.

### C27-03 — D&C Media / single-IP global anime launch

Solo Leveling's January 2024 Crunchyroll launch created a direct global visibility event for a Korean IP owner.  The price path produced +29.31% MFE but also -46.37% 180D MAE.  This is usable as a Stage2-Actionable positive but not a Green promotion row: anime visibility alone must be linked to revenue share, royalty, merchandise/game, or sequel economics before a durable C27 rerating.

### C27-04 — DearU / paid subscription fandom platform

DearU's bubble model is closer to recurring platform economics than one-off title success.  The 2024 trigger had a weak 30D/90D profile but a +67.19% 180D MFE.  The -31.09% 90D/180D MAE still argues against fast Green: subscription/platform IP monetization needs subscriber, ARPU, partner expansion, and revenue/profit bridge confirmation.

### C27-05 — Studio Dragon / global hit title without listed-company monetization bridge

The Glory Part 2 was a global Netflix hit, but entry at the global-hit news window produced only +2.89% MFE and -39.47% 180D MAE.  This is the core C27 false-positive archetype: a global hit is not automatically a listed-stock earnings bridge if production amortization, delivery cadence, platform economics, and margin conversion are not clear.

### C27-06 — CJ ENM / content pipeline loss break

CJ ENM's 2023 media/content path was burdened by TVING and Fifth Season losses.  The trigger profile produced +4.68% 180D MFE and -35.63% 180D MAE.  This is a hard 4C candidate for content/IP monetization: large catalogue and global production exposure do not help if the pipeline is loss-dominated.

### C27-07 — HYBE / artist-IP key-person and label dispute

HYBE's ADOR/NewJeans dispute is not merely price volatility.  It is a visibility break around artist-IP control, label governance, and future release cadence.  The path had only +3.47% MFE through 90D against -20.60% 90D MAE.  Treat as 4B until direct contract/revenue impairment is confirmed; if key-artist release cadence or contractual economics break, it becomes hard 4C.

### C27-08 — YG Entertainment / concentrated artist contract uncertainty

BLACKPINK contract uncertainty is a concentrated artist-IP thesis break.  The price path after the uncertainty trigger showed +3.61% 180D MFE versus -40.96% 180D MAE.  Later renewal news may create a separate positive trigger, but this row remains a valid 4C guardrail for concentrated-IP contract uncertainty.

## 8. Machine-readable trigger rows JSONL

```jsonl
{"row_type": "trigger", "case_id": "C27-01", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "CONTENT_IP_GLOBAL_PLATFORM_RECURRING_MONETIZATION_GATE", "symbol": "035900", "company_name": "JYP Ent.", "trigger_type": "Stage3-Green", "trigger_date": "2023-05-15", "entry_date": "2023-05-15", "entry_price": 95500.0, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 47.23, "MFE_90D_pct": 53.51, "MFE_180D_pct": 53.51, "MAE_30D_pct": -3.46, "MAE_90D_pct": -3.46, "MAE_180D_pct": -21.99, "MFE_180D_peak_date": "2023-07-25", "MAE_180D_trough_date": "2024-02-01", "calibration_usable": true, "evidence_family": "record_earnings_global_artist_monetization", "outcome_label": "positive", "evidence_summary": "JYP Q1 2023 record revenue/OP, global albums/streams/tours", "evidence_url": "https://view.asiae.co.kr/en/article/2023051516315466013", "source_proxy_only": false, "evidence_url_pending": false, "do_not_count_as_new_case": false, "reuse_reason": null, "same_entry_group_id": "C27-035900-2023-05-15", "corporate_action_contaminated_180D": false}
{"row_type": "trigger", "case_id": "C27-02", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "CONTENT_IP_GLOBAL_PLATFORM_RECURRING_MONETIZATION_GATE", "symbol": "041510", "company_name": "SM Entertainment", "trigger_type": "Stage4B", "trigger_date": "2023-08-02", "entry_date": "2023-08-03", "entry_price": 132600.0, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 10.86, "MFE_90D_pct": 10.86, "MFE_180D_pct": 10.86, "MAE_30D_pct": -5.43, "MAE_90D_pct": -37.78, "MAE_180D_pct": -47.21, "MFE_180D_peak_date": "2023-08-29", "MAE_180D_trough_date": "2024-03-07", "calibration_usable": true, "evidence_family": "record_quarter_but_artist_cycle_valuation_drawdown", "outcome_label": "counterexample", "evidence_summary": "Q2 OP beat on album sales/concerts, but peak-to-drawdown exposed high-MAE cycle risk", "evidence_url": "https://koreajoongangdaily.joins.com/2023/08/02/business/industry/SM-Entertainment/20230802173305180.html", "source_proxy_only": false, "evidence_url_pending": false, "do_not_count_as_new_case": false, "reuse_reason": null, "same_entry_group_id": "C27-041510-2023-08-03", "corporate_action_contaminated_180D": false}
{"row_type": "trigger", "case_id": "C27-03", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "CONTENT_IP_GLOBAL_PLATFORM_RECURRING_MONETIZATION_GATE", "symbol": "263720", "company_name": "D&C Media", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-08", "entry_date": "2024-01-08", "entry_price": 29850.0, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 29.31, "MFE_90D_pct": 29.31, "MFE_180D_pct": 29.31, "MAE_30D_pct": -19.26, "MAE_90D_pct": -27.81, "MAE_180D_pct": -46.37, "MFE_180D_peak_date": "2024-01-24", "MAE_180D_trough_date": "2024-09-09", "calibration_usable": true, "evidence_family": "single_ip_global_anime_launch", "outcome_label": "positive_with_4b_watch", "evidence_summary": "Solo Leveling global Crunchyroll launch converts Korean IP into worldwide anime visibility, but monetization proof lagged", "evidence_url": "https://www.crunchyroll.com/news/announcements/2024/1/5/solo-leveling-anime-release-date", "source_proxy_only": true, "evidence_url_pending": false, "do_not_count_as_new_case": false, "reuse_reason": null, "same_entry_group_id": "C27-263720-2024-01-08", "corporate_action_contaminated_180D": false}
{"row_type": "trigger", "case_id": "C27-04", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "CONTENT_IP_GLOBAL_PLATFORM_RECURRING_MONETIZATION_GATE", "symbol": "376300", "company_name": "DearU", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-05-16", "entry_date": "2024-05-16", "entry_price": 25600.0, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 7.23, "MFE_90D_pct": 9.77, "MFE_180D_pct": 67.19, "MAE_30D_pct": -12.3, "MAE_90D_pct": -31.09, "MAE_180D_pct": -31.09, "MFE_180D_peak_date": "2025-02-12", "MAE_180D_trough_date": "2024-09-09", "calibration_usable": true, "evidence_family": "subscription_fandom_platform_repeat_revenue", "outcome_label": "positive", "evidence_summary": "DearU bubble paid subscription platform and 1Q24 IR revenue/profitability bridge", "evidence_url": "https://www.dear-u.co/data/file/ir_etc/20240513135145_f8a07ae8b0ed22a9f975e37fa86dfdc4.pdf", "source_proxy_only": false, "evidence_url_pending": false, "do_not_count_as_new_case": false, "reuse_reason": null, "same_entry_group_id": "C27-376300-2024-05-16", "corporate_action_contaminated_180D": false}
{"row_type": "trigger", "case_id": "C27-05", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "CONTENT_IP_GLOBAL_PLATFORM_RECURRING_MONETIZATION_GATE", "symbol": "253450", "company_name": "Studio Dragon", "trigger_type": "Stage4C", "trigger_date": "2023-03-13", "entry_date": "2023-03-13", "entry_price": 76000.0, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 2.89, "MFE_90D_pct": 2.89, "MFE_180D_pct": 2.89, "MAE_30D_pct": -11.58, "MAE_90D_pct": -36.12, "MAE_180D_pct": -39.47, "MFE_180D_peak_date": "2023-03-13", "MAE_180D_trough_date": "2023-10-26", "calibration_usable": true, "evidence_family": "hit_drama_without_company_level_monetization_bridge", "outcome_label": "counterexample", "evidence_summary": "The Glory Part 2 global top ranking did not translate into durable listed-company rerating", "evidence_url": "https://en.yna.co.kr/view/AEN20230313003200315", "source_proxy_only": false, "evidence_url_pending": false, "do_not_count_as_new_case": false, "reuse_reason": null, "same_entry_group_id": "C27-253450-2023-03-13", "corporate_action_contaminated_180D": false}
{"row_type": "trigger", "case_id": "C27-06", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "CONTENT_IP_GLOBAL_PLATFORM_RECURRING_MONETIZATION_GATE", "symbol": "035760", "company_name": "CJ ENM", "trigger_type": "Stage4C", "trigger_date": "2023-05-04", "entry_date": "2023-05-08", "entry_price": 76900.0, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 4.55, "MFE_90D_pct": 4.55, "MFE_180D_pct": 4.68, "MAE_30D_pct": -6.5, "MAE_90D_pct": -26.53, "MAE_180D_pct": -35.63, "MFE_180D_peak_date": "2023-12-04", "MAE_180D_trough_date": "2023-10-20", "calibration_usable": true, "evidence_family": "content_pipeline_loss_break", "outcome_label": "counterexample", "evidence_summary": "TVING/Fifth Season/movie-drama loss burden overrode content narrative", "evidence_url": "https://koreajoongangdaily.joins.com/2023/08/10/business/industry/CJ-ENM/20230810181556376.html", "source_proxy_only": false, "evidence_url_pending": false, "do_not_count_as_new_case": false, "reuse_reason": null, "same_entry_group_id": "C27-035760-2023-05-08", "corporate_action_contaminated_180D": false}
{"row_type": "trigger", "case_id": "C27-07", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "CONTENT_IP_GLOBAL_PLATFORM_RECURRING_MONETIZATION_GATE", "symbol": "352820", "company_name": "HYBE", "trigger_type": "Stage4B", "trigger_date": "2024-04-26", "entry_date": "2024-04-26", "entry_price": 201500.0, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 3.47, "MFE_90D_pct": 3.47, "MFE_180D_pct": 12.41, "MAE_30D_pct": -7.84, "MAE_90D_pct": -20.6, "MAE_180D_pct": -21.74, "MFE_180D_peak_date": "2025-01-17", "MAE_180D_trough_date": "2024-09-23", "calibration_usable": true, "evidence_family": "artist_ip_key_person_label_dispute", "outcome_label": "counterexample", "evidence_summary": "ADOR/NewJeans dispute impaired IP monetization visibility and caused share-price damage", "evidence_url": "https://www.reuters.com/business/media-telecom/k-pop-giant-hybe-shares-take-another-hit-dispute-with-newjeans-label-drags-2024-04-26/", "source_proxy_only": false, "evidence_url_pending": false, "do_not_count_as_new_case": false, "reuse_reason": null, "same_entry_group_id": "C27-352820-2024-04-26", "corporate_action_contaminated_180D": false}
{"row_type": "trigger", "case_id": "C27-08", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "fine_archetype_id": "CONTENT_IP_GLOBAL_PLATFORM_RECURRING_MONETIZATION_GATE", "symbol": "122870", "company_name": "YG Entertainment", "trigger_type": "Stage4C", "trigger_date": "2023-09-22", "entry_date": "2023-09-22", "entry_price": 66400.0, "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 3.61, "MFE_90D_pct": 3.61, "MFE_180D_pct": 3.61, "MAE_30D_pct": -24.55, "MAE_90D_pct": -39.61, "MAE_180D_pct": -40.96, "MFE_180D_peak_date": "2023-09-25", "MAE_180D_trough_date": "2024-03-07", "calibration_usable": true, "evidence_family": "key_artist_contract_uncertainty", "outcome_label": "counterexample", "evidence_summary": "BLACKPINK contract uncertainty showed concentrated artist-IP thesis break risk before later renewal", "evidence_url": "https://www.billboard.com/pro/blackpink-contract-uncertainty-yg-entertainment-stock-drop/", "source_proxy_only": true, "evidence_url_pending": false, "do_not_count_as_new_case": false, "reuse_reason": null, "same_entry_group_id": "C27-122870-2023-09-22", "corporate_action_contaminated_180D": false}
```

## 9. Raw component score breakdown JSONL

These are research-run score proxies only.  They are not production scoring changes.

```jsonl
{"symbol": "035900", "trigger_type": "Stage3-Green", "eps_fcf_explosion": 22, "earnings_visibility": 25, "bottleneck_pricing": 7, "market_mispricing": 13, "valuation_rerating": 10, "capital_allocation": 6, "information_confidence": 13, "risk_penalty": 8, "total_score_proxy": 88.0, "note": "current profile captures positive but 180D MAE argues Green should require drawdown-aware hold confirmation"}
{"symbol": "041510", "trigger_type": "Stage4B", "eps_fcf_explosion": 16, "earnings_visibility": 19, "bottleneck_pricing": 6, "market_mispricing": 9, "valuation_rerating": 9, "capital_allocation": 5, "information_confidence": 14, "risk_penalty": 16, "total_score_proxy": 62.0, "note": "record quarter alone over-credits artist-cycle peak; 4B should cap until repeat monetization survives next release cycle"}
{"symbol": "263720", "trigger_type": "Stage2-Actionable", "eps_fcf_explosion": 15, "earnings_visibility": 19, "bottleneck_pricing": 8, "market_mispricing": 15, "valuation_rerating": 9, "capital_allocation": 5, "information_confidence": 15, "risk_penalty": 12, "total_score_proxy": 74.0, "note": "single IP launch has real global surface but monetization proof is thin; Stage2-Actionable only, not Green"}
{"symbol": "376300", "trigger_type": "Stage3-Yellow", "eps_fcf_explosion": 16, "earnings_visibility": 25, "bottleneck_pricing": 6, "market_mispricing": 12, "valuation_rerating": 10, "capital_allocation": 7, "information_confidence": 17, "risk_penalty": 9, "total_score_proxy": 79.0, "note": "paid subscription fan platform gives recurring economics but high-MAE requires Green delay"}
{"symbol": "253450", "trigger_type": "Stage4C", "eps_fcf_explosion": 8, "earnings_visibility": 12, "bottleneck_pricing": 6, "market_mispricing": 9, "valuation_rerating": 7, "capital_allocation": 4, "information_confidence": 18, "risk_penalty": 16, "total_score_proxy": 48.0, "note": "global hit title is not enough when listed-company profit bridge is absent"}
{"symbol": "035760", "trigger_type": "Stage4C", "eps_fcf_explosion": 4, "earnings_visibility": 9, "bottleneck_pricing": 6, "market_mispricing": 8, "valuation_rerating": 7, "capital_allocation": 5, "information_confidence": 17, "risk_penalty": 18, "total_score_proxy": 42.0, "note": "content pipeline losses and platform losses overwhelm catalogue value; hard 4C candidate"}
{"symbol": "352820", "trigger_type": "Stage4B", "eps_fcf_explosion": 12, "earnings_visibility": 12, "bottleneck_pricing": 8, "market_mispricing": 8, "valuation_rerating": 9, "capital_allocation": 5, "information_confidence": 18, "risk_penalty": 17, "total_score_proxy": 55.0, "note": "artist/label governance dispute damages visibility; 4B watch before hard 4C unless monetization contract breaks"}
{"symbol": "122870", "trigger_type": "Stage4C", "eps_fcf_explosion": 7, "earnings_visibility": 8, "bottleneck_pricing": 7, "market_mispricing": 8, "valuation_rerating": 8, "capital_allocation": 5, "information_confidence": 18, "risk_penalty": 17, "total_score_proxy": 44.0, "note": "key artist contract uncertainty breaks IP cashflow visibility; concentrated-artist hard 4C path"}
```

## 10. Aggregate interpretation

```text
aggregate_positive_180D_MFE_median = 53.51% for clean/recurring positive group after excluding single-IP high-MAE watch rows
aggregate_counterexample_180D_MAE_median = approximately -39% across Studio Dragon, CJ ENM, HYBE, YG, and SM high-MAE/counter rows
most_common_false_positive_mechanism = global_hit_or_artist_headline_without_revenue_margin_bridge
most_common_4C_mechanism = concentrated artist contract uncertainty or loss-dominated content pipeline
most_common_4B_mechanism = real IP/title/platform evidence with high-MAE before repeat monetization confirmation
```

C27 behaves like a theatre with two doors.  One door opens to durable monetization: recurring subscriptions, tour/merchandise economics, platform revenue share, royalty recognition, repeat title cadence, and operating leverage.  The other door opens only to applause: one global hit, one artist headline, one streaming ranking, or one contract rumor.  The price path punishes confusing applause for cashflow.

## 11. Current calibrated profile stress test

The global v12 guardrails are directionally correct: price-only blowoff should not open positive stage, full 4B needs non-price evidence, and hard 4C should require thesis break.  The residual C27 issue is more specific:

```text
current_profile_residual_error:
  - over-credits global ranking / hit title as if it were direct listed-company monetization
  - under-penalizes concentrated artist contract uncertainty until price damage is already visible
  - sometimes treats platform/subscription IP as the same as one-off content success
  - needs a distinct repeat-monetization bridge before Stage3-Green
```

## 12. Shadow rule candidate

```text
new_axis_proposed = C27_IP_MONETIZATION_RECURRING_ECONOMICS_GATE
production_scoring_changed = false
shadow_weight_only = true
```

Rule candidate:

```text
For C27_CONTENT_IP_GLOBAL_MONETIZATION, do not allow Stage3-Green from global ranking, hit-title visibility, or artist headline alone.  Require at least two of:
  1. recurring subscription / fan-platform revenue,
  2. tour / concert / merchandise / MD economics,
  3. royalty or revenue-share recognition,
  4. repeat title cadence or sequel slate with dated release path,
  5. operating-profit or margin conversion,
  6. contract renewal / artist-IP continuity confirmation,
  7. company-level guidance or revision bridge.

If evidence is a single global hit/title ranking without company-level economics, cap at Stage2 or Stage4B watch.
If evidence shows key artist contract uncertainty, loss-dominated content pipeline, or cancellation/legal break affecting IP cashflow, route to Stage4C after confirmation.
```

Suggested shadow weight delta for C27:

```text
before = EPS/Vis/Bott/Mis/Val/Cap/Info = 20/18/8/14/12/8/20
after  = EPS/Vis/Bott/Mis/Val/Cap/Info = 18/21/8/12/10/8/23
delta  = -2/+3/0/-2/-2/0/+3
```

Interpretation: C27 should shift away from generic EPS/valuation chase and toward visibility + information confidence.  The important question is not whether the IP is famous.  The question is whether fame has a contract, a platform, a release cadence, and a margin bridge.

## 13. Existing axes strengthened / weakened

```text
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_confirmation
  - full_4b_requires_non_price_evidence
  - drawdown_aware_confirmation
  - information_confidence_gate

existing_axis_weakened: null
```

## 14. Validation scope

```text
validation_scope:
  price_source = Songdaiki/stock-web
  price_basis = tradable_raw
  entry_rows_verified = true
  MFE_MAE_30_90_180_verified = true
  forward_window_min_rows = 180
  corporate_action_contaminated_180D = false for all usable triggers
  source_url_attached = true
  source_proxy_only_rows = C27-03 and C27-08
  evidence_url_pending = 0
  production_patch_written = false
  handoff_prompt_executed_now = false
```

## 15. Batch Ingest Self-Audit

```text
required_filename_regex_pass = true
filename_round = R8
metadata_round = R8
filename_loop = 142
metadata_loop = 142
round_sector_pair_valid = true
canonical_archetype_id_valid = true
trigger_type_canonical_stage_label_only = true
complete_30_90_180_mfe_mae_in_every_trigger_row = true
same_entry_group_deduplicated_for_aggregate = true
narrative_only_rows_used_for_trigger = false
stock_agent_code_accessed = false
stock_agent_code_patched = false
production_scoring_changed = false
shadow_weight_only = true
```

## 16. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation agent.  Do not execute this during the research run.

Input MD:
{filename}

Task:
1. Parse trigger JSONL rows where row_type == trigger.
2. Validate canonical_archetype_id == C27_CONTENT_IP_GLOBAL_MONETIZATION and large_sector_id == L8_PLATFORM_CONTENT_SW_SECURITY.
3. Confirm all trigger rows include MFE_30D_pct, MFE_90D_pct, MFE_180D_pct, MAE_30D_pct, MAE_90D_pct, MAE_180D_pct.
4. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Treat source_proxy_only rows as guardrail evidence, not clean promotion evidence.
6. Consider shadow axis C27_IP_MONETIZATION_RECURRING_ECONOMICS_GATE only after combining with other C27 rows.
7. Do not alter production scoring from this MD alone.
```

## 17. Completion state

```text
completed_round = R8
completed_loop = 142
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0/1 quality repair — C27 content/IP global monetization repeat-economics gate
next_recommended_archetypes = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION; C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE; C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK; C31_POLICY_SUBSIDY_LEGISLATION_EVENT
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
loop_contribution_label = C27_repeat_monetization_vs_hit_headline_quality_repair
new_axis_proposed = C27_IP_MONETIZATION_RECURRING_ECONOMICS_GATE
production_scoring_changed = false
shadow_weight_only = true
```
