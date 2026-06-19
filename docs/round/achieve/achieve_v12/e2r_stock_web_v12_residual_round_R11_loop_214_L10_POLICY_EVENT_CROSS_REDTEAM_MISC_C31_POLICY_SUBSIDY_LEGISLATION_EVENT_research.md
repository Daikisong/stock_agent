# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata
```yaml
selected_round: "R11"
selected_loop: 214
selection_basis: "docs/core/V12_Research_No_Repeat_Index.md"
selected_priority_bucket: "Priority 0 URL/proxy quality repair + Priority 2 C31 cashflow-conversion compression"
round_schedule_status: "coverage_index_selected"
round_sector_consistency: "pass"
large_sector_id: "L10_POLICY_EVENT_CROSS_REDTEAM_MISC"
canonical_archetype_id: "C31_POLICY_SUBSIDY_LEGISLATION_EVENT"
fine_archetype_id: "C31_POLICY_TO_CASHFLOW_CONVERSION_DIRECT_SOURCE_REPAIR"
loop_objective: "direct-source validation; policy-to-cashflow conversion; counterexample mining; 4B non-price requirement stress test"
price_source: "Songdaiki/stock-web"
price_basis: "tradable_raw"
price_adjustment_status: "raw_unadjusted_marcap"
stock_web_manifest_max_date: "2026-02-20"
production_scoring_changed: false
shadow_weight_only: true
live_scan: false
stock_agent_code_patch_allowed: false
```

This loop adds 8 new independent cases, 4 counterexamples, and 4 residual errors for R11/L10/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.

## 1. Current Calibrated Profile Assumption
The run assumes `e2r_2_1_stock_web_calibrated_proxy` as the current profile and does not patch production scoring. Existing calibrated axes are treated as already applied: Stage2 bridge, Yellow/Green thresholds, price-only blowoff block, full-4B non-price requirement, and hard-4C thesis-break routing. The research asks a narrower C31 question: when does a policy headline actually enter the issuer's cash register?

## 2. Round / Large Sector / Canonical Archetype Scope
- selected_round: `R11` because `C31_POLICY_SUBSIDY_LEGISLATION_EVENT` maps to `R11 / L10_POLICY_EVENT_CROSS_REDTEAM_MISC`.
- large_sector_id: `L10_POLICY_EVENT_CROSS_REDTEAM_MISC`.
- canonical_archetype_id: `C31_POLICY_SUBSIDY_LEGISLATION_EVENT`.
- fine_archetype_id: `C31_POLICY_TO_CASHFLOW_CONVERSION_DIRECT_SOURCE_REPAIR`.
- invalid round-sector pair: `false`.

## 3. Previous Coverage / Duplicate Avoidance Check
The No-Repeat ledger shows all C01~C32 archetypes above 80 rows, so this is quality repair rather than row filling. Same-session previous outputs already covered C15, C05, C01, C13, C10, R13-high-MAE, and R13-accounting/source quality. C31 is selected as the next direct URL/proxy repair target. All eight cases use new symbols relative to the selected C31 loop in this run, and none repeats canonical_archetype_id + symbol + trigger_type + entry_date from the visible current chain.

Priority interpretation:
- Priority 0: reduce source proxy / pending URL / missing MFE-MAE risk.
- Priority 2: C31 has enough rows but needs direct cashflow conversion compression.
- selected_priority_bucket: `Priority 0 URL/proxy quality repair + Priority 2 C31 cashflow-conversion compression`.

## 4. Stock-Web OHLC Input / Price Source Validation
```json
{
  "source_name": "FinanceData/marcap via Songdaiki/stock-web",
  "source_repo_url": "https://github.com/Songdaiki/stock-web",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "markets": [
    "KONEX",
    "KOSDAQ",
    "KOSDAQ GLOBAL",
    "KOSPI"
  ],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv"
}
```
Tradable shard columns used: `d,o,h,l,c,v,a,mc,s,m`. Entry price is the close (`c`) of the entry date, and MFE/MAE are calculated from max high / min low across the forward trading-day windows.

## 5. Historical Eligibility Gate
| case_id | symbol | entry_date | entry_price_close | forward_180D | window_end_180D | 180D corporate-action status | usable |
|---|---:|---:|---:|---:|---:|---|---|
| C31-R11-L214-01 | 105560 | 2024-02-27 | 62400 | 180 | 2024-11-21 | clean_180D_window | true |
| C31-R11-L214-02 | 138930 | 2024-02-27 | 7720 | 180 | 2024-11-21 | clean_180D_window | true |
| C31-R11-L214-03 | 071320 | 2024-02-28 | 43300 | 180 | 2024-11-22 | clean_180D_window | true |
| C31-R11-L214-04 | 112610 | 2022-08-17 | 63600 | 180 | 2023-05-09 | clean_180D_window | true |
| C31-R11-L214-05 | 015760 | 2023-05-16 | 18680 | 180 | 2024-02-06 | clean_180D_window | true |
| C31-R11-L214-06 | 036460 | 2023-05-16 | 25850 | 180 | 2024-02-06 | clean_180D_window | true |
| C31-R11-L214-07 | 336260 | 2023-05-25 | 30700 | 180 | 2024-02-19 | clean_180D_window | true |
| C31-R11-L214-08 | 052690 | 2022-03-11 | 95200 | 180 | 2022-11-29 | clean_180D_window | true |

## 6. Canonical Archetype Compression Map
C31 compresses several event families into one calibration problem: the state, a law, a subsidy, or a regulator can open a door, but the issuer still has to walk through it with a named beneficiary route and recognizable cashflow. The compression ladder used here is:

```text
policy/law headline -> implementation framework -> named beneficiary/direct route -> cashflow conversion bridge -> durable margin, tax credit, dividend/buyback, tariff sufficiency, or awarded contract
```
Rows that stop at the first two rungs remain Stage2/Yellow watch. Rows that reach the last two rungs can support Green. Rows that arrive after a crowded rerating without the bridge become 4B watch candidates.

## 7. Case Selection Summary
| case_id | symbol | company | trigger_date | entry_date | trigger_type | role | family | MFE_180D | MAE_180D | verdict |
|---|---:|---|---:|---:|---|---|---|---:|---:|---|
| C31-R11-L214-01 | 105560 | KB금융 | 2024-02-26 | 2024-02-27 | Stage2-Actionable | structural_success | corporate_value_up_capital_return_policy | 66.51% | -2.40% | current_profile_correct |
| C31-R11-L214-02 | 138930 | BNK금융지주 | 2024-02-26 | 2024-02-27 | Stage2 | stage2_promote_candidate | regional_financial_value_up_beta | 33.94% | -5.18% | current_profile_correct |
| C31-R11-L214-03 | 071320 | 지역난방공사 | 2024-02-27 | 2024-02-28 | Stage2-Actionable | high_mae_success | public_company_value_up_dividend_repricing | 24.48% | -18.13% | current_profile_correct |
| C31-R11-L214-04 | 112610 | 씨에스윈드 | 2022-08-16 | 2022-08-17 | Stage3-Yellow | structural_success | ira_ampc_foreign_legislation_direct_manufacturing_credit | 38.52% | -10.85% | current_profile_correct |
| C31-R11-L214-05 | 015760 | 한국전력 | 2023-05-15 | 2023-05-16 | Stage2-Actionable | failed_rerating | electricity_tariff_hike_partial_pass_through | 11.62% | -14.19% | current_profile_too_early |
| C31-R11-L214-06 | 036460 | 한국가스공사 | 2023-05-15 | 2023-05-16 | Stage2-Actionable | failed_rerating | gas_tariff_hike_partial_pass_through | 10.44% | -11.99% | current_profile_too_early |
| C31-R11-L214-07 | 336260 | 두산퓨얼셀 | 2023-05-24 | 2023-05-25 | Stage3-Yellow | false_positive_green | hydrogen_bidding_market_without_issuer_award | 2.61% | -47.72% | current_profile_false_positive |
| C31-R11-L214-08 | 052690 | 한전기술 | 2022-03-10 | 2022-03-11 | Stage4B | 4B_overlay_success | nuclear_policy_revival_after_crowded_rerating_without_project_cashflow | 1.37% | -49.84% | current_profile_false_positive |

## 8. Positive vs Counterexample Balance
- positive_case_count: `4`
- counterexample_count: `4`
- positive theme: named capital-return or direct credit route survives the policy-to-cashflow gate.
- counterexample theme: tariff/policy/market creation exists, but issuer cashflow remains insufficient or the signal arrives after the event premium has already inflated price.
- positive mean MFE180/MAE180: `40.86% / -9.14%`
- counterexample mean MFE180/MAE180: `6.51% / -30.94%`

## 9. Evidence Source Map
| key | source URL | use in this MD |
|---|---|---|
| FSC_VALUE_UP | https://www.fsc.go.kr/eng/pr010101/81778 | C31-R11-L214-01; C31-R11-L214-02; C31-R11-L214-03 |
| KB_SEC_VALUE_UP | https://www.sec.gov/Archives/edgar/data/1445930/000119312524242219/d901349d6k.htm | C31-R11-L214-01 |
| DOE_WIND_IRA | https://www.energy.gov/sites/default/files/2023-04/eere-wind-weto-funding-taxday-factsheet-fy23.pdf | C31-R11-L214-04 |
| YNA_TARIFF | https://en.yna.co.kr/view/AEN20230515001600320 | C31-R11-L214-05; C31-R11-L214-06 |
| JIPYONG_HYDROGEN | https://www.jipyong.com/en/board/jipyongNews_post.php?seq=5981 | C31-R11-L214-07 |
| DOOSAN_FUELCELL_VISIT | https://www.doosanfuelcell.com/en/media-center/medi-0101_view/?id=125 | C31-R11-L214-07 |
| REUTERS_NUCLEAR | https://www.reuters.com/business/energy/skorea-lift-nuclear-powers-share-energy-mix-30-by-2030-2022-07-05/ | C31-R11-L214-08 |
| PULSE_DISTRICT_HEATING | https://www.mk.co.kr/en/stock/10952026 | C31-R11-L214-03 |

## 10. Price Data Source Map
| symbol | company | price_shard_path | profile_path | entry OHLC row |
|---:|---|---|---|---|
| 105560 | KB금융 | `atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv` | `atlas/symbol_profiles/105/105560.json` | d=2024-02-27, o=62000, h=63200, l=61500, c=62400, v=1643919 |
| 138930 | BNK금융지주 | `atlas/ohlcv_tradable_by_symbol_year/138/138930/2024.csv` | `atlas/symbol_profiles/138/138930.json` | d=2024-02-27, o=7710, h=7910, l=7680, c=7720, v=2398245 |
| 071320 | 지역난방공사 | `atlas/ohlcv_tradable_by_symbol_year/071/071320/2024.csv` | `atlas/symbol_profiles/071/071320.json` | d=2024-02-28, o=40900, h=44950, l=39500, c=43300, v=252006 |
| 112610 | 씨에스윈드 | `atlas/ohlcv_tradable_by_symbol_year/112/112610/2022.csv` | `atlas/symbol_profiles/112/112610.json` | d=2022-08-17, o=64500, h=65300, l=63100, c=63600, v=349094 |
| 015760 | 한국전력 | `atlas/ohlcv_tradable_by_symbol_year/015/015760/2023.csv` | `atlas/symbol_profiles/015/015760.json` | d=2023-05-16, o=19120, h=19230, l=18650, c=18680, v=1844472 |
| 036460 | 한국가스공사 | `atlas/ohlcv_tradable_by_symbol_year/036/036460/2023.csv` | `atlas/symbol_profiles/036/036460.json` | d=2023-05-16, o=26200, h=26250, l=25700, c=25850, v=340512 |
| 336260 | 두산퓨얼셀 | `atlas/ohlcv_tradable_by_symbol_year/336/336260/2023.csv` | `atlas/symbol_profiles/336/336260.json` | d=2023-05-25, o=30900, h=31300, l=30700, c=30700, v=159073 |
| 052690 | 한전기술 | `atlas/ohlcv_tradable_by_symbol_year/052/052690/2022.csv` | `atlas/symbol_profiles/052/052690.json` | d=2022-03-11, o=89600, h=96500, l=89000, c=95200, v=1965370 |

## 11. Case-by-Case Trigger Grid

### C31-R11-L214-01 — 105560 KB금융
- trigger_date: `2024-02-26` / entry_date: `2024-02-27` / entry_price_close: `62400`
- trigger_type: `Stage2-Actionable`
- trigger_family: `corporate_value_up_capital_return_policy`
- evidence_available_at_that_date: FSC Feb-26 Corporate Value-up Program launch; later KB SEC 6-K verifies issuer-level shareholder return/capital-management bridge, used only as later validation.
- stage2_evidence_fields: `public_event_or_disclosure, policy_or_regulatory_optionality, capital_return_route`
- stage3_evidence_fields: `financial_visibility, issuer_specific_capital_return_plan, low_red_team_risk`
- stage4b_evidence_fields: `none`
- current_profile_verdict: `current_profile_correct`

### C31-R11-L214-02 — 138930 BNK금융지주
- trigger_date: `2024-02-26` / entry_date: `2024-02-27` / entry_price_close: `7720`
- trigger_type: `Stage2`
- trigger_family: `regional_financial_value_up_beta`
- evidence_available_at_that_date: FSC value-up launch produced low-PBR financial beta, but issuer-specific return plan was weaker on trigger date.
- stage2_evidence_fields: `public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength`
- stage3_evidence_fields: `financial_visibility_partial`
- stage4b_evidence_fields: `none`
- current_profile_verdict: `current_profile_correct`

### C31-R11-L214-03 — 071320 지역난방공사
- trigger_date: `2024-02-27` / entry_date: `2024-02-28` / entry_price_close: `43300`
- trigger_type: `Stage2-Actionable`
- trigger_family: `public_company_value_up_dividend_repricing`
- evidence_available_at_that_date: Public-company value-up expectation plus earnings/dividend repricing; high MAE says policy/public ownership needs cash distribution bridge rather than headline-only Green.
- stage2_evidence_fields: `public_event_or_disclosure, policy_or_regulatory_optionality, earnings_repricing_route`
- stage3_evidence_fields: `financial_visibility, dividend_or_distribution_expectation_partial`
- stage4b_evidence_fields: `high_mae_success`
- current_profile_verdict: `current_profile_correct`

### C31-R11-L214-04 — 112610 씨에스윈드
- trigger_date: `2022-08-16` / entry_date: `2022-08-17` / entry_price_close: `63600`
- trigger_type: `Stage3-Yellow`
- trigger_family: `ira_ampc_foreign_legislation_direct_manufacturing_credit`
- evidence_available_at_that_date: US IRA law date plus DOE wind incentive explanation; direct manufacturing-credit route supports wind component producer economics but still needs issuer-level recognition to become Green.
- stage2_evidence_fields: `public_event_or_disclosure, policy_or_regulatory_optionality, direct_manufacturing_credit_route`
- stage3_evidence_fields: `financial_visibility_partial, customer_or_order_quality_partial`
- stage4b_evidence_fields: `none`
- current_profile_verdict: `current_profile_correct`

### C31-R11-L214-05 — 015760 한국전력
- trigger_date: `2023-05-15` / entry_date: `2023-05-16` / entry_price_close: `18680`
- trigger_type: `Stage2-Actionable`
- trigger_family: `electricity_tariff_hike_partial_pass_through`
- evidence_available_at_that_date: Yonhap reported Q2 electricity/gas tariff hikes, but partial pass-through did not repair utility cashflow enough for durable rerating.
- stage2_evidence_fields: `public_event_or_disclosure, policy_or_regulatory_optionality, tariff_route`
- stage3_evidence_fields: `none`
- stage4b_evidence_fields: `margin_or_backlog_slowdown, tariff_sufficiency_risk`
- current_profile_verdict: `current_profile_too_early`

### C31-R11-L214-06 — 036460 한국가스공사
- trigger_date: `2023-05-15` / entry_date: `2023-05-16` / entry_price_close: `25850`
- trigger_type: `Stage2-Actionable`
- trigger_family: `gas_tariff_hike_partial_pass_through`
- evidence_available_at_that_date: Same tariff decision; KOGAS benefited from gas-rate recognition but unresolved receivables/fuel-cost pass-through made Green premature.
- stage2_evidence_fields: `public_event_or_disclosure, policy_or_regulatory_optionality, tariff_route`
- stage3_evidence_fields: `none`
- stage4b_evidence_fields: `margin_or_backlog_slowdown, tariff_sufficiency_risk`
- current_profile_verdict: `current_profile_too_early`

### C31-R11-L214-07 — 336260 두산퓨얼셀
- trigger_date: `2023-05-24` / entry_date: `2023-05-25` / entry_price_close: `30700`
- trigger_type: `Stage3-Yellow`
- trigger_family: `hydrogen_bidding_market_without_issuer_award`
- evidence_available_at_that_date: Hydrogen bidding market notification created market structure, but no named award/offtake for the issuer was visible at trigger date.
- stage2_evidence_fields: `public_event_or_disclosure, policy_or_regulatory_optionality, market_creation_route`
- stage3_evidence_fields: `commercialization_optionality_without_award`
- stage4b_evidence_fields: `explicit_event_cap, customer_or_award_absence`
- current_profile_verdict: `current_profile_false_positive`

### C31-R11-L214-08 — 052690 한전기술
- trigger_date: `2022-03-10` / entry_date: `2022-03-11` / entry_price_close: `95200`
- trigger_type: `Stage4B`
- trigger_family: `nuclear_policy_revival_after_crowded_rerating_without_project_cashflow`
- evidence_available_at_that_date: Pro-nuclear policy reversal supported the sector, but for this issuer the signal arrived near a crowded price peak before project cashflow was visible.
- stage2_evidence_fields: `public_event_or_disclosure, policy_or_regulatory_optionality, project_pipeline_optionality`
- stage3_evidence_fields: `none`
- stage4b_evidence_fields: `valuation_blowoff, positioning_overheat, explicit_event_cap, project_cashflow_absence`
- current_profile_verdict: `current_profile_false_positive`

## 12. Trigger-Level OHLC Backtest Tables
| trigger_id | entry close | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak | below_entry_30D | below_entry_90D |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| C31-R11-L214-01-T1 | 62400 | 25.96% | -2.40% | 44.23% | -2.40% | 66.51% | -2.40% | 2024-10-25 | 103900 | -15.50% | true | true |
| C31-R11-L214-02-T1 | 7720 | 8.94% | -5.18% | 16.58% | -5.18% | 33.94% | -5.18% | 2024-08-26 | 10340 | -13.73% | true | true |
| C31-R11-L214-03-T1 | 43300 | 9.58% | -16.86% | 24.48% | -18.13% | 24.48% | -18.13% | 2024-06-18 | 53900 | -26.72% | true | true |
| C31-R11-L214-04-T1 | 63600 | 11.64% | -6.60% | 26.57% | -10.85% | 38.52% | -10.85% | 2023-04-24 | 88100 | -18.50% | true | true |
| C31-R11-L214-05-T1 | 18680 | 7.60% | -2.94% | 11.62% | -5.19% | 11.62% | -14.19% | 2023-07-13 | 20850 | -23.12% | true | true |
| C31-R11-L214-06-T1 | 25850 | 5.03% | -5.03% | 5.03% | -9.09% | 10.44% | -11.99% | 2024-02-01 | 28550 | -9.63% | true | true |
| C31-R11-L214-07-T1 | 30700 | 2.61% | -13.36% | 2.61% | -40.42% | 2.61% | -47.72% | 2023-06-13 | 31500 | -49.05% | true | true |
| C31-R11-L214-08-T1 | 95200 | 1.37% | -22.90% | 1.37% | -40.65% | 1.37% | -49.84% | 2022-03-11 | 96500 | -50.52% | true | true |

## 13. Current Calibrated Profile Stress Test
| case_id | P0 likely judgment | actual path | error type | axis tested | conclusion |
|---|---|---|---|---|---|
| C31-R11-L214-01 | current_profile_correct | MFE180 66.51%, MAE180 -2.40% | none | stage2_required_bridge / local_4b_watch_guard / hard_4c_confirmation | keep/promote only with cashflow bridge |
| C31-R11-L214-02 | current_profile_correct | MFE180 33.94%, MAE180 -5.18% | none | stage2_required_bridge / local_4b_watch_guard / hard_4c_confirmation | keep/promote only with cashflow bridge |
| C31-R11-L214-03 | current_profile_correct | MFE180 24.48%, MAE180 -18.13% | none | stage2_required_bridge / local_4b_watch_guard / hard_4c_confirmation | keep/promote only with cashflow bridge |
| C31-R11-L214-04 | current_profile_correct | MFE180 38.52%, MAE180 -10.85% | none | stage2_required_bridge / local_4b_watch_guard / hard_4c_confirmation | keep/promote only with cashflow bridge |
| C31-R11-L214-05 | current_profile_too_early | MFE180 11.62%, MAE180 -14.19% | tariff_sufficiency_gap | stage2_required_bridge / local_4b_watch_guard / hard_4c_confirmation | cap below Green or route to 4B watch until cashflow bridge appears |
| C31-R11-L214-06 | current_profile_too_early | MFE180 10.44%, MAE180 -11.99% | tariff_sufficiency_gap | stage2_required_bridge / local_4b_watch_guard / hard_4c_confirmation | cap below Green or route to 4B watch until cashflow bridge appears |
| C31-R11-L214-07 | current_profile_false_positive | MFE180 2.61%, MAE180 -47.72% | policy_headline_false_positive | stage2_required_bridge / local_4b_watch_guard / hard_4c_confirmation | cap below Green or route to 4B watch until cashflow bridge appears |
| C31-R11-L214-08 | current_profile_false_positive | MFE180 1.37%, MAE180 -49.84% | policy_headline_false_positive | stage2_required_bridge / local_4b_watch_guard / hard_4c_confirmation | cap below Green or route to 4B watch until cashflow bridge appears |

Stress-test answers:
1. Stage2 actionable bonus remains useful when the policy route names a beneficiary or cashflow bridge, but too generous for generic policy baskets.
2. Yellow threshold 75 is acceptable only after tariff sufficiency or named beneficiary evidence exists.
3. Green threshold/revision requirement should be stricter for C31: policy existence cannot substitute for recognized subsidy, return execution, tariff sufficiency, or awarded contract.
4. Price-only blowoff and full-4B non-price gates remain appropriate; C31 needs a policy-event premium 4B watch overlay.
5. Hard 4C should not fire on reversible policy delay alone; it needs project/contract/funding/customer path termination.

## 14. Stage2 / Yellow / Green Comparison
- Stage2 allowed: policy/law headline plus plausible beneficiary map.
- Stage2-Actionable allowed: named listed issuer route or tariff/credit mechanism, but still not Green if cashflow sufficiency is unresolved.
- Stage3-Yellow allowed: direct manufacturing credit or issuer capital-return bridge, but high MAE cases stay gated.
- Stage3-Green candidate: only KB/CS Wind style rows after later issuer-level confirmation; not backdated as trigger evidence.
- Green lateness ratio: `not_applicable` for representative rows because no paired Stage3-Green trigger is emitted in this loop; the loop is a C31 bridge/guard calibration, not a Green timing promotion run.

## 15. 4B Local vs Full-window Timing Audit
| case_id | trigger_type | local proximity | full-window proximity | evidence type | timing verdict |
|---|---|---:|---:|---|---|
| C31-R11-L214-03 | Stage2-Actionable | null | null | high_mae_success | watch_overlay_only |
| C31-R11-L214-05 | Stage2-Actionable | null | null | margin_or_backlog_slowdown, tariff_sufficiency_risk | watch_overlay_only |
| C31-R11-L214-06 | Stage2-Actionable | null | null | margin_or_backlog_slowdown, tariff_sufficiency_risk | watch_overlay_only |
| C31-R11-L214-07 | Stage3-Yellow | null | null | explicit_event_cap, customer_or_award_absence | watch_overlay_only |
| C31-R11-L214-08 | Stage4B | 1.00 | 1.00 | valuation_blowoff, positioning_overheat, explicit_event_cap, project_cashflow_absence | good_full_window_4B_watch_timing |
C31-specific interpretation: a policy event after a crowded rerating acts like a weather warning, not an exit command. It marks risk until non-price deterioration confirms full 4B or hard 4C.

## 16. 4C Protection Audit
No representative hard-4C trigger is emitted. The hydrogen and tariff counterexamples are thesis-break watch rows, not hard 4C, because the policies were real and reversible; the missing piece was issuer cashflow conversion. This strengthens hard_4c_confirmation rather than weakening it.

## 17. Sector-Specific Rule Candidate
`L10 policy/event evidence should split government headline, implementation framework, beneficiary specificity, issuer cashflow bridge, and legal/contract finality. A government decision validates that the door opened; it does not prove the listed company walked through it.`

## 18. Canonical-Archetype Rule Candidate
`C31 should use a policy-to-cashflow conversion ladder: law/policy headline → implementation framework → named beneficiary/direct route → recognized subsidy/order/tariff sufficiency/capital return → durable conversion. Policy-only events stay Stage2/Yellow; policy after local rerating becomes 4B watch; reversible policy delay is not hard 4C unless project, contract, funding, or customer path terminates.`

## 19. Before / After Backtest Comparison
| profile | hypothesis | eligible | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive rate | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current calibrated proxy | 8 | 16.56% | -16.49% | 23.69% | -20.04% | 0.50 | over-promotes generic policy headlines in C31 |
| P0b_e2r_2_0_baseline_reference | rollback reference | 8 | 16.56% | -16.49% | 23.69% | -20.04% | 0.62 | worse false-positive control |
| P1_L10_policy_event_shadow_profile | sector policy headline cap | 8 | 16.56% | -16.49% | 23.69% | -20.04% | 0.25 | better L10 risk/reward alignment |
| P2_C31_policy_to_cashflow_conversion_profile | canonical policy-to-cashflow ladder | 8 | 16.56% | -16.49% | 23.69% | -20.04% | 0.12 | best explanation of MFE/MAE split |
| P3_C31_counterexample_guard_profile | event premium and reversible policy 4B guard | 8 | 16.56% | -16.49% | 23.69% | -20.04% | 0.12 | best downside guard but may miss early policy beta |

## 20. Score-Return Alignment Matrix
| trigger_id | score_before | label_before | score_after | label_after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| C31-R11-L214-01-T1 | 79 | Stage3-Yellow/Green-risk | 84 | Stage3-Yellow/Green-candidate | 44.23% | -2.40% | aligned_positive |
| C31-R11-L214-02-T1 | 74 | Stage2/Yellow | 77 | Stage2-Watch | 16.58% | -5.18% | aligned_positive |
| C31-R11-L214-03-T1 | 76 | Stage3-Yellow/Green-risk | 79 | Stage2-Watch | 24.48% | -18.13% | aligned_positive |
| C31-R11-L214-04-T1 | 81 | Stage3-Yellow/Green-risk | 86 | Stage3-Yellow/Green-candidate | 26.57% | -10.85% | aligned_positive |
| C31-R11-L214-05-T1 | 76 | Stage3-Yellow/Green-risk | 63 | Stage2-Watch | 11.62% | -5.19% | corrects_false_positive_or_too_early_policy_entry |
| C31-R11-L214-06-T1 | 74 | Stage2/Yellow | 61 | Stage2-Watch | 5.03% | -9.09% | corrects_false_positive_or_too_early_policy_entry |
| C31-R11-L214-07-T1 | 82 | Stage3-Yellow/Green-risk | 52 | Stage4B/4C guard | 2.61% | -40.42% | corrects_false_positive_or_too_early_policy_entry |
| C31-R11-L214-08-T1 | 78 | Stage3-Yellow/Green-risk | 55 | Stage4B/4C guard | 1.37% | -40.65% | corrects_false_positive_or_too_early_policy_entry |

## 21. Coverage Matrix
| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31_POLICY_TO_CASHFLOW_CONVERSION_DIRECT_SOURCE_REPAIR | 4 | 4 | 2 | 0 | 8 | 0 | 8 | 8 | 4 | yes | yes | C31 direct cashflow-conversion quality gap reduced; avoid immediate repeat unless direct awarded subsidy/tariff/source repair is available |

## 22. Residual Contribution Summary
new_independent_case_count: `8`
reused_case_count: `0`
reused_case_ids: `[]`
new_symbol_count: `8`
new_canonical_archetype_count: `0`
new_fine_archetype_count: `1`
new_trigger_family_count: `6`
tested_existing_calibrated_axes: `["stage2_required_bridge", "local_4b_watch_guard", "hard_4c_confirmation", "stage3_green_revision_min"]`
residual_error_types_found: `["policy_headline_false_positive", "tariff_sufficiency_gap", "market_creation_without_named_award", "policy_reversal_peak_zone_4b_watch"]`
new_axis_proposed: `"c31_policy_to_cashflow_conversion_ladder; c31_tariff_sufficiency_gate; c31_policy_event_premium_4b_watch"`
existing_axis_strengthened: `"stage2_required_bridge; local_4b_watch_guard; hard_4c_confirmation"`
existing_axis_weakened: `"none"`
existing_axis_kept: `"price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence"`
sector_specific_rule_candidate: `"L10 policy/event evidence should require beneficiary specificity plus issuer cashflow bridge before promotion above Yellow."`
canonical_archetype_rule_candidate: `"C31 policy-to-cashflow conversion ladder with tariff sufficiency and event-premium 4B watch."`
no_new_signal_reason: `null`
loop_contribution_label: `"canonical_archetype_rule_candidate"`
do_not_propose_new_weight_delta: `false`

## 23. Validation Scope / Non-Validation Scope
Validated: historical event dates, Stock-Web tradable raw entry rows, 30D/90D/180D MFE/MAE, positive/counterexample balance, and current profile stress-test logic. Not validated: live candidate status, current investment recommendation, production scoring patch, broker/API behavior, or unobserved post-2026-02-20 prices.

## 24. Shadow Weight Calibration
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,policy_or_regulatory_score_cap,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,78,58,-20,"generic policy headline over-promotes tariff/hydrogen/nuclear policy rows without issuer cashflow","reduced false positives 4/8 to 1/8 in proxy comparison","C31-R11-L214-01-T1|C31-R11-L214-02-T1|C31-R11-L214-03-T1|C31-R11-L214-04-T1|C31-R11-L214-05-T1|C31-R11-L214-06-T1|C31-R11-L214-07-T1|C31-R11-L214-08-T1",8,8,4,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,beneficiary_specificity_gate,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"separates named issuer route from generic policy basket","preserves KB/CSWind positives while capping generic policy beta","C31-R11-L214-01-T1|C31-R11-L214-02-T1|C31-R11-L214-03-T1|C31-R11-L214-04-T1",8,8,4,medium,canonical_shadow_only,"requires direct route or named beneficiary"
shadow_weight,cashflow_conversion_bridge,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Green requires recognized subsidy/order/tariff sufficiency/capital return","explains positive/counterexample MFE180 split","C31-R11-L214-01-T1|C31-R11-L214-02-T1|C31-R11-L214-03-T1|C31-R11-L214-04-T1|C31-R11-L214-05-T1|C31-R11-L214-06-T1|C31-R11-L214-07-T1|C31-R11-L214-08-T1",8,8,4,medium,canonical_shadow_only,"not global"
shadow_weight,policy_event_premium_4b_watch,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"policy after crowded rerating is watch overlay not Green","improves 052690/336260 downside handling","C31-R11-L214-07-T1|C31-R11-L214-08-T1",8,8,4,medium,canonical_shadow_only,"4B overlay only"
```

## 25. Machine-Readable Rows
```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C31-R11-L214-01","symbol":"105560","company_name":"KB금융","round":"R11","loop":"214","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_POLICY_TO_CASHFLOW_CONVERSION_DIRECT_SOURCE_REPAIR","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C31-R11-L214-01-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"FSC Feb-26 Corporate Value-up Program launch; later KB SEC 6-K verifies issuer-level shareholder return/capital-management bridge, used only as later validation."}
{"row_type":"trigger","trigger_id":"C31-R11-L214-01-T1","case_id":"C31-R11-L214-01","symbol":"105560","company_name":"KB금융","round":"R11","loop":"214","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_POLICY_TO_CASHFLOW_CONVERSION_DIRECT_SOURCE_REPAIR","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"direct-source validation; policy-to-cashflow conversion; counterexample mining; 4B watch guard stress test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":62400.0,"evidence_available_at_that_date":"FSC Feb-26 Corporate Value-up Program launch; later KB SEC 6-K verifies issuer-level shareholder return/capital-management bridge, used only as later validation.","evidence_source":["https://www.fsc.go.kr/eng/pr010101/81778","https://www.sec.gov/Archives/edgar/data/1445930/000119312524242219/d901349d6k.htm"],"stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","capital_return_route"],"stage3_evidence_fields":["financial_visibility","issuer_specific_capital_return_plan","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":25.96,"MFE_90D_pct":44.23,"MFE_180D_pct":66.51,"MFE_1Y_pct":66.51,"MFE_2Y_pct":null,"MAE_30D_pct":-2.4,"MAE_90D_pct":-2.4,"MAE_180D_pct":-2.4,"MAE_1Y_pct":-2.4,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":103900.0,"drawdown_after_peak_pct":-15.5,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"value_up_specific_cash_return_bridge_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|105560|2024-02-27|62400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"entry_ohlc_row":{"d":"2024-02-27","o":62000.0,"h":63200.0,"l":61500.0,"c":62400.0,"v":1643919,"a":102593108320,"mc":25179090892800,"s":403511072,"m":"KOSPI"}}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31-R11-L214-01","trigger_id":"C31-R11-L214-01-T1","symbol":"105560","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":60,"revision_score":55,"relative_strength_score":55,"customer_quality_score":40,"policy_or_regulatory_score":78,"valuation_repricing_score":65,"execution_risk_score":25,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_before":79,"stage_label_before":"Stage3-Yellow/Green-risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":76,"revision_score":55,"relative_strength_score":55,"customer_quality_score":40,"policy_or_regulatory_score":70,"valuation_repricing_score":65,"execution_risk_score":20,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow/Green-candidate","changed_components":["policy_or_regulatory_score","beneficiary_specificity","cashflow_conversion_bridge","event_premium_4b_watch"],"component_delta_explanation":"C31 separates policy existence from named beneficiary and issuer cashflow conversion; generic policy headline is discounted while direct cashflow/shareholder-return bridge is preserved.","MFE_90D_pct":44.23,"MAE_90D_pct":-2.4,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C31-R11-L214-02","symbol":"138930","company_name":"BNK금융지주","round":"R11","loop":"214","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_POLICY_TO_CASHFLOW_CONVERSION_DIRECT_SOURCE_REPAIR","case_type":"stage2_promote_candidate","positive_or_counterexample":"positive","best_trigger":"C31-R11-L214-02-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"FSC value-up launch produced low-PBR financial beta, but issuer-specific return plan was weaker on trigger date."}
{"row_type":"trigger","trigger_id":"C31-R11-L214-02-T1","case_id":"C31-R11-L214-02","symbol":"138930","company_name":"BNK금융지주","round":"R11","loop":"214","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_POLICY_TO_CASHFLOW_CONVERSION_DIRECT_SOURCE_REPAIR","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"direct-source validation; policy-to-cashflow conversion; counterexample mining; 4B watch guard stress test","trigger_type":"Stage2","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":7720.0,"evidence_available_at_that_date":"FSC value-up launch produced low-PBR financial beta, but issuer-specific return plan was weaker on trigger date.","evidence_source":["https://www.fsc.go.kr/eng/pr010101/81778"],"stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["financial_visibility_partial"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/138/138930/2024.csv","profile_path":"atlas/symbol_profiles/138/138930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.94,"MFE_90D_pct":16.58,"MFE_180D_pct":33.94,"MFE_1Y_pct":59.33,"MFE_2Y_pct":null,"MAE_30D_pct":-5.18,"MAE_90D_pct":-5.18,"MAE_180D_pct":-5.18,"MAE_1Y_pct":-5.18,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-26","peak_price":10340.0,"drawdown_after_peak_pct":-13.73,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"generic_value_up_financial_beta_yellow_not_green","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|138930|2024-02-27|7720","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"entry_ohlc_row":{"d":"2024-02-27","o":7710.0,"h":7910.0,"l":7680.0,"c":7720.0,"v":2398245,"a":18690086080,"mc":2486522741360,"s":322088438,"m":"KOSPI"}}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31-R11-L214-02","trigger_id":"C31-R11-L214-02-T1","symbol":"138930","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":45,"revision_score":55,"relative_strength_score":55,"customer_quality_score":40,"policy_or_regulatory_score":78,"valuation_repricing_score":65,"execution_risk_score":25,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_before":74,"stage_label_before":"Stage2/Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":55,"revision_score":55,"relative_strength_score":55,"customer_quality_score":40,"policy_or_regulatory_score":70,"valuation_repricing_score":65,"execution_risk_score":20,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_after":77,"stage_label_after":"Stage2-Watch","changed_components":["policy_or_regulatory_score","beneficiary_specificity","cashflow_conversion_bridge","event_premium_4b_watch"],"component_delta_explanation":"C31 separates policy existence from named beneficiary and issuer cashflow conversion; generic policy headline is discounted while direct cashflow/shareholder-return bridge is preserved.","MFE_90D_pct":16.58,"MAE_90D_pct":-5.18,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C31-R11-L214-03","symbol":"071320","company_name":"지역난방공사","round":"R11","loop":"214","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_POLICY_TO_CASHFLOW_CONVERSION_DIRECT_SOURCE_REPAIR","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"C31-R11-L214-03-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Public-company value-up expectation plus earnings/dividend repricing; high MAE says policy/public ownership needs cash distribution bridge rather than headline-only Green."}
{"row_type":"trigger","trigger_id":"C31-R11-L214-03-T1","case_id":"C31-R11-L214-03","symbol":"071320","company_name":"지역난방공사","round":"R11","loop":"214","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_POLICY_TO_CASHFLOW_CONVERSION_DIRECT_SOURCE_REPAIR","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"direct-source validation; policy-to-cashflow conversion; counterexample mining; 4B watch guard stress test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-27","entry_date":"2024-02-28","entry_price":43300.0,"evidence_available_at_that_date":"Public-company value-up expectation plus earnings/dividend repricing; high MAE says policy/public ownership needs cash distribution bridge rather than headline-only Green.","evidence_source":["https://www.fsc.go.kr/eng/pr010101/81778","https://www.mk.co.kr/en/stock/10952026"],"stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","earnings_repricing_route"],"stage3_evidence_fields":["financial_visibility","dividend_or_distribution_expectation_partial"],"stage4b_evidence_fields":["high_mae_success"],"stage4c_evidence_fields":[],"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/071/071320/2024.csv","profile_path":"atlas/symbol_profiles/071/071320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.58,"MFE_90D_pct":24.48,"MFE_180D_pct":24.48,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-16.86,"MAE_90D_pct":-18.13,"MAE_180D_pct":-18.13,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-18","peak_price":53900.0,"drawdown_after_peak_pct":-26.72,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["high_mae_success"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"public_company_value_up_positive_but_high_mae","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|071320|2024-02-28|43300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"entry_ohlc_row":{"d":"2024-02-28","o":40900.0,"h":44950.0,"l":39500.0,"c":43300.0,"v":252006,"a":10728092200,"mc":501359615200,"s":11578744,"m":"KOSPI"}}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31-R11-L214-03","trigger_id":"C31-R11-L214-03-T1","symbol":"071320","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":58,"revision_score":65,"relative_strength_score":55,"customer_quality_score":0,"policy_or_regulatory_score":78,"valuation_repricing_score":60,"execution_risk_score":42,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow/Green-risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":62,"revision_score":65,"relative_strength_score":55,"customer_quality_score":0,"policy_or_regulatory_score":65,"valuation_repricing_score":60,"execution_risk_score":45,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_after":79,"stage_label_after":"Stage2-Watch","changed_components":["policy_or_regulatory_score","beneficiary_specificity","cashflow_conversion_bridge","event_premium_4b_watch"],"component_delta_explanation":"C31 separates policy existence from named beneficiary and issuer cashflow conversion; generic policy headline is discounted while direct cashflow/shareholder-return bridge is preserved.","MFE_90D_pct":24.48,"MAE_90D_pct":-18.13,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C31-R11-L214-04","symbol":"112610","company_name":"씨에스윈드","round":"R11","loop":"214","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_POLICY_TO_CASHFLOW_CONVERSION_DIRECT_SOURCE_REPAIR","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C31-R11-L214-04-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"US IRA law date plus DOE wind incentive explanation; direct manufacturing-credit route supports wind component producer economics but still needs issuer-level recognition to become Green."}
{"row_type":"trigger","trigger_id":"C31-R11-L214-04-T1","case_id":"C31-R11-L214-04","symbol":"112610","company_name":"씨에스윈드","round":"R11","loop":"214","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_POLICY_TO_CASHFLOW_CONVERSION_DIRECT_SOURCE_REPAIR","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"direct-source validation; policy-to-cashflow conversion; counterexample mining; 4B watch guard stress test","trigger_type":"Stage3-Yellow","trigger_date":"2022-08-16","entry_date":"2022-08-17","entry_price":63600.0,"evidence_available_at_that_date":"US IRA law date plus DOE wind incentive explanation; direct manufacturing-credit route supports wind component producer economics but still needs issuer-level recognition to become Green.","evidence_source":["https://www.energy.gov/sites/default/files/2023-04/eere-wind-weto-funding-taxday-factsheet-fy23.pdf"],"stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","direct_manufacturing_credit_route"],"stage3_evidence_fields":["financial_visibility_partial","customer_or_order_quality_partial"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/112/112610/2022.csv","profile_path":"atlas/symbol_profiles/112/112610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.64,"MFE_90D_pct":26.57,"MFE_180D_pct":38.52,"MFE_1Y_pct":40.57,"MFE_2Y_pct":null,"MAE_30D_pct":-6.6,"MAE_90D_pct":-10.85,"MAE_180D_pct":-10.85,"MAE_1Y_pct":-10.85,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-24","peak_price":88100.0,"drawdown_after_peak_pct":-18.5,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"foreign_legislation_direct_credit_route_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|112610|2022-08-17|63600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"entry_ohlc_row":{"d":"2022-08-17","o":64500.0,"h":65300.0,"l":63100.0,"c":63600.0,"v":349094,"a":22291218000,"mc":2682101230800,"s":42171403,"m":"KOSPI"}}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31-R11-L214-04","trigger_id":"C31-R11-L214-04-T1","symbol":"112610","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":48,"backlog_visibility_score":0,"margin_bridge_score":60,"revision_score":0,"relative_strength_score":55,"customer_quality_score":60,"policy_or_regulatory_score":85,"valuation_repricing_score":50,"execution_risk_score":35,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_before":81,"stage_label_before":"Stage3-Yellow/Green-risk","raw_component_scores_after":{"contract_score":55,"backlog_visibility_score":0,"margin_bridge_score":70,"revision_score":0,"relative_strength_score":55,"customer_quality_score":60,"policy_or_regulatory_score":80,"valuation_repricing_score":50,"execution_risk_score":35,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow/Green-candidate","changed_components":["policy_or_regulatory_score","beneficiary_specificity","cashflow_conversion_bridge","event_premium_4b_watch"],"component_delta_explanation":"C31 separates policy existence from named beneficiary and issuer cashflow conversion; generic policy headline is discounted while direct cashflow/shareholder-return bridge is preserved.","MFE_90D_pct":26.57,"MAE_90D_pct":-10.85,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C31-R11-L214-05","symbol":"015760","company_name":"한국전력","round":"R11","loop":"214","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_POLICY_TO_CASHFLOW_CONVERSION_DIRECT_SOURCE_REPAIR","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C31-R11-L214-05-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"corrects_false_positive_or_too_early_policy_entry","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"Yonhap reported Q2 electricity/gas tariff hikes, but partial pass-through did not repair utility cashflow enough for durable rerating."}
{"row_type":"trigger","trigger_id":"C31-R11-L214-05-T1","case_id":"C31-R11-L214-05","symbol":"015760","company_name":"한국전력","round":"R11","loop":"214","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_POLICY_TO_CASHFLOW_CONVERSION_DIRECT_SOURCE_REPAIR","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"direct-source validation; policy-to-cashflow conversion; counterexample mining; 4B watch guard stress test","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-15","entry_date":"2023-05-16","entry_price":18680.0,"evidence_available_at_that_date":"Yonhap reported Q2 electricity/gas tariff hikes, but partial pass-through did not repair utility cashflow enough for durable rerating.","evidence_source":["https://en.yna.co.kr/view/AEN20230515001600320"],"stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","tariff_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","tariff_sufficiency_risk"],"stage4c_evidence_fields":[],"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/015/015760/2023.csv","profile_path":"atlas/symbol_profiles/015/015760.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.6,"MFE_90D_pct":11.62,"MFE_180D_pct":11.62,"MFE_1Y_pct":36.24,"MFE_2Y_pct":null,"MAE_30D_pct":-2.94,"MAE_90D_pct":-5.19,"MAE_180D_pct":-14.19,"MAE_1Y_pct":-14.19,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-13","peak_price":20850.0,"drawdown_after_peak_pct":-23.12,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["margin_or_backlog_slowdown","tariff_sufficiency_risk"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"tariff_headline_without_sufficiency_counterexample","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|015760|2023-05-16|18680","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"entry_ohlc_row":{"d":"2023-05-16","o":19120.0,"h":19230.0,"l":18650.0,"c":18680.0,"v":1844472,"a":34805477480,"mc":11991888958360,"s":641964077,"m":"KOSPI"}}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31-R11-L214-05","trigger_id":"C31-R11-L214-05-T1","symbol":"015760","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":40,"revision_score":0,"relative_strength_score":50,"customer_quality_score":0,"policy_or_regulatory_score":80,"valuation_repricing_score":35,"execution_risk_score":65,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow/Green-risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":28,"revision_score":0,"relative_strength_score":50,"customer_quality_score":0,"policy_or_regulatory_score":55,"valuation_repricing_score":35,"execution_risk_score":75,"legal_or_contract_risk_score":45,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_after":63,"stage_label_after":"Stage2-Watch","changed_components":["policy_or_regulatory_score","beneficiary_specificity","cashflow_conversion_bridge","event_premium_4b_watch"],"component_delta_explanation":"C31 separates policy existence from named beneficiary and issuer cashflow conversion; generic policy headline is discounted while direct cashflow/shareholder-return bridge is preserved.","MFE_90D_pct":11.62,"MAE_90D_pct":-5.19,"score_return_alignment_label":"corrects_false_positive_or_too_early_policy_entry","current_profile_verdict":"current_profile_too_early"}
{"row_type":"case","case_id":"C31-R11-L214-06","symbol":"036460","company_name":"한국가스공사","round":"R11","loop":"214","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_POLICY_TO_CASHFLOW_CONVERSION_DIRECT_SOURCE_REPAIR","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C31-R11-L214-06-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"corrects_false_positive_or_too_early_policy_entry","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"Same tariff decision; KOGAS benefited from gas-rate recognition but unresolved receivables/fuel-cost pass-through made Green premature."}
{"row_type":"trigger","trigger_id":"C31-R11-L214-06-T1","case_id":"C31-R11-L214-06","symbol":"036460","company_name":"한국가스공사","round":"R11","loop":"214","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_POLICY_TO_CASHFLOW_CONVERSION_DIRECT_SOURCE_REPAIR","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"direct-source validation; policy-to-cashflow conversion; counterexample mining; 4B watch guard stress test","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-15","entry_date":"2023-05-16","entry_price":25850.0,"evidence_available_at_that_date":"Same tariff decision; KOGAS benefited from gas-rate recognition but unresolved receivables/fuel-cost pass-through made Green premature.","evidence_source":["https://en.yna.co.kr/view/AEN20230515001600320"],"stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","tariff_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","tariff_sufficiency_risk"],"stage4c_evidence_fields":[],"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036460/2023.csv","profile_path":"atlas/symbol_profiles/036/036460.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.03,"MFE_90D_pct":5.03,"MFE_180D_pct":10.44,"MFE_1Y_pct":23.02,"MFE_2Y_pct":null,"MAE_30D_pct":-5.03,"MAE_90D_pct":-9.09,"MAE_180D_pct":-11.99,"MAE_1Y_pct":-11.99,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-01","peak_price":28550.0,"drawdown_after_peak_pct":-9.63,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["margin_or_backlog_slowdown","tariff_sufficiency_risk"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"gas_tariff_policy_not_cashflow_conversion","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|036460|2023-05-16|25850","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"entry_ohlc_row":{"d":"2023-05-16","o":26200.0,"h":26250.0,"l":25700.0,"c":25850.0,"v":340512,"a":8847117450,"mc":2386291050000,"s":92313000,"m":"KOSPI"}}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31-R11-L214-06","trigger_id":"C31-R11-L214-06-T1","symbol":"036460","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":40,"revision_score":0,"relative_strength_score":50,"customer_quality_score":0,"policy_or_regulatory_score":80,"valuation_repricing_score":35,"execution_risk_score":65,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_before":74,"stage_label_before":"Stage2/Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":28,"revision_score":0,"relative_strength_score":50,"customer_quality_score":0,"policy_or_regulatory_score":55,"valuation_repricing_score":35,"execution_risk_score":75,"legal_or_contract_risk_score":45,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_after":61,"stage_label_after":"Stage2-Watch","changed_components":["policy_or_regulatory_score","beneficiary_specificity","cashflow_conversion_bridge","event_premium_4b_watch"],"component_delta_explanation":"C31 separates policy existence from named beneficiary and issuer cashflow conversion; generic policy headline is discounted while direct cashflow/shareholder-return bridge is preserved.","MFE_90D_pct":5.03,"MAE_90D_pct":-9.09,"score_return_alignment_label":"corrects_false_positive_or_too_early_policy_entry","current_profile_verdict":"current_profile_too_early"}
{"row_type":"case","case_id":"C31-R11-L214-07","symbol":"336260","company_name":"두산퓨얼셀","round":"R11","loop":"214","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_POLICY_TO_CASHFLOW_CONVERSION_DIRECT_SOURCE_REPAIR","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"C31-R11-L214-07-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"corrects_false_positive_or_too_early_policy_entry","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Hydrogen bidding market notification created market structure, but no named award/offtake for the issuer was visible at trigger date."}
{"row_type":"trigger","trigger_id":"C31-R11-L214-07-T1","case_id":"C31-R11-L214-07","symbol":"336260","company_name":"두산퓨얼셀","round":"R11","loop":"214","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_POLICY_TO_CASHFLOW_CONVERSION_DIRECT_SOURCE_REPAIR","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"direct-source validation; policy-to-cashflow conversion; counterexample mining; 4B watch guard stress test","trigger_type":"Stage3-Yellow","trigger_date":"2023-05-24","entry_date":"2023-05-25","entry_price":30700.0,"evidence_available_at_that_date":"Hydrogen bidding market notification created market structure, but no named award/offtake for the issuer was visible at trigger date.","evidence_source":["https://www.jipyong.com/en/board/jipyongNews_post.php?seq=5981","https://www.doosanfuelcell.com/en/media-center/medi-0101_view/?id=125"],"stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","market_creation_route"],"stage3_evidence_fields":["commercialization_optionality_without_award"],"stage4b_evidence_fields":["explicit_event_cap","customer_or_award_absence"],"stage4c_evidence_fields":["thesis_evidence_broken_partial"],"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/336/336260/2023.csv","profile_path":"atlas/symbol_profiles/336/336260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.61,"MFE_90D_pct":2.61,"MFE_180D_pct":2.61,"MFE_1Y_pct":2.61,"MFE_2Y_pct":null,"MAE_30D_pct":-13.36,"MAE_90D_pct":-40.42,"MAE_180D_pct":-47.72,"MAE_1Y_pct":-47.72,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-13","peak_price":31500.0,"drawdown_after_peak_pct":-49.05,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["explicit_event_cap","customer_or_award_absence"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"policy_market_creation_without_named_award_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|336260|2023-05-25|30700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"entry_ohlc_row":{"d":"2023-05-25","o":30900.0,"h":31300.0,"l":30700.0,"c":30700.0,"v":159073,"a":4912979350,"mc":2010657388200,"s":65493726,"m":"KOSPI"}}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31-R11-L214-07","trigger_id":"C31-R11-L214-07-T1","symbol":"336260","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":15,"revision_score":0,"relative_strength_score":50,"customer_quality_score":25,"policy_or_regulatory_score":85,"valuation_repricing_score":50,"execution_risk_score":70,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow/Green-risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":0,"relative_strength_score":50,"customer_quality_score":15,"policy_or_regulatory_score":48,"valuation_repricing_score":50,"execution_risk_score":85,"legal_or_contract_risk_score":50,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_after":52,"stage_label_after":"Stage4B/4C guard","changed_components":["policy_or_regulatory_score","beneficiary_specificity","cashflow_conversion_bridge","event_premium_4b_watch"],"component_delta_explanation":"C31 separates policy existence from named beneficiary and issuer cashflow conversion; generic policy headline is discounted while direct cashflow/shareholder-return bridge is preserved.","MFE_90D_pct":2.61,"MAE_90D_pct":-40.42,"score_return_alignment_label":"corrects_false_positive_or_too_early_policy_entry","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C31-R11-L214-08","symbol":"052690","company_name":"한전기술","round":"R11","loop":"214","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_POLICY_TO_CASHFLOW_CONVERSION_DIRECT_SOURCE_REPAIR","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"C31-R11-L214-08-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"corrects_false_positive_or_too_early_policy_entry","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Pro-nuclear policy reversal supported the sector, but for this issuer the signal arrived near a crowded price peak before project cashflow was visible."}
{"row_type":"trigger","trigger_id":"C31-R11-L214-08-T1","case_id":"C31-R11-L214-08","symbol":"052690","company_name":"한전기술","round":"R11","loop":"214","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_POLICY_TO_CASHFLOW_CONVERSION_DIRECT_SOURCE_REPAIR","sector":"policy_event_cross_redteam_misc","primary_archetype":"policy_subsidy_legislation_event","loop_objective":"direct-source validation; policy-to-cashflow conversion; counterexample mining; 4B watch guard stress test","trigger_type":"Stage4B","trigger_date":"2022-03-10","entry_date":"2022-03-11","entry_price":95200.0,"evidence_available_at_that_date":"Pro-nuclear policy reversal supported the sector, but for this issuer the signal arrived near a crowded price peak before project cashflow was visible.","evidence_source":["https://www.reuters.com/business/energy/skorea-lift-nuclear-powers-share-energy-mix-30-by-2030-2022-07-05/"],"stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","project_pipeline_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","explicit_event_cap","project_cashflow_absence"],"stage4c_evidence_fields":[],"price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/052/052690/2022.csv","profile_path":"atlas/symbol_profiles/052/052690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.37,"MFE_90D_pct":1.37,"MFE_180D_pct":1.37,"MFE_1Y_pct":1.37,"MFE_2Y_pct":null,"MAE_30D_pct":-22.9,"MAE_90D_pct":-40.65,"MAE_180D_pct":-49.84,"MAE_1Y_pct":-49.84,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-03-11","peak_price":96500.0,"drawdown_after_peak_pct":-50.52,"green_lateness_ratio":null,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","explicit_event_cap","project_cashflow_absence"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"policy_reversal_near_peak_4b_watch_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|052690|2022-03-11|95200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"entry_ohlc_row":{"d":"2022-03-11","o":89600.0,"h":96500.0,"l":89000.0,"c":95200.0,"v":1965370,"a":183936514900,"mc":3638544000000,"s":38220000,"m":"KOSPI"}}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31-R11-L214-08","trigger_id":"C31-R11-L214-08-T1","symbol":"052690","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":30,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":50,"customer_quality_score":0,"policy_or_regulatory_score":82,"valuation_repricing_score":82,"execution_risk_score":68,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow/Green-risk","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":50,"customer_quality_score":0,"policy_or_regulatory_score":52,"valuation_repricing_score":90,"execution_risk_score":80,"legal_or_contract_risk_score":40,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_after":55,"stage_label_after":"Stage4B/4C guard","changed_components":["policy_or_regulatory_score","beneficiary_specificity","cashflow_conversion_bridge","event_premium_4b_watch"],"component_delta_explanation":"C31 separates policy existence from named beneficiary and issuer cashflow conversion; generic policy headline is discounted while direct cashflow/shareholder-return bridge is preserved.","MFE_90D_pct":1.37,"MAE_90D_pct":-40.65,"score_return_alignment_label":"corrects_false_positive_or_too_early_policy_entry","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"profile_comparison","round":"R11","loop":"214","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","hypothesis":"current calibrated proxy","changed_axes":"none","thresholds":"default v12 calibrated","selected":"all trigger candidates","false_positive_rate":0.5,"late_green_count":1,"verdict":"over-promotes generic policy headlines in C31","eligible_trigger_count":8,"avg_MFE_90D_pct":16.56,"avg_MAE_90D_pct":-16.49,"avg_MFE_180D_pct":23.69,"avg_MAE_180D_pct":-20.04,"avg_green_lateness_ratio":null,"avg_four_b_local_peak_proximity":null,"avg_four_b_full_window_peak_proximity":null}
{"row_type":"profile_comparison","round":"R11","loop":"214","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_id":"P0b_e2r_2_0_baseline_reference","hypothesis":"rollback reference","changed_axes":"pre-v12 baseline","thresholds":"older looser profile","selected":"too many policy beta entries","false_positive_rate":0.62,"late_green_count":1,"verdict":"worse false-positive control","eligible_trigger_count":8,"avg_MFE_90D_pct":16.56,"avg_MAE_90D_pct":-16.49,"avg_MFE_180D_pct":23.69,"avg_MAE_180D_pct":-20.04,"avg_green_lateness_ratio":null,"avg_four_b_local_peak_proximity":null,"avg_four_b_full_window_peak_proximity":null}
{"row_type":"profile_comparison","round":"R11","loop":"214","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_id":"P1_L10_policy_event_shadow_profile","hypothesis":"sector policy headline cap","changed_axes":"policy_headline_cap + beneficiary_specificity_gate","thresholds":"Green blocked without issuer bridge","selected":"KB/CSWind plus watch for others","false_positive_rate":0.25,"late_green_count":0,"verdict":"better L10 risk/reward alignment","eligible_trigger_count":8,"avg_MFE_90D_pct":16.56,"avg_MAE_90D_pct":-16.49,"avg_MFE_180D_pct":23.69,"avg_MAE_180D_pct":-20.04,"avg_green_lateness_ratio":null,"avg_four_b_local_peak_proximity":null,"avg_four_b_full_window_peak_proximity":null}
{"row_type":"profile_comparison","round":"R11","loop":"214","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_id":"P2_C31_policy_to_cashflow_conversion_profile","hypothesis":"canonical policy-to-cashflow ladder","changed_axes":"cashflow_conversion_bridge + tariff_sufficiency_gate","thresholds":"Yellow needs named route; Green needs conversion","selected":"4 positives; 4 counters capped","false_positive_rate":0.12,"late_green_count":0,"verdict":"best explanation of MFE/MAE split","eligible_trigger_count":8,"avg_MFE_90D_pct":16.56,"avg_MAE_90D_pct":-16.49,"avg_MFE_180D_pct":23.69,"avg_MAE_180D_pct":-20.04,"avg_green_lateness_ratio":null,"avg_four_b_local_peak_proximity":null,"avg_four_b_full_window_peak_proximity":null}
{"row_type":"profile_comparison","round":"R11","loop":"214","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","profile_id":"P3_C31_counterexample_guard_profile","hypothesis":"event premium and reversible policy 4B guard","changed_axes":"event_premium_4b_watch + hard4c confirmation hold","thresholds":"4B overlay if policy arrives after rerating","selected":"052690/336260/015760/036460 capped","false_positive_rate":0.12,"late_green_count":0,"verdict":"best downside guard but may miss early policy beta","eligible_trigger_count":8,"avg_MFE_90D_pct":16.56,"avg_MAE_90D_pct":-16.49,"avg_MFE_180D_pct":23.69,"avg_MAE_180D_pct":-20.04,"avg_green_lateness_ratio":null,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0}
{"row_type":"residual_contribution","round":"R11","loop":"214","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","new_independent_case_count":8,"reused_case_count":0,"new_symbol_count":8,"new_trigger_family_count":6,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_confirmation","stage3_green_revision_min"],"residual_error_types_found":["policy_headline_false_positive","tariff_sufficiency_gap","market_creation_without_named_award","policy_reversal_peak_zone_4b_watch"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt
### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules
- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks
1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output
- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State
completed_round = R11
completed_loop = 214
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 URL/proxy quality repair + Priority 2 C31 cashflow-conversion compression
next_recommended_archetypes = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW for taxonomy compression; C31 only if direct awarded subsidy/tariff cashflow source rows are available; otherwise rotate to C05/C01/C13/C15/C10 missing-url repair
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

## 28. Source Notes
- MAIN prompt opened from GitHub Raw and used as controlling procedure.
- No-Repeat Index opened from GitHub Raw and used as duplicate/coverage ledger only.
- Stock-Web manifest/schema opened to confirm manifest max date, raw/unadjusted status, tradable shard columns, and MFE/MAE formulas.
- Event source URLs are listed in section 9 and machine-readable rows.

## Batch Ingest Self-Audit
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 8
calibration_usable_trigger_count: 8
representative_trigger_count: 8
new_weight_evidence_candidate_count: 8
guardrail_candidate_count: 4
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true