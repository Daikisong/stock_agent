# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R12
selected_loop: 104
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: FORMAL_TENDER_MINORITY_CASH_EXIT_VS_CAPITAL_RETURN_POLICY_AND_VALUEUP_RECLASSIFICATION
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  uncached_symbol_shards: cache_miss_observed
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP` remains a Priority 0 archetype in the no-repeat index: 3 representative rows, still 27 rows short of the 30-row minimum. The v12 scheduler maps C32 to `R12 / L10_POLICY_EVENT_CROSS_REDTEAM_MISC`.

This run continues the local C32 sequence after `R12/C32 loop 103`; selected loop is therefore `104`.

This file focuses on a boundary that has appeared repeatedly in C21/C22/C31/R13 rows:

```text
formal tender / appraisal / squeeze-out / legally visible cash-exit price
≠
shareholder return / value-up / payout / buyback policy label
```

Both can involve cash. But C32 is the minority cash-exit / control-premium archetype. A dividend, payout promise or low-PBR Value-up thesis can be real, but if there is no tender, appraisal, squeeze-out, buyback at a defined minority exit price, or binding cash-exit mechanism, C32 should cap contribution and reclassify to C21/C22/C31.

Direct uncached stock-web symbol shards returned cache misses in this turn, so the trigger rows below reuse stock-web-derived rows already calculated in current-session C32/C21/C22/C31/R13 files. No production scoring is changed.

---

## 1. Research thesis

C32 is not `shareholder-friendly policy = tender premium`.

It is the minority cash-exit bridge:

```text
formal tender / control battle cash offer / buyback with defined exit mechanics / appraisal / squeeze-out
→ legally visible price and participation mechanics for minority holders
→ price path validation
→ post-resolution local 4B
```

The confusing boundary:

```text
capital return
low PBR
Value-up
shareholder return plan
bank/insurer payout
governance activism
```

These can be valuable, but they are not necessarily C32. They belong to C21, C22 or C31 unless minority holders have an executable cash-exit path.

This loop separates four routes:

1. **Formal tender / cash-exit positive-control**
   - Stage2 survives while tender or buyback cash mechanics are active.
   - Post-resolution local 4B is required.

2. **Control-sale / activism without minority cash exit**
   - Stage2 false positive or Watch.

3. **Capital-return policy bridge without tender mechanics**
   - Cap C32 contribution and reclassify to C21/C22/C31.

4. **Value-up / low-PBR label without execution**
   - Stage2 cap or false-positive block if MFE is weak and MAE expands.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 8
  actual_cases: 11
  source_archetypes:
    - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
    - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
    - C22_INSURANCE_RATE_CYCLE_RESERVE
    - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
    - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C32 canonical rule refinement
    - tender cash-exit vs capital-return policy split
    - wrong-archetype reclassification guard
    - post-resolution local 4B guard
    - no production scoring changes
```

---

## 3. Source validation

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  caveat: Raw/unadjusted OHLC; corporate-action-contaminated windows blocked by default.
```

Local stock-web-derived row provenance:

```yaml
reused_price_rows_from_current_session:
  - R12/C32 loop 102
  - R12/C32 loop 103
  - R6/C21 loop 112
  - R6/C22 loop 111
  - R11/C31 loop 103
  - R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C guardrail rows
reason:
  - all rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - current file changes canonical scope to C32 for financial/capital-return boundary rows
  - exact source-archetype keys should be deduped separately from this C32 canonical key
  - no production scoring changed
```

Symbol caveats:

```yaml
041510:
  name: 에스엠
  role: formal tender/control contest positive-control
  calibration_usable: true
  aggregate_credit_note: likely represented in C32 loop 102/103; use as positive-control if deduped

036560:
  name: KZ정밀
  role: control-battle affiliate tender positive-control
  calibration_usable: true
  aggregate_credit_note: likely represented in C32 loop 102/103; use as positive-control if deduped

040300:
  name: YTN
  role: control-sale headline without minority tender cash exit
  calibration_usable: true
  aggregate_credit_note: likely represented in C32 loop 102/103; use as hard control if deduped

028260:
  name: 삼성물산
  role: activism/NAV proposal without executed cash bridge
  calibration_usable: true
  aggregate_credit_note: likely represented in C32 loop 102/103; use as watch control if deduped

005940:
  name: NH투자증권
  role: capital-return positive in C21, but reclassify away from C32 tender mechanics
  calibration_usable: true

105560:
  name: KB금융
  role: bank Value-up/capital-return bridge with local 4B, not C32 cash-exit tender
  calibration_usable: true

005830:
  name: DB손해보험
  role: nonlife reserve/capital-return positive in C22/C31, not C32 tender mechanics
  calibration_usable: true

316140:
  name: 우리금융지주
  role: low-PBR bank Value-up label without tender/cash-exit mechanics
  calibration_usable: true

006800:
  name: 미래에셋증권
  role: low-PBR brokerage label false-positive; not C32
  calibration_usable: true

088350:
  name: 한화생명
  role: life-insurance Value-up label cap; not C32
  calibration_usable: true

244920:
  name: 에이플러스에셋
  role: GA distribution commission bridge; wrong archetype for C22 and not C32 tender
  calibration_usable: true
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R12","loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"FORMAL_TENDER_CASH_EXIT_POSITIVE_POST_RESOLUTION_4B","source_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"041510","name":"에스엠","trigger_type":"Stage2-Actionable","entry_date":"2023-02-10","entry_close":114700,"price_basis":"tradable_raw","mfe_30d_pct":40.54,"mae_30d_pct":-6.45,"mfe_90d_pct":40.54,"mae_90d_pct":-21.10,"mfe_180d_pct":40.54,"mae_180d_pct":-21.10,"forward_high_30d":161200,"forward_low_30d":107300,"forward_high_90d":161200,"forward_low_90d":90500,"forward_high_180d":161200,"forward_low_180d":90500,"calibration_usable":true,"case_role":"reused_tender_positive_control","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|041510|Stage2-Actionable|2023-02-10","non_price_bridge":"formal tender/control contest cash path with visible minority exit mechanics","score_alignment":"keep Stage2 during tender mechanics; post-resolution local 4B watch required","aggregate_credit_note":"exact key likely already represented; use as positive-control if deduped"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R12","loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_BATTLE_AFFILIATE_TENDER_CASH_PATH_POSITIVE_CONTROL","source_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"036560","name":"KZ정밀","trigger_type":"Stage2-Actionable","entry_date":"2024-09-13","entry_close":12180,"price_basis":"tradable_raw","mfe_30d_pct":201.31,"mae_30d_pct":0.00,"mfe_90d_pct":201.31,"mae_90d_pct":0.00,"mfe_180d_pct":201.31,"mae_180d_pct":-11.25,"forward_high_30d":36700,"forward_low_30d":12180,"forward_high_90d":36700,"forward_low_90d":12180,"forward_high_180d":36700,"forward_low_180d":10810,"calibration_usable":true,"case_role":"reused_tender_positive_control","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|036560|Stage2-Actionable|2024-09-13","non_price_bridge":"control-battle affiliate tender cash-exit mechanics with legal price anchor","score_alignment":"Stage2 valid during tender mechanics; post-offer normalization watch required","aggregate_credit_note":"exact key likely already represented; use as positive-control if deduped"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R12","loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_SALE_WITHOUT_MINORITY_TENDER_HARD_BLOCK","source_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"040300","name":"YTN","trigger_type":"Stage2-FalsePositive","entry_date":"2023-10-24","entry_close":7800,"price_basis":"tradable_raw","mfe_30d_pct":23.08,"mae_30d_pct":-30.64,"mfe_90d_pct":23.08,"mae_90d_pct":-30.64,"mfe_180d_pct":23.08,"mae_180d_pct":-49.29,"forward_high_30d":9600,"forward_low_30d":5410,"forward_high_90d":9600,"forward_low_90d":5410,"forward_high_180d":9600,"forward_low_180d":3955,"calibration_usable":true,"case_role":"reused_hard_counterexample","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|040300|Stage2-FalsePositive|2023-10-24","non_price_bridge":"control-sale headline without public minority tender/appraisal/squeeze-out cash path","score_alignment":"block Stage2-Actionable; control sale is not minority cash exit","aggregate_credit_note":"exact key likely already represented; use as hard counterexample if deduped"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R12","loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"ACTIVISM_NAV_PROPOSAL_WITHOUT_EXECUTED_CASH_EXIT_STAGE2_WATCH","source_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"028260","name":"삼성물산","trigger_type":"Stage2-Watch","entry_date":"2024-03-15","entry_close":154100,"price_basis":"tradable_raw","mfe_30d_pct":7.98,"mae_30d_pct":-10.32,"mfe_90d_pct":7.98,"mae_90d_pct":-14.02,"mfe_180d_pct":7.98,"mae_180d_pct":-15.96,"forward_high_30d":166400,"forward_low_30d":138200,"forward_high_90d":166400,"forward_low_90d":132500,"forward_high_180d":166400,"forward_low_180d":129500,"calibration_usable":true,"case_role":"reused_watch_control","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|028260|Stage2-Watch|2024-03-15","non_price_bridge":"NAV-discount activism proposal without passed vote, tender, appraisal, buyback/cancellation or cash-exit mechanics","score_alignment":"Watch only; require executed minority cash mechanics before C32 Actionable","aggregate_credit_note":"exact key likely already represented; use as activism watch control if deduped"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R12","loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"SECURITIES_CAPITAL_RETURN_POSITIVE_BUT_NOT_TENDER_RECLASSIFY","source_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"005940","name":"NH투자증권","trigger_type":"Stage2-Watch","entry_date":"2024-02-26","entry_close":11420,"price_basis":"tradable_raw","mfe_30d_pct":14.71,"mae_30d_pct":-2.36,"mfe_90d_pct":14.71,"mae_90d_pct":-2.36,"mfe_180d_pct":26.09,"mae_180d_pct":-2.36,"forward_high_30d":13100,"forward_low_30d":11150,"forward_high_90d":13100,"forward_low_90d":11150,"forward_high_180d":14400,"forward_low_180d":11150,"calibration_usable":true,"case_role":"new_reclassification_positive_elsewhere","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|005940|Stage2-Watch|2024-02-26","non_price_bridge":"securities ROE/capital-return bridge is positive in C21, but has no C32 tender/appraisal/control-premium cash-exit mechanics","score_alignment":"cap C32 contribution; reclassify to C21 rather than C32"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R12","loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"BANK_VALUEUP_CAPITAL_RETURN_LOCAL_4B_NOT_C32_TENDER","source_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"105560","name":"KB금융","trigger_type":"Stage2-Watch","entry_date":"2024-07-26","entry_close":87900,"price_basis":"tradable_raw","mfe_30d_pct":5.12,"mae_30d_pct":-15.81,"mfe_90d_pct":18.20,"mae_90d_pct":-15.81,"mfe_180d_pct":18.20,"mae_180d_pct":-15.81,"forward_high_30d":92400,"forward_low_30d":74000,"forward_high_90d":103900,"forward_low_90d":74000,"forward_high_180d":103900,"forward_low_180d":74000,"calibration_usable":true,"case_role":"new_reclassification_local_4B","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|105560|Stage2-Watch|2024-07-26","non_price_bridge":"bank Value-up/capital-return bridge may be real, but it is not a minority tender/control-premium cash-exit event","score_alignment":"cap C32 contribution; reclassify to C21/C31 and require capital/payout refresh there"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R12","loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"NONLIFE_CAPITAL_RETURN_POSITIVE_BUT_NOT_C32_TENDER_RECLASSIFY","source_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"005830","name":"DB손해보험","trigger_type":"Stage2-Watch","entry_date":"2024-02-26","entry_close":95000,"price_basis":"tradable_raw","mfe_30d_pct":15.79,"mae_30d_pct":-4.11,"mfe_90d_pct":27.05,"mae_90d_pct":-9.26,"mfe_180d_pct":30.53,"mae_180d_pct":-9.26,"forward_high_30d":110000,"forward_low_30d":91100,"forward_high_90d":120700,"forward_low_90d":86200,"forward_high_180d":124000,"forward_low_180d":86200,"calibration_usable":true,"case_role":"new_reclassification_positive_elsewhere","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|005830|Stage2-Watch|2024-02-26","non_price_bridge":"nonlife reserve/capital-return bridge is positive in C22/C31, but lacks formal tender, appraisal or control-premium minority exit mechanics","score_alignment":"cap C32 contribution; reclassify to C22/C31"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R12","loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"LOW_PBR_BANK_VALUEUP_LABEL_WITHOUT_TENDER_CAP","source_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"316140","name":"우리금융지주","trigger_type":"Stage2-Watch","entry_date":"2024-07-26","entry_close":16180,"price_basis":"tradable_raw","mfe_30d_pct":4.08,"mae_30d_pct":-15.08,"mfe_90d_pct":5.69,"mae_90d_pct":-15.08,"mfe_180d_pct":5.69,"mae_180d_pct":-15.08,"forward_high_30d":16840,"forward_low_30d":13740,"forward_high_90d":17100,"forward_low_90d":13740,"forward_high_180d":17100,"forward_low_180d":13740,"calibration_usable":true,"case_role":"new_label_cap","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|316140|Stage2-Watch|2024-07-26","non_price_bridge":"low-PBR bank Value-up label without C32 cash-exit mechanics and without differentiated minority tender price","score_alignment":"cap C32 bonus; if valid at all, it belongs to C21/C31 after capital-return execution"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R12","loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"LOW_PBR_BROKERAGE_LABEL_WITHOUT_TENDER_OR_CAPITAL_RETURN_EXECUTION_BLOCK","source_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"006800","name":"미래에셋증권","trigger_type":"Stage2-FalsePositive","entry_date":"2024-02-26","entry_close":8680,"price_basis":"tradable_raw","mfe_30d_pct":5.53,"mae_30d_pct":-10.71,"mfe_90d_pct":5.53,"mae_90d_pct":-20.16,"mfe_180d_pct":5.53,"mae_180d_pct":-23.96,"forward_high_30d":9160,"forward_low_30d":7750,"forward_high_90d":9160,"forward_low_90d":6930,"forward_high_180d":9160,"forward_low_180d":6600,"calibration_usable":true,"case_role":"new_wrong_archetype_hard_counterexample","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|006800|Stage2-FalsePositive|2024-02-26","non_price_bridge":"low-PBR brokerage label lacked both capital-return execution and any C32 tender/control-premium cash-exit mechanics","score_alignment":"hard block C32; do not treat cheapness or value-up label as tender premium"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R12","loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"LIFE_INSURANCE_VALUEUP_LABEL_WITHOUT_C32_TENDER_CAP","source_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"088350","name":"한화생명","trigger_type":"Stage2-Watch","entry_date":"2024-02-26","entry_close":3060,"price_basis":"tradable_raw","mfe_30d_pct":9.31,"mae_30d_pct":-8.17,"mfe_90d_pct":9.31,"mae_90d_pct":-15.69,"mfe_180d_pct":9.31,"mae_180d_pct":-15.69,"forward_high_30d":3345,"forward_low_30d":2810,"forward_high_90d":3345,"forward_low_90d":2580,"forward_high_180d":3345,"forward_low_180d":2580,"calibration_usable":true,"case_role":"new_label_cap","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|088350|Stage2-Watch|2024-02-26","non_price_bridge":"life-insurance Value-up label without CSM/solvency bridge and without C32 minority cash-exit mechanics","score_alignment":"cap C32; reclassify only if C22/C31 bridge appears"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R12","loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"GA_DISTRIBUTION_COMMISSION_WRONG_ARCHETYPE_NOT_C32_TENDER","source_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"244920","name":"에이플러스에셋","trigger_type":"Stage2-Watch","entry_date":"2024-05-10","entry_close":4100,"price_basis":"tradable_raw","mfe_30d_pct":9.76,"mae_30d_pct":-2.32,"mfe_90d_pct":9.76,"mae_90d_pct":-13.78,"mfe_180d_pct":14.63,"mae_180d_pct":-13.78,"forward_high_30d":4500,"forward_low_30d":4005,"forward_high_90d":4500,"forward_low_90d":3535,"forward_high_180d":4700,"forward_low_180d":3535,"calibration_usable":true,"case_role":"new_wrong_archetype_reclassification","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|244920|Stage2-Watch|2024-05-10","non_price_bridge":"GA distribution commission bridge may exist, but it is neither insurance reserve-cycle nor C32 tender cash-exit mechanics","score_alignment":"cap C32 contribution and reclassify to distribution commission axis"}
```

---

## 5. Case analysis

### 5.1 SM Entertainment / 041510 — tender positive-control

SM remains the clean formal-tender control. Stage2 survives during the cash-exit window, but post-resolution drawdown proves the need for 4B.

```yaml
entry_close: 114700
90D_MFE_MAE: +40.54 / -21.10
180D_MFE_MAE: +40.54 / -21.10
route: KeepStage2 during tender, post-resolution 4B
```

### 5.2 KZ Precision / 036560 — tender affiliate positive-control

KZ Precision validates tender mechanics and cash price anchoring.

```yaml
entry_close: 12180
90D_MFE_MAE: +201.31 / 0.00
180D_MFE_MAE: +201.31 / -11.25
route: KeepStage2 during offer, post-offer 4B
```

### 5.3 YTN / 040300 — control sale without minority cash exit

Control-sale vocabulary is not public minority cash exit.

```yaml
entry_close: 7800
90D_MFE_MAE: +23.08 / -30.64
180D_MFE_MAE: +23.08 / -49.29
route: Stage2-FalsePositive
```

### 5.4 Samsung C&T / 028260 — activism proposal without execution

Activism/NAV discount is not C32 until execution creates a cash path.

```yaml
entry_close: 154100
90D_MFE_MAE: +7.98 / -14.02
180D_MFE_MAE: +7.98 / -15.96
route: Stage2-Watch
```

### 5.5 NH Investment & Securities / 005940 — capital return positive, but not C32

This is a positive C21 row, not a C32 row. It proves the reclassification rule.

```yaml
entry_close: 11420
90D_MFE_MAE: +14.71 / -2.36
180D_MFE_MAE: +26.09 / -2.36
route: Reclassify to C21
```

### 5.6 KB Financial / 105560 — bank capital return, not tender

KB can have a valid capital-return bridge, but C32 should not claim it.

```yaml
entry_close: 87900
90D_MFE_MAE: +18.20 / -15.81
180D_MFE_MAE: +18.20 / -15.81
route: Reclassify to C21/C31, C32 cap
```

### 5.7 DB Insurance / 005830 — insurance capital return, not tender

DB Insurance is positive elsewhere but not C32.

```yaml
entry_close: 95000
90D_MFE_MAE: +27.05 / -9.26
180D_MFE_MAE: +30.53 / -9.26
route: Reclassify to C22/C31
```

### 5.8 Woori Financial / 316140 — low-PBR label cap

Low-PBR/Value-up label has no formal cash-exit mechanics.

```yaml
entry_close: 16180
90D_MFE_MAE: +5.69 / -15.08
180D_MFE_MAE: +5.69 / -15.08
route: C32 cap
```

### 5.9 Mirae Asset Securities / 006800 — cheapness is not tender premium

Mirae is a hard wrong-archetype counterexample.

```yaml
entry_close: 8680
90D_MFE_MAE: +5.53 / -20.16
180D_MFE_MAE: +5.53 / -23.96
route: Stage2-FalsePositive
```

### 5.10 Hanwha Life / 088350 — life Value-up label cap

No tender/appraisal/squeeze-out mechanics.

```yaml
entry_close: 3060
90D_MFE_MAE: +9.31 / -15.69
180D_MFE_MAE: +9.31 / -15.69
route: C32 cap
```

### 5.11 A Plus Asset / 244920 — wrong archetype reclassification

Commission distribution bridge is not C32.

```yaml
entry_close: 4100
90D_MFE_MAE: +9.76 / -13.78
180D_MFE_MAE: +14.63 / -13.78
route: Reclassify
```

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 7
reused_control_case_count: 4
calibration_usable_case_count: 11
calibration_usable_trigger_count: 11
positive_C32_tender_case_count: 2
counterexample_or_cap_count: 9
wrong_archetype_reclassification_count: 7
post_resolution_or_watch_count: 4
current_profile_error_count: 7
```

| symbol | role | 90D MFE/MAE | 180D MFE/MAE | C32 lesson |
|---|---:|---:|---:|---|
| 041510 | tender positive | +40.54 / -21.10 | +40.54 / -21.10 | formal cash-exit validates, then 4B |
| 036560 | tender positive | +201.31 / 0.00 | +201.31 / -11.25 | tender anchor validates |
| 040300 | hard counterexample | +23.08 / -30.64 | +23.08 / -49.29 | control sale without minority cash exit fails |
| 028260 | activism watch | +7.98 / -14.02 | +7.98 / -15.96 | proposal needs execution |
| 005940 | reclassify positive elsewhere | +14.71 / -2.36 | +26.09 / -2.36 | capital return is C21, not C32 |
| 105560 | reclassify local 4B | +18.20 / -15.81 | +18.20 / -15.81 | bank payout bridge is not tender |
| 005830 | reclassify positive elsewhere | +27.05 / -9.26 | +30.53 / -9.26 | insurance capital return is not tender |
| 316140 | label cap | +5.69 / -15.08 | +5.69 / -15.08 | low-PBR label lacks cash-exit mechanics |
| 006800 | hard block | +5.53 / -20.16 | +5.53 / -23.96 | cheapness is not tender premium |
| 088350 | label cap | +9.31 / -15.69 | +9.31 / -15.69 | life Value-up label lacks C32 mechanics |
| 244920 | reclassify | +9.76 / -13.78 | +14.63 / -13.78 | GA commission bridge belongs elsewhere |

---

## 7. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"041510","raw_tender_cash_exit":5,"raw_legal_visibility":5,"raw_execution_status":4,"raw_minority_participation":5,"raw_wrong_archetype_risk":0,"raw_validation":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"TenderPositive_PostResolution4B"}
{"row_type":"score_simulation","symbol":"036560","raw_tender_cash_exit":5,"raw_legal_visibility":5,"raw_execution_status":4,"raw_minority_participation":5,"raw_wrong_archetype_risk":0,"raw_validation":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"TenderPositive_PostOffer4B"}
{"row_type":"score_simulation","symbol":"040300","raw_tender_cash_exit":0,"raw_legal_visibility":1,"raw_execution_status":1,"raw_minority_participation":0,"raw_wrong_archetype_risk":1,"raw_validation":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"ControlSaleNoTenderBlock"}
{"row_type":"score_simulation","symbol":"028260","raw_tender_cash_exit":0,"raw_legal_visibility":2,"raw_execution_status":0,"raw_minority_participation":1,"raw_wrong_archetype_risk":2,"raw_validation":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"ActivismWatch"}
{"row_type":"score_simulation","symbol":"005940","raw_tender_cash_exit":0,"raw_legal_visibility":1,"raw_execution_status":3,"raw_minority_participation":1,"raw_wrong_archetype_risk":5,"raw_validation":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"ReclassifyC21"}
{"row_type":"score_simulation","symbol":"105560","raw_tender_cash_exit":0,"raw_legal_visibility":1,"raw_execution_status":3,"raw_minority_participation":1,"raw_wrong_archetype_risk":5,"raw_validation":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"ReclassifyC21C31"}
{"row_type":"score_simulation","symbol":"005830","raw_tender_cash_exit":0,"raw_legal_visibility":1,"raw_execution_status":3,"raw_minority_participation":1,"raw_wrong_archetype_risk":5,"raw_validation":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"ReclassifyC22C31"}
{"row_type":"score_simulation","symbol":"316140","raw_tender_cash_exit":0,"raw_legal_visibility":1,"raw_execution_status":1,"raw_minority_participation":1,"raw_wrong_archetype_risk":5,"raw_validation":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"C32Cap_ValueupLabel"}
{"row_type":"score_simulation","symbol":"006800","raw_tender_cash_exit":0,"raw_legal_visibility":0,"raw_execution_status":0,"raw_minority_participation":0,"raw_wrong_archetype_risk":5,"raw_validation":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"HardBlock_LowPBRNoTender"}
{"row_type":"score_simulation","symbol":"088350","raw_tender_cash_exit":0,"raw_legal_visibility":1,"raw_execution_status":1,"raw_minority_participation":1,"raw_wrong_archetype_risk":5,"raw_validation":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"C32Cap_LifeValueup"}
{"row_type":"score_simulation","symbol":"244920","raw_tender_cash_exit":0,"raw_legal_visibility":0,"raw_execution_status":1,"raw_minority_participation":0,"raw_wrong_archetype_risk":5,"raw_validation":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"ReclassifyDistributionCommission"}
```

---

## 8. Current calibrated profile stress test

### Existing error risk

C32 can still over-credit any event that looks shareholder-friendly:

```text
capital return
low PBR
Value-up
governance activism
payout policy
buyback language
```

The correct C32 question is narrower:

```text
Can minority holders exit at a legally visible price through tender/appraisal/squeeze-out/binding cash-exit mechanics?
```

A dividend is cash rain. A tender is a checkout counter. C32 is the checkout counter.

### Rule candidate

```text
C32_FORMAL_TENDER_MINORITY_CASH_EXIT_REQUIREMENT_V104

if C32
and governance_control_premium_or_shareholder_friendly_label == true
and formal_tender_appraisal_squeezeout_binding_cash_exit_or_defined_minority_exit_price == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C32
and formal_tender_or_cash_exit_path == true
and legally_visible_price_or_mechanics == true:
    keep_stage2_actionable_bonus = true
    if offer_resolution_expiry_or_cash_path_fade == true:
        local_4B_watch = true
```

```text
if C32
and capital_return_or_valueup_bridge == true
and tender_or_control_cash_exit_mechanics == false:
    cap_C32_contribution = true
    require_reclassification_to_C21_C22_or_C31 = true
```

```text
if C32
and control_sale_headline == true
and minority_cash_exit_path == false
and MAE_90D_pct <= -20:
    route = Stage2_FalsePositive_Block
```

```text
if C32
and low_PBR_or_shareholder_return_label == true
and MFE_90D_pct < +10
and tender_cash_exit_path == false:
    route = Stage2Cap_or_FalsePositiveBlock
```

---

## 9. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C32_FORMAL_TENDER_MINORITY_CASH_EXIT_REQUIREMENT_V104
existing_axis_strengthened:
  - C32_formal_tender_cash_exit_positive_escape_hatch
  - C32_post_resolution_local_4B_watch
  - C32_control_sale_without_minority_cash_exit_block
  - C32_capital_return_policy_reclassification_guard
  - C32_low_PBR_valueup_label_not_tender_premium
existing_axis_weakened: null
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Batch this C32 loop with C32 loops 102~103, C21 loop 112, C22 loop 111, C31 loop 103 and adjacent R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C files. Extract `C32_FORMAL_TENDER_MINORITY_CASH_EXIT_REQUIREMENT_V104` as a shadow-rule candidate. Preserve formal tender/appraisal/squeeze-out/minority cash-exit positives and post-resolution local 4B, while reclassifying capital-return, Value-up, bank/insurance payout and GA commission cases away from C32 unless an executable minority cash-exit price exists.
```

---

## 11. Next research state

```yaml
completed_round: R12
completed_loop: 104
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
  - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```
