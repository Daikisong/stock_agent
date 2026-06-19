# E2R Historical Calibration Prompt v12 — Stock-Web OHLC Atlas / Sector-Archetype Residual Expansion / MD Handoff

## 0. Metadata

```yaml
research_file: e2r_stock_web_v12_residual_round_R3_loop_190_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
selected_round: R3
selected_loop: 190
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 / Priority 2 quality repair after prior C05 and C01 loops
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: BATTERY_JV_UTILIZATION_AMPC_EX_SUBSIDY_MARGIN_GATE
loop_objective: C13 JV/utilization/AMPC/IRA evidence-quality repair; separate subsidy/JV vocabulary from actual utilization and ex-AMPC margin conversion
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This file is a standalone v12 residual research MD. It does not patch `stock_agent`, does not run live discovery, and does not change production scoring.

---

## 1. Current calibrated profile assumption

Current profile is treated as already post-global calibration. The repeated global axes are not re-proposed:

- Stage2-Actionable evidence bonus is already assumed.
- Stage3-Yellow / Stage3-Green thresholds remain strict.
- Price-only blowoff remains blocked from positive-stage promotion.
- Full 4B still requires non-price evidence.
- Hard 4C still routes to 4C only when the non-price thesis break is confirmed.

Residual question for this loop:

> In C13 battery JV / utilization / AMPC / IRA cases, when is a JV or subsidy headline a real Stage2-Actionable bridge, and when is it only policy vocabulary that should be held at Stage2, 4B, or 4C until utilization and ex-AMPC margin conversion are visible?

---

## 2. Selection / coverage gap check

The No-Repeat ledger is used as duplicate-avoidance and coverage context, not as a code source. The prior two local outputs covered C05 and C01. The next quality-repair path selected here is C13 because it is a known L3 battery archetype where AMPC/IRA/JV language can be over-credited unless the evidence is tied to eligible production volume, plant utilization, customer pull, and non-subsidy margin.

Selected target:

```text
C13_BATTERY_JV_UTILIZATION_AMPC_IRA
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
selected_round = R3
selected_loop = 190
focus = AMPC/IRA/JV vocabulary versus actual utilization / ex-AMPC margin bridge
```

Duplicate key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Batch hard keys:

```text
C13_BATTERY_JV_UTILIZATION_AMPC_IRA|003670|Stage2-Actionable|2023-06-02
C13_BATTERY_JV_UTILIZATION_AMPC_IRA|006400|Stage2|2023-04-26
C13_BATTERY_JV_UTILIZATION_AMPC_IRA|006400|Stage4C|2024-08-29
C13_BATTERY_JV_UTILIZATION_AMPC_IRA|373220|Stage4B|2024-04-25
C13_BATTERY_JV_UTILIZATION_AMPC_IRA|373220|Stage2-Actionable|2025-04-30
C13_BATTERY_JV_UTILIZATION_AMPC_IRA|096770|Stage2|2023-07-28
C13_BATTERY_JV_UTILIZATION_AMPC_IRA|051910|Stage2-Actionable|2022-11-22
```

Within-batch same-entry dedupe: pass. `006400` and `373220` each appear twice, but with different trigger families and entry dates.

---

## 3. Stock-Web manifest / schema validation

Stock-Web validation basis:

```yaml
source_name: Songdaiki/stock-web
source_repo_url: https://github.com/Songdaiki/stock-web
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
raw_row_count: 15214118
symbol_count: 5414
active_like_symbol_count: 2868
inactive_or_delisted_like_symbol_count: 2546
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

Tradable shard schema used:

```text
d = date
o = open
h = high
l = low
c = close
v = volume
a = amount
mc = market_cap
s = shares
m = market
```

MFE / MAE method:

```text
entry_price = entry_date c column
MFE_N_pct = (max high from entry_date through N trading rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N trading rows / entry_price - 1) * 100
N = 30, 90, 180 trading days
```

All representative trigger rows below have the six required canonical MFE/MAE fields and a clean 180D corporate-action window.

---

## 4. Archetype map

```yaml
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: BATTERY_JV_UTILIZATION_AMPC_EX_SUBSIDY_MARGIN_GATE
primary_research_axis:
  - JV / customer plant headline
  - eligible volume / utilization conversion
  - AMPC / IRA quality of earnings
  - ex-AMPC margin bridge
  - factory schedule delay / capex deferral 4B-4C split
```

C13 is a bridge archetype. A battery JV or IRA production-credit headline is like a factory blueprint: useful, but not the same as machines running at yield, eligible units shipped, and margin becoming cash. This loop tests that gap directly.

---

## 5. Case summary matrix

| symbol | company | trigger_type | entry_date | entry_c | MFE30/90/180 | MAE30/90/180 | peak_180 | drawdown_after_peak | case_role | usable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 003670 | POSCO Future M | Stage2-Actionable | 2023-06-02 | 374,000 | 12.3/85.56/85.56 | -7.89/-16.18/-38.1 | 2023-07-26 694,000 | -66.64 | high_MFE_success_with_later_drawdown | true |
| 006400 | Samsung SDI | Stage2 | 2023-04-26 | 703,000 | 5.97/5.97/5.97 | -6.83/-17.07/-47.72 | 2023-06-12 745,000 | -50.67 | failed_rerating | true |
| 006400 | Samsung SDI | Stage4C | 2024-08-29 | 358,500 | 9.76/9.76/9.76 | -7.39/-35.98/-56.01 | 2024-09-30 393,500 | -59.92 | 4C_success | true |
| 373220 | LG Energy Solution | Stage4B | 2024-04-25 | 372,500 | 6.58/12.48/19.19 | -12.48/-16.51/-16.51 | 2024-10-08 444,000 | -23.31 | 4B_overlay_success | true |
| 373220 | LG Energy Solution | Stage2-Actionable | 2025-04-30 | 324,500 | 7.4/24.19/62.4 | -18.03/-18.03/-18.03 | 2025-10-29 527,000 | -31.97 | stage2_promote_candidate | true |
| 096770 | SK Innovation | Stage2 | 2023-07-28 | 189,500 | 19.79/19.79/19.79 | -10.77/-36.62/-45.86 | 2023-08-01 227,000 | -54.8 | failed_rerating | true |
| 051910 | LG Chem | Stage2-Actionable | 2022-11-22 | 687,000 | 9.9/10.19/24.75 | -13.68/-16.3/-16.3 | 2023-04-11 857,000 | -28.94 | structural_success | true |

Positive/counterexample balance:

```text
positive_case_count = 3
counterexample_or_guardrail_case_count = 4
4B_case_count = 1
4C_case_count = 1
new_independent_case_count = 7
unique_symbol_count = 5
calibration_usable_trigger_count = 7
```

---

## 6. Price row audit

| symbol | entry_date | o | h | l | c | v | m | shard | profile_CA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 003670 | 2023-06-02 | 361,500 | 381,500 | 358,500 | 374,000 | 1,467,089 | KOSPI | atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv | clean_180D_window_no_CA_candidate |
| 006400 | 2023-04-26 | 707,000 | 721,000 | 701,000 | 703,000 | 220,437 | KOSPI | atlas/ohlcv_tradable_by_symbol_year/006/006400/2023.csv | clean_180D_window_no_CA_candidate |
| 006400 | 2024-08-29 | 339,000 | 362,500 | 338,000 | 358,500 | 759,750 | KOSPI | atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv | clean_180D_window_no_CA_candidate |
| 373220 | 2024-04-25 | 380,000 | 381,000 | 372,000 | 372,500 | 176,196 | KOSPI | atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv | clean_180D_window_no_CA_candidate |
| 373220 | 2025-04-30 | 347,500 | 348,500 | 323,000 | 324,500 | 471,209 | KOSPI | atlas/ohlcv_tradable_by_symbol_year/373/373220/2025.csv | clean_180D_window_no_CA_candidate |
| 096770 | 2023-07-28 | 182,500 | 191,700 | 182,200 | 189,500 | 1,384,523 | KOSPI | atlas/ohlcv_tradable_by_symbol_year/096/096770/2023.csv | clean_180D_window_no_CA_candidate |
| 051910 | 2022-11-22 | 682,000 | 721,000 | 679,000 | 687,000 | 310,815 | KOSPI | atlas/ohlcv_tradable_by_symbol_year/051/051910/2022.csv | clean_180D_window_no_CA_candidate |

Corporate-action notes:

```text
003670 profile CA candidates: 2015-05-04, 2021-02-03; no overlap with 2023-06-02~2024-02-26 180D window.
006400 profile CA candidates: 1996-01-03, 1998-11-03, 2014-07-15; no overlap with 2023/2024 rows.
373220 profile CA candidates: none.
096770 profile CA candidate: 2024-11-20; no overlap with selected 2023-07-28~2024-04-23 180D window. The later 2024 SK On case is intentionally not used as a representative trigger because it would overlap the 2024-11-20 candidate window.
051910 profile CA candidates: none.
```

---

## 7. Case evidence / price-path audits

### 7.1. 003670 POSCO Future M — Stage2-Actionable — high_MFE_success_with_later_drawdown

```yaml
case_id: C13_R3L190_003670_POSCO_GM_ULTIUM_CAM_EXPANSION
trigger_id: R3L190_C13_003670_20230602_STAGE2_ACTIONABLE
trigger_date: 2023-06-02
entry_date: 2023-06-02
entry_price: 374000
evidence_source: POSCO Future M / GM official June 2023 Ultium CAM expansion
evidence_url: https://www.poscofuturem.com/en/pr/view.do?num=695 ; https://news.gm.com/home.detail.html/Pages/news/us/en/2023/jun/0602-posco.html
```

Evidence available at trigger:

> GM/POSCO Future M North America CAM+precursor expansion; Ultium CAM supports GM/LGES Ultium Cells supply; capacity tied to 2025-2030 production window, but near-term utilization and ex-subsidy margin bridge still absent.

Actual 1D OHLC entry row:

```text
2023-06-02 o=361,500 h=381,500 l=358,500 c=374,000 v=1,467,089 m=KOSPI
```

Price path:

```text
30D: MFE=12.3% / MAE=-7.89% / end=2023-07-14
90D: MFE=85.56% / MAE=-16.18% / end=2023-10-16
180D: MFE=85.56% / MAE=-38.1% / peak=2023-07-26 694,000 / drawdown_after_peak=-66.64% / end=2024-02-26
```

Current-profile stress-test verdict:

```text
current_profile_missed_structural_if_CAM_JV_capacity_not_mapped_to_C13_but_green_block_correct
```

C13 interpretation:

```text
good_stage2_high_MFE_but_high_drawdown_not_green
```

### 7.2. 006400 Samsung SDI — Stage2 — failed_rerating

```yaml
case_id: C13_R3L190_006400_GM_JV_2023_LONG_LEAD_FALSE_POSITIVE
trigger_id: R3L190_C13_006400_20230426_STAGE2
trigger_date: 2023-04-25
entry_date: 2023-04-26
entry_price: 703000
evidence_source: Samsung SDI official GM JV announcement
evidence_url: https://www.samsungsdi.com/sdi-now/sdi-news/3162.html?idx=3162&pageIndex=2&pagesize=15
```

Evidence available at trigger:

> Samsung SDI and GM agreed to form a U.S. EV battery-cell JV. Evidence quality was real but mostly long-lead customer/JV optionality; no near-term utilization, AMPC dollar capture, or margin conversion bridge was visible by entry.

Actual 1D OHLC entry row:

```text
2023-04-26 o=707,000 h=721,000 l=701,000 c=703,000 v=220,437 m=KOSPI
```

Price path:

```text
30D: MFE=5.97% / MAE=-6.83% / end=2023-06-12
90D: MFE=5.97% / MAE=-17.07% / end=2023-09-05
180D: MFE=5.97% / MAE=-47.72% / peak=2023-06-12 745,000 / drawdown_after_peak=-50.67% / end=2024-01-19
```

Current-profile stress-test verdict:

```text
current_profile_false_positive_if_policy_JV_language_overcredited_as_actionable
```

C13 interpretation:

```text
stage2_false_positive_long_lead_JV_low_MFE_deep_MAE
```

### 7.3. 006400 Samsung SDI — Stage4C — 4C_success

```yaml
case_id: C13_R3L190_006400_GM_JV_2024_DELAY_4C
trigger_id: R3L190_C13_006400_20240829_STAGE4C
trigger_date: 2024-08-28
entry_date: 2024-08-29
entry_price: 358500
evidence_source: Samsung SDI official final agreement plus WardsAuto delay report
evidence_url: https://samsungsdi.com/sdi-now/sdi-news/3942.html ; https://www.wardsauto.com/news/archive-auto-GM-Samsung-SDI-finalize-joint-venture-push-production-2027/725559/
```

Evidence available at trigger:

> The finalized GM/Samsung SDI JV targeted 2027 mass production; third-party report framed this as a year later than previously expected. In C13, a pushed-out plant schedule is direct non-price evidence that AMPC/utilization will not arrive inside the earlier rerating window.

Actual 1D OHLC entry row:

```text
2024-08-29 o=339,000 h=362,500 l=338,000 c=358,500 v=759,750 m=KOSPI
```

Price path:

```text
30D: MFE=9.76% / MAE=-7.39% / end=2024-10-17
90D: MFE=9.76% / MAE=-35.98% / end=2025-01-14
180D: MFE=9.76% / MAE=-56.01% / peak=2024-09-30 393,500 / drawdown_after_peak=-59.92% / end=2025-05-30
```

Current-profile stress-test verdict:

```text
current_profile_4C_too_late_if_it_waits_for_actual_losses_after_schedule_delay
```

C13 interpretation:

```text
hard_4c_success_deep_180D_drawdown_after_schedule_slip
```

### 7.4. 373220 LG Energy Solution — Stage4B — 4B_overlay_success

```yaml
case_id: C13_R3L190_373220_Q1_2024_AMPC_CAPEX_SLOWDOWN_4B
trigger_id: R3L190_C13_373220_20240425_STAGE4B
trigger_date: 2024-04-25
entry_date: 2024-04-25
entry_price: 372500
evidence_source: Reuters Q1 2024 LGES weak EV demand / capex minimization
evidence_url: https://www.reuters.com/technology/battery-firm-lg-energy-solution-q1-profit-plunges-weak-ev-sales-2024-04-25/
```

Evidence available at trigger:

> LGES Q1 2024 profit plunged, revenue fell, capex was to be minimized due slow EV demand, and without IRA production tax credit the quarter would have been loss-making. Yet GM/new-platform optionality remained, so the proper route is local 4B watch rather than immediate hard 4C.

Actual 1D OHLC entry row:

```text
2024-04-25 o=380,000 h=381,000 l=372,000 c=372,500 v=176,196 m=KOSPI
```

Price path:

```text
30D: MFE=6.58% / MAE=-12.48% / end=2024-06-11
90D: MFE=12.48% / MAE=-16.51% / end=2024-09-04
180D: MFE=19.19% / MAE=-16.51% / peak=2024-10-08 444,000 / drawdown_after_peak=-23.31% / end=2025-01-21
```

Current-profile stress-test verdict:

```text
current_profile_correct_if_non_price_4B_required_but_false_hard_4C_if_subsidy_dependency_alone_is_thesis_break
```

C13 interpretation:

```text
local_4B_watch_correct_AMPC_dependency_not_full_4C
```

### 7.5. 373220 LG Energy Solution — Stage2-Actionable — stage2_promote_candidate

```yaml
case_id: C13_R3L190_373220_Q1_2025_AMPC_RETURN_STAGE2_ACTIONABLE
trigger_id: R3L190_C13_373220_20250430_STAGE2_ACTIONABLE
trigger_date: 2025-04-30
entry_date: 2025-04-30
entry_price: 324500
evidence_source: LGES Q1 2025 financial release and YNA AMPC amount
evidence_url: https://inside.lgensol.com/en/2025/04/lg-energy-solution-releases-2025-first-quarter-financial-results/ ; https://en.yna.co.kr/view/AEN20250430002851320
```

Evidence available at trigger:

> LGES returned to operating profit in Q1 2025. The AMPC amount was larger than reported operating profit, which makes the row a positive Stage2-Actionable recovery but not an unguarded Stage3-Green until non-AMPC margin/utilization is visible.

Actual 1D OHLC entry row:

```text
2025-04-30 o=347,500 h=348,500 l=323,000 c=324,500 v=471,209 m=KOSPI
```

Price path:

```text
30D: MFE=7.4% / MAE=-18.03% / end=2025-06-17
90D: MFE=24.19% / MAE=-18.03% / end=2025-09-10
180D: MFE=62.4% / MAE=-18.03% / peak=2025-10-29 527,000 / drawdown_after_peak=-31.97% / end=2026-01-26
```

Current-profile stress-test verdict:

```text
current_profile_missed_structural_if_AMPC_utilization_recovery_is_ignored_but_green_block_correct
```

C13 interpretation:

```text
good_stage2_high_MFE_but_green_requires_ex_AMPC_profit_bridge
```

### 7.6. 096770 SK Innovation — Stage2 — failed_rerating

```yaml
case_id: C13_R3L190_096770_SKON_Q2_2023_LOSS_NARROW_STAGE2_FAIL
trigger_id: R3L190_C13_096770_20230728_STAGE2
trigger_date: 2023-07-28
entry_date: 2023-07-28
entry_price: 189500
evidence_source: YNA SK Innovation Q2 2023 battery loss narrowing
evidence_url: https://en.yna.co.kr/view/AEN20230728002051320
```

Evidence available at trigger:

> SK Innovation battery business narrowed losses as sales rose and new-factory productivity improved, but the business was still loss-making. This is Stage2 evidence at most; the stock path shows why loss narrowing is not the same as utilization/margin conversion.

Actual 1D OHLC entry row:

```text
2023-07-28 o=182,500 h=191,700 l=182,200 c=189,500 v=1,384,523 m=KOSPI
```

Price path:

```text
30D: MFE=19.79% / MAE=-10.77% / end=2023-09-08
90D: MFE=19.79% / MAE=-36.62% / end=2023-12-08
180D: MFE=19.79% / MAE=-45.86% / peak=2023-08-01 227,000 / drawdown_after_peak=-54.8% / end=2024-04-23
```

Current-profile stress-test verdict:

```text
current_profile_false_positive_if_loss_narrowing_treated_as_utilization_conversion
```

C13 interpretation:

```text
stage2_false_positive_loss_narrowing_high_MAE
```

### 7.7. 051910 LG Chem — Stage2-Actionable — structural_success

```yaml
case_id: C13_R3L190_051910_TENNESSEE_CATHODE_IRA_SUPPLY_CHAIN
trigger_id: R3L190_C13_051910_20221122_STAGE2_ACTIONABLE
trigger_date: 2022-11-22
entry_date: 2022-11-22
entry_price: 687000
evidence_source: LG Corp official LG Chem Tennessee cathode MOU
evidence_url: https://www.lgcorp.com/media/release/25594
```

Evidence available at trigger:

> LG Chem signed an MOU to invest more than USD 3B in a Tennessee cathode plant, targeting 120,000 tons/year by 2027. This is a credible IRA supply-chain route, but the long construction/production schedule keeps it below Green without customer pull and utilization evidence.

Actual 1D OHLC entry row:

```text
2022-11-22 o=682,000 h=721,000 l=679,000 c=687,000 v=310,815 m=KOSPI
```

Price path:

```text
30D: MFE=9.9% / MAE=-13.68% / end=2023-01-03
90D: MFE=10.19% / MAE=-16.3% / end=2023-03-31
180D: MFE=24.75% / MAE=-16.3% / peak=2023-04-11 857,000 / drawdown_after_peak=-28.94% / end=2023-08-10
```

Current-profile stress-test verdict:

```text
current_profile_correct_if_actionable_but_Yellow_or_Green_blocked_until_utilization_bridge
```

C13 interpretation:

```text
good_stage2_medium_MFE_long_leadtime_not_green
```

---

## 8. Score simulations and component breakdown

C13 runtime-weight proxy used for this research row:

```text
EPS/FCF = 20
Earnings visibility = 18
Bottleneck / pricing = 14
Market mispricing = 12
Valuation rerating = 10
Capital allocation = 10
Information confidence = 16
```

This is a research proxy decomposition, not production scoring.

| trigger_id | trigger_type | score_before | score_after_shadow | MFE90 | MAE90 | verdict |
| --- | --- | --- | --- | --- | --- | --- |
| R3L190_C13_003670_20230602_STAGE2_ACTIONABLE | Stage2-Actionable | 62.7 | 64.7 | 85.56 | -16.18 | current_profile_missed_structural_if_CAM_JV_capacity_not_mapped_to_C13_but_green_block_correct |
| R3L190_C13_006400_20230426_STAGE2 | Stage2 | 45.8 | 41.8 | 5.97 | -17.07 | current_profile_false_positive_if_policy_JV_language_overcredited_as_actionable |
| R3L190_C13_006400_20240829_STAGE4C | Stage4C | 33.2 | 28.2 | 9.76 | -35.98 | current_profile_4C_too_late_if_it_waits_for_actual_losses_after_schedule_delay |
| R3L190_C13_373220_20240425_STAGE4B | Stage4B | 41.6 | 41.6 | 12.48 | -16.51 | current_profile_correct_if_non_price_4B_required_but_false_hard_4C_if_subsidy_dependency_alone_is_thesis_break |
| R3L190_C13_373220_20250430_STAGE2_ACTIONABLE | Stage2-Actionable | 69.1 | 70.6 | 24.19 | -18.03 | current_profile_missed_structural_if_AMPC_utilization_recovery_is_ignored_but_green_block_correct |
| R3L190_C13_096770_20230728_STAGE2 | Stage2 | 41.8 | 38.8 | 19.79 | -36.62 | current_profile_false_positive_if_loss_narrowing_treated_as_utilization_conversion |
| R3L190_C13_051910_20221122_STAGE2_ACTIONABLE | Stage2-Actionable | 62.4 | 63.4 | 10.19 | -16.3 | current_profile_correct_if_actionable_but_Yellow_or_Green_blocked_until_utilization_bridge |

Core score insight:

```text
- 006400 2023 and 096770 2023 show that customer/JV or loss-narrowing evidence can be real but still fail if utilization and ex-AMPC margin bridge are missing.
- 006400 2024 shows that delayed mass production is a true C13 thesis-timing break and can route to hard 4C.
- 373220 2024 shows that AMPC-dependency and capex minimization are 4B-quality non-price warnings, but not automatically hard 4C while customer/platform optionality remains alive.
- 373220 2025 and 003670/051910 show that real supply-chain/JV evidence can produce upside, but the Green gate must still require ex-AMPC profit or actual utilization conversion.
```

---

## 9. Profile comparison

| profile_id | scope | changed_axes | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | baseline_current_proxy | none | 23.99 | -22.38 | 32.49 | -34.08 | mixed; needs C13 bridge gate |
| P0b_e2r_2_0_baseline_reference | rollback_reference | rollback_only | 23.99 | -22.38 | 32.49 | -34.08 | weaker than P0 |
| P1_L3_BATTERY_UTILIZATION_AMP_CANDIDATE | sector_specific_candidate_profile | utilization_bridge_gate + ex_ampc_margin_quality | 39.98 | -16.84 | 57.57 | -24.14 | better separates positives from high-MAE counters |
| P2_C13_JV_AMPC_QUALITY_GATE | canonical_archetype_candidate_profile | ampc_quality_gate, factory_schedule_gate, non_ampc_margin_gate | 39.98 | -16.84 | 57.57 | -24.14 | best candidate |
| P3_COUNTEREXAMPLE_GUARD_PROFILE | counterexample_guard_profile | hard_4c_schedule_slip_trigger + local_4b_ampc_dependency_watch | 12.0 | -26.54 | 13.68 | -41.52 | guards high-MAE/low-MFE false positives |

Profile interpretation:

```text
P2_C13_JV_AMPC_QUALITY_GATE is the best shadow candidate.
It does not lower global Stage3-Green thresholds.
It does not make AMPC or IRA language automatically positive.
It only tells C13 to check whether the subsidy/JV headline has crossed into eligible production volume, utilization, customer pull, and ex-AMPC margin conversion.
```

---

## 10. Shadow weight proposal

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,utilization_bridge_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,"JV/IRA/AMPC words did not distinguish 006400/096770 false positives from 003670/051910/373220 recoveries unless eligible volume/utilization was explicit","blocks two deep-MAE false positives while preserving three positive Stage2 rows","R3L190_C13_003670_20230602_STAGE2_ACTIONABLE|R3L190_C13_006400_20230426_STAGE2|R3L190_C13_096770_20230728_STAGE2",7,7,4,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,ex_ampc_profit_quality_gate,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,"AMPC greater than or necessary for OP is not Green-quality margin; it remains Stage2/Yellow until ex-AMPC profit path appears","keeps 373220 2025 as good Stage2 not premature Green","R3L190_C13_373220_20250430_STAGE2_ACTIONABLE|R3L190_C13_373220_20240425_STAGE4B",7,7,4,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,factory_schedule_slip_routes_4c,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,"pushed-out mass production or capex minimization is non-price thesis damage for utilization timing","006400 2024 hard 4C followed by -56.01% MAE180","R3L190_C13_006400_20240829_STAGE4C",7,7,4,medium,sector_shadow_only,"not production; post-calibrated residual"
```

Production scoring changed: false. These are sector/canonical shadow candidates only.

---

## 11. Residual Contribution Summary

```yaml
new_independent_case_count: 7
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 1
new_fine_archetype_count: 7
new_trigger_family_count: 7
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - JV_headline_false_positive
  - AMPC_dependency_green_risk
  - factory_schedule_slip_4C
  - loss_narrowing_not_margin_conversion
  - high_MAE_after_real_supply_chain_positive
new_axis_proposed: true
existing_axis_strengthened:
  - stage2_required_bridge
  - full_4b_requires_non_price_evidence
  - hard_4c_confirmation_with_schedule_slip
existing_axis_weakened: []
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: L3_BATTERY_FACTORY_SCHEDULE_AND_UTILIZATION_GATE
canonical_archetype_rule_candidate: C13_JV_AMPC_EX_SUBSIDY_MARGIN_GATE
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

---

## 12. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | BATTERY_JV_UTILIZATION_AMPC_EX_SUBSIDY_MARGIN_GATE | 3 | 4 | 1 | 1 | 7 | 0 | 7 | 7 | 7 | L3_BATTERY_FACTORY_SCHEDULE_AND_UTILIZATION_GATE | C13_JV_AMPC_EX_SUBSIDY_MARGIN_GATE | C13 still needs more direct-URL repair and more ex-AMPC positive/negative pairs |

---

## 13. Machine-readable JSONL rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C13_R3L190_003670_POSCO_GM_ULTIUM_CAM_EXPANSION","symbol":"003670","company_name":"POSCO Future M","round":"R3","loop":"190","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"GM_POSCO_ULTIUM_CAM_JV_CAPACITY_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R3L190_C13_003670_20230602_STAGE2_ACTIONABLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"good_stage2_high_MFE_but_high_drawdown_not_green","current_profile_verdict":"current_profile_missed_structural_if_CAM_JV_capacity_not_mapped_to_C13_but_green_block_correct","price_source":"Songdaiki/stock-web","notes":"GM/POSCO Future M North America CAM+precursor expansion; Ultium CAM supports GM/LGES Ultium Cells supply; capacity tied to 2025-2030 production window, but near-term utilization and ex-subsidy margin bridge still absent."}
{"row_type":"trigger","trigger_id":"R3L190_C13_003670_20230602_STAGE2_ACTIONABLE","case_id":"C13_R3L190_003670_POSCO_GM_ULTIUM_CAM_EXPANSION","symbol":"003670","company_name":"POSCO Future M","round":"R3","loop":"190","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"GM_POSCO_ULTIUM_CAM_JV_CAPACITY_BRIDGE","sector":"battery_EV_green_mobility","primary_archetype":"North_America_CAM_JV_capacity_bridge","loop_objective":"C13 JV/utilization/AMPC/IRA bridge quality repair after C05 and C01 loops","trigger_type":"Stage2-Actionable","trigger_date":"2023-06-02","entry_date":"2023-06-02","entry_price":374000,"evidence_available_at_that_date":"GM/POSCO Future M North America CAM+precursor expansion; Ultium CAM supports GM/LGES Ultium Cells supply; capacity tied to 2025-2030 production window, but near-term utilization and ex-subsidy margin bridge still absent.","evidence_source":"https://www.poscofuturem.com/en/pr/view.do?num=695 ; https://news.gm.com/home.detail.html/Pages/news/us/en/2023/jun/0602-posco.html","evidence_source_name":"POSCO Future M / GM official June 2023 Ultium CAM expansion","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources","capacity_or_volume_route","customer_or_supply_chain_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.3,"MFE_90D_pct":85.56,"MFE_180D_pct":85.56,"MFE_1Y_pct":85.56,"MFE_2Y_pct":null,"MAE_30D_pct":-7.89,"MAE_90D_pct":-16.18,"MAE_180D_pct":-38.1,"MAE_1Y_pct":-38.1,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":694000,"drawdown_after_peak_pct":-66.64,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"good_stage2_high_MFE_but_high_drawdown_not_green","current_profile_verdict":"current_profile_missed_structural_if_CAM_JV_capacity_not_mapped_to_C13_but_green_block_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_no_CA_candidate","same_entry_group_id":"003670_2023-06-02_374000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C13_R3L190_003670_POSCO_GM_ULTIUM_CAM_EXPANSION","trigger_id":"R3L190_C13_003670_20230602_STAGE2_ACTIONABLE","symbol":"003670","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":0.82,"backlog_visibility_score":0.7,"margin_bridge_score":0.42,"revision_score":0.45,"relative_strength_score":0.75,"customer_quality_score":0.82,"policy_or_regulatory_score":0.75,"valuation_repricing_score":0.6,"execution_risk_score":0.45,"legal_or_contract_risk_score":0.15,"dilution_cb_risk_score":0.1,"accounting_trust_risk_score":0.05,"utilization_score":0.35,"ampc_quality_score":0.35,"ex_ampc_profit_score":0.3,"factory_schedule_score":0.62},"weighted_score_before":62.7,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0.82,"backlog_visibility_score":0.7,"margin_bridge_score":0.42,"revision_score":0.45,"relative_strength_score":0.75,"customer_quality_score":0.82,"policy_or_regulatory_score":0.75,"valuation_repricing_score":0.6,"execution_risk_score":0.45,"legal_or_contract_risk_score":0.15,"dilution_cb_risk_score":0.1,"accounting_trust_risk_score":0.05,"utilization_score":0.43,"ampc_quality_score":0.35,"ex_ampc_profit_score":0.3,"factory_schedule_score":0.67},"weighted_score_after":64.7,"stage_label_after":"Stage2-Actionable","changed_components":["utilization_score","margin_bridge_score","factory_schedule_score","execution_risk_score"],"component_delta_explanation":"C13 shadow gate separates JV/IRA/AMPC vocabulary from actual eligible volume, utilization, and ex-AMPC margin conversion.","MFE_90D_pct":85.56,"MAE_90D_pct":-16.18,"score_return_alignment_label":"good_stage2_high_MFE_but_high_drawdown_not_green","current_profile_verdict":"current_profile_missed_structural_if_CAM_JV_capacity_not_mapped_to_C13_but_green_block_correct"}
{"row_type":"case","case_id":"C13_R3L190_006400_GM_JV_2023_LONG_LEAD_FALSE_POSITIVE","symbol":"006400","company_name":"Samsung SDI","round":"R3","loop":"190","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"GM_SDI_JV_HEADLINE_WITHOUT_NEAR_TERM_UTILIZATION","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R3L190_C13_006400_20230426_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"stage2_false_positive_long_lead_JV_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_policy_JV_language_overcredited_as_actionable","price_source":"Songdaiki/stock-web","notes":"Samsung SDI and GM agreed to form a U.S. EV battery-cell JV. Evidence quality was real but mostly long-lead customer/JV optionality; no near-term utilization, AMPC dollar capture, or margin conversion bridge was visible by entry."}
{"row_type":"trigger","trigger_id":"R3L190_C13_006400_20230426_STAGE2","case_id":"C13_R3L190_006400_GM_JV_2023_LONG_LEAD_FALSE_POSITIVE","symbol":"006400","company_name":"Samsung SDI","round":"R3","loop":"190","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"GM_SDI_JV_HEADLINE_WITHOUT_NEAR_TERM_UTILIZATION","sector":"battery_EV_green_mobility","primary_archetype":"customer_JV_long_leadtime_without_utilization_bridge","loop_objective":"C13 JV/utilization/AMPC/IRA bridge quality repair after C05 and C01 loops","trigger_type":"Stage2","trigger_date":"2023-04-25","entry_date":"2023-04-26","entry_price":703000,"evidence_available_at_that_date":"Samsung SDI and GM agreed to form a U.S. EV battery-cell JV. Evidence quality was real but mostly long-lead customer/JV optionality; no near-term utilization, AMPC dollar capture, or margin conversion bridge was visible by entry.","evidence_source":"https://www.samsungsdi.com/sdi-now/sdi-news/3162.html?idx=3162&pageIndex=2&pagesize=15","evidence_source_name":"Samsung SDI official GM JV announcement","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality","customer_JV_route","IRA_or_AMPC_optionality"],"stage3_evidence_fields":["margin_bridge_missing","utilization_conversion_missing","financial_visibility_missing"],"stage4b_evidence_fields":["deep_MAE","utilization_bridge_missing","negative_earnings_or_loss_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006400/2023.csv","profile_path":"atlas/symbol_profiles/006/006400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.97,"MFE_90D_pct":5.97,"MFE_180D_pct":5.97,"MFE_1Y_pct":5.97,"MFE_2Y_pct":5.97,"MAE_30D_pct":-6.83,"MAE_90D_pct":-17.07,"MAE_180D_pct":-47.72,"MAE_1Y_pct":-51.35,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-12","peak_price":745000,"drawdown_after_peak_pct":-50.67,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["deep_MAE","utilization_bridge_missing","negative_earnings_or_loss_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"stage2_false_positive_long_lead_JV_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_policy_JV_language_overcredited_as_actionable","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_no_CA_candidate","same_entry_group_id":"006400_2023-04-26_703000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C13_R3L190_006400_GM_JV_2023_LONG_LEAD_FALSE_POSITIVE","trigger_id":"R3L190_C13_006400_20230426_STAGE2","symbol":"006400","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":0.74,"backlog_visibility_score":0.4,"margin_bridge_score":0.12,"revision_score":0.18,"relative_strength_score":0.42,"customer_quality_score":0.78,"policy_or_regulatory_score":0.7,"valuation_repricing_score":0.35,"execution_risk_score":0.7,"legal_or_contract_risk_score":0.15,"dilution_cb_risk_score":0.1,"accounting_trust_risk_score":0.05,"utilization_score":0.08,"ampc_quality_score":0.15,"ex_ampc_profit_score":0.1,"factory_schedule_score":0.32},"weighted_score_before":45.8,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0.74,"backlog_visibility_score":0.4,"margin_bridge_score":0.07,"revision_score":0.18,"relative_strength_score":0.42,"customer_quality_score":0.78,"policy_or_regulatory_score":0.7,"valuation_repricing_score":0.35,"execution_risk_score":0.75,"legal_or_contract_risk_score":0.15,"dilution_cb_risk_score":0.1,"accounting_trust_risk_score":0.05,"utilization_score":0.03,"ampc_quality_score":0.15,"ex_ampc_profit_score":0.1,"factory_schedule_score":0.32},"weighted_score_after":41.8,"stage_label_after":"Stage2","changed_components":["utilization_score","margin_bridge_score","factory_schedule_score","execution_risk_score"],"component_delta_explanation":"C13 shadow gate separates JV/IRA/AMPC vocabulary from actual eligible volume, utilization, and ex-AMPC margin conversion.","MFE_90D_pct":5.97,"MAE_90D_pct":-17.07,"score_return_alignment_label":"stage2_false_positive_long_lead_JV_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_policy_JV_language_overcredited_as_actionable"}
{"row_type":"case","case_id":"C13_R3L190_006400_GM_JV_2024_DELAY_4C","symbol":"006400","company_name":"Samsung SDI","round":"R3","loop":"190","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"GM_SDI_JV_DELAYED_PRODUCTION_UTILIZATION_BREAK","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"R3L190_C13_006400_20240829_STAGE4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"hard_4c_success_deep_180D_drawdown_after_schedule_slip","current_profile_verdict":"current_profile_4C_too_late_if_it_waits_for_actual_losses_after_schedule_delay","price_source":"Songdaiki/stock-web","notes":"The finalized GM/Samsung SDI JV targeted 2027 mass production; third-party report framed this as a year later than previously expected. In C13, a pushed-out plant schedule is direct non-price evidence that AMPC/utilization will not arrive inside the earlier rerating window."}
{"row_type":"trigger","trigger_id":"R3L190_C13_006400_20240829_STAGE4C","case_id":"C13_R3L190_006400_GM_JV_2024_DELAY_4C","symbol":"006400","company_name":"Samsung SDI","round":"R3","loop":"190","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"GM_SDI_JV_DELAYED_PRODUCTION_UTILIZATION_BREAK","sector":"battery_EV_green_mobility","primary_archetype":"JV_schedule_delay_as_non_price_thesis_break","loop_objective":"C13 JV/utilization/AMPC/IRA bridge quality repair after C05 and C01 loops","trigger_type":"Stage4C","trigger_date":"2024-08-28","entry_date":"2024-08-29","entry_price":358500,"evidence_available_at_that_date":"The finalized GM/Samsung SDI JV targeted 2027 mass production; third-party report framed this as a year later than previously expected. In C13, a pushed-out plant schedule is direct non-price evidence that AMPC/utilization will not arrive inside the earlier rerating window.","evidence_source":"https://samsungsdi.com/sdi-now/sdi-news/3942.html ; https://www.wardsauto.com/news/archive-auto-GM-Samsung-SDI-finalize-joint-venture-push-production-2027/725559/","evidence_source_name":"Samsung SDI official final agreement plus WardsAuto delay report","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality","customer_JV_route","IRA_or_AMPC_optionality"],"stage3_evidence_fields":["margin_bridge_missing","utilization_conversion_missing","financial_visibility_missing"],"stage4b_evidence_fields":["contract_delay","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["call_off_or_order_cut","qualification_or_schedule_failure","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv","profile_path":"atlas/symbol_profiles/006/006400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.76,"MFE_90D_pct":9.76,"MFE_180D_pct":9.76,"MFE_1Y_pct":9.76,"MFE_2Y_pct":null,"MAE_30D_pct":-7.39,"MAE_90D_pct":-35.98,"MAE_180D_pct":-56.01,"MAE_1Y_pct":-56.01,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-30","peak_price":393500,"drawdown_after_peak_pct":-59.92,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"hard_4C_schedule_or_utilization_break","four_b_evidence_type":["contract_delay","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"hard_4c_success_deep_180D_drawdown_after_schedule_slip","current_profile_verdict":"current_profile_4C_too_late_if_it_waits_for_actual_losses_after_schedule_delay","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_no_CA_candidate","same_entry_group_id":"006400_2024-08-29_358500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C13_R3L190_006400_GM_JV_2024_DELAY_4C","trigger_id":"R3L190_C13_006400_20240829_STAGE4C","symbol":"006400","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":0.62,"backlog_visibility_score":0.22,"margin_bridge_score":0.08,"revision_score":0.08,"relative_strength_score":0.22,"customer_quality_score":0.66,"policy_or_regulatory_score":0.62,"valuation_repricing_score":0.2,"execution_risk_score":0.86,"legal_or_contract_risk_score":0.45,"dilution_cb_risk_score":0.1,"accounting_trust_risk_score":0.05,"utilization_score":0.04,"ampc_quality_score":0.18,"ex_ampc_profit_score":0.06,"factory_schedule_score":0.12},"weighted_score_before":33.2,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":0.62,"backlog_visibility_score":0.22,"margin_bridge_score":0.03,"revision_score":0.08,"relative_strength_score":0.22,"customer_quality_score":0.66,"policy_or_regulatory_score":0.62,"valuation_repricing_score":0.2,"execution_risk_score":0.91,"legal_or_contract_risk_score":0.45,"dilution_cb_risk_score":0.1,"accounting_trust_risk_score":0.05,"utilization_score":0,"ampc_quality_score":0.18,"ex_ampc_profit_score":0.06,"factory_schedule_score":0.12},"weighted_score_after":28.2,"stage_label_after":"Stage4C","changed_components":["utilization_score","margin_bridge_score","factory_schedule_score","execution_risk_score"],"component_delta_explanation":"C13 shadow gate separates JV/IRA/AMPC vocabulary from actual eligible volume, utilization, and ex-AMPC margin conversion.","MFE_90D_pct":9.76,"MAE_90D_pct":-35.98,"score_return_alignment_label":"hard_4c_success_deep_180D_drawdown_after_schedule_slip","current_profile_verdict":"current_profile_4C_too_late_if_it_waits_for_actual_losses_after_schedule_delay"}
{"row_type":"case","case_id":"C13_R3L190_373220_Q1_2024_AMPC_CAPEX_SLOWDOWN_4B","symbol":"373220","company_name":"LG Energy Solution","round":"R3","loop":"190","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"AMPC_DEPENDENCE_AND_CAPEX_SLOWDOWN_4B_NOT_HARD_4C","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"R3L190_C13_373220_20240425_STAGE4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"local_4B_watch_correct_AMPC_dependency_not_full_4C","current_profile_verdict":"current_profile_correct_if_non_price_4B_required_but_false_hard_4C_if_subsidy_dependency_alone_is_thesis_break","price_source":"Songdaiki/stock-web","notes":"LGES Q1 2024 profit plunged, revenue fell, capex was to be minimized due slow EV demand, and without IRA production tax credit the quarter would have been loss-making. Yet GM/new-platform optionality remained, so the proper route is local 4B watch rather than immediate hard 4C."}
{"row_type":"trigger","trigger_id":"R3L190_C13_373220_20240425_STAGE4B","case_id":"C13_R3L190_373220_Q1_2024_AMPC_CAPEX_SLOWDOWN_4B","symbol":"373220","company_name":"LG Energy Solution","round":"R3","loop":"190","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"AMPC_DEPENDENCE_AND_CAPEX_SLOWDOWN_4B_NOT_HARD_4C","sector":"battery_EV_green_mobility","primary_archetype":"AMPC_subsidy_dependency_vs_customer_JV_offset","loop_objective":"C13 JV/utilization/AMPC/IRA bridge quality repair after C05 and C01 loops","trigger_type":"Stage4B","trigger_date":"2024-04-25","entry_date":"2024-04-25","entry_price":372500,"evidence_available_at_that_date":"LGES Q1 2024 profit plunged, revenue fell, capex was to be minimized due slow EV demand, and without IRA production tax credit the quarter would have been loss-making. Yet GM/new-platform optionality remained, so the proper route is local 4B watch rather than immediate hard 4C.","evidence_source":"https://www.reuters.com/technology/battery-firm-lg-energy-solution-q1-profit-plunges-weak-ev-sales-2024-04-25/","evidence_source_name":"Reuters Q1 2024 LGES weak EV demand / capex minimization","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality","IRA_or_AMPC_optionality"],"stage3_evidence_fields":["margin_bridge_missing","utilization_conversion_missing","financial_visibility_missing"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","contract_delay","capex_or_utilization_slowdown","non_price_4B_evidence"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv","profile_path":"atlas/symbol_profiles/373/373220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.58,"MFE_90D_pct":12.48,"MFE_180D_pct":19.19,"MFE_1Y_pct":19.19,"MFE_2Y_pct":null,"MAE_30D_pct":-12.48,"MAE_90D_pct":-16.51,"MAE_180D_pct":-16.51,"MAE_1Y_pct":-16.64,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-08","peak_price":444000,"drawdown_after_peak_pct":-23.31,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"non_price_4B_watch","four_b_evidence_type":["margin_or_backlog_slowdown","contract_delay","capex_or_utilization_slowdown","non_price_4B_evidence"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"local_4B_watch_correct_AMPC_dependency_not_full_4C","current_profile_verdict":"current_profile_correct_if_non_price_4B_required_but_false_hard_4C_if_subsidy_dependency_alone_is_thesis_break","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_no_CA_candidate","same_entry_group_id":"373220_2024-04-25_372500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C13_R3L190_373220_Q1_2024_AMPC_CAPEX_SLOWDOWN_4B","trigger_id":"R3L190_C13_373220_20240425_STAGE4B","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":0.45,"backlog_visibility_score":0.32,"margin_bridge_score":0.12,"revision_score":0.16,"relative_strength_score":0.3,"customer_quality_score":0.7,"policy_or_regulatory_score":0.72,"valuation_repricing_score":0.35,"execution_risk_score":0.78,"legal_or_contract_risk_score":0.2,"dilution_cb_risk_score":0.1,"accounting_trust_risk_score":0.05,"utilization_score":0.18,"ampc_quality_score":0.24,"ex_ampc_profit_score":0.04,"factory_schedule_score":0.25},"weighted_score_before":41.6,"stage_label_before":"Stage4B","raw_component_scores_after":{"contract_score":0.45,"backlog_visibility_score":0.32,"margin_bridge_score":0.07,"revision_score":0.16,"relative_strength_score":0.3,"customer_quality_score":0.7,"policy_or_regulatory_score":0.72,"valuation_repricing_score":0.35,"execution_risk_score":0.83,"legal_or_contract_risk_score":0.2,"dilution_cb_risk_score":0.1,"accounting_trust_risk_score":0.05,"utilization_score":0.13,"ampc_quality_score":0.24,"ex_ampc_profit_score":0.04,"factory_schedule_score":0.25},"weighted_score_after":41.6,"stage_label_after":"Stage4B","changed_components":["utilization_score","margin_bridge_score","factory_schedule_score","execution_risk_score"],"component_delta_explanation":"C13 shadow gate separates JV/IRA/AMPC vocabulary from actual eligible volume, utilization, and ex-AMPC margin conversion.","MFE_90D_pct":12.48,"MAE_90D_pct":-16.51,"score_return_alignment_label":"local_4B_watch_correct_AMPC_dependency_not_full_4C","current_profile_verdict":"current_profile_correct_if_non_price_4B_required_but_false_hard_4C_if_subsidy_dependency_alone_is_thesis_break"}
{"row_type":"case","case_id":"C13_R3L190_373220_Q1_2025_AMPC_RETURN_STAGE2_ACTIONABLE","symbol":"373220","company_name":"LG Energy Solution","round":"R3","loop":"190","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"AMPC_LED_PROFITABILITY_WITH_UTILIZATION_OPTIONALITY_GREEN_BLOCK","case_type":"stage2_promote_candidate","positive_or_counterexample":"positive","best_trigger":"R3L190_C13_373220_20250430_STAGE2_ACTIONABLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"good_stage2_high_MFE_but_green_requires_ex_AMPC_profit_bridge","current_profile_verdict":"current_profile_missed_structural_if_AMPC_utilization_recovery_is_ignored_but_green_block_correct","price_source":"Songdaiki/stock-web","notes":"LGES returned to operating profit in Q1 2025. The AMPC amount was larger than reported operating profit, which makes the row a positive Stage2-Actionable recovery but not an unguarded Stage3-Green until non-AMPC margin/utilization is visible."}
{"row_type":"trigger","trigger_id":"R3L190_C13_373220_20250430_STAGE2_ACTIONABLE","case_id":"C13_R3L190_373220_Q1_2025_AMPC_RETURN_STAGE2_ACTIONABLE","symbol":"373220","company_name":"LG Energy Solution","round":"R3","loop":"190","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"AMPC_LED_PROFITABILITY_WITH_UTILIZATION_OPTIONALITY_GREEN_BLOCK","sector":"battery_EV_green_mobility","primary_archetype":"AMPC_profit_recovery_with_ex_ampc_quality_gate","loop_objective":"C13 JV/utilization/AMPC/IRA bridge quality repair after C05 and C01 loops","trigger_type":"Stage2-Actionable","trigger_date":"2025-04-30","entry_date":"2025-04-30","entry_price":324500,"evidence_available_at_that_date":"LGES returned to operating profit in Q1 2025. The AMPC amount was larger than reported operating profit, which makes the row a positive Stage2-Actionable recovery but not an unguarded Stage3-Green until non-AMPC margin/utilization is visible.","evidence_source":"https://inside.lgensol.com/en/2025/04/lg-energy-solution-releases-2025-first-quarter-financial-results/ ; https://en.yna.co.kr/view/AEN20250430002851320","evidence_source_name":"LGES Q1 2025 financial release and YNA AMPC amount","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality","IRA_or_AMPC_optionality"],"stage3_evidence_fields":["multiple_public_sources","capacity_or_volume_route","customer_or_supply_chain_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2025.csv","profile_path":"atlas/symbol_profiles/373/373220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.4,"MFE_90D_pct":24.19,"MFE_180D_pct":62.4,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-18.03,"MAE_90D_pct":-18.03,"MAE_180D_pct":-18.03,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-10-29","peak_price":527000,"drawdown_after_peak_pct":-31.97,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"good_stage2_high_MFE_but_green_requires_ex_AMPC_profit_bridge","current_profile_verdict":"current_profile_missed_structural_if_AMPC_utilization_recovery_is_ignored_but_green_block_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_no_CA_candidate","same_entry_group_id":"373220_2025-04-30_324500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C13_R3L190_373220_Q1_2025_AMPC_RETURN_STAGE2_ACTIONABLE","trigger_id":"R3L190_C13_373220_20250430_STAGE2_ACTIONABLE","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":0.62,"backlog_visibility_score":0.52,"margin_bridge_score":0.45,"revision_score":0.52,"relative_strength_score":0.72,"customer_quality_score":0.72,"policy_or_regulatory_score":0.86,"valuation_repricing_score":0.58,"execution_risk_score":0.45,"legal_or_contract_risk_score":0.15,"dilution_cb_risk_score":0.08,"accounting_trust_risk_score":0.05,"utilization_score":0.44,"ampc_quality_score":0.78,"ex_ampc_profit_score":0.26,"factory_schedule_score":0.5},"weighted_score_before":69.1,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0.62,"backlog_visibility_score":0.52,"margin_bridge_score":0.45,"revision_score":0.52,"relative_strength_score":0.72,"customer_quality_score":0.72,"policy_or_regulatory_score":0.86,"valuation_repricing_score":0.58,"execution_risk_score":0.45,"legal_or_contract_risk_score":0.15,"dilution_cb_risk_score":0.08,"accounting_trust_risk_score":0.05,"utilization_score":0.52,"ampc_quality_score":0.78,"ex_ampc_profit_score":0.26,"factory_schedule_score":0.55},"weighted_score_after":70.6,"stage_label_after":"Stage2-Actionable","changed_components":["utilization_score","margin_bridge_score","factory_schedule_score","execution_risk_score"],"component_delta_explanation":"C13 shadow gate separates JV/IRA/AMPC vocabulary from actual eligible volume, utilization, and ex-AMPC margin conversion.","MFE_90D_pct":24.19,"MAE_90D_pct":-18.03,"score_return_alignment_label":"good_stage2_high_MFE_but_green_requires_ex_AMPC_profit_bridge","current_profile_verdict":"current_profile_missed_structural_if_AMPC_utilization_recovery_is_ignored_but_green_block_correct"}
{"row_type":"case","case_id":"C13_R3L190_096770_SKON_Q2_2023_LOSS_NARROW_STAGE2_FAIL","symbol":"096770","company_name":"SK Innovation","round":"R3","loop":"190","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"SKON_LOSS_NARROWING_WITHOUT_MARGIN_CONVERSION","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R3L190_C13_096770_20230728_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"stage2_false_positive_loss_narrowing_high_MAE","current_profile_verdict":"current_profile_false_positive_if_loss_narrowing_treated_as_utilization_conversion","price_source":"Songdaiki/stock-web","notes":"SK Innovation battery business narrowed losses as sales rose and new-factory productivity improved, but the business was still loss-making. This is Stage2 evidence at most; the stock path shows why loss narrowing is not the same as utilization/margin conversion."}
{"row_type":"trigger","trigger_id":"R3L190_C13_096770_20230728_STAGE2","case_id":"C13_R3L190_096770_SKON_Q2_2023_LOSS_NARROW_STAGE2_FAIL","symbol":"096770","company_name":"SK Innovation","round":"R3","loop":"190","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"SKON_LOSS_NARROWING_WITHOUT_MARGIN_CONVERSION","sector":"battery_EV_green_mobility","primary_archetype":"battery_loss_narrowing_without_utilization_margin_bridge","loop_objective":"C13 JV/utilization/AMPC/IRA bridge quality repair after C05 and C01 loops","trigger_type":"Stage2","trigger_date":"2023-07-28","entry_date":"2023-07-28","entry_price":189500,"evidence_available_at_that_date":"SK Innovation battery business narrowed losses as sales rose and new-factory productivity improved, but the business was still loss-making. This is Stage2 evidence at most; the stock path shows why loss narrowing is not the same as utilization/margin conversion.","evidence_source":"https://en.yna.co.kr/view/AEN20230728002051320","evidence_source_name":"YNA SK Innovation Q2 2023 battery loss narrowing","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality"],"stage3_evidence_fields":["margin_bridge_missing","utilization_conversion_missing","financial_visibility_missing"],"stage4b_evidence_fields":["deep_MAE","utilization_bridge_missing","negative_earnings_or_loss_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/096/096770/2023.csv","profile_path":"atlas/symbol_profiles/096/096770.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":19.79,"MFE_90D_pct":19.79,"MFE_180D_pct":19.79,"MFE_1Y_pct":19.79,"MFE_2Y_pct":19.79,"MAE_30D_pct":-10.77,"MAE_90D_pct":-36.62,"MAE_180D_pct":-45.86,"MAE_1Y_pct":-51.61,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-01","peak_price":227000,"drawdown_after_peak_pct":-54.8,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["deep_MAE","utilization_bridge_missing","negative_earnings_or_loss_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"stage2_false_positive_loss_narrowing_high_MAE","current_profile_verdict":"current_profile_false_positive_if_loss_narrowing_treated_as_utilization_conversion","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_no_CA_candidate","same_entry_group_id":"096770_2023-07-28_189500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C13_R3L190_096770_SKON_Q2_2023_LOSS_NARROW_STAGE2_FAIL","trigger_id":"R3L190_C13_096770_20230728_STAGE2","symbol":"096770","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":0.35,"backlog_visibility_score":0.3,"margin_bridge_score":0.1,"revision_score":0.2,"relative_strength_score":0.38,"customer_quality_score":0.62,"policy_or_regulatory_score":0.58,"valuation_repricing_score":0.32,"execution_risk_score":0.78,"legal_or_contract_risk_score":0.18,"dilution_cb_risk_score":0.12,"accounting_trust_risk_score":0.05,"utilization_score":0.22,"ampc_quality_score":0.22,"ex_ampc_profit_score":0.06,"factory_schedule_score":0.25},"weighted_score_before":41.8,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0.35,"backlog_visibility_score":0.3,"margin_bridge_score":0.05,"revision_score":0.2,"relative_strength_score":0.38,"customer_quality_score":0.62,"policy_or_regulatory_score":0.58,"valuation_repricing_score":0.32,"execution_risk_score":0.83,"legal_or_contract_risk_score":0.18,"dilution_cb_risk_score":0.12,"accounting_trust_risk_score":0.05,"utilization_score":0.17,"ampc_quality_score":0.22,"ex_ampc_profit_score":0.06,"factory_schedule_score":0.25},"weighted_score_after":38.8,"stage_label_after":"Stage2","changed_components":["utilization_score","margin_bridge_score","factory_schedule_score","execution_risk_score"],"component_delta_explanation":"C13 shadow gate separates JV/IRA/AMPC vocabulary from actual eligible volume, utilization, and ex-AMPC margin conversion.","MFE_90D_pct":19.79,"MAE_90D_pct":-36.62,"score_return_alignment_label":"stage2_false_positive_loss_narrowing_high_MAE","current_profile_verdict":"current_profile_false_positive_if_loss_narrowing_treated_as_utilization_conversion"}
{"row_type":"case","case_id":"C13_R3L190_051910_TENNESSEE_CATHODE_IRA_SUPPLY_CHAIN","symbol":"051910","company_name":"LG Chem","round":"R3","loop":"190","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"TENNESSEE_CATHODE_IRA_SUPPLY_CHAIN_LONG_LEAD_STAGE2","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R3L190_C13_051910_20221122_STAGE2_ACTIONABLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"good_stage2_medium_MFE_long_leadtime_not_green","current_profile_verdict":"current_profile_correct_if_actionable_but_Yellow_or_Green_blocked_until_utilization_bridge","price_source":"Songdaiki/stock-web","notes":"LG Chem signed an MOU to invest more than USD 3B in a Tennessee cathode plant, targeting 120,000 tons/year by 2027. This is a credible IRA supply-chain route, but the long construction/production schedule keeps it below Green without customer pull and utilization evidence."}
{"row_type":"trigger","trigger_id":"R3L190_C13_051910_20221122_STAGE2_ACTIONABLE","case_id":"C13_R3L190_051910_TENNESSEE_CATHODE_IRA_SUPPLY_CHAIN","symbol":"051910","company_name":"LG Chem","round":"R3","loop":"190","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"TENNESSEE_CATHODE_IRA_SUPPLY_CHAIN_LONG_LEAD_STAGE2","sector":"battery_EV_green_mobility","primary_archetype":"US_cathode_capacity_critical_mineral_IRA_route","loop_objective":"C13 JV/utilization/AMPC/IRA bridge quality repair after C05 and C01 loops","trigger_type":"Stage2-Actionable","trigger_date":"2022-11-22","entry_date":"2022-11-22","entry_price":687000,"evidence_available_at_that_date":"LG Chem signed an MOU to invest more than USD 3B in a Tennessee cathode plant, targeting 120,000 tons/year by 2027. This is a credible IRA supply-chain route, but the long construction/production schedule keeps it below Green without customer pull and utilization evidence.","evidence_source":"https://www.lgcorp.com/media/release/25594","evidence_source_name":"LG Corp official LG Chem Tennessee cathode MOU","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality","IRA_or_AMPC_optionality"],"stage3_evidence_fields":["multiple_public_sources","capacity_or_volume_route","customer_or_supply_chain_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/051/051910/2022.csv","profile_path":"atlas/symbol_profiles/051/051910.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.9,"MFE_90D_pct":10.19,"MFE_180D_pct":24.75,"MFE_1Y_pct":24.75,"MFE_2Y_pct":24.75,"MAE_30D_pct":-13.68,"MAE_90D_pct":-16.3,"MAE_180D_pct":-16.3,"MAE_1Y_pct":-38.21,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-11","peak_price":857000,"drawdown_after_peak_pct":-28.94,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"good_stage2_medium_MFE_long_leadtime_not_green","current_profile_verdict":"current_profile_correct_if_actionable_but_Yellow_or_Green_blocked_until_utilization_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_no_CA_candidate","same_entry_group_id":"051910_2022-11-22_687000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C13_R3L190_051910_TENNESSEE_CATHODE_IRA_SUPPLY_CHAIN","trigger_id":"R3L190_C13_051910_20221122_STAGE2_ACTIONABLE","symbol":"051910","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":0.7,"backlog_visibility_score":0.6,"margin_bridge_score":0.32,"revision_score":0.36,"relative_strength_score":0.55,"customer_quality_score":0.72,"policy_or_regulatory_score":0.78,"valuation_repricing_score":0.48,"execution_risk_score":0.46,"legal_or_contract_risk_score":0.12,"dilution_cb_risk_score":0.1,"accounting_trust_risk_score":0.05,"utilization_score":0.3,"ampc_quality_score":0.34,"ex_ampc_profit_score":0.24,"factory_schedule_score":0.56},"weighted_score_before":62.4,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0.7,"backlog_visibility_score":0.6,"margin_bridge_score":0.32,"revision_score":0.36,"relative_strength_score":0.55,"customer_quality_score":0.72,"policy_or_regulatory_score":0.78,"valuation_repricing_score":0.48,"execution_risk_score":0.46,"legal_or_contract_risk_score":0.12,"dilution_cb_risk_score":0.1,"accounting_trust_risk_score":0.05,"utilization_score":0.38,"ampc_quality_score":0.34,"ex_ampc_profit_score":0.24,"factory_schedule_score":0.61},"weighted_score_after":63.4,"stage_label_after":"Stage2-Actionable","changed_components":["utilization_score","margin_bridge_score","factory_schedule_score","execution_risk_score"],"component_delta_explanation":"C13 shadow gate separates JV/IRA/AMPC vocabulary from actual eligible volume, utilization, and ex-AMPC margin conversion.","MFE_90D_pct":10.19,"MAE_90D_pct":-16.3,"score_return_alignment_label":"good_stage2_medium_MFE_long_leadtime_not_green","current_profile_verdict":"current_profile_correct_if_actionable_but_Yellow_or_Green_blocked_until_utilization_bridge"}
{"row_type":"residual_contribution","round":"R3","loop":"190","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","new_independent_case_count":7,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":7,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["JV_headline_false_positive","AMPC_dependency_green_risk","factory_schedule_slip_4C","loss_narrowing_not_margin_conversion","high_MAE_after_real_supply_chain_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

---

## 14. Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 7
new_weight_evidence_candidate_count: 3
guardrail_candidate_count: 4
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
source_proxy_only_count: 0
evidence_url_pending_count: 0
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0
new_independent_ratio: 1.00
ready_for_batch_ingest: true
```

---

## 15. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent for Songdaiki/stock_agent. Do not execute this handoff unless explicitly asked in a later coding session.

Read this MD together with other v12 residual research files. Parse only machine-readable JSONL rows that pass:
- calibration_usable == true
- dedupe_for_aggregate == true
- aggregate_group_role == representative
- required MFE_30D/90D/180D and MAE_30D/90D/180D fields present
- source_proxy_only == false
- evidence_url_pending == false

For C13_BATTERY_JV_UTILIZATION_AMPC_IRA, evaluate a shadow-only canonical archetype gate:
1. JV/IRA/AMPC vocabulary alone does not qualify for Stage2-Actionable or Yellow.
2. Stage2-Actionable requires at least one of eligible production volume, actual utilization, customer pull/call-off confirmation, or explicit margin/FCF bridge.
3. Stage3-Yellow/Green requires ex-AMPC profit quality or credible non-subsidy margin bridge; AMPC larger than operating profit is a Green blocker.
4. Factory schedule slip, mass-production pushout, capex minimization caused by slow EV demand, or utilization decline is non-price 4B/4C evidence.
5. Keep all changes canonical-archetype-specific or L3 sector-specific. Do not lower global Green thresholds.

Output patch specs only after batch aggregation confirms this signal across additional C13 rows.
```

---

## 16. Next Research State

```text
completed_round = R3
completed_loop = 190
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 / Priority 2 quality repair after prior C05 and C01 loops
next_recommended_archetypes = C15_MATERIAL_SPREAD_SUPERCYCLE, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C02_POWER_GRID_DATACENTER_CAPEX, C14_EV_DEMAND_SLOWDOWN_4B_4C, C13_EX_AMPC_MARGIN_POSITIVE_NEGATIVE_PAIR_REPAIR
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
