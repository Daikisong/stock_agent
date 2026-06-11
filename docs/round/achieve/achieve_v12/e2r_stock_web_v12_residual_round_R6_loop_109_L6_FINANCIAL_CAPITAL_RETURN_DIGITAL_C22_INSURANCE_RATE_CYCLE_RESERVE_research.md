# E2R Stock-Web v12 Residual Research — R6 / C22 Insurance Rate Cycle Reserve

```text
output_file = e2r_stock_web_v12_residual_round_R6_loop_109_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
schema_family = v12_sector_archetype_residual
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R6
selected_loop = 109
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = LIFE_AND_INSURANCE_HOLDCO_VALUEUP_CSM_KICS_CAPITAL_RETURN_BRIDGE_VS_LIFE_INSURANCE_VALUEUP_LABEL_FALSE_POSITIVE
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
```

## 1. Selection and no-repeat check

`C22_INSURANCE_RATE_CYCLE_RESERVE` remains under-covered in the No-Repeat Index: 6 representative rows / 6 unique symbols / need-to-30 = 24. Existing C22 representative symbols are `000540`, `000810`, `001450`, `003690`, `085620`, `138930`; this loop uses only new C22 symbols: `032830`, `088350`, `138040`.

Loop rule applied:

```text
selected_loop = max(existing loop for selected_round and selected_canonical_archetype_id) + 1
existing R6/C22 max loop = 108
selected_loop = 109
```

## 2. Research question

C22 should not treat every “insurance/value-up/rate-cycle” label as a rerating trigger. The bridge must resemble a real reserve/capital-return engine:

```text
CSM / reserve quality
+ K-ICS or capital buffer
+ recurring shareholder-return execution
+ rate / loss-ratio cycle that improves distributable earnings
= C22 Stage2-Actionable candidate
```

The counterfactual is equally important:

```text
life-insurance or insurance-value-up label
+ weak or unclear reserve/capital-return bridge
+ low MFE / high MAE
= Stage2 block or local 4B watch
```

## 3. Case table

| case_id | symbol | name | entry_date | entry_price | classification | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | verdict |
|---|---:|---|---:|---:|---|---:|---:|---:|---|
| C22_032830_2024-07-26 | 032830 | 삼성생명 | 2024-07-26 | 94,700 | positive_with_high_MAE_4B_watch | 7.71 / -13.20 | 17.21 / -13.20 | 17.21 / -22.60 | Stage2 possible, Green needs reserve/capital buffer confirmation |
| C22_138040_2024-08-16 | 138040 | 메리츠금융지주 | 2024-08-16 | 88,800 | positive_low_MAE | 12.50 / -1.46 | 20.72 / -1.46 | 43.47 / -1.46 | strong C22 bridge if capital-return execution remains visible |
| C22_088350_2024-07-11 | 088350 | 한화생명 | 2024-07-11 | 3,150 | counterexample_high_MAE | 2.86 / -14.29 | 2.86 / -14.29 | 2.86 / -24.76 | life-insurance label alone should be blocked |

## 4. Price-source validation

| symbol | profile | shard(s) | source | caveat |
|---:|---|---|---|---|
| 032830 | atlas/symbol_profiles/032/032830.json | 2024, 2025 | FinanceData/marcap via Songdaiki/stock-web | no corporate-action candidate in active profile window |
| 088350 | atlas/symbol_profiles/088/088350.json | 2024, 2025 | FinanceData/marcap via Songdaiki/stock-web | no corporate-action candidate in active profile window |
| 138040 | atlas/symbol_profiles/138/138040.json | 2024, 2025 | FinanceData/marcap via Songdaiki/stock-web | historical corporate-action candidates pre-2024; selected 2024/2025 window treated as usable |

## 5. Case notes

### 5.1 삼성생명 — positive, but full-window high-MAE watch

`032830` had a usable Stage2-style insurance/value-up trigger at 2024-07-26. Entry close was 94,700. The path reached 102,000 by 2024-09-03 and 111,000 by 2024-11-18, validating that the insurance value-up / CSM / capital-buffer bridge was not immediately false. However, the same path later reached a 2025-04-09 low of 73,300. This is not a clean Green case; it is a Stage2 candidate that needs a high-MAE/local-4B guard.

Interpretation:

```text
Correct: allow Stage2-Actionable when reserve quality + capital buffer + shareholder-return bridge exists.
Guard: do not promote to Green from label alone; high MAE requires 4B watch unless CSM/K-ICS/shareholder-return evidence is refreshed.
```

### 5.2 메리츠금융지주 — positive low-MAE insurance holdco bridge

`138040` is the cleanest positive in this loop. Entry close at 2024-08-16 was 88,800. The 30D low stayed near 87,500 while the path moved to 99,900 within the short window, 107,200 by the 90D window, and 127,400 by 2025-03-06. This is the archetypal case where insurance-holdco capital-return execution and balance-sheet confidence acted like a well-oiled gear train: the score and the price path turned in the same direction without violent drawdown.

Interpretation:

```text
C22 can reward insurance holdco cases when capital-return execution is explicit and reserve/capital quality does not break.
```

### 5.3 한화생명 — counterexample: life-insurance label without durable bridge

`088350` entered at 3,150 on 2024-07-11. It made only a 2.86% MFE at the 30D/90D/180D checkpoints and later fell to 2,370. This is the canonical false positive for “life insurer + value-up/rate-cycle label” without enough distributable earnings, reserve-quality, K-ICS, or shareholder-return execution bridge.

Interpretation:

```text
C22 should block life-insurance label-only Stage2.
If CSM/K-ICS/shareholder-return path is not visible, classify as Stage2-FalsePositive or local 4B watch.
```

## 6. Current calibrated profile stress test

| rule axis | observation | stress-test result |
|---|---|---|
| Stage2 required bridge | 138040 passes; 032830 partial pass; 088350 fails | strengthen |
| Reserve quality / capital buffer | missing bridge leads to low MFE / high MAE in 088350 | strengthen |
| Shareholder-return execution | durable returns require actual capital-return mechanism, not just insurance label | strengthen |
| 4B local vs full-window | 032830 shows upside then large drawdown; not a clean Green | strengthen local 4B watch |
| Price-only positive block | 088350 and 032830 high-MAE path show why label-only price move is insufficient | maintain |

## 7. Raw component score breakdown simulation

| component | 032830 | 138040 | 088350 |
|---|---:|---:|---:|
| CSM / reserve-quality bridge | 15 / 22 | 19 / 22 | 6 / 22 |
| K-ICS / capital buffer | 14 / 18 | 18 / 18 | 7 / 18 |
| capital-return execution | 13 / 24 | 23 / 24 | 5 / 24 |
| rate/loss-ratio or spread cycle | 10 / 14 | 13 / 14 | 7 / 14 |
| valuation/PBR rerating room | 8 / 12 | 9 / 12 | 7 / 12 |
| evidence freshness | 7 / 10 | 9 / 10 | 5 / 10 |
| high-MAE guard penalty | -8 | 0 | -18 |
| simulated_total | 59 | 91 | 19 |
| simulated_stage | Stage2-Actionable / 4B-watch | Stage3-Green candidate | Stage2-FalsePositive |

## 8. Trigger rows JSONL

```jsonl
{"MAE_180D_pct": -22.6, "MAE_30D_pct": -13.2, "MAE_90D_pct": -13.2, "MFE_180D_pct": 17.21, "MFE_30D_pct": 7.71, "MFE_90D_pct": 17.21, "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "case_id": "C22_032830_2024-07-26_Stage2-Actionable_life_insurance_valueup_csm_capital_bridge", "classification": "positive_with_high_MAE_4B_watch", "corporate_action_contaminated": false, "current_profile_verdict": "likely_stage2_actionable_but_needs_high_MAE_watch", "entry_date": "2024-07-26", "entry_price": 94700, "evidence_family": "life_insurance_CSM_KICS_capital_return_valueup", "fine_archetype_id": "LIFE_AND_INSURANCE_HOLDCO_VALUEUP_CSM_KICS_CAPITAL_RETURN_BRIDGE_VS_LIFE_INSURANCE_VALUEUP_LABEL_FALSE_POSITIVE", "forward_high_180D": 111000, "forward_high_30D": 102000, "forward_high_90D": 111000, "forward_low_180D": 73300, "forward_low_30D": 82200, "forward_low_90D": 82200, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "name": "삼성생명", "novelty_key": "032830|C22_INSURANCE_RATE_CYCLE_RESERVE|Stage2-Actionable|2024-07-26|2024-07-26|life_insurance_CSM_KICS_capital_return_valueup", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "score_return_alignment": "partial_positive: 90D upside confirms Stage2 but 180D drawdown warns against Green without reserve/capital buffer confirmation", "selected_loop": 109, "selected_round": "R6", "stock_web_price_shards": ["atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/032/032830/2025.csv"], "stock_web_symbol_profile": "atlas/symbol_profiles/032/032830.json", "symbol": "032830", "trigger_date": "2024-07-26", "trigger_family": "life_insurer_valueup_capital_return_execution_bridge", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -1.46, "MAE_30D_pct": -1.46, "MAE_90D_pct": -1.46, "MFE_180D_pct": 43.47, "MFE_30D_pct": 12.5, "MFE_90D_pct": 20.72, "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "case_id": "C22_138040_2024-08-16_Stage2-Actionable_insurance_holding_capital_return_bridge", "classification": "positive_low_MAE", "corporate_action_contaminated": false, "current_profile_verdict": "correct_positive_if_capital_return_execution_and_reserve_quality_are_present", "entry_date": "2024-08-16", "entry_price": 88800, "evidence_family": "insurance_holdco_capital_return_execution_KICS_buffer", "fine_archetype_id": "LIFE_AND_INSURANCE_HOLDCO_VALUEUP_CSM_KICS_CAPITAL_RETURN_BRIDGE_VS_LIFE_INSURANCE_VALUEUP_LABEL_FALSE_POSITIVE", "forward_high_180D": 127400, "forward_high_30D": 99900, "forward_high_90D": 107200, "forward_low_180D": 87500, "forward_low_30D": 87500, "forward_low_90D": 87500, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "name": "메리츠금융지주", "novelty_key": "138040|C22_INSURANCE_RATE_CYCLE_RESERVE|Stage2-Actionable|2024-08-16|2024-08-16|insurance_holdco_capital_return_execution_KICS_buffer", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "score_return_alignment": "positive: low MAE and durable 180D MFE support C22 bridge when capital return is explicit and balance-sheet buffer is visible", "selected_loop": 109, "selected_round": "R6", "stock_web_price_shards": ["atlas/ohlcv_tradable_by_symbol_year/138/138040/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/138/138040/2025.csv"], "stock_web_symbol_profile": "atlas/symbol_profiles/138/138040.json", "symbol": "138040", "trigger_date": "2024-08-16", "trigger_family": "capital_return_compounding_with_reserve_quality", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -24.76, "MAE_30D_pct": -14.29, "MAE_90D_pct": -14.29, "MFE_180D_pct": 2.86, "MFE_30D_pct": 2.86, "MFE_90D_pct": 2.86, "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "case_id": "C22_088350_2024-07-11_Stage2-FalsePositive_life_insurance_valueup_label_without_reserve_capital_return_bridge", "classification": "counterexample_high_MAE", "corporate_action_contaminated": false, "current_profile_verdict": "should_block_stage2_actionable_without_CSM_KICS_capital_return_bridge", "entry_date": "2024-07-11", "entry_price": 3150, "evidence_family": "life_insurance_valueup_label_without_reserve_quality_capital_return", "fine_archetype_id": "LIFE_AND_INSURANCE_HOLDCO_VALUEUP_CSM_KICS_CAPITAL_RETURN_BRIDGE_VS_LIFE_INSURANCE_VALUEUP_LABEL_FALSE_POSITIVE", "forward_high_180D": 3240, "forward_high_30D": 3240, "forward_high_90D": 3240, "forward_low_180D": 2370, "forward_low_30D": 2700, "forward_low_90D": 2700, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "name": "한화생명", "novelty_key": "088350|C22_INSURANCE_RATE_CYCLE_RESERVE|Stage2-FalsePositive|2024-07-11|2024-07-11|life_insurance_valueup_label_without_reserve_quality_capital_return", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "score_return_alignment": "negative: low MFE/high MAE shows that life-insurance label alone should not earn C22 Stage2-Actionable", "selected_loop": 109, "selected_round": "R6", "stock_web_price_shards": ["atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv", "atlas/ohlcv_tradable_by_symbol_year/088/088350/2025.csv"], "stock_web_symbol_profile": "atlas/symbol_profiles/088/088350.json", "symbol": "088350", "trigger_date": "2024-07-11", "trigger_family": "label_only_life_insurer_rate_cycle_false_positive", "trigger_type": "Stage2-FalsePositive"}
```

## 9. Residual contribution summary

```text
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
positive_case_count = 2
counterexample_count = 1
current_profile_error_count = 1
diversity_score_summary = new_C22_symbol=3, new_trigger_family=3, positive/counterexample=2/1, life-insurance-label false-positive guard=1, high-MAE 4B-watch=1
do_not_propose_new_weight_delta = false
sector_specific_rule_candidate = false
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = null
existing_axis_strengthened = C22_reserve_quality_KICS_capital_return_bridge_requirement; C22_life_insurance_valueup_label_stage2_block; C22_high_MAE_local_4B_watch
existing_axis_weakened = null
```

## 10. Shadow weight suggestion

No immediate production scoring change. Shadow-only adjustment candidate:

```json
{
  "profile": "e2r_2_2_shadow_only",
  "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE",
  "shadow_weight_delta": {
    "reserve_quality_CSM_KICS_bridge": 1.0,
    "capital_return_execution": 1.0,
    "life_insurance_label_without_bridge_penalty": -1.5,
    "high_MAE_local_4B_watch": 1.0
  },
  "promotion_decision": "hold_for_more_evidence",
  "reason": "C22 still has low row count. Three new cases support a bridge requirement, but more nonlife/life/reinsurance split is needed before production patch."
}
```

## 11. Deferred Coding Agent Handoff Prompt

Do not execute this during the research run.

```text
You are the coding agent for stock_agent. Read this MD as a historical calibration artifact only.
Do not treat it as live investment advice.
Parse the JSONL trigger rows, validate stock-web price fields, dedupe on:
symbol + canonical_archetype_id + trigger_type + trigger_date + entry_date + evidence_family.
If validation passes, append only as v12 calibration candidate rows.
Do not alter production scoring unless a separate promotion planner approves a patch.
Preferred planner treatment:
- strengthen C22 reserve_quality_KICS_capital_return_bridge_requirement
- strengthen C22_life_insurance_valueup_label_stage2_block
- strengthen C22_high_MAE_local_4B_watch
- keep this loop shadow-only until C22 reaches broader coverage.
```

## 12. Next recommended archetypes

```text
C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```
