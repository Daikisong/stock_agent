---
research_version: stock_web_v12_residual
selected_round: R7
selected_loop: 140
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0/1 quality repair — C25 medical-device export/reimbursement bridge, direct URL/proxy repair, 4C-thin path repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: DEVICE_EXPORT_REIMBURSEMENT_REPEAT_USAGE_MARGIN_BRIDGE
file_name: e2r_stock_web_v12_residual_round_R7_loop_140_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: '2026-02-20'
production_scoring_changed: false
shadow_weight_only: true
---

# E2R v12 Residual Calibration — R7 / C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT / loop 140

## 0. Execution binding

MAIN EXECUTION PROMPT: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt

NO-REPEAT INDEX: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md

This standalone MD follows the v12 historical calibration protocol: no live scan, no `stock_agent` code patch, no production scoring change, no auto-trading, and no price-route hunt. The No-Repeat Index is used only as a duplicate/coverage ledger. This file is intended as a batch-ingestable research artifact for C25 quality repair.

## 1. Coverage-index selection rationale

The current No-Repeat Index has moved from raw row-count filling to quality repair. All C01~C32 canonical archetypes exceed the old 80-row minimum, while URL/proxy quality, complete 30/90/180D MFE/MAE, entry-basis consistency, and thin 4C paths remain repair targets.

C25 is a suitable repair target because the ledger shows `244` representative rows, `52` symbols, `31/60` positive/counter split, and only `24/4` 4B/4C coverage. The selected fine path focuses on the difference between a real device/reimbursement/export bridge and a product-launch, reimbursement-status, or policy-tailwind headline that never converts into repeat usage, hospital adoption, export channel growth, or margin.

## 2. Scope and duplicate avoidance

- Previous immediate R7 work in this session covered C23 FDA approval/commercialization and C24 trial-data event risk.
- This file avoids those by using C25 medical-device/export/reimbursement mechanics: installed base, consumables, dental/diagnostic imaging exports, CGM reimbursement/CE, AI medical software reimbursement, and detector/device margin recovery.
- Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date + evidence_family`.
- Reused case count: 0.

## 3. Canonical / fine / deep compression map

| canonical_archetype_id | fine_archetype_id | deep path | scoring implication |
|---|---|---|---|
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | DEVICE_EXPORT_REIMBURSEMENT_REPEAT_USAGE_MARGIN_BRIDGE | FDA/CE/reimbursement + export channel + repeat usage/consumable + OP margin bridge | Allow Stage2-Actionable when at least two bridge proofs exist |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | MEDICAL_AI_REIMBURSEMENT_REVENUE_WITH_PROFITABILITY_DELAY | AI device/reimbursement status with delayed hospital adoption/profitability | Stage4B until adoption/profit bridge proves durable |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | DENTAL_IMPLANT_CHINA_EXPORT_VBP_RISK | dental implant export exposed to reimbursement/pricing/patient-flow risk | Stage4C when VBP/channel pressure breaks the thesis |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | DETECTOR_EXPORT_HIGH_VALUE_ADDED_PRODUCT_MARGIN_RECOVERY | high-value detector export and margin recovery | Stage2-Actionable / Yellow candidate with drawdown-aware confirmation |

## 4. Stock-Web price validation binding

- Manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- Schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
- `price_source = Songdaiki/stock-web`
- `price_basis = tradable_raw`
- `price_adjustment_status = raw_unadjusted_marcap`
- `calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year`
- `stock_web_manifest_max_date = 2026-02-20`
- MFE/MAE definition: entry close versus forward N-tradable-day maximum high / minimum low.
- Entry rule in this file: because disclosure time is either post-market or not safe to prove as pre-close for every row, use the next tradable day after the evidence date.
- All rows below contain complete `MFE_30D_pct`, `MFE_90D_pct`, `MFE_180D_pct`, `MAE_30D_pct`, `MAE_90D_pct`, and `MAE_180D_pct` fields.
- No row below has corporate-action contamination in its entry~D+180 usable window. Classys/Vieworks have old corporate-action candidates outside the tested window; Dentium has none; other tested rows have no overlap in D~D+180.

## 5. Evidence source map

| case_id | symbol | company | source quality | source_proxy_only | evidence note |
| --- | --- | --- | --- | --- | --- |
| C25-R7-L140-001 | 145720 | Dentium | article + company global export confirmation | false | China dental implant VBP result allocated Dentium about 400,000 sets and classified domestic winners as Class A; Dentium global site states exports to 80+ countries. |
| C25-R7-L140-002 | 338220 | VUNO | company product/history + article confirmation | false | VUNO history lists FDA Breakthrough Device designation for VUNO Med-DeepCARS in Jun. 2023 and later reimbursement/market-access milestones; product page states MFDS approval, CE certification, and FDA breakthrough designation. |
| C25-R7-L140-003 | 099190 | i-SENS | company history + industry article | false | i-SENS applied for a European CE mark change for CareSens Air and disclosed Netherlands/Germany launches with plans for 14 countries by end-2024. |
| C25-R7-L140-004 | 214150 | Classys | company IR | false | Classys posted its 43rd J.P. Morgan Healthcare Conference IR material dated Jan. 16, 2025, providing direct company-level device/export platform evidence. |
| C25-R7-L140-005 | 322510 | JLK | article with fee status | false | JLK stroke AI solution JBS-01K received non-reimbursed status and a 54,300 won fee ceiling, but the forward path showed the fee event alone did not prove adoption or profitability. |
| C25-R7-L140-006 | 228670 | Ray | sell-side PDF proxy | true | Mirae Asset described Ray as a digital dentistry player with China lockdown/VBP tailwinds and vertical-integration optionality, but the row is source-proxy and later suffered high MAE. |
| C25-R7-L140-007 | 043150 | Vatech | company result release | false | VATECH reported Q2 2024 revenue/OP, 89.8% export sales, and North America growth, but the forward path failed to rerate and broke into drawdown. |
| C25-R7-L140-008 | 100120 | Vieworks | company result release | false | Vieworks reported 2024 revenue of KRW 222.9bn, OP of KRW 22.2bn, profit improvement, high-value detector sales, dental/non-destructive detector growth, and export-driven finance income. |

### Source URLs

- Dentium / China VBP allocation: https://www.asiae.co.kr/en/article/2023011308342450737
- Dentium global export profile: https://www.dentiumusa.com/about-dentium
- VUNO history: https://www.vuno.co/en/history
- VUNO DeepCARS product page: https://www.vuno.co/en/deepcars
- i-SENS CareSens Air CE / Europe launch: https://www.koreabiomed.com/news/articleView.html?idxno=25045
- i-SENS history: https://i-sens.com/history/
- Classys JP Morgan IR material: https://classys.co.kr/investment/ir-book/?mod=document&pageid=2&uid=516
- JLK non-reimbursed fee status: https://www.asiae.co.kr/en/article/2023103109514061131
- Ray Mirae report: https://securities.miraeasset.com/bbs/download/2104927.pdf?attachmentId=2104927
- Vatech Q2 2024 official result: https://www.vatech.com/news/525049
- Vieworks 2024 result: https://www.vieworks.com/kr/board/news_view/17473

## 6. Case selection table

| case_id | symbol | company | trigger_date | entry_date | trigger_type | classification | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | source_proxy_only |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C25-R7-L140-001 | 145720 | Dentium | 2023-01-13 | 2023-01-16 | Stage3-Green | positive | 97000 | 39.18 | 75.26 | 90.72 | -2.99 | -2.99 | -2.99 | false |
| C25-R7-L140-002 | 338220 | VUNO | 2023-06-08 | 2023-06-09 | Stage3-Yellow | positive | 28000 | 62.14 | 148.21 | 148.21 | -9.11 | -10.36 | -14.64 | false |
| C25-R7-L140-003 | 099190 | i-SENS | 2024-09-04 | 2024-09-05 | Stage2-Actionable | positive | 15530 | 35.22 | 35.22 | 35.22 | -6.5 | -6.5 | -16.48 | false |
| C25-R7-L140-004 | 214150 | Classys | 2025-01-16 | 2025-01-17 | Stage3-Green | positive | 52200 | 36.97 | 42.53 | 42.53 | -6.7 | -6.7 | -12.07 | false |
| C25-R7-L140-005 | 322510 | JLK | 2023-10-31 | 2023-11-01 | Stage4C | counterexample | 25850 | 21.86 | 21.86 | 21.86 | -21.66 | -53.23 | -65.22 | false |
| C25-R7-L140-006 | 228670 | Ray | 2023-03-28 | 2023-03-29 | Stage4B | counterexample | 31350 | 26.0 | 34.45 | 34.45 | -2.87 | -2.87 | -38.12 | true |
| C25-R7-L140-007 | 043150 | Vatech | 2024-08-08 | 2024-08-09 | Stage4C | counterexample | 24850 | 2.41 | 4.23 | 4.23 | -8.65 | -22.9 | -25.55 | false |
| C25-R7-L140-008 | 100120 | Vieworks | 2025-02-11 | 2025-02-12 | Stage2-Actionable | positive | 21600 | 15.51 | 17.13 | 17.13 | -1.85 | -2.55 | -15.69 | false |

## 7. Trigger-level OHLC / price-path rows

| case_id | symbol | price_shard_path | entry_row | peak_180D_date | peak_180D_high | trough_180D_date | trough_180D_low |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C25-R7-L140-001 | 145720 | `atlas/ohlcv_tradable_by_symbol_year/145/145720/2023.csv` | `2023-01-16,94500.0,97000.0,94100.0,97000.0,51438,4954469900,1073676510000,11068830,KOSPI` | 2023-06-02 | 185000 | 2023-01-16 | 94100 |
| C25-R7-L140-002 | 338220 | `atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv` | `2023-06-09,26300.0,28000.0,25450.0,28000.0,1306431,35363061900,319817568000,11422056,KOSDAQ` | 2023-09-07 | 69500 | 2023-10-24 | 23900 |
| C25-R7-L140-003 | 099190 | `atlas/ohlcv_tradable_by_symbol_year/099/099190/2024.csv` | `2024-09-05,15660.0,16170.0,15490.0,15530.0,120929,1895360050,429206849690,27637273,KOSDAQ` | 2024-10-18 | 21000 | 2025-04-09 | 12970 |
| C25-R7-L140-004 | 214150 | `atlas/ohlcv_tradable_by_symbol_year/214/214150/2025.csv` | `2025-01-17,51300.0,53200.0,51300.0,52200.0,115240,6022984900,3419395399800,65505659,KOSDAQ GLOBAL` | 2025-05-12 | 74400 | 2025-10-15 | 45900 |
| C25-R7-L140-005 | 322510 | `atlas/ohlcv_tradable_by_symbol_year/322/322510/2023.csv` | `2023-11-01,24600.0,25900.0,23300.0,25850.0,907005,22386097000,417935355200,16167712,KOSDAQ` | 2023-11-06 | 31500 | 2024-04-25 | 8990 |
| C25-R7-L140-006 | 228670 | `atlas/ohlcv_tradable_by_symbol_year/228/228670/2023.csv` | `2023-03-29,31000.0,32750.0,30900.0,31350.0,201956,6362411900,444761101950,14186957,KOSDAQ` | 2023-06-15 | 42150 | 2023-10-27 | 19400 |
| C25-R7-L140-007 | 043150 | `atlas/ohlcv_tradable_by_symbol_year/043/043150/2024.csv` | `2024-08-09,25450.0,25450.0,24500.0,24850.0,79412,1969778100,369128261600,14854256,KOSDAQ` | 2024-10-29 | 25900 | 2025-02-03 | 18500 |
| C25-R7-L140-008 | 100120 | `atlas/ohlcv_tradable_by_symbol_year/100/100120/2025.csv` | `2025-02-12,22000.0,22000.0,21250.0,21600.0,39760,859197350,216040284000,10001865,KOSDAQ` | 2025-04-16 | 25300 | 2025-11-05 | 18210 |

## 8. Positive / counterexample balance

### Positive cases

1. **Dentium (145720)** — China dental implant VBP changed from a price-cut fear into a volume/allocation bridge. The row shows a clean 180D MFE with shallow MAE, so C25 should not blindly penalize all reimbursement/VBP events.
2. **VUNO (338220)** — FDA Breakthrough Device status and existing medical-AI market-access history created a real de-risking bridge. It is kept as Stage3-Yellow rather than immediate Green because hospital adoption/profit conversion still required confirmation.
3. **i-SENS (099190)** — CareSens Air Europe launch/CE-change path created a valid CGM export bridge. It opens Stage2-Actionable, but Green still requires repeat sensor revenue and reimbursement breadth.
4. **Classys (214150)** — Aesthetic device installed-base and global IR evidence produced a durable forward path. Green is allowed only after drawdown-aware confirmation.
5. **Vieworks (100120)** — Detector export/high-value-added product mix and OP recovery formed a direct result bridge. This is a cleaner C25 positive than generic medical-device beta.

### Counterexamples / guardrail cases

1. **JLK (322510)** — Non-reimbursed fee status produced an early spike but then collapsed. Fee status alone is not hospital adoption or profitability.
2. **Ray (228670)** — China VBP and digital-dentistry tailwinds were real but broker-proxy-heavy and later high-MAE. This is local 4B, not Green.
3. **Vatech (043150)** — Official Q2 results and high export mix were not enough for a forward rerating. Backward results without new adoption/order/reimbursement acceleration should not be overcredited.

## 9. Stage2 / Yellow / Green calibration stress test

| stage gate | observed residual | repair implication |
|---|---|---|
| Stage2 | Product approval, launch, FDA/CE, reimbursement label, or export mix alone often fires too early | Require at least two of reimbursement breadth, export channel, installed base, repeat usage/consumable pull, revenue/OP conversion |
| Stage2-Actionable | Direct quarterly revenue/OP and product export bridge can work even with initial MAE | Allow Actionable but attach drawdown-aware confirmation before Yellow/Green |
| Stage3-Yellow | Repeat usage, installed base, and reimbursement/export channel evidence improve durability | Yellow allowed when company-level revenue/margin evidence confirms the device economics |
| Stage3-Green | Green is unsafe from launch headline alone | Green should require commercial uptake, reimbursement/export repeatability, and margin bridge; otherwise cap at Yellow/4B |
| Stage4B | Strong story + high MAE + incomplete profit/adoption bridge | Use 4B for Ray/VUNO-like cases where evidence is real but conversion quality remains incomplete |
| Stage4C | Launch/fee/export/result story breaks through weak adoption, pricing, or forward economics | Use 4C for JLK/Vatech-style cases when market adoption/reimbursement/pricing/forward-rerating thesis breaks |

## 10. 4B timing audit

C25 has a dangerous false comfort zone: medical-device stories can have real products and real regulatory status, but commercialization cadence is slow. A product can be clinically real and still financially premature. The proper 4B trigger is not simply `price fell`; it is:

- high-MAE after a launch/reimbursement/status event,
- missing current revenue or margin bridge,
- weak hospital/channel adoption proof,
- unclear reimbursement breadth or payment level,
- weak repeat usage/consumable economics,
- source-proxy-heavy evidence where the direct company revenue path is not yet visible.

Ray is the clean 4B example in this loop: the report's China VBP/digital dentistry logic was plausible, but the row demanded a conversion-quality checkpoint before any Green promotion.

## 11. 4C hard-break audit

C25 hard 4C should be reserved for cases where the financial bridge breaks, not merely where the device story is early.

Hard 4C conditions strengthened by this loop:

- launch/event occurs but adoption/reimbursement uptake fails to appear,
- revenue bridge is too small relative to valuation reset,
- pricing/reimbursement regime changes damage unit economics,
- export channel or patient-flow weakness undermines the thesis,
- backward result looks fine but forward order/adoption/reimbursement acceleration is absent,
- operating/margin bridge reverses despite product status.

## 12. Canonical rule candidate

```text
new_axis_proposed: C25_DEVICE_EXPORT_REIMBURSEMENT_REPEAT_USAGE_GATE
```

**Rule candidate:** For C25, do not open Stage2-Actionable or Green from `medical device`, `FDA/CE`, `reimbursement`, `export`, `AI medical`, `CGM`, `implant`, `detector`, or `aesthetic device` keywords alone. Require at least two of:

1. named device/product with material company exposure,
2. named reimbursement / FDA / CE / payer / market-access status,
3. export channel or overseas installed-base evidence,
4. repeat usage / consumable / sensor / service revenue proof,
5. current revenue, OP, margin, or revision conversion,
6. hospital adoption or distributor reorder proof.

**Exception:** A direct quarterly result bridge can open Stage2-Actionable before full reimbursement proof, but Yellow/Green should be delayed if 30D/90D MAE exceeds guardrail thresholds.

## 13. Raw component score breakdown

| case_id | eps_fcf | visibility | bottleneck_pricing | mispricing | valuation_rerating | capital_return | info_confidence | stage_before | stage_after |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C25-R7-L140-001 | 21 | 27 | 14 | 9 | 10 | 2 | 12 | Stage3-Green | Stage3-Green_candidate_with_margin_watch |
| C25-R7-L140-002 | 10 | 24 | 13 | 13 | 11 | 0 | 13 | Stage3-Yellow | Stage3-Yellow_keep_not_green_until_hospital_revenue_profit_bridge |
| C25-R7-L140-003 | 12 | 23 | 12 | 11 | 10 | 1 | 13 | Stage2-Actionable | Stage2-Actionable_with_sensor_revenue_confirmation_needed |
| C25-R7-L140-004 | 22 | 25 | 13 | 11 | 10 | 5 | 12 | Stage3-Green | Stage3-Green_candidate_allowed_after_drawdown_confirmation |
| C25-R7-L140-005 | 5 | 11 | 10 | 16 | 14 | 0 | 9 | Stage4C | Stage4C |
| C25-R7-L140-006 | 12 | 15 | 13 | 14 | 12 | 1 | 6 | Stage4B | Stage4B_watch_not_green |
| C25-R7-L140-007 | 14 | 18 | 10 | 12 | 10 | 2 | 12 | Stage4C | Stage4C |
| C25-R7-L140-008 | 19 | 23 | 12 | 10 | 8 | 3 | 12 | Stage2-Actionable | Stage2-Actionable_with_yellow_confirmation_needed |

## 14. Shadow weight proposal

Production scoring remains unchanged. This is a shadow-only candidate.

| component | before | after | delta | rationale |
|---|---:|---:|---:|---|
| eps_fcf | 20 | 20 | +0 | unchanged; EPS/OP conversion still matters but should not overwhelm adoption/reimbursement quality |
| visibility | 22 | 24 | +2 | increase; reimbursement/export/installed-base/repeat-usage proof is the core separator |
| bottleneck_pricing | 13 | 12 | -1 | slight decrease; product niche alone overcredits early device stories |
| mispricing | 14 | 12 | -2 | decrease; many device stories are valuation/event overcredits |
| valuation_rerating | 12 | 11 | -1 | slight decrease; launch headlines invite premature rerating |
| capital_return | 9 | 9 | +0 | unchanged; mostly irrelevant to C25 |
| info_confidence | 10 | 12 | +2 | increase; direct company URLs and reimbursement/adoption specificity are essential |

## 15. Residual contribution summary

```text
auto_selected_coverage_gap: C25 source/proxy quality repair + reimbursement/export bridge + hard 4C path repair
sector_specific_rule_candidate: L7 medical-device/healthcare에서 approval/reimbursement/export label만으로 Stage2-Actionable을 열지 않고, repeat usage·installed base·hospital/channel adoption·revenue/OP conversion을 요구
canonical_archetype_rule_candidate: C25는 named device/reimbursement/export proof + commercial/usage/margin bridge 중 최소 2개 이상 충족 전에는 Stage2/Watch cap; hard 4C는 adoption/reimbursement/pricing/channel/forward-rerating thesis break가 필요
loop_contribution_label: C25_device_export_reimbursement_repeat_usage_quality_repair
new_axis_proposed: C25_DEVICE_EXPORT_REIMBURSEMENT_REPEAT_USAGE_GATE
existing_axis_strengthened: stage2_required_bridge; local_4b_watch_guard; hard_4c_confirmation; full_4b_requires_non_price_evidence; drawdown_aware_confirmation; information_confidence_gate
existing_axis_weakened: null
do_not_propose_new_weight_delta: false
production_scoring_changed: false
shadow_weight_only: true
```

## 16. Machine-readable trigger JSONL

```jsonl
{"MAE_180D_pct": -2.99, "MAE_30D_pct": -2.99, "MAE_90D_pct": -2.99, "MFE_180D_pct": 90.72, "MFE_30D_pct": 39.18, "MFE_90D_pct": 75.26, "calibration_usable": true, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25-R7-L140-001", "classification": "positive", "company_name": "Dentium", "current_profile_error_type": "undercredit_volume_based_procurement_export_bridge", "do_not_count_as_new_case": false, "entry_date": "2023-01-16", "entry_price": 97000, "evidence_family": "china_vbp_allocated_volume_export_reimbursement_policy", "evidence_url": "https://www.asiae.co.kr/en/article/2023011308342450737", "evidence_url_pending": false, "fine_archetype_id": "DENTAL_IMPLANT_CHINA_VBP_EXPORT_VOLUME_BRIDGE", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "peak_180D_date": "2023-06-02", "peak_180D_high": 185000, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/145/145720/2023.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/145/145720.json", "row_type": "trigger", "same_entry_group_id": "C25-145720-2023-01-16-china_vbp_allocated_volume_export_reimbursement_policy", "source_proxy_only": false, "symbol": "145720", "trigger_date": "2023-01-13", "trigger_type": "Stage3-Green", "trough_180D_date": "2023-01-16", "trough_180D_low": 94100}
{"MAE_180D_pct": -14.64, "MAE_30D_pct": -9.11, "MAE_90D_pct": -10.36, "MFE_180D_pct": 148.21, "MFE_30D_pct": 62.14, "MFE_90D_pct": 148.21, "calibration_usable": true, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25-R7-L140-002", "classification": "positive", "company_name": "VUNO", "current_profile_error_type": "undercredit_regulatory_de_risking_but_green_needs_profit_bridge", "do_not_count_as_new_case": false, "entry_date": "2023-06-09", "entry_price": 28000, "evidence_family": "fda_breakthrough_medical_ai_reimbursement_status", "evidence_url": "https://www.vuno.co/en/history", "evidence_url_pending": false, "fine_archetype_id": "MEDICAL_AI_FDA_BREAKTHROUGH_REIMBURSEMENT_ADOPTION_BRIDGE", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "peak_180D_date": "2023-09-07", "peak_180D_high": 69500, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/338/338220.json", "row_type": "trigger", "same_entry_group_id": "C25-338220-2023-06-09-fda_breakthrough_medical_ai_reimbursement_status", "source_proxy_only": false, "symbol": "338220", "trigger_date": "2023-06-08", "trigger_type": "Stage3-Yellow", "trough_180D_date": "2023-10-24", "trough_180D_low": 23900}
{"MAE_180D_pct": -16.48, "MAE_30D_pct": -6.5, "MAE_90D_pct": -6.5, "MFE_180D_pct": 35.22, "MFE_30D_pct": 35.22, "MFE_90D_pct": 35.22, "calibration_usable": true, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25-R7-L140-003", "classification": "positive", "company_name": "i-SENS", "current_profile_error_type": "stage2_actionable_allowed_but_green_requires_sensor_repeat_revenue", "do_not_count_as_new_case": false, "entry_date": "2024-09-05", "entry_price": 15530, "evidence_family": "cgm_eu_launch_ce_change_international_rollout", "evidence_url": "https://www.koreabiomed.com/news/articleView.html?idxno=25045", "evidence_url_pending": false, "fine_archetype_id": "CGM_EU_CE_LAUNCH_SENSOR_REPEAT_REVENUE_BRIDGE", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "peak_180D_date": "2024-10-18", "peak_180D_high": 21000, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/099/099190/2024.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/099/099190.json", "row_type": "trigger", "same_entry_group_id": "C25-099190-2024-09-05-cgm_eu_launch_ce_change_international_rollout", "source_proxy_only": false, "symbol": "099190", "trigger_date": "2024-09-04", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2025-04-09", "trough_180D_low": 12970}
{"MAE_180D_pct": -12.07, "MAE_30D_pct": -6.7, "MAE_90D_pct": -6.7, "MFE_180D_pct": 42.53, "MFE_30D_pct": 36.97, "MFE_90D_pct": 42.53, "calibration_usable": true, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25-R7-L140-004", "classification": "positive", "company_name": "Classys", "current_profile_error_type": "positive_bridge_with_drawdown_aware_confirmation", "do_not_count_as_new_case": false, "entry_date": "2025-01-17", "entry_price": 52200, "evidence_family": "medical_aesthetic_device_global_ir_installed_base_consumables", "evidence_url": "https://classys.co.kr/investment/ir-book/?mod=document&pageid=2&uid=516", "evidence_url_pending": false, "fine_archetype_id": "AESTHETIC_DEVICE_GLOBAL_INSTALLED_BASE_CONSUMABLE_EXPORT_BRIDGE", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "peak_180D_date": "2025-05-12", "peak_180D_high": 74400, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214150/2025.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/214/214150.json", "row_type": "trigger", "same_entry_group_id": "C25-214150-2025-01-17-medical_aesthetic_device_global_ir_installed_base_consumables", "source_proxy_only": false, "symbol": "214150", "trigger_date": "2025-01-16", "trigger_type": "Stage3-Green", "trough_180D_date": "2025-10-15", "trough_180D_low": 45900}
{"MAE_180D_pct": -65.22, "MAE_30D_pct": -21.66, "MAE_90D_pct": -53.23, "MFE_180D_pct": 21.86, "MFE_30D_pct": 21.86, "MFE_90D_pct": 21.86, "calibration_usable": true, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25-R7-L140-005", "classification": "counterexample", "company_name": "JLK", "current_profile_error_type": "approval_reimbursement_label_overcredit_hard_4c", "do_not_count_as_new_case": false, "entry_date": "2023-11-01", "entry_price": 25850, "evidence_family": "non_reimbursed_fee_status_without_adoption_profit_bridge", "evidence_url": "https://www.asiae.co.kr/en/article/2023103109514061131", "evidence_url_pending": false, "fine_archetype_id": "AI_STROKE_NON_REIMBURSED_FEE_WITH_WEAK_ADOPTION_REVENUE_BRIDGE", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "peak_180D_date": "2023-11-06", "peak_180D_high": 31500, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/322/322510/2023.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/322/322510.json", "row_type": "trigger", "same_entry_group_id": "C25-322510-2023-11-01-non_reimbursed_fee_status_without_adoption_profit_bridge", "source_proxy_only": false, "symbol": "322510", "trigger_date": "2023-10-31", "trigger_type": "Stage4C", "trough_180D_date": "2024-04-25", "trough_180D_low": 8990}
{"MAE_180D_pct": -38.12, "MAE_30D_pct": -2.87, "MAE_90D_pct": -2.87, "MFE_180D_pct": 34.45, "MFE_30D_pct": 26.0, "MFE_90D_pct": 34.45, "calibration_usable": true, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25-R7-L140-006", "classification": "counterexample", "company_name": "Ray", "current_profile_error_type": "proxy_tailwind_overcredit_local_4b", "do_not_count_as_new_case": false, "entry_date": "2023-03-29", "entry_price": 31350, "evidence_family": "broker_proxy_digital_dentistry_china_vbp_tailwind", "evidence_url": "https://securities.miraeasset.com/bbs/download/2104927.pdf?attachmentId=2104927", "evidence_url_pending": false, "fine_archetype_id": "DIGITAL_DENTISTRY_CHINA_VBP_PROXY_WITH_HIGH_MAE", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "peak_180D_date": "2023-06-15", "peak_180D_high": 42150, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/228/228670/2023.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/228/228670.json", "row_type": "trigger", "same_entry_group_id": "C25-228670-2023-03-29-broker_proxy_digital_dentistry_china_vbp_tailwind", "source_proxy_only": true, "symbol": "228670", "trigger_date": "2023-03-28", "trigger_type": "Stage4B", "trough_180D_date": "2023-10-27", "trough_180D_low": 19400}
{"MAE_180D_pct": -25.55, "MAE_30D_pct": -8.65, "MAE_90D_pct": -22.9, "MFE_180D_pct": 4.23, "MFE_30D_pct": 2.41, "MFE_90D_pct": 4.23, "calibration_usable": true, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25-R7-L140-007", "classification": "counterexample", "company_name": "Vatech", "current_profile_error_type": "backward_result_export_mix_overcredit_hard_4c", "do_not_count_as_new_case": false, "entry_date": "2024-08-09", "entry_price": 24850, "evidence_family": "official_quarterly_result_export_mix_but_forward_break", "evidence_url": "https://www.vatech.com/news/525049", "evidence_url_pending": false, "fine_archetype_id": "DENTAL_IMAGING_EXPORT_RESULT_WITH_WEAK_FORWARD_RERATING", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "peak_180D_date": "2024-10-29", "peak_180D_high": 25900, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/043/043150/2024.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/043/043150.json", "row_type": "trigger", "same_entry_group_id": "C25-043150-2024-08-09-official_quarterly_result_export_mix_but_forward_break", "source_proxy_only": false, "symbol": "043150", "trigger_date": "2024-08-08", "trigger_type": "Stage4C", "trough_180D_date": "2025-02-03", "trough_180D_low": 18500}
{"MAE_180D_pct": -15.69, "MAE_30D_pct": -1.85, "MAE_90D_pct": -2.55, "MFE_180D_pct": 17.13, "MFE_30D_pct": 15.51, "MFE_90D_pct": 17.13, "calibration_usable": true, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25-R7-L140-008", "classification": "positive", "company_name": "Vieworks", "current_profile_error_type": "positive_bridge_but_requires_export_detector_durability_confirmation", "do_not_count_as_new_case": false, "entry_date": "2025-02-12", "entry_price": 21600, "evidence_family": "official_annual_result_detector_export_margin_recovery", "evidence_url": "https://www.vieworks.com/kr/board/news_view/17473", "evidence_url_pending": false, "fine_archetype_id": "XRAY_DETECTOR_EXPORT_HIGH_VALUE_ADDED_MARGIN_RECOVERY", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "peak_180D_date": "2025-04-16", "peak_180D_high": 25300, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/100/100120/2025.csv", "price_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/100/100120.json", "row_type": "trigger", "same_entry_group_id": "C25-100120-2025-02-12-official_annual_result_detector_export_margin_recovery", "source_proxy_only": false, "symbol": "100120", "trigger_date": "2025-02-11", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2025-11-05", "trough_180D_low": 18210}
```

## 17. Machine-readable score simulation JSONL

```jsonl
{"canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25-R7-L140-001", "component_scores": {"bottleneck_pricing": 14, "capital_return": 2, "eps_fcf": 21, "info_confidence": 12, "mispricing": 9, "valuation_rerating": 10, "visibility": 27}, "production_scoring_changed": false, "row_type": "score_simulation", "shadow_weight_only": true, "stage_after": "Stage3-Green_candidate_with_margin_watch", "stage_before": "Stage3-Green"}
{"canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25-R7-L140-002", "component_scores": {"bottleneck_pricing": 13, "capital_return": 0, "eps_fcf": 10, "info_confidence": 13, "mispricing": 13, "valuation_rerating": 11, "visibility": 24}, "production_scoring_changed": false, "row_type": "score_simulation", "shadow_weight_only": true, "stage_after": "Stage3-Yellow_keep_not_green_until_hospital_revenue_profit_bridge", "stage_before": "Stage3-Yellow"}
{"canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25-R7-L140-003", "component_scores": {"bottleneck_pricing": 12, "capital_return": 1, "eps_fcf": 12, "info_confidence": 13, "mispricing": 11, "valuation_rerating": 10, "visibility": 23}, "production_scoring_changed": false, "row_type": "score_simulation", "shadow_weight_only": true, "stage_after": "Stage2-Actionable_with_sensor_revenue_confirmation_needed", "stage_before": "Stage2-Actionable"}
{"canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25-R7-L140-004", "component_scores": {"bottleneck_pricing": 13, "capital_return": 5, "eps_fcf": 22, "info_confidence": 12, "mispricing": 11, "valuation_rerating": 10, "visibility": 25}, "production_scoring_changed": false, "row_type": "score_simulation", "shadow_weight_only": true, "stage_after": "Stage3-Green_candidate_allowed_after_drawdown_confirmation", "stage_before": "Stage3-Green"}
{"canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25-R7-L140-005", "component_scores": {"bottleneck_pricing": 10, "capital_return": 0, "eps_fcf": 5, "info_confidence": 9, "mispricing": 16, "valuation_rerating": 14, "visibility": 11}, "production_scoring_changed": false, "row_type": "score_simulation", "shadow_weight_only": true, "stage_after": "Stage4C", "stage_before": "Stage4C"}
{"canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25-R7-L140-006", "component_scores": {"bottleneck_pricing": 13, "capital_return": 1, "eps_fcf": 12, "info_confidence": 6, "mispricing": 14, "valuation_rerating": 12, "visibility": 15}, "production_scoring_changed": false, "row_type": "score_simulation", "shadow_weight_only": true, "stage_after": "Stage4B_watch_not_green", "stage_before": "Stage4B"}
{"canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25-R7-L140-007", "component_scores": {"bottleneck_pricing": 10, "capital_return": 2, "eps_fcf": 14, "info_confidence": 12, "mispricing": 12, "valuation_rerating": 10, "visibility": 18}, "production_scoring_changed": false, "row_type": "score_simulation", "shadow_weight_only": true, "stage_after": "Stage4C", "stage_before": "Stage4C"}
{"canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25-R7-L140-008", "component_scores": {"bottleneck_pricing": 12, "capital_return": 3, "eps_fcf": 19, "info_confidence": 12, "mispricing": 10, "valuation_rerating": 8, "visibility": 23}, "production_scoring_changed": false, "row_type": "score_simulation", "shadow_weight_only": true, "stage_after": "Stage2-Actionable_with_yellow_confirmation_needed", "stage_before": "Stage2-Actionable"}
```

## 18. Batch Ingest Self-Audit

| audit field | value |
|---|---|
| standard_v12_filename | pass |
| filename_round_loop_matches_metadata | pass |
| round_sector_consistency | pass |
| selected_round | R7 |
| selected_loop | 140 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL |
| canonical_archetype_id | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT |
| canonical_trigger_labels_only | pass |
| trigger_rows_total | {len(cases)} |
| calibration_usable_trigger_count | {len(cases)} |
| rows_missing_required_mfe_mae | 0 |
| evidence_url_pending_count | 0 |
| source_proxy_only_count | {source_proxy} |
| new_independent_case_count | {len(cases)} |
| reused_case_count | 0 |
| same_archetype_new_symbol_count | {len(set(c['symbol'] for c in cases))} |
| same_archetype_new_trigger_family_count | {len(set(c['evidence_family'] for c in cases))} |
| positive_case_count | {positive} |
| counterexample_count | {counter} |
| stage4b_case_count | {stage4b} |
| stage4c_case_count | {stage4c} |
| current_profile_error_count | {current_profile_errors} |
| production_scoring_changed | false |
| shadow_weight_only | true |

## 19. Deferred Coding Agent Handoff Prompt

```text
Read this MD as a v12 C25 quality-repair research artifact only. Do not patch production scoring automatically.
Validate JSONL rows against the v12 parser gates:
- standard filename regex
- canonical trigger labels only
- complete MFE_30D_pct/MFE_90D_pct/MFE_180D_pct/MAE_30D_pct/MAE_90D_pct/MAE_180D_pct
- price_source = Songdaiki/stock-web
- price_basis = tradable_raw
- price_adjustment_status = raw_unadjusted_marcap
- no corporate-action contamination within D~D+180
If accepted, aggregate under C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT and evaluate the shadow axis C25_DEVICE_EXPORT_REIMBURSEMENT_REPEAT_USAGE_GATE.
Promotion should remain blocked unless holdout rows confirm that visibility/info-confidence weight increases reduce approval/reimbursement/event false positives without suppressing Dentium/VUNO/i-SENS/Classys/Vieworks-style positive bridges.
```

## 20. Next recommended archetypes

- C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
- C27_CONTENT_IP_GLOBAL_MONETIZATION
- C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
- C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE

## 21. Final state

```text
completed_round = R7
completed_loop = 140
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0/1 quality repair — C25 medical-device export/reimbursement bridge and 4C-thin repair
next_recommended_archetypes = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE; C27_CONTENT_IP_GLOBAL_MONETIZATION; C28_SOFTWARE_SECURITY_CONTRACT_RETENTION; C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
completed_state = true
```
