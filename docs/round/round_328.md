순서상 이번은 **R7 Loop 17 — 바이오·헬스케어·의료기기 trigger-level price validation 라운드**다.

```text
round = R7 Loop 17
round_id = round_256
large_sector = BIO_HEALTHCARE_MEDICAL_DEVICE
method = trigger_level_backtest_v1_after_redteam
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R8 Loop 17
```

이번 R7도 KRX/Naver/Yahoo/Stooq 수정주가 일봉 OHLC window를 안정적으로 확보하지 못했다. 그래서 MFE/MAE/peak/drawdown은 만들지 않고 `price_data_unavailable_after_deep_search`로 둔다. 대신 Reuters/FT/WSJ/MarketWatch/Allure의 **reported event return, deal value, acquisition price, approval status, litigation trigger, facility capacity, tender/acquisition price**를 trigger anchor로 사용한다.

---

# 1. 이번 라운드 대섹터

```text
R7 = 바이오·헬스케어·의료기기
```

R7의 core gate는 아래다.

```text
CDMO / biomanufacturing:
계약 또는 공장 인수 → 생산능력 → 고객사/제품 mix → tariff hedge → utilization → margin

Biosimilar / specialty pharma:
FDA/EMA approval → 특허/소송 → commercial launch → payer/rebate → margin

Biotech platform:
임상 성공 / 비열등성 / 파트너 launch plan → royalty / enzyme supply / patent dispute → 실제 매출

Medical aesthetics:
FDA approval / U.S. launch → distributor/channel → pricing vs Botox → repeat treatment → margin

Medical device / PE M&A:
tender offer / acquisition valuation → delisting / founder reinvestment → global expansion → public-stock liquidity loss

4B / 4C:
FDA CRL, patent lawsuit, clinical failure, manufacturing inspection, tariff, dilution, cyber/privacy, reimbursement failure
```

---

# 2. 대상 canonical archetype

```text
BIOPHARMA_POLICY_SUPPORT_STAGE2_ACTIONABLE
CDMO_US_FACILITY_TARIFF_HEDGE_STAGE2_PRICE_FAILED
VACCINE_CDMO_CROSS_BORDER_MA_STAGE2_ACTIONABLE
BIOSIMILAR_US_LOCALIZATION_STAGE2_NO_PRICE
PLATFORM_ENZYME_BLOCKBUSTER_STAGE3_YELLOW
AESTHETIC_TOXIN_US_FDA_STAGE2
MEDICAL_AESTHETIC_DEVICE_MA_STAGE2
BIOSIMILAR_PATENT_LITIGATION_4B
```

---

# 3. deep sub-archetype

```text
Samsung Biologics / pharma policy support:
- Korean government pledged support for biopharma exporters against U.S. tariff risk.
- pharma sector +3.97%; Samsung Biologics +6.23%, Celltrion +0.35%, KOSPI +0.99%.
- Stage2-Actionable sector policy support, but not company-specific Green.

Samsung Biologics / GSK U.S. facility:
- Samsung Biologics to buy GSK's U.S. drug production facility for $280M.
- facility has 60,000 liters of drug substance capacity.
- shares -0.4%, broader market +2%.
- evidence good but price failed; tariff hedge Stage2, not Actionable.

SK Bioscience / IDT Biologika:
- SK Bioscience to buy 60% stake in Germany’s IDT Biologika for 339B won / $244M.
- first major M&A since IPO.
- shares +11.7%.
- Stage2-Actionable cross-border CDMO/vaccine manufacturing.

Celltrion / U.S. factory:
- Celltrion became preferred bidder for U.S. pharma factory to offset tariff risk.
- planned 700B won investment; final acquisition of Eli Lilly’s ImClone facility for $330M.
- later up to 700B won / $478M expansion.
- Stage2 tariff hedge; no direct event price anchor.

Alteogen / Keytruda SC:
- Merck plans U.S. launch of subcutaneous Keytruda using Alteogen enzyme.
- FDA decision target was Sep 23, 2025; Merck expected 30~40% peak adoption.
- Keytruda had nearly $30B 2024 sales.
- Stage3-Yellow candidate platform/royalty trigger; patent dispute with Halozyme is 4B.

Hugel / Letybo:
- Letybo, manufactured by Hugel, received U.S. FDA approval for glabellar lines and entered U.S. dermatology offices.
- price could be cheaper than Botox, with U.S. availability expected from March 2025.
- Stage2 regulatory/commercial launch, no KRX price anchor.

Jeisys Medical / ArchiMed:
- ArchiMed acquired Korean energy-based aesthetic device company Jeisys Medical for about $742M.
- shares closed around 12,860 won, little changed.
- Stage2 M&A valuation reference, but delisting/liquidity and no large price reaction.

Samsung Bioepis / Amgen lawsuit:
- Amgen sued Samsung Bioepis over proposed Prolia/Xgeva biosimilars.
- Amgen alleged infringement of 34 patents.
- Prolia/Xgeva U.S. sales were over $4.2B in prior year.
- Biosimilar patent litigation 4B, not hard 4C unless launch blocked materially.
```

---

# 4. 선정 case 요약

| bucket                                 | case                                      | 핵심 판정                                                           |
| -------------------------------------- | ----------------------------------------- | --------------------------------------------------------------- |
| structural_success / Stage2-Actionable | **SK Bioscience / IDT Biologika**         | 339B won / $244M M&A, shares +11.7%                             |
| Stage2-Actionable policy               | **Samsung Biologics / pharma support**    | pharma sector +3.97%, Samsung Bio +6.23%                        |
| evidence_good_but_price_failed         | **Samsung Biologics / GSK U.S. facility** | $280M acquisition, 60,000L capacity, shares -0.4% vs market +2% |
| Stage2 no-price                        | **Celltrion / U.S. factory**              | 700B won plan, $330M ImClone acquisition, up to $478M expansion |
| Stage3-Yellow candidate                | **Alteogen / Keytruda SC**                | Keytruda SC launch plan, 30~40% adoption target, $30B franchise |
| Stage2 regulatory                      | **Hugel / Letybo FDA**                    | U.S. FDA-approved toxin, U.S. commercial availability           |
| Stage2 M&A valuation                   | **Jeisys Medical / ArchiMed**             | $742M acquisition, 12,860 won tender/close context              |
| 4B litigation                          | **Samsung Bioepis / Amgen lawsuit**       | 34 patents, Prolia/Xgeva biosimilar launch risk                 |

이번 source set에서는 **신뢰 가능한 국장 hard 4C price anchor는 확인하지 못했다.** 그래서 억지로 clinical failure 4C를 만들지 않고 `hard_4c_not_confirmed`로 둔다. R7에서 hard 4C는 FDA CRL, pivotal trial failure, manufacturing inspection failure, reimbursement failure가 가격과 같이 확인될 때만 올린다.

---

# 5. 각 case별 trigger grid

## Case A — SK Bioscience / IDT Biologika acquisition

```text
symbol = 302440
case_type = Stage2-Actionable vaccine/CDMO cross-border M&A
archetype = VACCINE_CDMO_CROSS_BORDER_MA_STAGE2_ACTIONABLE
```

| trigger |              type | date       | 당시 공개 evidence                                                        | 가격 anchor     | outcome |
| ------- | ----------------: | ---------- | --------------------------------------------------------------------- | ------------- | ------- |
| T0      |            Stage1 | 2024H1     | SK Group business rebalancing, vaccine/CDMO expansion 필요              | no entry      |         |
| T1      | Stage2-Actionable | 2024-06-27 | SK Bioscience, Germany IDT Biologika 60% stake 인수                     | shares +11.7% |         |
| T2      |        validation | 2024-06-27 | deal value 339B won / $243.75M, first major M&A since 2021 IPO        | same          |         |
| T3      |          4B-watch | 2024~      | integration, utilization, European cost base, vaccine demand, M&A ROI | 4B            |         |
| T4      |     Stage3-Yellow | N/A        | acquired facility utilization / margin / orderbook 확인 필요              | 보류            |         |

SK Bioscience는 이번 R7에서 가장 깨끗한 Stage2-Actionable이다. Reuters에 따르면 SK Bioscience는 Germany CDMO IDT Biologika 60%를 339B won, 약 $243.75M에 인수했고, 발표 후 shares는 오전 거래에서 +11.7%였다. 이건 단순 바이오 테마가 아니라 **자산 인수 + 생산능력/지역 확장 + 가격반응**이 같이 닫힌 trigger다. 다만 Green은 IDT facility utilization, CDMO orderbook, margin, integration cost가 확인되어야 한다. ([Reuters][1])

```json
{
  "case_id": "r7_loop17_sk_bioscience_idt_biologika",
  "symbol": "302440",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2-Actionable_vaccine_CDMO_cross_border_MA",
  "trigger_date": "2024-06-27",
  "stake_acquired_pct": 60,
  "deal_value_krw_bn": 339,
  "deal_value_usd_mn": 243.75,
  "event_return_pct": 11.7,
  "strategic_logic": [
    "global_CDMO_expansion",
    "vaccine_manufacturing_capacity",
    "SK_Group_business_rebalancing",
    "post_IPO_first_major_MA"
  ],
  "4B_overlay": [
    "integration_cost",
    "European_cost_base",
    "facility_utilization",
    "CDMO_orderbook_visibility",
    "M&A_ROI"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "excellent_stage2_actionable_CDMO_MA"
}
```

---

## Case B — Samsung Biologics / pharma policy support

```text
symbol = 207940
case_type = Stage2-Actionable policy support
archetype = BIOPHARMA_POLICY_SUPPORT_STAGE2_ACTIONABLE
```

| trigger |              type | date       | 당시 공개 evidence                                                            | 가격 anchor                                              | outcome |
| ------- | ----------------: | ---------- | ------------------------------------------------------------------------- | ------------------------------------------------------ | ------- |
| T0      |            Stage1 | 2025-05    | U.S. pharma tariff risk, Korea export support 논의                          | no entry                                               |         |
| T1      | Stage2-Actionable | 2025-05-21 | Korean government pledges support for biopharma exporters                 | pharma sector +3.97%, Samsung Bio +6.23%, KOSPI +0.99% |         |
| T2      |        validation | 2025-05-21 | pharma exports $9.59B in 2024, 16% to U.S.; support for U-turn investment | same                                                   |         |
| T3      |          4B-watch | 2025       | tariff details, U.S. inspection, actual subsidy/support terms             | 4B                                                     |         |
| T4      |     Stage3-Yellow | N/A        | contract backlog / facility utilization / margin 확인 필요                    | 보류                                                     |         |

Samsung Biologics의 policy support trigger는 R7의 sector Stage2-Actionable이다. Reuters는 한국 정부가 U.S. tariff risk에 대응해 biopharma support를 예고했고, 같은 날 pharma sector가 +3.97%, Samsung Biologics가 +6.23%, KOSPI가 +0.99%였다고 보도했다. 다만 이건 회사별 신규 수주가 아니라 policy/tariff hedge trigger라서, Green은 backlog·utilization·margin이 확인되어야 한다. ([Reuters][2])

```json
{
  "case_id": "r7_loop17_samsung_biologics_policy_support",
  "symbol": "207940",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2-Actionable_biopharma_policy_support",
  "trigger_date": "2025-05-21",
  "pharma_sector_event_return_pct": 3.97,
  "samsung_biologics_event_return_pct": 6.23,
  "celltrion_same_context_return_pct": 0.35,
  "kospi_same_context_pct": 0.99,
  "korea_pharma_exports_2024_usd_bn": 9.59,
  "us_export_share_pct": 16,
  "4B_overlay": [
    "tariff_detail_uncertainty",
    "FDA_inspection",
    "policy_support_terms_unclear",
    "company_specific_contract_not_confirmed"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "good_stage2_policy_support_not_green"
}
```

---

## Case C — Samsung Biologics / GSK U.S. facility acquisition

```text
symbol = 207940
case_type = evidence good but price failed
archetype = CDMO_US_FACILITY_TARIFF_HEDGE_STAGE2_PRICE_FAILED
```

| trigger |            type | date       | 당시 공개 evidence                                                               | 가격 anchor                | outcome |
| ------- | --------------: | ---------- | ---------------------------------------------------------------------------- | ------------------------ | ------- |
| T0      | Stage2 facility | 2025-12-22 | Samsung Biologics to buy first U.S. drug production facility from GSK        | shares -0.4%, market +2% |         |
| T1      |      validation | 2025-12-22 | $280M acquisition, Rockville facility, 60,000L drug-substance capacity       | same                     |         |
| T2      |        4B-watch | 2025~2026  | capex to expand/upgrade, closing risk, utilization, tariff benefit uncertain | 4B                       |         |
| T3      |   Stage3-Yellow | N/A        | customer transfer / margin / utilization 확인 필요                               | 보류                       |         |

GSK U.S. facility acquisition은 evidence는 좋지만 가격은 실패했다. Reuters는 Samsung Biologics가 GSK로부터 U.S. drug production facility를 $280M에 인수하고, 해당 site가 60,000L drug-substance capacity를 갖췄다고 보도했다. 그런데 발표 후 Samsung Biologics shares는 -0.4%였고 broader market은 +2%였다. 즉 이건 tariff hedge Stage2로 기록하되, price validation 기준으로는 **evidence_good_but_price_failed**다. ([Reuters][3])

```json
{
  "case_id": "r7_loop17_samsung_biologics_gsk_us_facility",
  "symbol": "207940",
  "best_trigger": "T0/T2",
  "best_trigger_type": "evidence_good_but_price_failed_CDMO_US_facility",
  "trigger_date": "2025-12-22",
  "deal_value_usd_mn": 280,
  "facility_capacity_liters": 60000,
  "event_return_pct": -0.4,
  "broader_market_same_context_pct": 2.0,
  "market_relative_return_pp": -2.4,
  "strategic_logic": [
    "US_local_manufacturing",
    "tariff_hedge",
    "long_term_US_demand",
    "CDMO_footprint_expansion"
  ],
  "4B_overlay": [
    "capex_upgrade_cost",
    "utilization_ramp",
    "closing_value_adjustment",
    "customer_transfer",
    "tariff_benefit_uncertain"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "evidence_good_but_price_failed"
}
```

---

## Case D — Celltrion / U.S. factory localization

```text
symbol = 068270
case_type = Stage2 tariff hedge / U.S. manufacturing
archetype = BIOSIMILAR_US_LOCALIZATION_STAGE2_NO_PRICE
```

| trigger |                    type | date       | 당시 공개 evidence                                                           | 가격 anchor                | outcome |
| ------- | ----------------------: | ---------- | ------------------------------------------------------------------------ | ------------------------ | ------- |
| T0      | Stage2 preferred bidder | 2025-07-29 | Celltrion becomes preferred bidder for U.S. pharma factory               | direct price unavailable |         |
| T1      |              validation | 2025-09-23 | Celltrion U.S. unit acquires Eli Lilly’s ImClone Systems for $330M       | no event return          |         |
| T2      |       expansion trigger | 2025-11-19 | Celltrion to invest up to 700B won / $478M to expand U.S. factory        | no event return          |         |
| T3      |                4B-watch | 2025~2026  | capex, tariff uncertainty, utilization, biosimilar price/rebate pressure | 4B                       |         |
| T4      |           Stage3-Yellow | N/A        | U.S. production ramp / margin / product transfer 확인 필요                   | 보류                       |         |

Celltrion은 U.S. localization Stage2다. Reuters는 Celltrion이 tariff risk 대응을 위해 U.S. pharma factory preferred bidder가 됐고, 700B won 투자를 계획한다고 보도했다. 이후 regulatory filing으로 Eli Lilly의 ImClone facility를 $330M에 인수했고, 추가로 최대 700B won, 약 $478M 확장을 발표했다. 다만 이 case는 직접 주가 anchor가 없으므로 Stage2 no-price로 둔다. ([Reuters][4])

```json
{
  "case_id": "r7_loop17_celltrion_us_factory_localization",
  "symbol": "068270",
  "best_trigger": "T0/T3",
  "best_trigger_type": "Stage2_US_factory_tariff_hedge_no_price",
  "preferred_bidder_date": "2025-07-29",
  "planned_initial_investment_krw_bn": 700,
  "imclone_acquisition_value_usd_mn": 330,
  "additional_expansion_investment_krw_bn": 700,
  "additional_expansion_investment_usd_mn": 478,
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "strategic_logic": [
    "US_tariff_hedge",
    "biosimilar_local_manufacturing",
    "commercial_and_pipeline_product_support",
    "future_US_launch_protection"
  ],
  "4B_overlay": [
    "facility_upgrade_cost",
    "biosimilar_rebate_pressure",
    "tariff_policy_uncertainty",
    "utilization_ramp",
    "capital_intensity"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_US_localization_no_price"
}
```

---

## Case E — Alteogen / Merck Keytruda subcutaneous formulation

```text
symbol = 196170
case_type = Stage3-Yellow candidate platform royalty/enzyme
archetype = PLATFORM_ENZYME_BLOCKBUSTER_STAGE3_YELLOW
```

| trigger |                    type | date       | 당시 공개 evidence                                                                                              | 가격 anchor                         | outcome |
| ------- | ----------------------: | ---------- | ----------------------------------------------------------------------------------------------------------- | --------------------------------- | ------- |
| T0      |         Stage2 clinical | 2024-11-19 | Merck says injectable Keytruda non-inferior to IV formulation                                               | Alteogen direct price unavailable |         |
| T1      | Stage3-Yellow candidate | 2025-03-27 | Merck plans U.S. launch of SC Keytruda on Oct 1 if FDA approves                                             | no KRX price                      |         |
| T2      |              validation | 2025-03~09 | Keytruda nearly $30B 2024 sales; peak adoption expected 30~40%; injection time 2 minutes vs 30-min infusion | no price                          |         |
| T3      |                4B-watch | 2025       | Halozyme patent dispute over enzyme technology                                                              | 4B                                |         |
| T4      |            Stage3-Green | N/A        | approval, launch, royalty/supply revenue and patent-risk resolution needed                                  | 보류                                |         |

Alteogen은 R7에서 가장 강한 platform/royalty Yellow 후보다. Reuters는 Merck의 injectable Keytruda가 IV formulation 대비 non-inferiority를 보였고, South Korea-based Alteogen이 Keytruda SC에 쓰이는 enzyme을 개발·제조한다고 보도했다. 이후 Merck는 U.S. launch를 Oct 1로 계획했고, Keytruda는 2024년 매출이 거의 $30B인 초대형 franchise이며 SC formulation의 peak adoption을 30~40%로 기대했다. 다만 Halozyme patent dispute가 4B라서 Green은 launch·royalty·patent-risk 확인 후다. ([Reuters][5])

```json
{
  "case_id": "r7_loop17_alteogen_keytruda_sc",
  "symbol": "196170",
  "best_trigger": "T0/T3",
  "best_trigger_type": "Stage3-Yellow_candidate_platform_enzyme_blockbuster",
  "clinical_trigger_date": "2024-11-19",
  "launch_plan_date": "2025-03-27",
  "merck_planned_us_launch_date": "2025-10-01",
  "fda_target_action_date": "2025-09-23",
  "keytruda_2024_sales_usd_bn": "nearly_30",
  "expected_peak_adoption_pct": "30-40",
  "administration_time_sc_minutes": 2,
  "administration_time_iv_minutes": 30,
  "direct_alteogen_price_anchor": "price_data_unavailable_after_deep_search",
  "4B_overlay": [
    "Halozyme_patent_dispute",
    "FDA_approval_timing",
    "royalty_terms_visibility",
    "commercial_conversion",
    "Merck_launch_execution"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage3_Yellow_candidate_not_Green"
}
```

---

## Case F — Hugel / Letybo U.S. FDA approval and launch

```text
symbol = 145020
case_type = Stage2 regulatory/commercial launch
archetype = AESTHETIC_TOXIN_US_FDA_STAGE2
```

| trigger |               type | date                   | 당시 공개 evidence                                                                           | 가격 anchor                      | outcome |
| ------- | -----------------: | ---------------------- | ---------------------------------------------------------------------------------------- | ------------------------------ | ------- |
| T0      |    Stage2 approval | 2024-02 / 2025 rollout | Letybo received U.S. FDA approval for glabellar lines                                    | Hugel direct price unavailable |         |
| T1      |  launch validation | 2025-03                | Letybo begins appearing in U.S. dermatology practices                                    | no KRX price                   |         |
| T2      | pricing validation | 2025-03                | possible $9~12/unit vs Botox $12~18/unit                                                 | no stock price                 |         |
| T3      |           4B-watch | 2025                   | U.S. distributor channel, price competition, physician adoption, toxin safety perception | 4B                             |         |
| T4      |      Stage3-Yellow | N/A                    | U.S. sell-through, reorder, margin 확인 필요                                                 | 보류                             |         |

Hugel Letybo는 regulatory Stage2다. Allure는 Hugel-manufactured Letybo가 U.S. FDA approval을 받고 U.S. dermatology offices에 들어가기 시작했다고 보도했고, NY Post/Allure는 Letybo가 Botox보다 저렴한 가격대가 될 수 있다고 설명했다. 하지만 주가 anchor와 U.S. sell-through는 없다. 따라서 FDA approval/commercial launch Stage2로 두고, physician adoption·pricing·margin이 Yellow gate다. ([Allure][6])

```json
{
  "case_id": "r7_loop17_hugel_letybo_us_fda",
  "symbol": "145020",
  "best_trigger": "T0/T3",
  "best_trigger_type": "Stage2_aesthetic_toxin_US_FDA_launch",
  "approval_context": "US_FDA_approval_for_glabellar_lines",
  "commercial_rollout_context": "US_dermatology_offices_from_March_2025",
  "estimated_letybo_unit_price_usd": "9-12",
  "estimated_botox_unit_price_usd": "12-18",
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "4B_overlay": [
    "US_channel_execution",
    "physician_adoption",
    "price_competition",
    "aesthetic_toxin_safety_perception",
    "repeat_treatment_durability"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_FDA_launch_no_price"
}
```

---

## Case G — Jeisys Medical / ArchiMed acquisition

```text
symbol = 287410
case_type = medical-aesthetic device M&A valuation reference
archetype = MEDICAL_AESTHETIC_DEVICE_MA_STAGE2
```

| trigger |          type | date       | 당시 공개 evidence                                            | 가격 anchor                                | outcome |
| ------- | ------------: | ---------- | --------------------------------------------------------- | ---------------------------------------- | ------- |
| T0      |    Stage2 M&A | 2024-09-11 | ArchiMed acquired Jeisys Medical for about $742M          | shares closed 12,860 won, little changed |         |
| T1      |    validation | 2024-09-11 | Jeisys makes EBD devices: radio waves, ultrasound, lasers | same                                     |         |
| T2      |      4B-watch | 2024       | delisting process, liquidity exit, tender already priced  | 4B                                       |         |
| T3      | Stage3-Yellow | N/A        | listed peers’ rerating / global EBD sell-through needed   | 보류                                       |         |

Jeisys는 의료기기 R7의 M&A valuation case다. WSJ는 healthcare PE ArchiMed가 Jeisys Medical을 약 $742M에 인수했고, Jeisys shares가 12,860 won, 약 $9.58에 “little changed”로 마감했다고 보도했다. Jeisys는 radio waves, ultrasound, lasers 기반 energy-based devices를 만들며 wrinkle, scar, body contouring 등에 쓰인다. M&A valuation은 sector reference로 좋지만, 주가가 크게 반응하지 않았고 delisting/liquidity exit라 Actionable보다는 Stage2 valuation reference다. ([월스트리트저널][7])

```json
{
  "case_id": "r7_loop17_jeisys_archimed_medical_aesthetic_ma",
  "symbol": "287410",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage2_medical_aesthetic_device_MA_reference",
  "trigger_date": "2024-09-11",
  "deal_value_usd_mn": 742,
  "event_close_price_krw": 12860,
  "price_reaction_context": "little_changed",
  "device_category": "energy_based_devices_EBD",
  "technology": [
    "radio_waves",
    "ultrasound",
    "lasers"
  ],
  "4B_overlay": [
    "delisting_process",
    "liquidity_exit",
    "tender_already_priced",
    "peer_readthrough_uncertain"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "MA_valuation_reference_not_actionable"
}
```

---

## Case H — Samsung Bioepis / Amgen Prolia-Xgeva patent lawsuit

```text
symbol = 207940 readthrough
case_type = biosimilar patent litigation 4B
archetype = BIOSIMILAR_PATENT_LITIGATION_4B
```

| trigger |          type | date       | 당시 공개 evidence                                           | 가격 anchor             | outcome |
| ------- | ------------: | ---------- | -------------------------------------------------------- | --------------------- | ------- |
| T0      | 4B litigation | 2024-08-13 | Amgen sues Samsung Bioepis over Prolia/Xgeva biosimilars | no stock price        |         |
| T1      |    validation | 2024-08-13 | Amgen alleges infringement of 34 patents                 | no price              |         |
| T2      |   market size | 2024-08-13 | Prolia U.S. sales $2.7B, Xgeva $1.5B previous year       | no price              |         |
| T3      | Stage2 relief | N/A        | settlement / launch timing / FDA approval pathway needed | 보류                    |         |
| T4      |       hard 4C | N/A        | launch permanently blocked not confirmed                 | hard 4C not confirmed |         |

Samsung Bioepis/Amgen lawsuit는 4B다. Reuters는 Amgen이 Samsung Bioepis의 Prolia/Xgeva biosimilar가 34개 patents를 침해한다고 주장하며 소송을 냈고, Prolia와 Xgeva의 prior-year U.S. sales가 각각 $2.7B, $1.5B였다고 보도했다. 이는 biosimilar opportunity는 크지만 patent litigation이 launch timing과 economics를 흔드는 전형적인 R7 4B다. 아직 영구 launch block이 확인된 것은 아니므로 4C는 아니다. ([Reuters][8])

```json
{
  "case_id": "r7_loop17_samsung_bioepis_amgen_patent_litigation",
  "symbol": "207940_readthrough",
  "best_trigger": "T0/T3",
  "best_trigger_type": "4B_biosimilar_patent_litigation",
  "trigger_date": "2024-08-13",
  "plaintiff": "Amgen",
  "defendant": "Samsung_Bioepis",
  "products": [
    "Prolia_biosimilar",
    "Xgeva_biosimilar"
  ],
  "patents_alleged_infringed": 34,
  "prolia_us_sales_prior_year_usd_bn": 2.7,
  "xgeva_us_sales_prior_year_usd_bn": 1.5,
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "hard_4C_status": "not_confirmed",
  "4B_overlay": [
    "patent_litigation",
    "launch_delay",
    "settlement_cost",
    "biosimilar_rebate_pressure",
    "FDA_and_commercial_timing"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "biosimilar_patent_litigation_4B_not_4C"
}
```

---

# 6. Trigger별 실제 가격경로 검증 요약

이번 R7 Loop 17은 full OHLC가 없으므로, 아래 표는 **reported event anchor 기준**이다.

| case                       | best trigger |                                   event return / price |  market-relative | full MFE/MAE | outcome                        |
| -------------------------- | -----------: | -----------------------------------------------------: | ---------------: | ------------ | ------------------------------ |
| SK Bioscience / IDT        |           T1 |                                                 +11.7% |      unavailable | unavailable  | excellent Stage2-Actionable    |
| Samsung Bio policy support |           T1 | Samsung Bio +6.23%, pharma sector +3.97%, KOSPI +0.99% | +5.24pp vs KOSPI | unavailable  | good Stage2-Actionable         |
| Samsung Bio / GSK facility |           T0 |                                      -0.4%, market +2% |           -2.4pp | unavailable  | evidence_good_but_price_failed |
| Celltrion / U.S. factory   |        T0/T2 |                                      price unavailable |              N/A | unavailable  | Stage2 no-price                |
| Alteogen / Keytruda SC     |        T0/T3 |                             Alteogen price unavailable |              N/A | unavailable  | Stage3-Yellow candidate        |
| Hugel / Letybo             |        T0/T2 |                                      price unavailable |              N/A | unavailable  | Stage2 regulatory approval     |
| Jeisys / ArchiMed          |           T0 |                             12,860 won, little changed |         no alpha | unavailable  | M&A valuation reference        |
| Samsung Bioepis / Amgen    |           T0 |                                      price unavailable |              N/A | unavailable  | biosimilar litigation 4B       |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
가장 좋은 Stage2:
1. SK Bioscience / IDT Biologika: +11.7%, M&A value and manufacturing asset clear.
2. Samsung Biologics / pharma support: +6.23%, policy support and tariff hedge.
3. Alteogen / Keytruda SC: blockbuster platform trigger, but no direct price anchor in this run.
4. Hugel / Letybo: FDA approval/commercial launch, no price anchor.
5. Celltrion / U.S. factory: tariff-localization, no price anchor.
```

## Stage2-Actionable entry 성과

```text
Stage2-Actionable:
- SK Bioscience / IDT.
- Samsung Biologics / pharma policy support.

Actionable 보류:
- Samsung Biologics / GSK facility: evidence good but price failed.
- Celltrion / U.S. factory: strategic but no direct price.
- Alteogen / Keytruda SC: Yellow candidate but direct KRX price unavailable.
- Hugel / Letybo: regulatory Stage2 but no sell-through/price.
- Jeisys / ArchiMed: M&A reference, not public-stock Actionable.
```

## Stage3-Yellow 후보

```text
Yellow 후보:
- Alteogen / Keytruda SC if approval-launch-royalty/supply revenue closes and Halozyme risk is contained.
- SK Bioscience / IDT if utilization/orderbook/margin confirms.
- Samsung Biologics if policy support converts into contracts/utilization/margin.
- Celltrion if U.S. factory transfer and product-level margin improves.
- Hugel if U.S. Letybo sell-through/reorder/margin appears.
```

## Stage3-Green

```text
이번 R7 Loop 17에서 확정 Green 없음.

이유:
- full OHLC/MFE/MAE가 없다.
- FDA/approval/platform evidence가 있어도 royalty, sell-through, reimbursement, margin이 아직 닫히지 않았다.
- Samsung Bio GSK deal은 오히려 price failed다.
- biosimilar litigation and patent risk가 R7 4B로 남아 있다.
```

---

# 8. score-price alignment 판정

```text
aligned:
- SK Bioscience / IDT as Stage2-Actionable.
- Samsung Biologics policy support as Stage2-Actionable.
- Samsung Biologics / GSK facility as evidence_good_but_price_failed.
- Celltrion / U.S. factory as Stage2 no-price.
- Alteogen / Keytruda SC as Stage3-Yellow candidate, not Green.
- Hugel / Letybo as Stage2 regulatory approval.
- Jeisys / ArchiMed as M&A valuation reference.
- Samsung Bioepis / Amgen as 4B litigation.

false_positive_score:
- Samsung Bio GSK facility를 price failed 무시하고 Green으로 올리는 경우.
- Celltrion U.S. factory를 utilization/margin 없이 Green으로 올리는 경우.
- Alteogen을 royalty/patent/approval 확인 없이 Green으로 올리는 경우.
- Hugel Letybo를 U.S. sell-through 없이 Green으로 올리는 경우.
- Jeisys acquisition을 listed-stock upside로 과대반영하는 경우.

Stage2_promote_candidate:
- SK Bioscience / IDT.
- Samsung Biologics policy support.
- Alteogen / Keytruda SC.
- Hugel / Letybo.
- Celltrion U.S. factory.

evidence_good_but_price_failed:
- Samsung Biologics / GSK U.S. facility.

4B-watch:
- Samsung Bioepis / Amgen patent litigation.
- Alteogen / Halozyme patent dispute.
- U.S. pharma tariff policy uncertainty.
- CDMO facility utilization.
- toxin pricing / physician adoption / safety perception.

hard_4C:
- hard_4c_not_confirmed in sourced Korean R7 cases.
```

---

# 9. 점수비중 교정

## 올릴 축

```csv
axis,delta,reason,cases
manufacturing_asset_MA,+5,"생산자산 인수와 가격반응이 같이 닫히면 Stage2-Actionable","SK Bioscience"
biopharma_policy_support,+4,"정부 support와 sector/stock reaction이 같이 닫히면 Stage2","Samsung Biologics"
US_localization_tariff_hedge,+4,"U.S. facility acquisition can hedge tariff risk","Samsung Bio, Celltrion"
blockbuster_platform_linkage,+5,"Keytruda 같은 blockbuster와 연결된 enzyme/platform은 Yellow 후보","Alteogen"
FDA_approval_commercial_launch,+4,"FDA approval and U.S. commercial rollout are Stage2 triggers","Hugel"
medical_device_MA_valuation,+3,"aesthetic device M&A는 peer valuation reference","Jeisys"
patent_litigation_risk,+5,"biosimilar/platform patent dispute is core R7 4B","Samsung Bioepis, Alteogen"
utilization_margin_conversion,+5,"CDMO/시설 인수는 utilization and margin 확인 전 Green 금지","Samsung Bio, Celltrion, SK Bioscience"
```

## 내릴 축

```csv
axis,delta,reason,cases
facility_acquisition_without_price_validation,-5,"공장 인수에도 주가가 시장을 못 이기면 Actionable 금지","Samsung Bio GSK"
policy_support_without_company_contract,-4,"정책지원만으로 회사별 Green 금지","Samsung Bio, Celltrion"
FDA_approval_without_sellthrough,-5,"FDA approval 후 actual sales/reorder 전까지 Green 금지","Hugel"
platform_link_without_royalty_visibility,-5,"blockbuster 파트너십도 royalty/revenue 전까지 Green 금지","Alteogen"
MA_reference_without_public_liquidity,-4,"delisting M&A는 listed upside로 과대평가 금지","Jeisys"
biosimilar_opportunity_without_patent_clearance,-5,"patent litigation 무시하면 biosimilar false positive","Samsung Bioepis"
CDMO_capacity_without_utilization,-5,"capacity liter만으로 Green 금지","Samsung Bio, Celltrion, SK Bioscience"
hard_4C_without_sourced_price_anchor,-5,"FDA CRL/임상실패는 price/source 없으면 억지 4C 금지","R7 hard 4C"
```

---

# 10. Stage2-Actionable 승격 조건

R7 Loop 17 shadow rule:

```text
R7에서 Stage2 evidence가 아래 중 4개 이상이면 Stage2-Actionable로 승격한다.

1. event return +5% 이상
2. deal value / approval / facility capacity / product launch가 명확하다
3. customer, product, facility, indication 중 하나가 구체적이다
4. revenue path가 CDMO utilization / royalty / launch sales / reimbursement로 연결된다
5. patent/litigation/tariff/manufacturing inspection 4B가 식별 가능하다
6. price reaction이 evidence와 같은 방향으로 검증된다
7. approval이나 M&A가 실제 commercial execution으로 넘어갈 수 있다
```

적용:

```text
SK Bioscience / IDT:
1,2,3,4,5,6 충족 → Stage2-Actionable.

Samsung Biologics policy support:
1,2 일부,5,6 충족 → Stage2-Actionable but company-specific Green 금지.

Samsung Biologics GSK:
2,3,4,5 충족 but 6 실패 → evidence_good_but_price_failed.

Celltrion U.S. factory:
2,3,4,5 충족 but 1/6 없음 → Stage2 no-price.

Alteogen:
2,3,4,5,7 충족 but direct price 없음 → Stage3-Yellow candidate.

Hugel:
2,3,5,7 충족 but direct price and sell-through 없음 → Stage2.

Jeisys:
2,3,5 충족 but price little changed and delisting → Stage2 reference only.

Samsung Bioepis litigation:
negative 4B → 승격 금지.
```

---

# 11. Stage3-Yellow 조건

```text
Stage3-Yellow:
Stage2-Actionable 이후 아래 중 2개 이상이 추가로 닫히면 Yellow.

1. CDMO utilization / orderbook / customer transfer 확인
2. FDA/EMA approval plus commercial launch
3. royalty or product-supply revenue visibility
4. patent/litigation risk contained
5. reimbursement / payer / physician adoption 확인
6. U.S. tariff hedge converted into margin or volume benefit
7. facility acquisition integration on schedule
```

Yellow 후보:

```text
Alteogen:
approval + launch + royalty/supply revenue + Halozyme risk containment 확인 시 Yellow 유지/상향.

SK Bioscience:
IDT utilization + orderbook + margin 확인 시 Yellow.

Samsung Biologics:
policy support가 계약/가동률/margin으로 연결되면 Yellow.

Celltrion:
U.S. product transfer + margin + tariff benefit 확인 시 Yellow.

Hugel:
Letybo U.S. sell-through + reorder + margin 확인 시 Yellow.
```

---

# 12. Stage3-Green 조건

```text
Stage3-Green:
- regulatory approval or facility acquisition converts into recurring revenue.
- CDMO utilization and margin are visible.
- platform royalty or supply economics are disclosed or inferable.
- patent/litigation/manufacturing-inspection risks are contained.
- launch sell-through and reimbursement are confirmed.
- full-window MFE/MAE is favorable.
```

이번 R7 Loop 17에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
reason = full OHLC unavailable + utilization/royalty/sell-through/patent-clearance gates not fully closed
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- FDA approval without launch sell-through.
- CDMO facility acquisition without utilization.
- policy support without company-specific contract.
- platform link without royalty economics.
- patent litigation around biosimilars or enzyme platform.
- U.S. tariff policy uncertainty.
- medical device M&A delisting / liquidity exit.
- FDA inspection or manufacturing CMC issue.
```

적용:

```text
Samsung Bio:
GSK facility price failed + utilization 4B.

Celltrion:
U.S. factory tariff hedge + capex/utilization 4B.

Alteogen:
Halozyme patent dispute 4B.

Hugel:
U.S. physician adoption / price competition 4B.

Jeisys:
delisting / liquidity exit 4B.

Samsung Bioepis:
Amgen patent lawsuit 4B.

SK Bioscience:
IDT integration/utilization 4B.
```

---

# 14. 4C hard gate 조건

```text
R7 4C:
- FDA CRL / approval rejection with stock crash
- pivotal trial failure
- manufacturing inspection failure preventing launch
- patent ruling permanently blocking product
- safety signal causing withdrawal
- reimbursement denial destroying commercial case
```

이번 R7 Loop 17에서는 **hard stock-specific 4C 확정 없음**.

```text
hard_4c_not_confirmed = true
reason = sourced Korean cases in this round were mostly Stage2/4B; no reliable Korean hard-4C price anchor was captured in the source set.
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

R7 production 설계 원칙:

```text
1. approval / deal / facility headline과 actual commercial revenue를 분리한다.
2. CDMO는 capacity보다 utilization and margin을 우선한다.
3. platform biotech은 partner launch보다 royalty/supply economics를 우선한다.
4. FDA approval은 Stage2지만 sell-through/reimbursement 전에는 Green 금지다.
5. biosimilar opportunity는 patent clearance 전까지 4B를 붙인다.
6. M&A valuation reference는 public-stock price reaction and liquidity를 확인한다.
7. hard 4C는 FDA CRL/trial failure/manufacturing failure + price anchor가 있을 때만 준다.
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_256.md 요약

```md
# R7 Loop 17. Bio / Healthcare / Medical Device Trigger-level Price Validation

이번 라운드는 R7 Loop 17 trigger-level validation 라운드다.

핵심 결론:
- SK Bioscience / IDT Biologika is the cleanest R7 Stage2-Actionable case. SK Bioscience acquired a 60% stake in German CDMO IDT Biologika for 339B won / $243.75M, and shares rose 11.7% in morning trade. Green requires utilization, margin and orderbook.
- Samsung Biologics / pharma policy support is Stage2-Actionable policy support. The Korean pharma sector rose 3.97%, Samsung Biologics +6.23%, KOSPI +0.99% after Korea pledged support for biopharma exporters facing U.S. tariff risk.
- Samsung Biologics / GSK U.S. facility is evidence_good_but_price_failed. The company agreed to buy GSK's U.S. drug production facility for $280M with 60,000L drug-substance capacity, but shares fell 0.4% while the broader market rose 2%.
- Celltrion / U.S. factory is Stage2 no-price. Celltrion became preferred bidder for a U.S. pharma factory, acquired Eli Lilly's ImClone facility for $330M, and later announced up to 700B won / $478M expansion. Direct stock-price anchor unavailable.
- Alteogen / Keytruda SC is Stage3-Yellow candidate. Merck's SC Keytruda uses Alteogen's enzyme, with expected 30~40% peak adoption and Keytruda 2024 sales near $30B. Halozyme patent dispute remains 4B.
- Hugel / Letybo is Stage2 regulatory/commercial launch. Letybo received U.S. FDA approval for glabellar lines and began reaching U.S. dermatology offices. U.S. sell-through and margin are missing.
- Jeisys Medical / ArchiMed is Stage2 M&A valuation reference. ArchiMed acquired Jeisys Medical for about $742M; shares closed around 12,860 won, little changed, and delisting limits public-stock upside.
- Samsung Bioepis / Amgen is biosimilar patent-litigation 4B. Amgen sued over Prolia/Xgeva biosimilars, alleging 34 patents, with Prolia/Xgeva prior-year U.S. sales over $4.2B.

Main calibration:
- Raise manufacturing_asset_MA, biopharma_policy_support, US_localization_tariff_hedge, blockbuster_platform_linkage, FDA_approval_commercial_launch, medical_device_MA_valuation, patent_litigation_risk, utilization_margin_conversion.
- Lower facility_acquisition_without_price_validation, policy_support_without_company_contract, FDA_approval_without_sellthrough, platform_link_without_royalty_visibility, MA_reference_without_public_liquidity, biosimilar_opportunity_without_patent_clearance, CDMO_capacity_without_utilization, hard_4C_without_sourced_price_anchor.
```

## docs/checkpoints/checkpoint_28a_round256_r7_loop17.md 요약

```md
# Checkpoint 28A Round 256 R7 Loop 17 Trigger-level Calibration

## 반영 내용
- R7 Loop 17 trigger-level validation을 수행했다.
- SK Bioscience/IDT, Samsung Biologics policy support, Samsung Biologics/GSK U.S. facility, Celltrion U.S. factory, Alteogen/Keytruda SC, Hugel/Letybo, Jeisys/ArchiMed, Samsung Bioepis/Amgen litigation을 검토했다.
- full adjusted OHLC는 확보하지 못했으므로 Reuters / FT / WSJ / MarketWatch / Allure reported event return과 event price anchor를 사용했다.
- MFE/MAE는 조작하지 않고 price_data_unavailable_after_deep_search로 분리했다.

## 핵심 보정
- CDMO and facility acquisition triggers require utilization and margin before Green.
- Pharma policy support can promote Stage2, but not company-specific Green without contracts.
- Platform biotech needs royalty/supply economics and patent-risk containment.
- FDA approval is Stage2; sell-through/reimbursement is Yellow/Green gate.
- Patent litigation is a core 4B for biosimilar/platform cases.
- Hard 4C must require FDA CRL/trial failure/manufacturing failure plus sourced price anchor.
```

## data/e2r_case_library/cases_r7_loop17_round256.jsonl 초안

```jsonl
{"case_id":"r7_loop17_sk_bioscience_idt_biologika","symbol":"302440","company_name":"SK Bioscience","case_type":"Stage2_Actionable_vaccine_CDMO_cross_border_MA","primary_archetype":"VACCINE_CDMO_CROSS_BORDER_MA_STAGE2_ACTIONABLE","best_trigger":"T1/T3","stage_candidate":"Stage2-Actionable","price_validation":{"trigger_date":"2024-06-27","stake_acquired_pct":60,"deal_value_krw_bn":339,"deal_value_usd_mn":243.75,"event_return_pct":11.7,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_actionable_CDMO_MA","notes":"M&A plus price reaction aligned; Green requires utilization, margin and orderbook."}
{"case_id":"r7_loop17_samsung_biologics_policy_support","symbol":"207940","company_name":"Samsung Biologics","case_type":"Stage2_Actionable_biopharma_policy_support","primary_archetype":"BIOPHARMA_POLICY_SUPPORT_STAGE2_ACTIONABLE","best_trigger":"T1/T3","stage_candidate":"Stage2-Actionable","price_validation":{"trigger_date":"2025-05-21","pharma_sector_event_return_pct":3.97,"samsung_biologics_event_return_pct":6.23,"celltrion_same_context_return_pct":0.35,"kospi_same_context_pct":0.99,"market_relative_return_pp":5.24,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"good_stage2_policy_support_not_green","notes":"Policy support worked as Stage2; company-specific contract/utilization/margin needed for Yellow."}
{"case_id":"r7_loop17_samsung_biologics_gsk_us_facility","symbol":"207940","company_name":"Samsung Biologics","case_type":"evidence_good_but_price_failed_CDMO_US_facility","primary_archetype":"CDMO_US_FACILITY_TARIFF_HEDGE_STAGE2_PRICE_FAILED","best_trigger":"T0/T2","stage_candidate":"Stage2 only","price_validation":{"trigger_date":"2025-12-22","deal_value_usd_mn":280,"facility_capacity_liters":60000,"event_return_pct":-0.4,"broader_market_same_context_pct":2.0,"market_relative_return_pp":-2.4,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"evidence_good_but_price_failed","notes":"Facility acquisition is strategically useful but price failed; utilization and customer transfer required."}
{"case_id":"r7_loop17_celltrion_us_factory_localization","symbol":"068270","company_name":"Celltrion","case_type":"Stage2_US_factory_tariff_hedge_no_price","primary_archetype":"BIOSIMILAR_US_LOCALIZATION_STAGE2_NO_PRICE","best_trigger":"T0/T3","stage_candidate":"Stage2","price_validation":{"preferred_bidder_date":"2025-07-29","planned_initial_investment_krw_bn":700,"imclone_acquisition_value_usd_mn":330,"additional_expansion_investment_krw_bn":700,"additional_expansion_investment_usd_mn":478,"direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_US_localization_no_price","notes":"U.S. localization hedges tariff risk, but direct price and margin/utilization are unavailable."}
{"case_id":"r7_loop17_alteogen_keytruda_sc","symbol":"196170","company_name":"Alteogen","case_type":"Stage3_Yellow_candidate_platform_enzyme_blockbuster","primary_archetype":"PLATFORM_ENZYME_BLOCKBUSTER_STAGE3_YELLOW","best_trigger":"T0/T3","stage_candidate":"Stage3-Yellow_candidate","price_validation":{"clinical_trigger_date":"2024-11-19","launch_plan_date":"2025-03-27","merck_planned_us_launch_date":"2025-10-01","fda_target_action_date":"2025-09-23","keytruda_2024_sales_usd_bn":"nearly_30","expected_peak_adoption_pct":"30-40","administration_time_sc_minutes":2,"administration_time_iv_minutes":30,"direct_alteogen_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage3_Yellow_candidate_not_Green","notes":"Blockbuster platform linkage is strong, but royalty/supply revenue and patent-risk containment are gates."}
{"case_id":"r7_loop17_hugel_letybo_us_fda","symbol":"145020","company_name":"Hugel","case_type":"Stage2_aesthetic_toxin_US_FDA_launch","primary_archetype":"AESTHETIC_TOXIN_US_FDA_STAGE2","best_trigger":"T0/T3","stage_candidate":"Stage2","price_validation":{"approval_context":"US_FDA_approval_for_glabellar_lines","commercial_rollout_context":"US_dermatology_offices_from_March_2025","estimated_letybo_unit_price_usd":"9-12","estimated_botox_unit_price_usd":"12-18","direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_FDA_launch_no_price","notes":"FDA approval and U.S. rollout are Stage2; sell-through, adoption and margin are gates."}
{"case_id":"r7_loop17_jeisys_archimed_medical_aesthetic_ma","symbol":"287410","company_name":"Jeisys Medical","case_type":"Stage2_medical_aesthetic_device_MA_reference","primary_archetype":"MEDICAL_AESTHETIC_DEVICE_MA_STAGE2","best_trigger":"T0/T2","stage_candidate":"Stage2 reference","price_validation":{"trigger_date":"2024-09-11","deal_value_usd_mn":742,"event_close_price_krw":12860,"price_reaction_context":"little_changed","device_category":"energy_based_devices_EBD","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"MA_valuation_reference_not_actionable","notes":"M&A validates medical aesthetics valuation but delisting/liquidity limits listed-stock upside."}
{"case_id":"r7_loop17_samsung_bioepis_amgen_patent_litigation","symbol":"207940_readthrough","company_name":"Samsung Bioepis / Samsung Biologics readthrough","case_type":"4B_biosimilar_patent_litigation","primary_archetype":"BIOSIMILAR_PATENT_LITIGATION_4B","best_trigger":"T0/T3","stage_candidate":"4B-watch","price_validation":{"trigger_date":"2024-08-13","plaintiff":"Amgen","defendant":"Samsung_Bioepis","products":["Prolia_biosimilar","Xgeva_biosimilar"],"patents_alleged_infringed":34,"prolia_us_sales_prior_year_usd_bn":2.7,"xgeva_us_sales_prior_year_usd_bn":1.5,"direct_price_anchor":"price_data_unavailable_after_deep_search","hard_4C_status":"not_confirmed"},"score_price_alignment":"biosimilar_patent_litigation_4B_not_4C","notes":"Large biosimilar opportunity, but patent litigation can delay or reduce launch economics."}
```

## data/e2r_trigger_calibration/triggers_r7_loop17_round256.jsonl 초안

```jsonl
{"trigger_id":"r7l17_sk_bioscience_idt_T1","case_id":"r7_loop17_sk_bioscience_idt_biologika","trigger_type":"Stage2-Actionable_CDMO_MA","trigger_date":"2024-06-27","event_return_pct":11.7,"trigger_outcome_label":"excellent_stage2_actionable_CDMO_MA","promote_to":"Stage2-Actionable"}
{"trigger_id":"r7l17_samsung_bio_policy_T1","case_id":"r7_loop17_samsung_biologics_policy_support","trigger_type":"Stage2-Actionable_biopharma_policy_support","trigger_date":"2025-05-21","event_return_pct":6.23,"market_relative_pp":5.24,"trigger_outcome_label":"good_stage2_policy_support_not_green","promote_to":"Stage2-Actionable"}
{"trigger_id":"r7l17_samsung_bio_gsk_T0","case_id":"r7_loop17_samsung_biologics_gsk_us_facility","trigger_type":"evidence_good_but_price_failed_CDMO_US_facility","trigger_date":"2025-12-22","event_return_pct":-0.4,"market_relative_pp":-2.4,"trigger_outcome_label":"evidence_good_but_price_failed","promote_to":"no_actionable"}
{"trigger_id":"r7l17_celltrion_us_factory_T0","case_id":"r7_loop17_celltrion_us_factory_localization","trigger_type":"Stage2_US_factory_tariff_hedge","trigger_date":"2025-07-29","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage2_US_localization_no_price","promote_to":"Stage2"}
{"trigger_id":"r7l17_alteogen_keytruda_T0","case_id":"r7_loop17_alteogen_keytruda_sc","trigger_type":"Stage3-Yellow_candidate_platform_blockbuster","trigger_date":"2024-11-19","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage3_Yellow_candidate_not_Green","promote_to":"Stage3-Yellow_candidate"}
{"trigger_id":"r7l17_hugel_letybo_T0","case_id":"r7_loop17_hugel_letybo_us_fda","trigger_type":"Stage2_FDA_commercial_launch","trigger_date":"2025-03","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage2_FDA_launch_no_price","promote_to":"Stage2"}
{"trigger_id":"r7l17_jeisys_archimed_T0","case_id":"r7_loop17_jeisys_archimed_medical_aesthetic_ma","trigger_type":"Stage2_medical_device_MA_reference","trigger_date":"2024-09-11","event_return_pct":"little_changed_at_12860_KRW","trigger_outcome_label":"MA_valuation_reference_not_actionable","promote_to":"Stage2_reference"}
{"trigger_id":"r7l17_samsung_bioepis_amgen_T0","case_id":"r7_loop17_samsung_bioepis_amgen_patent_litigation","trigger_type":"4B_biosimilar_patent_litigation","trigger_date":"2024-08-13","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"biosimilar_patent_litigation_4B_not_4C","promote_to":"4B-watch"}
```

## data/sector_taxonomy/score_weight_profiles_round256_r7_loop17_v1.csv 초안

```csv
archetype,manufacturing_asset_MA,biopharma_policy_support,US_localization_tariff_hedge,blockbuster_platform_linkage,FDA_approval_commercial_launch,medical_device_MA_valuation,patent_litigation_risk,utilization_margin_conversion,facility_acquisition_without_price_validation_penalty,policy_support_without_company_contract_penalty,FDA_approval_without_sellthrough_penalty,platform_link_without_royalty_visibility_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
VACCINE_CDMO_CROSS_BORDER_MA_STAGE2_ACTIONABLE,+5,+1,+3,+0,+1,+1,+1,+5,-2,-1,-1,-1,SK Bioscience IDT +11.7%,utilization/margin missing,orderbook+utilization+margin,SK Bioscience.
BIOPHARMA_POLICY_SUPPORT_STAGE2_ACTIONABLE,+1,+5,+3,+0,+0,+0,+1,+3,-1,-4,-1,-1,Samsung Bio +6.23 on policy support,company-specific contract missing,contract+utilization+margin,Samsung Biologics.
CDMO_US_FACILITY_TARIFF_HEDGE_STAGE2_PRICE_FAILED,+4,+1,+5,+0,+0,+0,+1,+5,-5,-1,-1,-1,GSK facility good but price failed,actionable prohibited,customer transfer+utilization,Samsung Bio.
BIOSIMILAR_US_LOCALIZATION_STAGE2_NO_PRICE,+4,+1,+5,+1,+1,+0,+2,+5,-3,-1,-1,-1,Celltrion US factory,price unavailable,product transfer+margin,Celltrion.
PLATFORM_ENZYME_BLOCKBUSTER_STAGE3_YELLOW,+0,+0,+1,+5,+3,+0,+5,+4,-1,-1,-1,-5,Keytruda SC platform,patent/royalty gate,approval+royalty+patent containment,Alteogen.
AESTHETIC_TOXIN_US_FDA_STAGE2,+0,+0,+1,+0,+5,+2,+2,+4,-1,-1,-5,-1,Letybo FDA launch,sell-through missing,physician adoption+margin,Hugel.
MEDICAL_AESTHETIC_DEVICE_MA_STAGE2,+1,+0,+0,+0,+1,+5,+1,+3,-1,-1,-1,-1,Jeisys ArchiMed M&A,delisting/liquidity,listed peer rerating+sell-through,Jeisys.
BIOSIMILAR_PATENT_LITIGATION_4B,+0,+0,+0,+2,+2,+0,+5,+2,-1,-1,-1,-2,Amgen lawsuit 34 patents,launch delay risk,settlement/clearance,Samsung Bioepis.
```

---

# 이번 R7 Loop 17 결론

```text
1. SK Bioscience / IDT Biologika는 R7의 가장 좋은 Stage2-Actionable이다.
   339B won / $244M M&A와 +11.7% 가격반응이 닫혔다.

2. Samsung Biologics policy support는 Stage2-Actionable이다.
   pharma sector +3.97%, Samsung Bio +6.23%, KOSPI +0.99%로 정책 trigger는 가격검증을 통과했다.

3. Samsung Biologics / GSK facility는 evidence_good_but_price_failed다.
   $280M U.S. facility, 60,000L capacity는 좋지만 주가는 -0.4%, market은 +2%였다.

4. Celltrion U.S. factory는 Stage2 no-price다.
   $330M ImClone acquisition과 최대 700B won expansion은 tariff hedge지만 직접 가격 anchor가 없다.

5. Alteogen / Keytruda SC는 Stage3-Yellow 후보이다.
   $30B Keytruda franchise, 30~40% adoption target은 강하지만 royalty와 patent risk가 gate다.

6. Hugel / Letybo는 Stage2 FDA/commercial launch다.
   U.S. FDA approval은 좋지만 U.S. sell-through와 margin 확인 전에는 Green 금지다.

7. Jeisys / ArchiMed는 medical aesthetic M&A valuation reference다.
   $742M acquisition은 sector reference지만 shares는 little changed였고 delisting risk가 있다.

8. Samsung Bioepis / Amgen lawsuit는 biosimilar patent-litigation 4B다.
   34 patents, Prolia/Xgeva $4.2B+ U.S. sales opportunity는 크지만 litigation이 launch economics를 흔든다.

9. 이번 R7에서는 sourced Korean hard 4C를 억지로 만들지 않는다.
   FDA CRL, 임상 실패, manufacturing failure는 price anchor와 같이 확인될 때만 hard 4C로 올린다.
```

한 문장으로 압축하면:

> **R7 Loop 17에서 배운 핵심은 “FDA approval·CDMO 공장·M&A·blockbuster partner headline”이 아니라, utilization, launch sell-through, royalty/supply revenue, reimbursement, patent clearance, facility margin이 닫혀야 Stage3로 올릴 수 있다는 것이다. Stage2를 너무 보수적으로 두면 SK Bioscience/Alteogen 같은 후보를 놓치고, headline만 믿고 Green을 주면 Samsung Bio GSK facility처럼 price failed이거나 patent/litigation 4B에 걸린다.**

다음 순서는 **R8 Loop 17 — 플랫폼·콘텐츠·SW·보안**이다.

[1]: https://www.reuters.com/markets/deals/south-koreas-sk-bioscience-buy-control-germanys-idt-biologika-244-mln-2024-06-27/ "https://www.reuters.com/markets/deals/south-koreas-sk-bioscience-buy-control-germanys-idt-biologika-244-mln-2024-06-27/"
[2]: https://www.reuters.com/business/healthcare-pharmaceuticals/south-korean-shares-rise-1-pharmaceutical-stocks-jump-2025-05-21/ "https://www.reuters.com/business/healthcare-pharmaceuticals/south-korean-shares-rise-1-pharmaceutical-stocks-jump-2025-05-21/"
[3]: https://www.reuters.com/business/healthcare-pharmaceuticals/samsung-biologics-buy-us-drug-production-facility-gsk-280-mln-2025-12-21/ "https://www.reuters.com/business/healthcare-pharmaceuticals/samsung-biologics-buy-us-drug-production-facility-gsk-280-mln-2025-12-21/"
[4]: https://www.reuters.com/business/healthcare-pharmaceuticals/south-koreas-celltrion-says-tapped-buy-us-pharma-factory-offset-tariff-risk-2025-07-29/ "https://www.reuters.com/business/healthcare-pharmaceuticals/south-koreas-celltrion-says-tapped-buy-us-pharma-factory-offset-tariff-risk-2025-07-29/"
[5]: https://www.reuters.com/business/healthcare-pharmaceuticals/merck-says-keytruda-injection-par-with-approved-iv-version-trial-2024-11-19/ "https://www.reuters.com/business/healthcare-pharmaceuticals/merck-says-keytruda-injection-par-with-approved-iv-version-trial-2024-11-19/"
[6]: https://www.allure.com/story/letybo-neuromodulator-injectable "https://www.allure.com/story/letybo-neuromodulator-injectable"
[7]: https://www.wsj.com/articles/europes-archimed-bets-on-anti-aging-trend-in-first-asia-deal-cbe16f5e "https://www.wsj.com/articles/europes-archimed-bets-on-anti-aging-trend-in-first-asia-deal-cbe16f5e"
[8]: https://www.reuters.com/legal/litigation/amgen-sues-samsung-biotech-unit-over-bone-drug-copies-2024-08-13/ "https://www.reuters.com/legal/litigation/amgen-sues-samsung-biotech-unit-over-bone-drug-copies-2024-08-13/"
