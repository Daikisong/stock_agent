# E2R Stock-Web V12 Residual Research — R7 / loop 137 / C23

## 0. Run metadata

- schema_family: `v12_sector_archetype_residual`
- selected_round: `R7`
- selected_loop: `137`
- large_sector_id: `L7_BIO_HEALTHCARE_MEDICAL`
- canonical_archetype_id: `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION`
- fine_archetype_id: `BIO_APPROVAL_TO_COMMERCIAL_REVENUE_ROYALTY_BRIDGE_VS_APPROVAL_LABEL_OR_PARENT_INDIRECT_HIGH_MAE`
- selection_basis: `docs/core/V12_Research_No_Repeat_Index.md`
- selected_priority_bucket: `Priority 0`
- loop_objective: `coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | bio_approval_commercialization_guardrail | canonical_archetype_compression`
- round_schedule_status: `coverage_index_selected`
- round_sector_consistency: `pass`
- price_source: `Songdaiki/stock-web`
- price_basis: `tradable_raw`
- price_adjustment_status: `raw_unadjusted_marcap`
- stock_web_manifest_max_date: `2026-02-20`
- do_not_propose_new_weight_delta: `false`

## 1. Coverage and no-repeat decision

`C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION` remained under-covered versus 30-row/50-row pull-up targets. The visible No-Repeat Index showed `C23` at 12 rows / 9 symbols, with top covered symbols concentrated in `195940`, `145020`, `000100`, `009420`, `067630`, `068270`.

The registry showed previous C23 loops at R7/loop 89, R7/loop 102, and R7/loop 136. Per v12 loop rule, this run uses `selected_loop = 137`.

This loop deliberately adds three not-visible-top-covered C23 symbols:

- `326030` SK바이오팜
- `006280` 녹십자
- `170900` 동아에스티

## 2. Research thesis

C23 must not treat “approval” as the finish line. In bio/pharma, regulatory approval is the door unlocking the corridor; rerating happens only when patients, prescriptions, reimbursement, partner economics, royalty recognition, shipment cadence, or commercial revenue walk through that corridor.

Therefore this loop separates:

1. **Commercialized approval with repeat revenue bridge** — can support Stage2/Stage3.
2. **Approval plus near-term launch/sales ramp but high-MAE risk** — Stage2 may be valid, but 4B watch should be earlier.
3. **Approval label without direct near-term economics** — should be blocked or capped until royalty/revenue timing is visible.

## 3. Trigger rows

```jsonl
{"row_type":"trigger","symbol":"326030","company_name":"SK바이오팜","selected_round":"R7","selected_loop":137,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_TO_COMMERCIAL_REVENUE_ROYALTY_BRIDGE_VS_APPROVAL_LABEL_OR_PARENT_INDIRECT_HIGH_MAE","trigger_type":"APPROVED_DRUG_US_COMMERCIALIZATION_REVENUE_RAMP","trigger_date":"2024-08-12","entry_date":"2024-08-12","entry_price":98800.0,"MFE_30D_pct":20.95,"MAE_30D_pct":-5.87,"MFE_90D_pct":31.58,"MAE_90D_pct":-5.87,"MFE_180D_pct":31.58,"MAE_180D_pct":-5.87,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","case_polarity":"positive","current_profile_verdict":"under_recognized_commercialization_bridge","calibration_usable":true,"evidence_family":"approved_drug_us_sales_profitability_bridge","non_price_evidence":"XCOPRI/cenobamate is not just an approval label; it is an already commercialized US drug where sales and profit bridge can be monitored.","rule_candidate":"C23 should reward approved-drug commercialization only when sales/profit or prescription bridge is visible."}
{"row_type":"trigger","symbol":"006280","company_name":"녹십자","selected_round":"R7","selected_loop":137,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_TO_COMMERCIAL_REVENUE_ROYALTY_BRIDGE_VS_APPROVAL_LABEL_OR_PARENT_INDIRECT_HIGH_MAE","trigger_type":"FDA_APPROVAL_US_LAUNCH_COMMERCIAL_BRIDGE","trigger_date":"2024-07-09","entry_date":"2024-07-09","entry_price":124900.0,"MFE_30D_pct":33.71,"MAE_30D_pct":-4.56,"MFE_90D_pct":45.56,"MAE_90D_pct":-4.56,"MFE_180D_pct":45.56,"MAE_180D_pct":-10.49,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","case_polarity":"positive_with_4b_watch","current_profile_verdict":"valid_stage2_but_watch_after_vertical_mfe","calibration_usable":true,"evidence_family":"fda_approval_to_us_launch_inventory_distribution_bridge","non_price_evidence":"ALYGLO-type FDA approval plus US launch path gives a clearer C23 bridge than an orphan approval headline, but the later fade requires 4B watch once launch revenue timing is priced in.","rule_candidate":"C23 should allow FDA-approval-to-launch rerating, but apply local 4B if MFE is vertical before quarterly commercial revenue is confirmed."}
{"row_type":"trigger","symbol":"170900","company_name":"동아에스티","selected_round":"R7","selected_loop":137,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_APPROVAL_TO_COMMERCIAL_REVENUE_ROYALTY_BRIDGE_VS_APPROVAL_LABEL_OR_PARENT_INDIRECT_HIGH_MAE","trigger_type":"BIOSIMILAR_APPROVAL_WITH_PARTNER_ECONOMICS_DELAY","trigger_date":"2024-10-11","entry_date":"2024-10-11","entry_price":76400.0,"MFE_30D_pct":5.63,"MAE_30D_pct":-20.16,"MFE_90D_pct":5.63,"MAE_90D_pct":-36.32,"MFE_180D_pct":5.63,"MAE_180D_pct":-46.47,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","case_polarity":"counterexample","current_profile_verdict":"approval_label_false_positive","calibration_usable":true,"evidence_family":"biosimilar_regulatory_approval_without_visible_direct_commercialization_bridge","non_price_evidence":"Imuldosa/ustekinumab approval is a real regulatory event, but if partner commercialization, launch timing, and royalty/margin capture are not visible for the listed company, the stock path can still be a high-MAE false positive.","rule_candidate":"C23 approval events need direct listed-company economics, not just a biosimilar approval label."}
```

## 4. Case analysis

### 4.1 SK바이오팜 (`326030`) — positive commercialization bridge

- entry_date: `2024-08-12`
- entry_price: `98,800`
- forward high used:
  - 30D: `119,500`
  - 90D: `130,000`
  - 180D: `130,000`
- forward low used:
  - 30D: `93,000`
  - 90D: `93,000`
  - 180D: `93,000`
- interpretation: `approved-drug commercialization bridge`
- C23 lesson: approval alone is not enough, but approved drug + visible US commercialization/sales/profit bridge deserves Stage2 recognition.

### 4.2 녹십자 (`006280`) — positive with 4B watch

- entry_date: `2024-07-09`
- entry_price: `124,900`
- forward high used:
  - 30D: `167,000`
  - 90D: `181,800`
  - 180D: `181,800`
- forward low used:
  - 30D: `119,200`
  - 90D: `119,200`
  - 180D: `111,800`
- interpretation: `FDA approval / US launch bridge, but vertical MFE needs local 4B watch`
- C23 lesson: when a bio name rerates on launch path before quarterly commercial revenue is fully proven, v12 should allow the Stage2 bridge but enforce early 4B watch.

### 4.3 동아에스티 (`170900`) — counterexample

- entry_date: `2024-10-11`
- entry_price: `76,400`
- forward high used:
  - 30D: `80,700`
  - 90D: `80,700`
  - 180D: `80,700`
- forward low used:
  - 30D: `61,000`
  - 90D: `48,650`
  - 180D: `40,900`
- interpretation: `approval label false positive`
- C23 lesson: biosimilar approval is not automatically commercial rerating. If launch economics, partner split, market access, and royalty timing are not visible, Stage2 should be capped or blocked.

## 5. Score simulation notes

| symbol | prior profile tendency | observed path | suggested interpretation |
|---|---|---:|---|
| 326030 | may underweight commercialized-drug profitability bridge | +31.58% MFE / -5.87% MAE | strengthen positive C23 commercialization bridge |
| 006280 | may correctly detect approval-to-launch but late 4B | +45.56% MFE / -10.49% MAE | Stage2 valid, local 4B after vertical MFE |
| 170900 | may overread approval label | +5.63% MFE / -46.47% MAE | block/cap until listed-company economics visible |

## 6. Residual contribution

- new_independent_case_count: `3`
- reused_case_count: `0`
- same_archetype_new_symbol_count_visible_index_basis: `3`
- same_archetype_new_trigger_family_count: `3`
- calibration_usable case 수: `3`
- calibration_usable trigger 수: `3`
- positive_case_count: `2`
- counterexample_count: `1`
- current_profile_error_count: `1`
- diversity_score_summary: `new_visible_C23_symbol=3, new_trigger_family=3, positive/counterexample=2/1, commercialization-bridge positive=1, FDA-launch vertical-MFE watch=1, biosimilar approval-label false-positive=1`

## 7. Candidate rule reinforcement

- existing_axis_strengthened:
  - `C23_approval_to_commercial_revenue_bridge_requirement`
  - `C23_US_launch_or_sales_ramp_visibility_bonus`
  - `C23_partner_economics_and_royalty_timing_requirement`
  - `C23_biosimilar_approval_label_stage2_block_without_direct_listed_company_cash_bridge`
  - `C23_vertical_MFE_local_4B_watch_before_revenue_confirmation`
- new_axis_proposed: `null`
- existing_axis_weakened: `null`
- sector_specific_rule_candidate: `false`
- canonical_archetype_rule_candidate: `true`
- loop_contribution_label: `canonical_archetype_rule_candidate`

## 8. Next recommended archetypes

- `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL`
- `R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW`
- `C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK`
- `C13_BATTERY_JV_UTILIZATION_AMPC_IRA`
