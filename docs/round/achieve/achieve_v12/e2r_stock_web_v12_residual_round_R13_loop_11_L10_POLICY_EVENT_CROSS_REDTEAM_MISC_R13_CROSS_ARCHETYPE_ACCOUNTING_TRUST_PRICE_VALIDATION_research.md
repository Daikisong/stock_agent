# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 11
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
fine_archetype_id: POLICY_CONTRACT_MATERIAL_CONSUMER_FINANCIAL_TENDER_CASH_BRIDGE_VALIDATION
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

R13 is a cross-archetype checkpoint, not a sector-specific positive-discovery round. This file uses the latest current-session C04, C15, C20, C21, C22, C31 and C32 rows and asks one accounting-trust question:

```text
Did the story become a company-specific cash bridge at the trigger date?
```

The previous local `R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION` run reached loop 10. This continuation is `loop 11`.

---

## 1. Research thesis

Accounting trust is the moment a story stops being vocabulary and starts behaving like a ledger.

```text
policy headline
→ must become legal clearance, final contract, budget, subsidy, refinancing, payout or cashflow

material label
→ must become ASP, utilization, margin, FCF

global consumer label
→ must become sell-through, repeat order, inventory quality, OPM/revision

financial/insurance value-up
→ must become CET1, payout, buyback, reserve quality, CSM, solvency, capital return

governance premium
→ must become formal tender, appraisal, squeeze-out, legally visible minority cash-exit mechanics
```

The profile should not ask whether a label sounds right. It should ask whether the label has a receipt attached.

This loop splits six cross-archetype routes:

1. **Project/policy bridge not final at trigger**
   - Preferred-bidder or support headline can be local 4B.
   - Later final contract or delayed rebound must not be backfilled into the original trigger.

2. **Material margin bridge vs material label**
   - Company-specific margin bridge validates.
   - Material label with no ASP/margin/FCF bridge blocks.

3. **Consumer distribution bridge vs brand label**
   - Sell-through and reorder validate.
   - Legacy brand / channel label without durable bridge blocks.

4. **Financial/insurance capital bridge vs low-PBR label**
   - ROE, payout, reserve and capital-return validate.
   - Low-PBR / value-up label without execution caps or blocks.

5. **Policy bridge vs policy umbrella**
   - C31 survives only when policy reaches issuer cashflow.
   - Sector support alone is Watch.

6. **Tender cash-exit vs shareholder-friendly cash**
   - Formal tender/cash-exit validates C32.
   - Capital return, payout and buyback policy are real elsewhere but not C32 unless minority exit mechanics exist.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 10
  actual_cases: 12
  source_archetypes:
    - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
    - C15_MATERIAL_SPREAD_SUPERCYCLE
    - C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
    - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
    - C22_INSURANCE_RATE_CYCLE_RESERVE
    - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
    - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - cross-archetype accounting-trust validation
    - label-to-cash-bridge guardrail
    - no-backfill guard
    - wrong-archetype reclassification guard
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
  - R1/C04 loop 114
  - R4/C15 loop 105
  - R5/C20 loop 115
  - R6/C21 loop 112
  - R6/C22 loop 111
  - R11/C31 loops 103~104
  - R12/C32 loop 104
  - R13 Stage2 false-positive loop 9
  - R13 high-MAE loop 7
  - R13 4B/4C loop 102
reason:
  - rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - current file changes canonical scope to R13 accounting-trust validation
  - exact source-archetype keys should be deduped separately from this R13 guardrail key
  - no production scoring changed
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":11,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"NUCLEAR_PREFERRED_BIDDER_NOT_FINAL_CONTRACT_ACCOUNTING_TRUST_4B","source_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"034020","name":"두산에너빌리티","trigger_type":"Stage2-Watch","entry_date":"2024-07-17","entry_close":21250,"price_basis":"tradable_raw","mfe_30d_pct":17.65,"mae_30d_pct":-28.71,"mfe_90d_pct":17.65,"mae_90d_pct":-28.71,"mfe_180d_pct":17.65,"mae_180d_pct":-28.71,"forward_high_30d":25000,"forward_low_30d":15150,"forward_high_90d":25000,"forward_low_90d":15150,"forward_high_180d":25000,"forward_low_180d":15150,"calibration_usable":true,"case_role":"accounting_trust_incomplete_local_4B","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|034020|Stage2-Watch|2024-07-17","accounting_bridge":"preferred-bidder supply-chain exposure without final contract, legal clearance, order-scope or cash bridge at trigger","route":"Local4B_NoFinalContractBackfill"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":11,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"NUCLEAR_SUPPLIER_SPIKE_NO_CONTRACT_SCOPE_ACCOUNTING_TRUST_BLOCK","source_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"457550","name":"우진엔텍","trigger_type":"Stage2-FalsePositive","entry_date":"2024-07-18","entry_close":31500,"price_basis":"tradable_raw","mfe_30d_pct":32.06,"mae_30d_pct":-50.83,"mfe_90d_pct":32.06,"mae_90d_pct":-58.25,"mfe_180d_pct":32.06,"mae_180d_pct":-58.25,"forward_high_30d":41600,"forward_low_30d":15490,"forward_high_90d":41600,"forward_low_90d":13150,"forward_high_180d":41600,"forward_low_180d":13150,"calibration_usable":true,"case_role":"accounting_trust_absent_hard_block","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|457550|Stage2-FalsePositive|2024-07-18","accounting_bridge":"supplier theme spike without listed-company final-contract, order-scope, margin or cash bridge","route":"Stage2FalsePositiveBlock"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":11,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"MATERIAL_COMPANY_MARGIN_BRIDGE_ACCOUNTING_TRUST_VALIDATED","source_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"002380","name":"KCC","trigger_type":"Stage2-Actionable","entry_date":"2024-01-30","entry_close":244000,"price_basis":"tradable_raw","mfe_30d_pct":17.62,"mae_30d_pct":-2.46,"mfe_90d_pct":20.49,"mae_90d_pct":-7.79,"mfe_180d_pct":41.39,"mae_180d_pct":-7.79,"forward_high_30d":287000,"forward_low_30d":238000,"forward_high_90d":294000,"forward_low_90d":225000,"forward_high_180d":345000,"forward_low_180d":225000,"calibration_usable":true,"case_role":"accounting_trust_validated","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|002380|Stage2-Actionable|2024-01-30","accounting_bridge":"company-specific materials/silicone/paint margin recovery, revision and cash bridge","route":"KeepStage2_MaterialMarginBridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":11,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"MATERIAL_BATTERY_FOIL_LABEL_WITHOUT_MARGIN_REFRESH_4B","source_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"006110","name":"삼아알미늄","trigger_type":"Stage2-Watch","entry_date":"2024-05-20","entry_close":75500,"price_basis":"tradable_raw","mfe_30d_pct":28.34,"mae_30d_pct":-7.28,"mfe_90d_pct":28.34,"mae_90d_pct":-47.55,"mfe_180d_pct":28.34,"mae_180d_pct":-53.58,"forward_high_30d":96900,"forward_low_30d":70000,"forward_high_90d":96900,"forward_low_90d":39600,"forward_high_180d":96900,"forward_low_180d":35050,"calibration_usable":true,"case_role":"accounting_trust_unrefreshed_local_4B","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|006110|Stage2-Watch|2024-05-20","accounting_bridge":"aluminium battery-foil label without refreshed customer order, utilization, ASP/margin or cash bridge","route":"Local4B_RequireMarginRefresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":11,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"GLOBAL_DISTRIBUTION_SELLTHROUGH_OPM_ACCOUNTING_TRUST_VALIDATED","source_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"003230","name":"삼양식품","trigger_type":"Stage2-Actionable","entry_date":"2024-05-17","entry_close":446500,"price_basis":"tradable_raw","mfe_30d_pct":60.81,"mae_30d_pct":0.00,"mfe_90d_pct":60.81,"mae_90d_pct":0.00,"mfe_180d_pct":106.05,"mae_180d_pct":0.00,"calibration_usable":true,"case_role":"accounting_trust_validated","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|003230|Stage2-Actionable|2024-05-17","accounting_bridge":"export sell-through, ASP, shipment/capacity, OPM/revision and repeat-order bridge","route":"KeepStage2_GlobalDistributionBridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":11,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"LEGACY_BEAUTY_CHANNEL_LABEL_WITHOUT_SELLTHROUGH_BLOCK","source_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"090430","name":"아모레퍼시픽","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-31","entry_close":194200,"price_basis":"tradable_raw","mfe_30d_pct":3.24,"mae_30d_pct":-14.68,"mfe_90d_pct":3.24,"mae_90d_pct":-40.32,"mfe_180d_pct":3.24,"mae_180d_pct":-48.76,"calibration_usable":true,"case_role":"accounting_trust_absent_hard_block","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|090430|Stage2-FalsePositive|2024-05-31","accounting_bridge":"legacy beauty/China-channel rebound label without durable non-China sell-through, reorder, margin or cash bridge","route":"Stage2FalsePositiveBlock"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":11,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"FINANCIAL_CAPITAL_RETURN_ACCOUNTING_TRUST_VALIDATED","source_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"005940","name":"NH투자증권","trigger_type":"Stage2-Actionable","entry_date":"2024-02-26","entry_close":11420,"price_basis":"tradable_raw","mfe_30d_pct":14.71,"mae_30d_pct":-2.36,"mfe_90d_pct":14.71,"mae_90d_pct":-2.36,"mfe_180d_pct":26.09,"mae_180d_pct":-2.36,"forward_high_30d":13100,"forward_low_30d":11150,"forward_high_90d":13100,"forward_low_90d":11150,"forward_high_180d":14400,"forward_low_180d":11150,"calibration_usable":true,"case_role":"accounting_trust_validated","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|005940|Stage2-Actionable|2024-02-26","accounting_bridge":"securities ROE, brokerage/IB/WM earnings and capital-return execution bridge","route":"KeepStage2_CapitalReturnBridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":11,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"LOW_PBR_LABEL_WITHOUT_CAPITAL_RETURN_EXECUTION_BLOCK","source_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"006800","name":"미래에셋증권","trigger_type":"Stage2-FalsePositive","entry_date":"2024-02-26","entry_close":8680,"price_basis":"tradable_raw","mfe_30d_pct":5.53,"mae_30d_pct":-10.71,"mfe_90d_pct":5.53,"mae_90d_pct":-20.16,"mfe_180d_pct":5.53,"mae_180d_pct":-23.96,"forward_high_30d":9160,"forward_low_30d":7750,"forward_high_90d":9160,"forward_low_90d":6930,"forward_high_180d":9160,"forward_low_180d":6600,"calibration_usable":true,"case_role":"accounting_trust_absent_hard_block","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|006800|Stage2-FalsePositive|2024-02-26","accounting_bridge":"low-PBR brokerage label without incremental ROE or capital-return execution bridge","route":"Stage2FalsePositiveBlock"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":11,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"NONLIFE_RESERVE_CAPITAL_RETURN_ACCOUNTING_TRUST_VALIDATED","source_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"005830","name":"DB손해보험","trigger_type":"Stage2-Actionable","entry_date":"2024-02-26","entry_close":95000,"price_basis":"tradable_raw","mfe_30d_pct":15.79,"mae_30d_pct":-4.11,"mfe_90d_pct":27.05,"mae_90d_pct":-9.26,"mfe_180d_pct":30.53,"mae_180d_pct":-9.26,"forward_high_30d":110000,"forward_low_30d":91100,"forward_high_90d":120700,"forward_low_90d":86200,"forward_high_180d":124000,"forward_low_180d":86200,"calibration_usable":true,"case_role":"accounting_trust_validated","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|005830|Stage2-Actionable|2024-02-26","accounting_bridge":"nonlife reserve quality, loss-ratio discipline, solvency and capital-return bridge","route":"KeepStage2_InsuranceReserveCapitalBridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":11,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"PF_POLICY_TO_ISSUER_CASH_BRIDGE_DELAYED_LOCAL_4B","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"294870","name":"HDC현대산업개발","trigger_type":"Stage2-Watch","entry_date":"2024-05-13","entry_close":17920,"price_basis":"tradable_raw","mfe_30d_pct":2.12,"mae_30d_pct":-6.58,"mfe_90d_pct":37.28,"mae_90d_pct":-6.58,"mfe_180d_pct":57.37,"mae_180d_pct":-6.58,"forward_high_30d":18300,"forward_low_30d":16740,"forward_high_90d":24600,"forward_low_90d":16740,"forward_high_180d":28200,"forward_low_180d":16740,"calibration_usable":true,"case_role":"accounting_trust_delayed_local_4B","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|294870|Stage2-Watch|2024-05-13","accounting_bridge":"housing/PF soft-landing policy path, but issuer-specific refinancing/liquidity bridge not visible at entry","route":"DelayedLocal4B_NoBackfill"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":11,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"FORMAL_TENDER_MINORITY_CASH_EXIT_ACCOUNTING_TRUST_VALIDATED","source_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"041510","name":"에스엠","trigger_type":"Stage2-Actionable","entry_date":"2023-02-10","entry_close":114700,"price_basis":"tradable_raw","mfe_30d_pct":40.54,"mae_30d_pct":-6.45,"mfe_90d_pct":40.54,"mae_90d_pct":-21.10,"mfe_180d_pct":40.54,"mae_180d_pct":-21.10,"forward_high_30d":161200,"forward_low_30d":107300,"forward_high_90d":161200,"forward_low_90d":90500,"forward_high_180d":161200,"forward_low_180d":90500,"calibration_usable":true,"case_role":"accounting_trust_validated_with_post_resolution_4B","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|041510|Stage2-Actionable|2023-02-10","accounting_bridge":"formal tender/control contest cash path with visible minority exit mechanics","route":"KeepStage2_PostResolution4B"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":11,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"CAPITAL_RETURN_POSITIVE_ELSEWHERE_NOT_TENDER_RECLASSIFY","source_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"105560","name":"KB금융","trigger_type":"Stage2-Watch","entry_date":"2024-07-26","entry_close":87900,"price_basis":"tradable_raw","mfe_30d_pct":5.12,"mae_30d_pct":-15.81,"mfe_90d_pct":18.20,"mae_90d_pct":-15.81,"mfe_180d_pct":18.20,"mae_180d_pct":-15.81,"forward_high_30d":92400,"forward_low_30d":74000,"forward_high_90d":103900,"forward_low_90d":74000,"forward_high_180d":103900,"forward_low_180d":74000,"calibration_usable":true,"case_role":"wrong_archetype_reclassification","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|105560|Stage2-Watch|2024-07-26","accounting_bridge":"bank Value-up/capital-return bridge may be real, but it is not formal tender/appraisal/minority cash-exit mechanics","route":"ReclassifyToC21C31_C32Cap"}
```

---

## 5. Case analysis

### 5.1 Doosan Enerbility / 034020 — accounting trust incomplete at trigger

The preferred-bidder story had economic potential, but at the trigger date it lacked final contract, legal clearance, scope and cash bridge.

```text
route = Local4B_NoFinalContractBackfill
```

### 5.2 Woojin Entech / 457550 — supplier spike without ledger bridge

High MFE without contract-scope economics is not accounting trust.

```text
route = Stage2FalsePositiveBlock
```

### 5.3 KCC / 002380 — material margin bridge validates

The material bridge reached company margin and price path validated.

```text
route = KeepStage2_MaterialMarginBridge
```

### 5.4 Sam-A Aluminium / 006110 — material label needs refresh

The first move was strong, but later MAE says accounting trust was not refreshed.

```text
route = Local4B_RequireMarginRefresh
```

### 5.5 Samyang Foods / 003230 — consumer distribution bridge validates

Sell-through, ASP and OPM became a real accounting bridge.

```text
route = KeepStage2_GlobalDistributionBridge
```

### 5.6 Amorepacific / 090430 — legacy brand label fails

A famous brand does not equal repeat-order accounting trust.

```text
route = Stage2FalsePositiveBlock
```

### 5.7 NH Investment & Securities / 005940 — capital-return bridge validates

The low drawdown and later MFE fit a real capital-return / ROE bridge.

```text
route = KeepStage2_CapitalReturnBridge
```

### 5.8 Mirae Asset Securities / 006800 — low-PBR label fails

Cheapness without execution is not accounting trust.

```text
route = Stage2FalsePositiveBlock
```

### 5.9 DB Insurance / 005830 — reserve/capital bridge validates

Insurance capital-return accounting bridge validated.

```text
route = KeepStage2_InsuranceReserveCapitalBridge
```

### 5.10 HDC Hyundai Development / 294870 — delayed issuer bridge only

Policy/housing soft-landing helped later, but not at trigger date.

```text
route = DelayedLocal4B_NoBackfill
```

### 5.11 SM Entertainment / 041510 — tender cash-exit validates

Formal tender mechanics create genuine accounting trust, followed by post-resolution 4B.

```text
route = KeepStage2_PostResolution4B
```

### 5.12 KB Financial / 105560 — real cash bridge, wrong archetype

Capital return can be real but not C32 tender mechanics.

```text
route = ReclassifyToC21C31_C32Cap
```

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 12
calibration_usable_case_count: 12
calibration_usable_trigger_count: 12
accounting_trust_validated_count: 5
local_4B_or_delayed_count: 4
stage2_false_positive_count: 3
wrong_archetype_reclassification_count: 1
current_profile_error_count: 8
```

| symbol | source | route | 90D MFE/MAE | 180D MFE/MAE | accounting lesson |
|---|---:|---:|---:|---:|---|
| 034020 | C04 | local 4B | +17.65 / -28.71 | +17.65 / -28.71 | preferred bidder lacks final contract bridge |
| 457550 | C04 | hard block | +32.06 / -58.25 | +32.06 / -58.25 | supplier spike lacks contract economics |
| 002380 | C15 | keep Stage2 | +20.49 / -7.79 | +41.39 / -7.79 | material margin bridge validates |
| 006110 | C15 | local 4B | +28.34 / -47.55 | +28.34 / -53.58 | material label needs utilization/margin refresh |
| 003230 | C20 | keep Stage2 | +60.81 / 0.00 | +106.05 / 0.00 | sell-through/OPM validates |
| 090430 | C20 | hard block | +3.24 / -40.32 | +3.24 / -48.76 | brand label lacks reorder bridge |
| 005940 | C21 | keep Stage2 | +14.71 / -2.36 | +26.09 / -2.36 | capital return validates |
| 006800 | C21 | hard block | +5.53 / -20.16 | +5.53 / -23.96 | low-PBR label lacks execution |
| 005830 | C22 | keep Stage2 | +27.05 / -9.26 | +30.53 / -9.26 | reserve/capital bridge validates |
| 294870 | C31 | delayed 4B | +37.28 / -6.58 | +57.37 / -6.58 | delayed policy bridge, no backfill |
| 041510 | C32 | keep Stage2 + 4B | +40.54 / -21.10 | +40.54 / -21.10 | tender cash-exit validates |
| 105560 | C32 boundary | reclassify | +18.20 / -15.81 | +18.20 / -15.81 | capital return is real but not tender |

---

## 7. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"034020","raw_label_signal":4,"raw_company_specific_cash_bridge":1,"raw_accounting_trust":1,"raw_price_validation":1,"raw_false_positive_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B_NoBackfill"}
{"row_type":"score_simulation","symbol":"457550","raw_label_signal":5,"raw_company_specific_cash_bridge":0,"raw_accounting_trust":0,"raw_price_validation":0,"raw_false_positive_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"002380","raw_label_signal":2,"raw_company_specific_cash_bridge":5,"raw_accounting_trust":5,"raw_price_validation":4,"raw_false_positive_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2"}
{"row_type":"score_simulation","symbol":"006110","raw_label_signal":4,"raw_company_specific_cash_bridge":1,"raw_accounting_trust":1,"raw_price_validation":1,"raw_false_positive_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4BRequireRefresh"}
{"row_type":"score_simulation","symbol":"003230","raw_label_signal":2,"raw_company_specific_cash_bridge":5,"raw_accounting_trust":5,"raw_price_validation":5,"raw_false_positive_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2"}
{"row_type":"score_simulation","symbol":"090430","raw_label_signal":4,"raw_company_specific_cash_bridge":0,"raw_accounting_trust":0,"raw_price_validation":0,"raw_false_positive_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"005940","raw_label_signal":2,"raw_company_specific_cash_bridge":5,"raw_accounting_trust":5,"raw_price_validation":4,"raw_false_positive_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2"}
{"row_type":"score_simulation","symbol":"006800","raw_label_signal":4,"raw_company_specific_cash_bridge":0,"raw_accounting_trust":0,"raw_price_validation":0,"raw_false_positive_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"005830","raw_label_signal":2,"raw_company_specific_cash_bridge":5,"raw_accounting_trust":5,"raw_price_validation":4,"raw_false_positive_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2"}
{"row_type":"score_simulation","symbol":"294870","raw_label_signal":3,"raw_company_specific_cash_bridge":2,"raw_accounting_trust":1,"raw_price_validation":3,"raw_false_positive_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"DelayedLocal4B"}
{"row_type":"score_simulation","symbol":"041510","raw_label_signal":3,"raw_company_specific_cash_bridge":5,"raw_accounting_trust":5,"raw_price_validation":4,"raw_false_positive_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_PostResolution4B"}
{"row_type":"score_simulation","symbol":"105560","raw_label_signal":3,"raw_company_specific_cash_bridge":4,"raw_accounting_trust":3,"raw_price_validation":2,"raw_false_positive_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"WrongArchetypeReclassify"}
```

---

## 8. Current calibrated profile stress test

### Existing error risk

The profile can still confuse three things:

```text
headline
bridge
cash
```

A headline points. A bridge carries. Cash lands. Accounting trust requires the last two.

### Rule candidate

```text
R13_ACCOUNTING_TRUST_LEDGER_BRIDGE_GATE_V11

if trigger_headline_or_label == true
and company_specific_cash_bridge_at_trigger_date == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if company_specific_cash_bridge_at_trigger_date == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    accounting_trust_validated = true
    keep_stage2_actionable_bonus = true
```

```text
if company_specific_bridge_exists_but_refresh_missing == true
and MAE_90D_pct <= -20:
    route = local_4B_watch
    block_stage3_green = true
    require_bridge_refresh = true
```

```text
if later_contract_policy_or_cash_bridge_after_trigger == true:
    do_not_backfill_to_original_trigger = true
    require_new_trigger_from_later_evidence_date = true
```

```text
if bridge_belongs_to_other_archetype == true:
    cap_selected_archetype_contribution = true
    require_reclassification = true
```

```text
if label_only == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage2_FalsePositive_Block
```

---

## 9. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
cross_archetype_rule_candidate: true
loop_contribution_label: cross_archetype_accounting_trust_ledger_bridge_candidate
new_axis_proposed: R13_ACCOUNTING_TRUST_LEDGER_BRIDGE_GATE_V11
existing_axis_strengthened:
  - accounting_bridge_at_trigger_date_required
  - company_cash_bridge_positive_escape_hatch
  - local_4B_until_bridge_refresh
  - later_evidence_no_backfill_guard
  - wrong_archetype_bridge_reclassification_guard
  - low_MFE_high_MAE_label_only_false_positive_block
existing_axis_weakened: null
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this single MD. Batch this R13 accounting-trust loop with R13 loops 7/9/10/102 and source loops C04/C15/C20/C21/C22/C31/C32 from this session. Extract `R13_ACCOUNTING_TRUST_LEDGER_BRIDGE_GATE_V11` as a cross-archetype shadow rule. Preserve rows where company-specific cash bridge is visible at the trigger date, route incomplete bridges to local 4B, block label-only rows, and prevent later evidence from being backfilled into earlier triggers.
```

---

## 11. Next research state

```yaml
completed_round: R13
completed_loop: 11
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
  - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
  - C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```
