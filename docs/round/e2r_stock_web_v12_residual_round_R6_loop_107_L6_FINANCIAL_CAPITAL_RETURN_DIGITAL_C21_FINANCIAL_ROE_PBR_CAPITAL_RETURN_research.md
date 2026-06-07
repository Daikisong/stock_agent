# e2r stock-web v12 residual research — R6 Loop 107 — C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R6
selected_loop = 107
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_SMALL_BANK_LABEL_BLOWOFF
output_format = one_standalone_markdown_file
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
production_scoring_changed = false
shadow_weight_only = true
price_source = Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year
price_basis = tradable_raw
```

## 1. Selection basis

`V12_Research_No_Repeat_Index.md` marks `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN` as Priority 1 with 48 rows and only 2 rows needed to reach the 50-row practical calibration zone. This run therefore prioritizes C21 even though C03/C16 still have larger absolute gaps.

Already-used C21 set avoided:
- KB금융 / 105560
- 하나금융지주 / 086790
- 카카오뱅크 / 323410

New case set:
- 신한지주 / 055550
- 우리금융지주 / 316140
- BNK금융지주 / 138930
- 제주은행 / 006220

## 2. External trigger spine

Common historical trigger:

```text
trigger_date = 2024-02-28
trigger_type = Korea Corporate Value-up Programme follow-up / shareholder-return enforcement expectation
external_evidence = Reuters 2024-02-28 + Reuters 2024-03-14
```

The February 2024 Reuters evidence says Korean authorities were considering consequences for companies that failed to improve shareholder returns, after the initial Corporate Value-up Programme disappointed the market. The March 2024 follow-up says regulators were preparing faster and stronger follow-up measures, including possible tax incentives and stewardship/index mechanisms.

For C21, the core distinction is not “financial stock went up.” The useful bridge is:

```text
low PBR / bank holding discount
→ plausible ROE and CET1-capital policy bridge
→ dividends / buybacks / cancellation / shareholder-return execution
→ rerating with tolerable MAE
```

The failure mode is:

```text
bank label or value-up sympathy
→ no clear capital-return execution bridge
→ price-only spike
→ high-MAE fade / 4C
```

## 3. Price source and caveats

Price rows are from `Songdaiki/stock-web` tradable calibration shards.

Manifest basis:
- source_name: FinanceData/marcap
- price_adjustment_status: raw_unadjusted_marcap
- max_date: 2026-02-20
- calibration_shard_root: `atlas/ohlcv_tradable_by_symbol_year`
- corporate-action-contaminated windows blocked by default

This run does not use pykrx/FDR/data.go.kr/Naver/Yahoo/Stooq route hunting. It only reads existing stock-web shards.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | peak_date | peak_price | trough_date | trough_price | MFE | MAE | label |
|---|---:|---|---|---|---:|---|---:|---|---:|---:|---:|---|
| C21_R6L107_055550_20240229 | 055550 | 신한지주 | 2024-02-28 | 2024-02-29 | 43,550 | 2024-08-26 | 64,600 | 2024-04-17 | 40,450 | +48.34% | -7.12% | positive |
| C21_R6L107_316140_20240229 | 316140 | 우리금융지주 | 2024-02-28 | 2024-02-29 | 14,900 | 2024-10-25 | 17,100 | 2024-04-15 | 13,150 | +14.77% | -11.74% | positive_high_MAE_watch |
| C21_R6L107_138930_20240229 | 138930 | BNK금융지주 | 2024-02-28 | 2024-02-29 | 7,500 | 2024-12-03 | 11,900 | 2024-02-29 | 7,440 | +58.67% | -0.80% | positive_full_window_4B_watch |
| C21_R6L107_006220_20240229 | 006220 | 제주은행 | 2024-02-28 | 2024-02-29 | 12,090 | 2024-04-19 | 16,900 | 2024-12-09 | 6,750 | +39.78% | -44.17% | counterexample_bank_label_blowoff |

## 5. Case notes

### 5.1 신한지주 / 055550 — bank holding value-up positive

`055550` has no corporate-action candidate in the stock-web profile for the tested window. Entry is 2024-02-29 close 43,550. The stock then made a high of 64,600 on 2024-08-26. The worst post-entry low used here is 40,450 on 2024-04-17.

Interpretation:

```text
C21 positive.
Traditional bank holding company + low-PBR/value-up theme + clearer capital-return expectation produced a large MFE with tolerable MAE.
This supports Stage2-Actionable / Stage3-Yellow potential when capital-return execution evidence is present.
```

Calibration implication:

```text
Do not score this merely as “financial sector beta.”
The useful axis is bank-holding discount + capital-return execution probability + ROE/PBR rerating.
```

### 5.2 우리금융지주 / 316140 — positive but high-MAE watch

`316140` has no corporate-action candidate in the stock-web profile. Entry is 2024-02-29 close 14,900. The stock made a later high of 17,100 on 2024-10-25, while the worst post-entry low used here is 13,150 on 2024-04-15.

Interpretation:

```text
C21 positive, but not clean enough for automatic Green.
MFE is real, but intermediate MAE was above 10%, so a profile must require capital policy confirmation, not just low-PBR bank label.
```

Calibration implication:

```text
Stage2-Actionable can be justified only with shareholder-return execution evidence.
Without that, keep as Yellow/high-MAE watch.
```

### 5.3 BNK금융지주 / 138930 — regional bank holding positive with late full-window extension

`138930` has older corporate-action candidates, but not in the 2024 trigger window. Entry is 2024-02-29 close 7,500. The post-entry price path eventually reached 11,900 on 2024-12-03. Initial downside was small in the immediate entry window, with the trigger-day low at 7,440.

Interpretation:

```text
C21 positive, but the peak is late enough to require a full-window 4B watch.
Regional financial holding can work when the market rerates low-PBR bank capital-return optionality, but late acceleration can include broader financial/value-up crowding.
```

Calibration implication:

```text
C21 should allow regional bank holdings to score when ROE/PBR and capital return are visible.
However, late blowoff after months of drift should not be used as clean Green evidence unless policy/capital-return execution is confirmed.
```

### 5.4 제주은행 / 006220 — small-bank label blowoff counterexample

`006220` has old corporate-action caveats but the 2024 window itself is not blocked by the listed corporate-action dates. Entry is 2024-02-29 close 12,090. The stock reached 16,900 on 2024-04-19, but later fell to 6,750 on 2024-12-09.

Interpretation:

```text
Hard C21 counterexample.
The “bank/value-up” label generated a large MFE, but the full path is a high-MAE blowoff without durable capital-return bridge.
```

Calibration implication:

```text
Small bank / speculative bank label should not inherit the same C21 score as major financial holding companies.
Require explicit capital policy, ROE/PBR discount credibility, liquidity, and shareholder-return execution evidence.
```

## 6. Residual profile error

Current calibrated profile likely still over-rewards broad “financial/value-up” labels if it does not separate:

```text
major bank holding + capital policy execution
vs.
small bank / bank label / speculative rerating without execution
```

Observed residual errors:
1. 제주은행: high MFE could look successful in a price-only window, but the full path is a -44% MAE hard fade.
2. 우리금융지주: positive but MAE >10%, so Green should require stronger capital-return confirmation.
3. BNK금융지주: positive, but late full-window extension should trigger 4B watch if only price evidence exists.

## 7. Proposed shadow rule

```text
rule_id = c21_bank_roe_pbr_capital_return_execution_bridge_required_shadow_only

IF canonical_archetype_id == C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
AND trigger_type IN {value_up_programme, shareholder_return_policy, low_pbr_bank_rerating}
THEN:
  - require company-specific evidence of capital-return execution or credible capital policy
  - require low-PBR/ROE discount relevance, not generic financial label
  - require bank-holding or insurer/financial-holding quality tier separation
  - cap Stage2 if evidence is only sector sympathy
  - cap Stage3-Green if MAE > 10% before evidence confirmation
  - mark small-bank/high-beta bank-label spikes as 4B/4C watch unless capital policy bridge is explicit
```

Suggested scoring behavior:

```text
major_bank_holding_capital_return_bridge: +1.0 shadow
explicit_buyback_or_cancellation_or_dividend_policy: +0.7 shadow
low_pbr_roe_discount_with_CET1_capacity: +0.5 shadow
small_bank_label_without_capital_policy: -0.8 shadow
price_only_valueup_spike_high_MAE: -1.0 shadow
```

## 8. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C21_R6L107_055550_20240229","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_SMALL_BANK_LABEL_BLOWOFF","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","symbol":"055550","name":"신한지주","trigger_date":"2024-02-28","entry_date":"2024-02-29","entry_price":43550,"peak_date":"2024-08-26","peak_price":64600,"trough_date":"2024-04-17","trough_price":40450,"mfe_pct":48.34,"mae_pct":-7.12,"label":"positive","calibration_usable":true,"source_price_repo":"Songdaiki/stock-web","price_basis":"tradable_raw"}
{"row_type":"case","case_id":"C21_R6L107_316140_20240229","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_SMALL_BANK_LABEL_BLOWOFF","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","symbol":"316140","name":"우리금융지주","trigger_date":"2024-02-28","entry_date":"2024-02-29","entry_price":14900,"peak_date":"2024-10-25","peak_price":17100,"trough_date":"2024-04-15","trough_price":13150,"mfe_pct":14.77,"mae_pct":-11.74,"label":"positive_high_MAE_watch","calibration_usable":true,"source_price_repo":"Songdaiki/stock-web","price_basis":"tradable_raw"}
{"row_type":"case","case_id":"C21_R6L107_138930_20240229","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_SMALL_BANK_LABEL_BLOWOFF","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","symbol":"138930","name":"BNK금융지주","trigger_date":"2024-02-28","entry_date":"2024-02-29","entry_price":7500,"peak_date":"2024-12-03","peak_price":11900,"trough_date":"2024-02-29","trough_price":7440,"mfe_pct":58.67,"mae_pct":-0.80,"label":"positive_full_window_4B_watch","calibration_usable":true,"source_price_repo":"Songdaiki/stock-web","price_basis":"tradable_raw"}
{"row_type":"case","case_id":"C21_R6L107_006220_20240229","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_SMALL_BANK_LABEL_BLOWOFF","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","symbol":"006220","name":"제주은행","trigger_date":"2024-02-28","entry_date":"2024-02-29","entry_price":12090,"peak_date":"2024-04-19","peak_price":16900,"trough_date":"2024-12-09","trough_price":6750,"mfe_pct":39.78,"mae_pct":-44.17,"label":"counterexample_bank_label_blowoff","calibration_usable":true,"source_price_repo":"Songdaiki/stock-web","price_basis":"tradable_raw"}
{"row_type":"aggregate","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","new_independent_case_count":4,"positive_case_count":3,"counterexample_count":1,"current_profile_error_count":3,"do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"C21 rows 48, 50-row target까지 2 부족","new_axis_proposed":"c21_bank_roe_pbr_capital_return_execution_bridge_required_shadow_only"}
{"row_type":"shadow_weight","rule_id":"c21_bank_roe_pbr_capital_return_execution_bridge_required_shadow_only","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","major_bank_holding_capital_return_bridge_delta":1.0,"explicit_buyback_or_cancellation_or_dividend_policy_delta":0.7,"low_pbr_roe_discount_with_CET1_capacity_delta":0.5,"small_bank_label_without_capital_policy_delta":-0.8,"price_only_valueup_spike_high_MAE_delta":-1.0,"production_scoring_changed":false}
```

## 9. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this Markdown as already-applied production logic. Batch this with other v12 residual MD files.

Task:
- Parse the JSONL rows in this MD.
- Add calibration cases for C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN only if they do not violate the no-repeat key:
  canonical_archetype_id + symbol + trigger_type + entry_date.
- Preserve price source metadata:
  source_repo = Songdaiki/stock-web
  price_basis = tradable_raw
  shard_root = atlas/ohlcv_tradable_by_symbol_year
- Implement only shadow/evaluation rules first:
  c21_bank_roe_pbr_capital_return_execution_bridge_required_shadow_only
- Do not change production scoring until enough v12 residual MDs are aggregated and reviewed.
- Keep small-bank/price-only bank label blowoffs separate from major bank holding capital-return execution evidence.
```

## 10. Final summary fields

```text
이번 라운드: R6 / Loop 107 / L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_round: R6
selected_loop: 107
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_SMALL_BANK_LABEL_BLOWOFF

new_independent_case_count: 4
reused_case_count: 0
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
calibration_usable case 수: 4
calibration_usable trigger 수: 4
positive_case_count: 3
counterexample_count: 1
current_profile_error_count: 3
verified_url_repair_needed_count: 1

diversity_score_summary: C21 Priority 1 보강 + 신한지주 clean value-up positive + 우리금융 high-MAE positive watch + BNK regional-bank positive/full-window 4B watch + 제주은행 small-bank label blowoff counterexample
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C21 rows 48, 50-row target까지 2 부족
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: c21_bank_roe_pbr_capital_return_execution_bridge_required_shadow_only
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C21 value-up/bank rallies
existing_axis_weakened: null
next_recommended_archetypes: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG, C16_STRATEGIC_RESOURCE_POLICY_SUPPLY, C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
```
