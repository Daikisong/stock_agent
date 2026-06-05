---
research_artifact_type: e2r_stock_web_v12_residual_research
scheduled_round: R10
scheduled_loop: 89
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: C30_PF_POLICY_LIQUIDITY_TO_COMPANY_SPECIFIC_BS_REPAIR_AND_ORDER_MARGIN_BRIDGE
round_schedule_status: valid
round_sector_consistency: pass
current_default_profile_proxy: e2r_2_1_stock_web_calibrated
previous_baseline_reference: e2r_2_0_baseline
price_atlas_repo: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
manifest_max_date: 2026-02-20
research_pack_default_price_basis: tradable_raw
new_independent_case_count: 3
same_archetype_new_symbol_count: 3
positive_case_count: 1
counterexample_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3
loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true
completed_round: R10
completed_loop: 89
next_round: R11
next_loop: 89
---

# E2R v12 residual research — R10/L9/C30

## 0. Scheduler validation

This run continues the sequential cycle after `R9 / loop 89`, so the scheduled slot is:

```text
scheduled_round = R10
scheduled_loop  = 89
required_large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
```

The selected archetype is:

```text
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id      = C30_PF_POLICY_LIQUIDITY_TO_COMPANY_SPECIFIC_BS_REPAIR_AND_ORDER_MARGIN_BRIDGE
```

R10 is the construction / real-estate / housing slot, so the `large_sector_id` is valid.

## 1. No-Repeat check

The current No-Repeat summary marks C30 as already broad and counterexample-heavy:

```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
rows/symbols: 81 / 31
date range: 2022-01-12 ~ 2024-08-26
positive/counterexample: 16 / 29
4B / 4C: 3 / 4
top repeated symbols: 002990, 294870, 375500, 004960, 013580, 006360
```

Recent local R10 samples already used:

```text
loop87: 034300, 005960, 010780
loop88: 047040, 012630, 021320
```

This run avoids those and uses:

```text
000720 현대건설
003070 코오롱글로벌
002780 진흥기업
```

All three are same-archetype new-symbol expansions for this local C30 pass. The row keys differ by `symbol + trigger_type + entry_date`, so none are hard duplicates.

## 2. Research question

C30 is not simply a “construction stocks rally” bucket. It is a balance-sheet and refinancing bucket.

The residual error to test:

```text
Does the calibrated profile still over-upgrade a construction/PF policy-liquidity headline
before company-level balance-sheet repair, refinancing, cash collection,
margin recovery, or order/backlog conversion is visible?
```

The policy backdrop matters, but it is sector beta. A policy support headline is like opening a fire door in a smoky building: it improves survival odds for everyone in the corridor, but the companies still need oxygen masks, working stairwells, and a clear exit route. In C30 language, that means refinancing, PF exposure reduction, cash collection, margin repair, or order-to-earnings conversion.

External backdrop used as narrative-only context:

```text
- 2024-03-27: Korea prepared financial support for builders and small businesses.
- 2024-05-13: Korean authorities tightened PF project assessments and accelerated restructuring.
```

These are sector-level liquidity / restructuring signals, not automatically company-specific Stage2 evidence.

## 3. Stock-web source check

Stock-web manifest basis:

```text
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14,354,401
symbol_count: 5,414
active_like_symbol_count: 2,868
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
```

Per-profile contamination checks:

```text
000720 현대건설
- available_years include 2024, 2025, 2026
- row_status_counts.tradable_ohlcv = 7,740
- corporate_action_candidate_dates = 1998-05-23, 1998-11-19, 1999-03-05, 2001-07-06, 2001-07-12, 2004-01-13, 2004-04-07
- entry windows in 2025 are not corporate-action contaminated

003070 코오롱글로벌
- available_years include 2024, 2025, 2026
- row_status_counts.tradable_ohlcv = 7,724
- corporate_action_candidate_dates include 2023-01-31 and 2025-12-11
- selected 2024-06-26 entry window has no D+180 contamination

002780 진흥기업
- available_years include 2024, 2025, 2026
- row_status_counts.tradable_ohlcv = 7,618
- corporate_action_candidate_dates are old and stop at 2015-01-28
- selected 2024-06-26 entry window has no D+180 contamination
```

## 4. Case table

| case_id | symbol | name | trigger_type | trigger_date | entry_date | entry_price | path label | calibration usable |
|---|---:|---|---|---:|---:|---:|---|---|
| C30_R10L89_000720 | 000720 | 현대건설 | company_specific_order_margin_repair_after_policy_liquidity | 2025-01-22 | 2025-01-22 | 28,450 | positive_with_local_4B_overlay | true |
| C30_R10L89_003070 | 003070 | 코오롱글로벌 | pf_liquidity_policy_price_spike_without_bs_repair_bridge | 2024-06-26 | 2024-06-26 | 13,630 | high_mae_counterexample | true |
| C30_R10L89_002780 | 002780 | 진흥기업 | small_builder_policy_beta_without_balance_sheet_conversion | 2024-06-26 | 2024-06-26 | 884 | stage2_false_positive_candidate | true |

## 5. Individual case notes

### 5.1 000720 현대건설 — positive, but not because of generic PF policy alone

**Observed path**

```text
entry_date: 2025-01-22
entry_price: 28,450

local path:
- 2025-01-22: close 28,450
- 2025-02-18: high 37,550
- 2025-07-01: high 83,900
- 2025-08-20: low 54,350 after the peak
```

Approximate return geometry:

```text
MFE to 2025-02-18 high: +32.0%
MFE to 2025-07-01 high: +194.9%
post-peak drawdown from 83,900 to 54,350: -35.2%
```

Interpretation:

```text
This is a positive control for C30 only after company-specific bridge appears.
It should not be counted as a generic PF policy positive.
The correct reading is:
policy-liquidity backdrop + company-specific order/margin/earnings visibility = Stage2-Actionable / Stage3 candidate.
policy-liquidity backdrop alone = Watch.
```

Residual lesson:

```text
C30 should allow upgrade only when construction-sector liquidity is coupled
with company-specific conversion evidence.
Otherwise the same policy headline would have falsely upgraded many weaker builders.
```

### 5.2 003070 코오롱글로벌 — policy-liquidity spike with high MAE

**Observed path**

```text
entry_date: 2024-06-26
entry_price: 13,630

forward path:
- 2024-06-27: high 15,200
- 2024-07-01: close 12,620
- 2024-08-05: low 8,500
- 2024-09-06: close 9,500
```

Approximate return geometry:

```text
MFE to 2024-06-27 high: +11.5%
MAE to 2024-08-05 low: -37.6%
drawdown from local high 15,200 to 8,500: -44.1%
```

Interpretation:

```text
This is the archetypal C30 false-positive shape:
short squeeze / policy-liquidity / PF support beta appears,
but without company-specific balance-sheet repair or cash conversion,
the price path fails the Stage2-Actionable durability test.
```

Stage comparison:

```text
e2r_2_0_baseline:
- likely over-credits policy-liquidity and construction beta
- could mark Stage2-Actionable too early

e2r_2_1_stock_web_calibrated:
- price-only blowoff guard helps
- but still needs a C30-specific high-MAE guard when the trigger family is PF-liquidity only

recommended interpretation:
- Watch or Stage2-FalsePositive-Candidate
- not Stage3-Yellow
- not Green
```

### 5.3 002780 진흥기업 — small-builder beta without conversion

**Observed path**

```text
entry_date: 2024-06-26
entry_price: 884

forward path:
- 2024-06-26: intraday high 1,009
- 2024-07-12: high 977
- 2024-08-05: low 797
- 2024-10-18: close 805
```

Approximate return geometry:

```text
MFE using same-day high: +14.1%
MFE using post-entry high 2024-07-12: +10.5%
MAE to 2024-08-05 low: -9.8%
later fade to 2024-10-18 close: -8.9%
```

Interpretation:

```text
This is not a collapse like 003070, but it is still not an E2R positive.
The signal is a sector-policy beta pulse, not an evidence bridge.
Because the MFE is shallow and the path then fades, the correct route is:
Watch / FalsePositive-Candidate, not Stage2-Actionable.
```

Residual lesson:

```text
For smaller construction names, the model must not confuse
policy liquidity plus volume spike with balance-sheet repair.
A clean C30 upgrade needs at least one of:
- refinancing/refunding completed
- PF guarantee exposure reduced
- impaired site exposure ring-fenced or sold
- cash collection visible
- margin or order conversion visible
```

## 6. Aggregate interpretation

```text
positive_case_count = 1
counterexample_count = 2
local_4b_overlay_case_count = 1
hard_4c_candidate_count = 1
```

The residual is not “C30 weight too low” or “C30 weight too high” globally.

The residual is a routing problem:

```text
generic PF policy / liquidity / restructuring headline
    -> Watch / Stage2-FalsePositive-Candidate

generic PF policy + price spike only
    -> local 4B watch or 4C guard if high MAE appears

company-specific balance-sheet repair / refinancing / cash collection / margin-order bridge
    -> Stage2-Actionable

company-specific bridge + repeated earnings/cash conversion
    -> Stage3-Yellow or Green review
```

## 7. Shadow rule candidate

```yaml
shadow_rule_candidate:
  id: C30_COMPANY_SPECIFIC_BS_REPAIR_BRIDGE_REQUIRED
  scope:
    large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
    canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  condition:
    all:
      - trigger_family in [
          pf_policy_liquidity_support,
          pf_restructuring_guideline,
          construction_sector_relief,
          real_estate_policy_beta,
          price_volume_spike_only
        ]
      - no_company_specific_evidence in [
          refinancing_completed,
          pf_exposure_reduction,
          cash_collection_visible,
          impaired_project_ringfence,
          margin_repair_visible,
          order_backlog_to_earnings_conversion
        ]
  action:
    max_stage: Watch
    block_green: true
    block_stage3_yellow_unless_company_specific_bridge: true
    add_local_4b_watch_if_mfe_gt_20pct_without_bridge: true
    add_4c_candidate_if_mae_lt_minus_30pct_with_no_bridge: true
  rationale:
    - C30 is a balance-sheet conversion archetype, not a policy headline archetype.
    - Sector liquidity support is necessary but not sufficient.
    - 003070 shows high-MAE failure after policy-liquidity spike.
    - 002780 shows shallow MFE and fade without company conversion.
    - 000720 shows that durable rerating requires a separate company-specific bridge.
  production_change:
    propose_immediate_weight_change: false
    do_not_propose_new_weight_delta: true
```

## 8. Machine-readable rows

```jsonl
{"row_type":"case","case_id":"C30_R10L89_000720","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"000720","name":"현대건설","trigger_type":"company_specific_order_margin_repair_after_policy_liquidity","trigger_date":"2025-01-22","entry_date":"2025-01-22","entry_price":28450,"peak_date":"2025-07-01","peak_price":83900,"mfe_pct":194.9,"mae_pct":-9.1,"post_peak_drawdown_pct":-35.2,"path_label":"positive_with_local_4B_overlay","calibration_usable":true,"do_not_propose_new_weight_delta":true}
{"row_type":"case","case_id":"C30_R10L89_003070","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"003070","name":"코오롱글로벌","trigger_type":"pf_liquidity_policy_price_spike_without_bs_repair_bridge","trigger_date":"2024-06-26","entry_date":"2024-06-26","entry_price":13630,"peak_date":"2024-06-27","peak_price":15200,"trough_date":"2024-08-05","trough_price":8500,"mfe_pct":11.5,"mae_pct":-37.6,"drawdown_from_peak_pct":-44.1,"path_label":"high_mae_counterexample","calibration_usable":true,"do_not_propose_new_weight_delta":true}
{"row_type":"case","case_id":"C30_R10L89_002780","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"002780","name":"진흥기업","trigger_type":"small_builder_policy_beta_without_balance_sheet_conversion","trigger_date":"2024-06-26","entry_date":"2024-06-26","entry_price":884,"peak_date":"2024-06-26","peak_price":1009,"trough_date":"2024-08-05","trough_price":797,"mfe_pct":14.1,"mae_pct":-9.8,"path_label":"stage2_false_positive_candidate","calibration_usable":true,"do_not_propose_new_weight_delta":true}
{"row_type":"aggregate","scheduled_round":"R10","scheduled_loop":89,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","new_independent_case_count":3,"positive_case_count":1,"counterexample_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_weight","shadow_rule_id":"C30_COMPANY_SPECIFIC_BS_REPAIR_BRIDGE_REQUIRED","target":"router_guard_not_weight_delta","production_change_now":false,"do_not_propose_new_weight_delta":true}
```

## 9. Deferred Coding Agent Handoff Prompt

```text
Implement a C30-specific router guard for e2r_2_1_stock_web_calibrated.

Do not change global weights immediately.

Target:
- large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
- canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK

Required behavior:
1. If trigger evidence is only PF policy liquidity support, restructuring guideline, construction sector relief, or price/volume spike:
   - cap at Watch
   - block Stage3-Yellow / Stage3-Green
   - set local_4b_watch if MFE/price surge is large without company-specific bridge
2. To allow Stage2-Actionable, require at least one company-specific bridge:
   - refinancing completed
   - PF exposure reduction
   - liquidity facility actually secured at company level
   - cash collection / receivables improvement
   - impaired site ringfence / sale
   - margin repair or order-backlog-to-earnings conversion
3. If MAE <= -30% after a policy-only trigger, label as high_mae_counterexample / possible 4C.
4. Preserve existing global price-only blowoff and hard 4C guards.

Validation cases:
- 000720 should be allowed only when company-specific bridge is present.
- 003070 should be blocked from Stage2-Actionable under policy-only evidence.
- 002780 should stay Watch / false-positive unless non-price company bridge appears.
```

## 10. Final status

```text
completed_round: R10
completed_loop: 89
next_round: R11
next_loop: 89
round_schedule_status: valid
round_sector_consistency: pass
```
