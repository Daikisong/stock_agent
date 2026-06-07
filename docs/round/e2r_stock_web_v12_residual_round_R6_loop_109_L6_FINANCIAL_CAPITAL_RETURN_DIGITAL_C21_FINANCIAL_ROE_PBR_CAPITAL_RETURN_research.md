# E2R v12 residual calibration research — R6 / loop 109 / C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R6
selected_loop = 109
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = BANK_ROE_PBR_VALUEUP_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_REGIONAL_BANK_LABEL_WEAK_BRIDGE
output_format = one_standalone_markdown_file
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
stock_web_price_atlas_access_required = true
```

## 1. Selection rationale

This run targets `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN`.

The no-repeat / coverage ledger marks C21 as Priority 1 with 48 rows and only 2 rows short of the 50-row practical calibration band. The purpose here is not to repeat the already used KB Financial, Hana Financial, KakaoBank, Shinhan, Woori, BNK, or Jeju Bank case sets. This run therefore adds a new bank / regional financial-holding set:

- `024110` 기업은행
- `175330` JB금융지주
- `139130` DGB금융지주 / iM금융지주

The shared macro trigger is the 2024-02-28 Korea Corporate Value-up follow-up expectation: the Financial Supervisory Service discussed possible future consequences for listed companies that fail to improve shareholder return, and undervalued sectors such as banks were specifically part of the market reaction.

## 2. Price source and data caveats

Price source:

```text
repo = Songdaiki/stock-web
price_basis = tradable_raw
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
max_date = 2026-02-20
```

Calculation method:

```text
entry_price = close on trigger/entry date
MFE = (max_high_after_entry - entry_price) / entry_price
MAE = (min_low_after_entry - entry_price) / entry_price
```

Corporate-action note:

- The selected 2024 windows are outside the old corporate-action candidate dates shown in the profiles.
- C21 still requires caution because finance names can rally on common value-up beta while failing to show company-specific shareholder-return execution.

## 3. Shared trigger

```text
trigger_id = KOREA_VALUEUP_FOLLOWUP_BANK_LOW_PBR_2024_02_28
trigger_date = 2024-02-28
entry_date = 2024-02-29
trigger_family = policy_valueup_shareholder_return_bank_low_pbr
external_source = Reuters, 2024-02-28, South Korea considering penalties on firms failing to boost shareholder return
```

Interpretation:

The trigger is not “buy all banks.” It is a policy shock that should only help C21 scoring when the stock also has a credible bridge:

```text
low PBR / ROE discount
→ explicit capital policy or shareholder-return execution
→ dividend / buyback / cancellation or credible payout discipline
→ rerating without excessive MAE
```

## 4. Case table

| case_id | symbol | name | label | entry | peak | trough | MFE | MAE |
|---|---:|---|---|---:|---:|---:|---:|---:|
| C21_024110_2024_VALUEUP_STATE_BANK_CAPITAL_RETURN_WATCH | 024110 | 기업은행 | positive_high_MAE_watch | 14,000 | 16,010 | 12,510 | 14.36% | -10.64% |
| C21_175330_2024_VALUEUP_REGIONAL_FINANCIAL_HOLDING_STRONG_POSITIVE | 175330 | JB금융지주 | positive_full_window_4B_watch | 13,160 | 20,500 | 11,700 | 55.78% | -11.09% |
| C21_139130_2024_VALUEUP_REGIONAL_BANK_WEAK_BRIDGE_COUNTEREXAMPLE | 139130 | DGB금융지주/iM금융지주 | counterexample_low_MFE_high_MAE | 8,860 | 9,410 | 7,750 | 6.21% | -12.53% |

## 5. Case notes

### 5.1 기업은행 (`024110`) — state-owned bank value-up positive, but high-MAE watch

Profile facts:

```text
symbol = 024110
name = 기업은행
market = KOSPI
2024 window corporate_action_block = none observed in selected window
```

Observed path:

```text
entry_date = 2024-02-29
entry_close = 14,000
peak_date = 2024-03-15
peak_high = 16,010
trough_date = 2024-04-15
trough_low = 12,510
MFE = +14.36%
MAE = -10.64%
```

Interpretation:

기업은행 confirms that C21 value-up / low-PBR bank exposure can work. However, the path is not clean: the MFE is moderate and the drawdown exceeds 10%. This should be treated as `positive_high_MAE_watch`, not as automatic Stage3-Green. For state-influenced banks, the scoring model should demand evidence that shareholder-return policy is executable rather than merely sector-implied.

### 5.2 JB금융지주 (`175330`) — regional financial holding strong positive, but full-window 4B watch

Profile facts:

```text
symbol = 175330
name = JB금융지주
market = KOSPI
2024 window corporate_action_block = none observed in selected window
```

Observed path:

```text
entry_date = 2024-02-29
entry_close = 13,160
peak_date = 2024-12-03
peak_high = 20,500
trough_date = 2024-04-19
trough_low = 11,700
MFE = +55.78%
MAE = -11.09%
```

Interpretation:

JB금융지주 is a strong positive for C21, but the peak was delayed and the interim path had a >10% drawdown. This supports a C21 shadow rule: regional financial holdings can rerate powerfully under value-up, but a model should distinguish “delayed full-window rerating” from an immediately clean Stage3-Green. The correct treatment is positive with 4B watch unless capital-return execution is explicitly verified.

### 5.3 DGB금융지주 / iM금융지주 (`139130`) — regional-bank label weak-bridge counterexample

Profile facts:

```text
symbol = 139130
name_on_trigger = DGB금융지주
latest_name = iM금융지주
market = KOSPI
2024 window corporate_action_block = none observed in selected window
```

Observed path:

```text
entry_date = 2024-02-29
entry_close = 8,860
peak_date = 2024-03-15
peak_high = 9,410
trough_date = 2024-06-27
trough_low = 7,750
MFE = +6.21%
MAE = -12.53%
```

Interpretation:

This is the key counterexample. DGB/iM had the same broad policy trigger and regional-bank label, but the upside was weak and the drawdown was material. The model should not map “regional bank + value-up” directly to C21 credit. Without evidence of ROE/PBR discount closure and actual capital-return execution, the case belongs in Stage1/Stage2 watch or 4C-prone reject, not Stage3.

## 6. Residual error diagnosis

Current residual mistake pattern:

```text
if sector == financial
and headline contains value-up / low-PBR / shareholder return
then C21 score too easily rises
```

Corrected interpretation:

```text
C21 is not a bank-label factor.
C21 is a capital-efficiency and shareholder-return execution factor.
```

The same macro trigger produced three different paths:

```text
기업은행: +14.36% MFE / -10.64% MAE = positive but high-MAE watch
JB금융지주: +55.78% MFE / -11.09% MAE = strong positive but delayed/full-window 4B watch
DGB/iM금융지주: +6.21% MFE / -12.53% MAE = weak-bridge counterexample
```

This spread means the model should gate C21 by evidence quality, not by financial-sector exposure.

## 7. Stage comparison

| case | current-profile likely error | corrected stage |
|---|---|---|
| 기업은행 | Treating state bank + value-up as clean Stage3 | Stage2-Actionable / Stage3-Yellow only if capital-return bridge verified |
| JB금융지주 | Treating high full-window MFE as clean Green | Stage3-Yellow / 4B watch until explicit payout/buyback execution bridge |
| DGB/iM금융지주 | Treating regional-bank label as C21 positive | Stage1/Stage2 watch or 4C-prone counterexample |

## 8. Shadow rule candidate

```yaml
shadow_rule_id: c21_bank_roe_pbr_capital_return_execution_bridge_required_v2
scope:
  large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
  canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
condition:
  trigger_family:
    - korea_valueup
    - low_pbr_financial
    - shareholder_return_policy
  sector:
    - bank
    - financial_holding
    - securities
required_bridge:
  any_two_of:
    - explicit dividend payout target / payout-ratio policy
    - buyback or cancellation plan
    - ROE improvement plan
    - CET1 / capital-ratio room supporting shareholder return
    - repeated investor-day or value-up disclosure with measurable target
penalty:
  if only sector_label_or_policy_beta:
    stage_cap: Stage2
  if MFE < 10% and MAE < -10%:
    classify_as: 4C_or_counterexample
  if MFE > 30% but MAE < -10%:
    classify_as: positive_full_window_4B_watch
production_change_now: false
shadow_weight_only: true
```

## 9. Machine-readable rows

```jsonl
{"row_type":"case","case_id":"C21_024110_2024_VALUEUP_STATE_BANK_CAPITAL_RETURN_WATCH","round":"R6","loop":109,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_ROE_PBR_VALUEUP_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_REGIONAL_BANK_LABEL_WEAK_BRIDGE","symbol":"024110","name":"기업은행","trigger_date":"2024-02-29","entry_date":"2024-02-29","entry_price":14000,"peak_date":"2024-03-15","peak_high":16010,"trough_date":"2024-04-15","trough_low":12510,"mfe_pct":14.36,"mae_pct":-10.64,"label":"positive_high_MAE_watch","calibration_usable":true}
{"row_type":"case","case_id":"C21_175330_2024_VALUEUP_REGIONAL_FINANCIAL_HOLDING_STRONG_POSITIVE","round":"R6","loop":109,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_ROE_PBR_VALUEUP_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_REGIONAL_BANK_LABEL_WEAK_BRIDGE","symbol":"175330","name":"JB금융지주","trigger_date":"2024-02-29","entry_date":"2024-02-29","entry_price":13160,"peak_date":"2024-12-03","peak_high":20500,"trough_date":"2024-04-19","trough_low":11700,"mfe_pct":55.78,"mae_pct":-11.09,"label":"positive_full_window_4B_watch","calibration_usable":true}
{"row_type":"case","case_id":"C21_139130_2024_VALUEUP_REGIONAL_BANK_WEAK_BRIDGE_COUNTEREXAMPLE","round":"R6","loop":109,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_ROE_PBR_VALUEUP_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_REGIONAL_BANK_LABEL_WEAK_BRIDGE","symbol":"139130","name":"DGB금융지주/iM금융지주","trigger_date":"2024-02-29","entry_date":"2024-02-29","entry_price":8860,"peak_date":"2024-03-15","peak_high":9410,"trough_date":"2024-06-27","trough_low":7750,"mfe_pct":6.21,"mae_pct":-12.53,"label":"counterexample_low_MFE_high_MAE","calibration_usable":true}
{"row_type":"trigger","trigger_id":"KOREA_VALUEUP_FOLLOWUP_BANK_LOW_PBR_2024_02_28","trigger_date":"2024-02-28","entry_date":"2024-02-29","trigger_family":"policy_valueup_shareholder_return_bank_low_pbr","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","evidence_source":"Reuters 2024-02-28 S.Korea considering penalties on firms failing to boost shareholder return"}
{"row_type":"score_simulation","shadow_rule_id":"c21_bank_roe_pbr_capital_return_execution_bridge_required_v2","case_count":3,"positive_case_count":2,"counterexample_count":1,"stage_cap_if_only_sector_label":"Stage2","stage3_green_requires":"explicit capital-return execution bridge plus acceptable MAE"}
{"row_type":"aggregate","round":"R6","loop":109,"canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","new_independent_case_count":3,"reused_case_count":0,"same_archetype_new_symbol_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":3}
{"row_type":"shadow_weight","shadow_rule_id":"c21_bank_roe_pbr_capital_return_execution_bridge_required_v2","production_scoring_changed":false,"shadow_weight_only":true,"suggested_effect":"reduce bank/value-up label-only false positives; require payout/buyback/ROE/CET1 bridge"}
{"row_type":"residual_contribution","loop_contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":"c21_bank_roe_pbr_capital_return_execution_bridge_required_v2","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to C21 bank/value-up rallies"}
```

## 10. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent. Do not run live scans. Do not change production scoring directly from one MD. Batch this MD with other v12 residual calibration MDs.

Research artifact:
- e2r_stock_web_v12_residual_round_R6_loop_109_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md

Task:
1. Parse the JSONL rows in section 9.
2. Add these cases to the C21 calibration evidence registry only if their no-repeat keys are absent.
3. Treat c21_bank_roe_pbr_capital_return_execution_bridge_required_v2 as a shadow-only rule candidate.
4. Do not immediately change production scoring.
5. If multiple C21 MDs agree, propose a gated rule:
   - bank/value-up/low-PBR labels can at most reach Stage2 without explicit shareholder-return execution evidence.
   - Stage3-Yellow/Green requires measurable capital-return execution evidence and acceptable MAE.
6. Preserve corporate-action blocking behavior from stock-web profile caveats.
```

## 11. Final run summary

```text
이번 라운드: R6 / Loop 109 / L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_round: R6
selected_loop: 109
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BANK_ROE_PBR_VALUEUP_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_REGIONAL_BANK_LABEL_WEAK_BRIDGE

new_independent_case_count: 3
reused_case_count: 0
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable case 수: 3
calibration_usable trigger 수: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 3
verified_url_repair_needed_count: 2

diversity_score_summary: C21 Priority 1 보강 + 기업은행 state-bank value-up high-MAE positive watch + JB금융지주 regional financial-holding strong full-window positive + DGB/iM금융지주 regional-bank weak-bridge counterexample
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C21 rows 48, 50-row target까지 2 부족
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: c21_bank_roe_pbr_capital_return_execution_bridge_required_v2
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C21 bank/value-up rallies
existing_axis_weakened: null
next_recommended_archetypes: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG, C16_STRATEGIC_RESOURCE_POLICY_SUPPLY, C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
```
