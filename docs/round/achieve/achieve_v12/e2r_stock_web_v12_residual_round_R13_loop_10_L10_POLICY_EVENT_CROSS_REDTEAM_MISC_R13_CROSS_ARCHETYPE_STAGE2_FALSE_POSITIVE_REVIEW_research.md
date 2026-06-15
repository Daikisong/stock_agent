# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 10
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
fine_archetype_id: CONTRACT_MATERIAL_CONSUMER_FINANCIAL_POLICY_TENDER_LABEL_TO_CASH_BRIDGE_STAGE2_GATE
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

R13 is a cross-archetype checkpoint. This file does not add a new sector-specific positive thesis. It red-teams the newest C04/C15/C20/C21/C22/C31/C32 rows through one question:

```text
Should this row really keep Stage2, or did the model pay for a label without a company-specific cash bridge?
```

The previous local `R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW` run reached loop 9. This continuation is therefore `loop 10`.

---

## 1. Research thesis

Stage2 false positives cluster around the same accounting error:

```text
a good-sounding headline
≠
a company-specific bridge into cash
```

Each archetype has its own vocabulary trap:

```text
C04 nuclear:
preferred bidder / supplier theme
≠ final contract / legal clearance / order-scope cash bridge

C15 materials:
metal / foil / chemical label
≠ ASP / utilization / margin / FCF bridge

C20 consumer:
K-food / K-beauty / global brand label
≠ sell-through / reorder / inventory quality / OPM bridge

C21 financial:
low-PBR / Value-up label
≠ ROE / payout / buyback / capital-return execution

C22 insurance:
insurance / GA / Value-up label
≠ reserve quality / CSM / solvency / capital-return bridge

C31 policy:
policy support headline
≠ issuer-specific refinancing / subsidy / budget / cashflow bridge

C32 governance:
shareholder-friendly cash
≠ formal tender / appraisal / squeeze-out / minority cash-exit mechanics
```

The R13 Stage2 false-positive gate should therefore act like customs at a border: the label can approach the gate, but the row needs papers before it enters Stage2.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 10
  actual_cases: 13
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
    - cross-archetype Stage2 false-positive guardrail
    - label-only hard block
    - bridge-present escape hatch
    - delayed bridge no-backfill guard
    - wrong-archetype reclassification guard
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
  - R13 accounting-trust loop 11
  - R13 high-MAE loop 7
  - R13 4B/4C loop 102
reason:
  - rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - current file changes canonical scope to R13 Stage2 false-positive review
  - exact source-archetype keys should be deduped separately from this R13 guardrail key
  - no production scoring changed
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":10,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"NUCLEAR_SUPPLIER_THEME_SPIKE_WITHOUT_CONTRACT_SCOPE_STAGE2_BLOCK","source_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"457550","name":"우진엔텍","trigger_type":"Stage2-FalsePositive","entry_date":"2024-07-18","entry_close":31500,"price_basis":"tradable_raw","mfe_30d_pct":32.06,"mae_30d_pct":-50.83,"mfe_90d_pct":32.06,"mae_90d_pct":-58.25,"mfe_180d_pct":32.06,"mae_180d_pct":-58.25,"forward_high_30d":41600,"forward_low_30d":15490,"forward_high_90d":41600,"forward_low_90d":13150,"forward_high_180d":41600,"forward_low_180d":13150,"calibration_usable":true,"case_role":"hard_false_positive","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|457550|Stage2-FalsePositive|2024-07-18","stage2_error":"supplier theme spike had no listed-company final-contract, order-scope, margin or cash bridge","route":"Stage2FalsePositiveBlock"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":10,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"NUCLEAR_PREFERRED_BIDDER_INCOMPLETE_BRIDGE_WATCH_NOT_ACTIONABLE","source_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"034020","name":"두산에너빌리티","trigger_type":"Stage2-Watch","entry_date":"2024-07-17","entry_close":21250,"price_basis":"tradable_raw","mfe_30d_pct":17.65,"mae_30d_pct":-28.71,"mfe_90d_pct":17.65,"mae_90d_pct":-28.71,"mfe_180d_pct":17.65,"mae_180d_pct":-28.71,"forward_high_30d":25000,"forward_low_30d":15150,"forward_high_90d":25000,"forward_low_90d":15150,"forward_high_180d":25000,"forward_low_180d":15150,"calibration_usable":true,"case_role":"watch_not_actionable","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|034020|Stage2-Watch|2024-07-17","stage2_error":"preferred-bidder headline lacked final contract, legal clearance and company cash bridge at trigger date","route":"Stage2Watch_NoBackfill"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":10,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"MATERIAL_MARGIN_BRIDGE_STAGE2_ESCAPE_HATCH","source_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"002380","name":"KCC","trigger_type":"Stage2-Actionable","entry_date":"2024-01-30","entry_close":244000,"price_basis":"tradable_raw","mfe_30d_pct":17.62,"mae_30d_pct":-2.46,"mfe_90d_pct":20.49,"mae_90d_pct":-7.79,"mfe_180d_pct":41.39,"mae_180d_pct":-7.79,"forward_high_30d":287000,"forward_low_30d":238000,"forward_high_90d":294000,"forward_low_90d":225000,"forward_high_180d":345000,"forward_low_180d":225000,"calibration_usable":true,"case_role":"positive_escape_hatch","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|002380|Stage2-Actionable|2024-01-30","stage2_error":"none; material margin bridge was company-specific and validated","route":"KeepStage2_MaterialMarginBridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":10,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"MATERIAL_LABEL_WITHOUT_ASP_MARGIN_REFRESH_CAP","source_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"006110","name":"삼아알미늄","trigger_type":"Stage2-Watch","entry_date":"2024-05-20","entry_close":75500,"price_basis":"tradable_raw","mfe_30d_pct":28.34,"mae_30d_pct":-7.28,"mfe_90d_pct":28.34,"mae_90d_pct":-47.55,"mfe_180d_pct":28.34,"mae_180d_pct":-53.58,"forward_high_30d":96900,"forward_low_30d":70000,"forward_high_90d":96900,"forward_low_90d":39600,"forward_high_180d":96900,"forward_low_180d":35050,"calibration_usable":true,"case_role":"stage2_cap_local_4B","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|006110|Stage2-Watch|2024-05-20","stage2_error":"battery-foil label had MFE but lacked refreshed order, utilization, ASP/margin or cash bridge","route":"Stage2Cap_Local4BUntilBridgeRefresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":10,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"GLOBAL_CONSUMER_SELLTHROUGH_STAGE2_ESCAPE_HATCH","source_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"003230","name":"삼양식품","trigger_type":"Stage2-Actionable","entry_date":"2024-05-17","entry_close":446500,"price_basis":"tradable_raw","mfe_30d_pct":60.81,"mae_30d_pct":0.00,"mfe_90d_pct":60.81,"mae_90d_pct":0.00,"mfe_180d_pct":106.05,"mae_180d_pct":0.00,"calibration_usable":true,"case_role":"positive_escape_hatch","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|003230|Stage2-Actionable|2024-05-17","stage2_error":"none; sell-through, ASP, shipment and OPM bridge validated","route":"KeepStage2_GlobalDistributionBridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":10,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LEGACY_BEAUTY_LABEL_WITHOUT_REORDER_STAGE2_BLOCK","source_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"090430","name":"아모레퍼시픽","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-31","entry_close":194200,"price_basis":"tradable_raw","mfe_30d_pct":3.24,"mae_30d_pct":-14.68,"mfe_90d_pct":3.24,"mae_90d_pct":-40.32,"mfe_180d_pct":3.24,"mae_180d_pct":-48.76,"calibration_usable":true,"case_role":"hard_false_positive","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|090430|Stage2-FalsePositive|2024-05-31","stage2_error":"legacy beauty / China rebound label lacked durable non-China sell-through, reorder and margin bridge","route":"Stage2FalsePositiveBlock"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":10,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"FINANCIAL_CAPITAL_RETURN_STAGE2_ESCAPE_HATCH","source_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"005940","name":"NH투자증권","trigger_type":"Stage2-Actionable","entry_date":"2024-02-26","entry_close":11420,"price_basis":"tradable_raw","mfe_30d_pct":14.71,"mae_30d_pct":-2.36,"mfe_90d_pct":14.71,"mae_90d_pct":-2.36,"mfe_180d_pct":26.09,"mae_180d_pct":-2.36,"forward_high_30d":13100,"forward_low_30d":11150,"forward_high_90d":13100,"forward_low_90d":11150,"forward_high_180d":14400,"forward_low_180d":11150,"calibration_usable":true,"case_role":"positive_escape_hatch","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|005940|Stage2-Actionable|2024-02-26","stage2_error":"none; ROE and capital-return bridge validated with controlled MAE","route":"KeepStage2_CapitalReturnBridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":10,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOW_PBR_BROKERAGE_LABEL_STAGE2_BLOCK","source_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"006800","name":"미래에셋증권","trigger_type":"Stage2-FalsePositive","entry_date":"2024-02-26","entry_close":8680,"price_basis":"tradable_raw","mfe_30d_pct":5.53,"mae_30d_pct":-10.71,"mfe_90d_pct":5.53,"mae_90d_pct":-20.16,"mfe_180d_pct":5.53,"mae_180d_pct":-23.96,"forward_high_30d":9160,"forward_low_30d":7750,"forward_high_90d":9160,"forward_low_90d":6930,"forward_high_180d":9160,"forward_low_180d":6600,"calibration_usable":true,"case_role":"hard_false_positive","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|006800|Stage2-FalsePositive|2024-02-26","stage2_error":"low-PBR brokerage label lacked incremental ROE and capital-return execution bridge","route":"Stage2FalsePositiveBlock"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":10,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"NONLIFE_RESERVE_CAPITAL_RETURN_STAGE2_ESCAPE_HATCH","source_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"005830","name":"DB손해보험","trigger_type":"Stage2-Actionable","entry_date":"2024-02-26","entry_close":95000,"price_basis":"tradable_raw","mfe_30d_pct":15.79,"mae_30d_pct":-4.11,"mfe_90d_pct":27.05,"mae_90d_pct":-9.26,"mfe_180d_pct":30.53,"mae_180d_pct":-9.26,"forward_high_30d":110000,"forward_low_30d":91100,"forward_high_90d":120700,"forward_low_90d":86200,"forward_high_180d":124000,"forward_low_180d":86200,"calibration_usable":true,"case_role":"positive_escape_hatch","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|005830|Stage2-Actionable|2024-02-26","stage2_error":"none; nonlife reserve quality, loss-ratio and capital-return bridge validated","route":"KeepStage2_InsuranceCapitalReturnBridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":10,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"INSURANCE_DISTRIBUTION_WRONG_ARCHETYPE_STAGE2_CAP","source_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"244920","name":"에이플러스에셋","trigger_type":"Stage2-Watch","entry_date":"2024-05-10","entry_close":4100,"price_basis":"tradable_raw","mfe_30d_pct":9.76,"mae_30d_pct":-2.32,"mfe_90d_pct":9.76,"mae_90d_pct":-13.78,"mfe_180d_pct":14.63,"mae_180d_pct":-13.78,"forward_high_30d":4500,"forward_low_30d":4005,"forward_high_90d":4500,"forward_low_90d":3535,"forward_high_180d":4700,"forward_low_180d":3535,"calibration_usable":true,"case_role":"reclassification_cap","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|244920|Stage2-Watch|2024-05-10","stage2_error":"GA distribution commission bridge may exist but selected C22/C32-style accounting bridge is absent","route":"Stage2Cap_Reclassify"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":10,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"PF_POLICY_SUPPORT_WITHOUT_ISSUER_CASH_BRIDGE_BLOCK","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"002990","name":"금호건설","trigger_type":"Stage2-FalsePositive","entry_date":"2024-01-26","entry_close":5030,"price_basis":"tradable_raw","mfe_30d_pct":5.00,"mae_30d_pct":-4.60,"mfe_90d_pct":5.00,"mae_90d_pct":-27.50,"mfe_180d_pct":5.00,"mae_180d_pct":-41.00,"forward_high_30d":5280,"forward_low_30d":4800,"forward_high_90d":5280,"forward_low_90d":3650,"forward_high_180d":5280,"forward_low_180d":2970,"calibration_usable":true,"case_role":"hard_false_positive","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|002990|Stage2-FalsePositive|2024-01-26","stage2_error":"PF support vocabulary lacked issuer-specific liquidity, debt-service, guarantee relief or cash bridge","route":"Stage2FalsePositiveBlock"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":10,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"FORMAL_TENDER_CASH_EXIT_STAGE2_ESCAPE_HATCH","source_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"041510","name":"에스엠","trigger_type":"Stage2-Actionable","entry_date":"2023-02-10","entry_close":114700,"price_basis":"tradable_raw","mfe_30d_pct":40.54,"mae_30d_pct":-6.45,"mfe_90d_pct":40.54,"mae_90d_pct":-21.10,"mfe_180d_pct":40.54,"mae_180d_pct":-21.10,"forward_high_30d":161200,"forward_low_30d":107300,"forward_high_90d":161200,"forward_low_90d":90500,"forward_high_180d":161200,"forward_low_180d":90500,"calibration_usable":true,"case_role":"positive_escape_hatch_with_post_resolution_4B","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|041510|Stage2-Actionable|2023-02-10","stage2_error":"none during tender; formal minority cash-exit mechanics validated, then post-resolution 4B applies","route":"KeepStage2_PostResolution4B"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":10,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"CAPITAL_RETURN_POSITIVE_ELSEWHERE_NOT_TENDER_STAGE2_CAP","source_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"105560","name":"KB금융","trigger_type":"Stage2-Watch","entry_date":"2024-07-26","entry_close":87900,"price_basis":"tradable_raw","mfe_30d_pct":5.12,"mae_30d_pct":-15.81,"mfe_90d_pct":18.20,"mae_90d_pct":-15.81,"mfe_180d_pct":18.20,"mae_180d_pct":-15.81,"forward_high_30d":92400,"forward_low_30d":74000,"forward_high_90d":103900,"forward_low_90d":74000,"forward_high_180d":103900,"forward_low_180d":74000,"calibration_usable":true,"case_role":"wrong_archetype_reclassification","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|105560|Stage2-Watch|2024-07-26","stage2_error":"bank capital-return bridge may be valid elsewhere but is not C32 tender/minority cash-exit mechanics","route":"Stage2Cap_ReclassifyToC21C31"}
```

---

## 5. Case analysis

### 5.1 Woojin Entech / 457550 — nuclear supplier spike false positive

The stock had MFE, but the row lacked a listed-company contract-scope cash bridge.

```text
route = Stage2FalsePositiveBlock
```

### 5.2 Doosan Enerbility / 034020 — preferred bidder watch, not Actionable

Preferred-bidder exposure is not final-contract accounting trust.

```text
route = Stage2Watch_NoBackfill
```

### 5.3 KCC / 002380 — material bridge escape hatch

Company-specific material margin bridge protects the row from hard block.

```text
route = KeepStage2_MaterialMarginBridge
```

### 5.4 Sam-A Aluminium / 006110 — material label local 4B

High MFE existed, but the later MAE demands margin refresh before any Green.

```text
route = Stage2Cap_Local4BUntilBridgeRefresh
```

### 5.5 Samyang Foods / 003230 — global distribution escape hatch

Sell-through and OPM bridge validated.

```text
route = KeepStage2_GlobalDistributionBridge
```

### 5.6 Amorepacific / 090430 — legacy brand false positive

Brand and channel rebound label did not become reorder/cash.

```text
route = Stage2FalsePositiveBlock
```

### 5.7 NH Investment & Securities / 005940 — capital-return escape hatch

ROE and shareholder-return execution validate Stage2.

```text
route = KeepStage2_CapitalReturnBridge
```

### 5.8 Mirae Asset Securities / 006800 — low-PBR false positive

Low-PBR label lacked execution and price path rejected it.

```text
route = Stage2FalsePositiveBlock
```

### 5.9 DB Insurance / 005830 — reserve/capital-return escape hatch

Reserve quality and capital-return bridge validate.

```text
route = KeepStage2_InsuranceCapitalReturnBridge
```

### 5.10 A Plus Asset / 244920 — wrong-archetype cap

GA distribution commission economics are not the selected accounting bridge.

```text
route = Stage2Cap_Reclassify
```

### 5.11 Kumho E&C / 002990 — PF support false positive

Policy umbrella did not reach issuer cashflow.

```text
route = Stage2FalsePositiveBlock
```

### 5.12 SM Entertainment / 041510 — tender cash-exit escape hatch

Formal tender mechanics are genuine accounting trust during the cash-exit window.

```text
route = KeepStage2_PostResolution4B
```

### 5.13 KB Financial / 105560 — real bridge, wrong C32 archetype

Capital-return bridge can be valid elsewhere, but not C32 tender mechanics.

```text
route = Stage2Cap_ReclassifyToC21C31
```

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 13
calibration_usable_case_count: 13
calibration_usable_trigger_count: 13
positive_escape_hatch_count: 5
stage2_watch_or_local_4B_count: 3
stage2_cap_or_reclassification_count: 2
stage2_false_positive_count: 4
current_profile_error_count: 9
```

| symbol | source | route | 90D MFE/MAE | 180D MFE/MAE | false-positive lesson |
|---|---:|---:|---:|---:|---|
| 457550 | C04 | hard block | +32.06 / -58.25 | +32.06 / -58.25 | supplier spike lacks contract economics |
| 034020 | C04 | watch | +17.65 / -28.71 | +17.65 / -28.71 | preferred bidder lacks final contract |
| 002380 | C15 | keep Stage2 | +20.49 / -7.79 | +41.39 / -7.79 | material margin bridge validates |
| 006110 | C15 | cap / 4B | +28.34 / -47.55 | +28.34 / -53.58 | material label needs refresh |
| 003230 | C20 | keep Stage2 | +60.81 / 0.00 | +106.05 / 0.00 | sell-through bridge validates |
| 090430 | C20 | hard block | +3.24 / -40.32 | +3.24 / -48.76 | brand label fails |
| 005940 | C21 | keep Stage2 | +14.71 / -2.36 | +26.09 / -2.36 | capital return validates |
| 006800 | C21 | hard block | +5.53 / -20.16 | +5.53 / -23.96 | low-PBR label fails |
| 005830 | C22 | keep Stage2 | +27.05 / -9.26 | +30.53 / -9.26 | reserve/capital bridge validates |
| 244920 | C22 | reclassify | +9.76 / -13.78 | +14.63 / -13.78 | GA bridge belongs elsewhere |
| 002990 | C31 | hard block | +5.00 / -27.50 | +5.00 / -41.00 | policy support lacks issuer cash |
| 041510 | C32 | keep Stage2 + 4B | +40.54 / -21.10 | +40.54 / -21.10 | tender cash-exit validates |
| 105560 | C32 boundary | reclassify | +18.20 / -15.81 | +18.20 / -15.81 | capital return is not tender |

---

## 7. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"457550","raw_label_signal":5,"raw_accounting_bridge":0,"raw_price_validation":0,"raw_reclassification_need":1,"raw_false_positive_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"034020","raw_label_signal":4,"raw_accounting_bridge":1,"raw_price_validation":1,"raw_reclassification_need":0,"raw_false_positive_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Watch_NoBackfill"}
{"row_type":"score_simulation","symbol":"002380","raw_label_signal":2,"raw_accounting_bridge":5,"raw_price_validation":4,"raw_reclassification_need":0,"raw_false_positive_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2"}
{"row_type":"score_simulation","symbol":"006110","raw_label_signal":4,"raw_accounting_bridge":1,"raw_price_validation":1,"raw_reclassification_need":1,"raw_false_positive_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Stage2CapLocal4B"}
{"row_type":"score_simulation","symbol":"003230","raw_label_signal":2,"raw_accounting_bridge":5,"raw_price_validation":5,"raw_reclassification_need":0,"raw_false_positive_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2"}
{"row_type":"score_simulation","symbol":"090430","raw_label_signal":4,"raw_accounting_bridge":0,"raw_price_validation":0,"raw_reclassification_need":0,"raw_false_positive_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"005940","raw_label_signal":2,"raw_accounting_bridge":5,"raw_price_validation":4,"raw_reclassification_need":0,"raw_false_positive_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2"}
{"row_type":"score_simulation","symbol":"006800","raw_label_signal":4,"raw_accounting_bridge":0,"raw_price_validation":0,"raw_reclassification_need":1,"raw_false_positive_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"005830","raw_label_signal":2,"raw_accounting_bridge":5,"raw_price_validation":4,"raw_reclassification_need":0,"raw_false_positive_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2"}
{"row_type":"score_simulation","symbol":"244920","raw_label_signal":3,"raw_accounting_bridge":1,"raw_price_validation":1,"raw_reclassification_need":5,"raw_false_positive_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2CapReclassify"}
{"row_type":"score_simulation","symbol":"002990","raw_label_signal":4,"raw_accounting_bridge":0,"raw_price_validation":0,"raw_reclassification_need":0,"raw_false_positive_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"041510","raw_label_signal":3,"raw_accounting_bridge":5,"raw_price_validation":4,"raw_reclassification_need":0,"raw_false_positive_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2PostResolution4B"}
{"row_type":"score_simulation","symbol":"105560","raw_label_signal":3,"raw_accounting_bridge":4,"raw_price_validation":2,"raw_reclassification_need":5,"raw_false_positive_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Reclassify"}
```

---

## 8. Current calibrated profile stress test

### Existing error risk

The current profile can still over-open Stage2 for:

```text
label + MFE
```

The safer test is:

```text
label + company-specific cash bridge + acceptable price path
```

If a case has no bridge, it is a painted door. If a case has a bridge in another archetype, it should be sent to that room. If a case has a bridge but it is incomplete, it waits in 4B.

### Rule candidate

```text
R13_STAGE2_FALSE_POSITIVE_BRIDGE_PASSPORT_GATE_V10

if trigger_label_exists == true
and company_specific_accounting_bridge_at_trigger_date == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if company_specific_accounting_bridge_at_trigger_date == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
```

```text
if label_only == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage2_FalsePositive_Block
```

```text
if label_only == true
and MFE_30D_pct >= +20
and MAE_90D_pct <= -25:
    route = Stage2_FalsePositive_Block_or_Local4B_then_Block
```

```text
if bridge_belongs_to_other_archetype == true:
    cap_selected_archetype_contribution = true
    require_reclassification = true
```

```text
if later_evidence_after_trigger == true:
    do_not_backfill_to_original_trigger = true
    require_new_trigger_from_later_evidence_date = true
```

---

## 9. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
cross_archetype_rule_candidate: true
loop_contribution_label: cross_archetype_stage2_false_positive_guardrail_candidate
new_axis_proposed: R13_STAGE2_FALSE_POSITIVE_BRIDGE_PASSPORT_GATE_V10
existing_axis_strengthened:
  - label_without_accounting_bridge_stage2_block
  - company_specific_bridge_stage2_escape_hatch
  - wrong_archetype_reclassification_guard
  - later_evidence_no_backfill_guard
  - local_4B_until_bridge_refresh
existing_axis_weakened: null
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this single MD. Batch this R13 Stage2 false-positive loop with R13 accounting-trust loop 11, R13 high-MAE loop 7, R13 4B/4C loop 102, and source loops C04/C15/C20/C21/C22/C31/C32 from this session. Extract `R13_STAGE2_FALSE_POSITIVE_BRIDGE_PASSPORT_GATE_V10` as a cross-archetype shadow rule. Preserve Stage2 where a company-specific accounting bridge is visible, block label-only rows, reclassify wrong-archetype rows, and prevent later evidence from being backfilled into earlier triggers.
```

---

## 11. Next research state

```yaml
completed_round: R13
completed_loop: 10
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
