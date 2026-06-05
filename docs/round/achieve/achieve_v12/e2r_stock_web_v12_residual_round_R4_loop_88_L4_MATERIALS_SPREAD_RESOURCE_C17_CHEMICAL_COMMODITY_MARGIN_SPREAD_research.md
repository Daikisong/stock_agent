# E2R Stock-Web v12 Residual Research — R4 Loop 88 — L4 / C17 Chemical Commodity Margin Spread

## 0. Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R4
scheduled_loop: 88
completed_round: R4
completed_loop: 88
next_round: R5
next_loop: 88
round_schedule_status: valid
round_sector_consistency: pass

large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: PETCHEM_OVERSUPPLY_NAPHTHA_SPREAD_RECOVERY_VS_ACTUAL_MARGIN_BRIDGE

output_file: e2r_stock_web_v12_residual_round_R4_loop_88_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
primary_price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Schedule resolution

Previous run state was interpreted as:

```text
completed_round = R3
completed_loop = 88
next_round = R4
next_loop = 88
```

Therefore this execution must use:

```text
scheduled_round = R4
scheduled_loop = 88
```

R4 maps to `L4_MATERIALS_SPREAD_RESOURCE`. This file keeps the round/sector pair valid and uses the C17 chemical commodity margin-spread canonical archetype.

## 2. No-Repeat / coverage check

The No-Repeat Index snapshot shows:

```text
C15_MATERIAL_SPREAD_SUPERCYCLE              rows=28 symbols=11 4B/4C=3/0
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY        rows=36 symbols=23 4B/4C=2/0
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD        rows=21 symbols=15 4B/4C=4/0
```

C17 already has some 4B samples but still has no 4C samples, and its key stress point remains whether **spread recovery headlines** are prematurely treated as Stage2/Stage3 evidence while actual naphtha / petrochemical margins remain structurally weak.

Hard duplicate rule used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

This file intentionally avoids the most repeated C17 symbols in the index where possible, but allows one soft-repeat symbol when the trigger family and date are materially different. The research value is the residual failure mode: **sector-level recovery narrative without actual spread, utilization, or cashflow bridge**.

## 3. External evidence context

Reuters reported in August 2024 that petrochemical producers in Asia and Europe were under pressure from years of China capacity build-out and weak margins, with oversupply expected to persist as new plants continued coming online in the Middle East and China.

Reuters later reported that LG Chem and Lotte Chemical both suffered in 2024 from persistent oversupply. The same Reuters report said Lotte Chemical's 2024 operating loss deepened materially and LG Chem's petrochemical division posted a Q4 operating loss, while both companies cited global glut / Northeast Asia oversupply as core drivers.

This matters for C17 because chemical spread signals are not like order backlog. A spread trade is a valve: if feedstock, product price, utilization, and inventory do not open in the same direction, the first pressure spike can vent through drawdown rather than rerating.

## 4. Stock-Web validation scope

| symbol | name | profile check | corp-action overlap with entry~D+180 | calibration status |
|---|---|---|---|---|
| 051910 | LG화학 | active_like, 2001~2026, tradable rows available, raw_unadjusted_marcap | none in profile | usable |
| 011170 | 롯데케미칼 | active_like, 1995~2026, tradable rows available, raw_unadjusted_marcap | profile has 2023-02-13 candidate, outside 2024 window | usable |
| 011780 | 금호석유화학 | active_like, 1995~2026, tradable rows available, raw_unadjusted_marcap | profile has 2001-01-16 candidate, outside 2024 window | usable |

## 5. Case grid

| case_id | symbol | trigger_type | entry_date | entry_price | verdict | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | main residual |
|---|---:|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---|
| R4L88_C17_051910_2024-02-02_PETCHEM_OVERSUPPLY_RECOVERY_WATCH | 051910 | Stage2-FalsePositive-Candidate | 2024-02-02 | 461000 | counterexample | +12.8% | -6.7% | +12.8% | -24.5% | +12.8% | -40.9% | recovery headline without division-level spread/cashflow bridge |
| R4L88_C17_011170_2024-02-01_PETCHEM_TURNAROUND_HEADLINE_NO_SPREAD_BRIDGE | 011170 | Stage2-FalsePositive | 2024-02-01 | 140100 | counterexample | +0.5% | -16.6% | +0.5% | -29.1% | +0.5% | -45.4% | loss-cycle name treated as turn before actual spread inflection |
| R4L88_C17_011780_2024-01-29_SYNTHETIC_RUBBER_SPREAD_LOCAL_4B_POSITIVE | 011780 | Stage2-Actionable | 2024-01-29 | 125400 | positive_with_local_4b_overlay | +30.7% | -1.0% | +30.7% | -2.3% | +33.2% | -3.7% | synthetic rubber chain did work, but local 4B must still protect peak capture |

## 6. Representative price-path notes

### 6.1 LG화학 / 051910

Stock-web rows show 051910 closed at 461,000 on 2024-02-02 after a large move. It reached a high of 520,000 on 2024-02-19, but later fell to a 2024-08-05 low near 263,500~272,500 range depending on low/close field. This is a classic failed C17 bridge: a short squeeze / recovery hope created local MFE, but the actual margin environment did not sustain rerating.

Interpretation:

```text
entry_price = 461000
peak_price_30d = 520000
trough_price_180d = 272500
MFE30 = (520000 / 461000 - 1) = +12.8%
MAE180 = (272500 / 461000 - 1) = -40.9%
```

### 6.2 롯데케미칼 / 011170

Stock-web rows show 011170 closed at 140,100 on 2024-02-01. The same window produced almost no upside: the high around the entry window was roughly 140,800. The share then slid through July/August and reached low levels near 79,400~76,500 in the 180D window.

Interpretation:

```text
entry_price = 140100
peak_price_30d = 140800
trough_price_180d = 76500
MFE30 = +0.5%
MAE180 = -45.4%
```

### 6.3 금호석유화학 / 011780

Stock-web rows show 011780 closed at 125,400 on 2024-01-29 after a strong move. The share reached 163,900 by 2024-02-19 and later 167,000 by 2024-07-15. That validates a C17 positive sub-case where synthetic rubber / butadiene-linked spread behavior diverged from broad NCC oversupply. The later fall to 120,700 on 2024-08-05 still makes a local 4B overlay appropriate once the move exceeded +30%.

Interpretation:

```text
entry_price = 125400
peak_price_30d = 163900
peak_price_180d = 167000
trough_price_180d = 120700
MFE30 = +30.7%
MFE180 = +33.2%
peak_to_trough_drawdown = (120700 / 167000 - 1) = -27.7%
```

## 7. Machine-readable trigger rows

```jsonl
{"row_type": "trigger", "research_version": "v12", "scheduled_round": "R4", "scheduled_loop": 88, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "PETCHEM_OVERSUPPLY_NAPHTHA_SPREAD_RECOVERY_VS_ACTUAL_MARGIN_BRIDGE", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "usable_for_new_weight_evidence": false, "case_id": "R4L88_C17_051910_2024-02-02_PETCHEM_OVERSUPPLY_RECOVERY_WATCH", "symbol": "051910", "name": "LG화학", "trigger_date": "2024-02-01", "entry_date": "2024-02-02", "entry_price": 461000, "trigger_type": "Stage2-FalsePositive-Candidate", "case_verdict": "counterexample", "mfe_30d_pct": 12.8, "mae_30d_pct": -6.7, "mfe_90d_pct": 12.8, "mae_90d_pct": -24.5, "mfe_180d_pct": 12.8, "mae_180d_pct": -40.9, "peak_date": "2024-02-19", "peak_price": 520000, "trough_date": "2024-08-05", "trough_price": 272500, "profile_error": "Stage2 oversupply-recovery watch was too early without division-level spread/cashflow bridge", "evidence": "2024 sector recovery hope / China stimulus expectation, but later Reuters reported LG Chem petrochemical division had Q4 operating loss and cited Northeast Asia oversupply.", "source_quality": "external_sector/company_reported_reuters + stock_web_price"}
{"row_type": "trigger", "research_version": "v12", "scheduled_round": "R4", "scheduled_loop": 88, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "PETCHEM_OVERSUPPLY_NAPHTHA_SPREAD_RECOVERY_VS_ACTUAL_MARGIN_BRIDGE", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "usable_for_new_weight_evidence": false, "case_id": "R4L88_C17_011170_2024-02-01_PETCHEM_TURNAROUND_HEADLINE_NO_SPREAD_BRIDGE", "symbol": "011170", "name": "롯데케미칼", "trigger_date": "2024-02-01", "entry_date": "2024-02-01", "entry_price": 140100, "trigger_type": "Stage2-FalsePositive", "case_verdict": "counterexample", "mfe_30d_pct": 0.5, "mae_30d_pct": -16.6, "mfe_90d_pct": 0.5, "mae_90d_pct": -29.1, "mfe_180d_pct": 0.5, "mae_180d_pct": -45.4, "peak_date": "2024-02-01", "peak_price": 140800, "trough_date": "2024-09-10", "trough_price": 76500, "profile_error": "Commodity spread headline failed because there was no confirmed spread inflection or loss-reduction bridge.", "evidence": "Reuters later reported Lotte Chemical 2024 operating losses deepened sharply under oversupply.", "source_quality": "external_company_reported_reuters + stock_web_price"}
{"row_type": "trigger", "research_version": "v12", "scheduled_round": "R4", "scheduled_loop": 88, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "PETCHEM_OVERSUPPLY_NAPHTHA_SPREAD_RECOVERY_VS_ACTUAL_MARGIN_BRIDGE", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "usable_for_new_weight_evidence": true, "case_id": "R4L88_C17_011780_2024-01-29_SYNTHETIC_RUBBER_SPREAD_LOCAL_4B_POSITIVE", "symbol": "011780", "name": "금호석유화학", "trigger_date": "2024-01-29", "entry_date": "2024-01-29", "entry_price": 125400, "trigger_type": "Stage2-Actionable", "case_verdict": "positive_with_local_4b_overlay", "mfe_30d_pct": 30.7, "mae_30d_pct": -1.0, "mfe_90d_pct": 30.7, "mae_90d_pct": -2.3, "mfe_180d_pct": 33.2, "mae_180d_pct": -3.7, "peak_date": "2024-07-15", "peak_price": 167000, "trough_date": "2024-08-05", "trough_price": 120700, "profile_error": "Positive case, but local 4B should activate after +30% spread rally because global petchem glut remained unresolved.", "evidence": "Synthetic rubber/butadiene chain behaved better than NCC-heavy commodity chemicals; price path confirms sustained MFE with later drawdown.", "source_quality": "stock_web_price + sector_context_reuters; company_specific_url_pending"}
```

## 8. Raw component score breakdown

The scores below are not production scoring changes. They are shadow research scores for explaining why the current calibrated profile should avoid global promotion from this small sample.

| component | 051910 | 011170 | 011780 | comment |
|---|---:|---:|---:|---|
| EPS/FCF Explosion | 5 | 3 | 10 | only 011780 had price-confirmed spread behavior; LG/Lotte lacked earnings bridge |
| Earnings Visibility | 6 | 4 | 11 | commodity margin visibility weak for NCC names |
| Bottleneck/Pricing | 8 | 4 | 13 | rubber/specialty exposure was better than broad ethylene/NCC |
| Market Mispricing | 8 | 6 | 12 | all had cheap/cyclic bounce narratives, but only one converted |
| Valuation Rerating | 7 | 4 | 12 | 051910 and 011170 failed sustained rerating |
| Capital Allocation | 4 | 4 | 6 | not the decisive driver |
| Information Confidence | 7 | 7 | 6 | Reuters/company-reported sector context strong, company-specific 011780 bridge still URL-pending |
| raw_total_proxy | 45 | 32 | 70 | only 011780 approaches Stage2-Actionable quality |

## 9. Score-return alignment

| symbol | expected if naive Stage2 | observed price path | alignment |
|---|---|---|---|
| 051910 | recovery theme should hold 90~180D | local upside failed, 180D MAE deep | bad Stage2 |
| 011170 | loss-cycle recovery should produce at least modest MFE | almost no MFE, deep MAE | bad Stage2 |
| 011780 | spread-sensitive rubber chain should produce fast MFE | +30% MFE reached quickly | good Stage2, but 4B overlay needed |

## 10. Local 4B vs full-window 4B

| symbol | local 4B? | full-window 4B? | reason |
|---|---|---|---|
| 051910 | false | false | MFE did not reach +20~30% and then collapsed |
| 011170 | false | false | no meaningful MFE |
| 011780 | true | partial | MFE30 exceeded +30%, but global petchem glut remained unresolved; local peak protection should activate |

## 11. Residual contribution

```yaml
new_independent_case_count: 3
reused_case_count: 0
same_archetype_new_symbol_count: 2
soft_repeat_symbol_count: 1
positive_case_count: 1
counterexample_count: 2
local_4b_overlay_case_count: 1
hard_4c_case_count: 0
calibration_usable_case_count: 3

loop_contribution_label: residual_error_found
do_not_propose_new_weight_delta: true
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
existing_axis_strengthened: stage2_required_bridge
existing_axis_weakened: null
new_axis_proposed: null
```

### Residual rule candidate, shadow-only

```text
For C17_CHEMICAL_COMMODITY_MARGIN_SPREAD:
    Stage2-Actionable should require at least two of:
      1. product-feedstock spread inflection visible in reported margin / industry spread data
      2. company-level utilization or inventory drawdown evidence
      3. earnings revision / loss-narrowing bridge that is not solely price-based
      4. segment mix away from broad NCC oversupply into higher-beta rubber/specialty spread

    If evidence is only "China stimulus / sector bottom / commodity bounce":
      classify as Stage2-Watch or Stage2-FalsePositive-Candidate, not Stage2-Actionable.

    If MFE30 >= +30% while global oversupply remains unresolved:
      activate local_4b_watch_guard even for positive spread cases.
```

## 12. Deferred Coding Agent Handoff Prompt

```text
Do not execute now.

Use this MD as one v12 calibration input for C17_CHEMICAL_COMMODITY_MARGIN_SPREAD.
Ingest trigger JSONL rows only after standard validation.
Do not change production scoring directly from this file.
Treat the proposed C17 bridge rule as shadow evidence only.
Strengthen existing stage2_required_bridge logic only if confirmed by broader C17 aggregate evidence.
Do not promote price-only chemical recovery headlines to Stage2/Green without non-price spread/utilization/margin bridge evidence.
```

## 13. Terminal state

```text
completed_round = R4
completed_loop = 88
next_round = R5
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
```
