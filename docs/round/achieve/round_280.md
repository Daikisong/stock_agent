순서상 이번은 **R11 Loop 13 — 정책·지정학·재난·이벤트 가격경로 검증 라운드**다.

```text
round = R11 Loop 13
round_id = round_208
large_sector = POLICY_GEOPOLITICS_DISASTER_EVENT
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true_for_macro_geopolitical_political_disaster_reference
next_round = R12 Loop 13
```

이번 R11은 **정치 충격, 중동 전쟁·유가·환율, AI 초과세수/배당 논쟁, 삼성전자 파업·정부개입, 중국 희토류·반도체 end-use 통제, 한미 관세협상, 중국 fab 장비 라이선스 relief, 대형 산불 disaster reference**를 묶어서 본다.

수정주가 일봉 OHLC 전체 구간은 이번 환경에서 안정적으로 확보하지 못했다. 그래서 30D/90D/180D/1Y full MFE·MAE는 만들지 않고, Reuters/FT/AP/WSJ/Barron’s가 보도한 **event return, index drawdown, 개별 대형주 event return, 환율, 정책금액, 피해규모**를 가격 anchor로 사용했다. full OHLC가 필요한 칸은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R11 = 정책·지정학·재난·이벤트
```

R11에서 진짜 Stage 3는 “정책이 좋다”, “정부가 돈을 푼다”, “전쟁 수혜”, “관세 완화”, “공급망 국산화”, “재난 복구”, “AI 배당” 같은 문장이 아니다.

R11의 핵심은 더 차갑다.

```text
정책 이벤트:
법안 / 예산 / 시행령 / 기업별 수혜 / EPS bridge 확인

지정학 이벤트:
에너지·FX·공급망·수출통제·관세가 실제 원가·마진·물량에 미치는 영향 확인

재난 이벤트:
보험·복구·건설·유통·농산물·전력망 피해가 실제 비용/수요로 닫히는지 확인

정치 이벤트:
국가 risk premium / 환율 / 외국인 수급 / sovereign credibility 확인
```

---

# 2. 대상 canonical archetype

```text
POLITICAL_SHOCK_KOREA_DISCOUNT_HARD_GATE
MIDDLE_EAST_ENERGY_FX_MACRO_HARD_4C
AI_WINDFALL_FISCAL_REDISTRIBUTION_EVENT
SYSTEMIC_LABOR_SUPPLY_CHAIN_INTERVENTION
RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C
US_KOREA_TARIFF_POLICY_4C_WATCH
CHINA_FAB_EXPORT_LICENSE_RELIEF
CLIMATE_DISASTER_SUPPLY_CHAIN_REFERENCE
```

---

# 3. deep sub-archetype

```text
정치 충격:
- 2024 martial law crisis
- KOSPI / won / Korea discount
- unlimited liquidity / 10T won stabilisation fund

중동 전쟁·에너지:
- Iran conflict
- Strait of Hormuz / oil import dependence
- KOSPI -12.06%, won 17-year low
- Samsung / SK Hynix / Hyundai / Korean Air selloff

AI 초과세수·분배:
- presidential adviser AI bonus proposal
- Samsung / SK Hynix / KOSPI selloff
- excess tax revenue vs corporate profit redistribution distinction

삼성 파업·공급망:
- 45,000 workers, 18-day strike threat
- emergency arbitration
- Samsung 22.8% of exports, 26% of domestic stock market
- one-day semiconductor factory halt up to 1T won direct loss

희토류·전략광물:
- China rare-earth export controls
- defence users denied; advanced semis case-by-case
- yttrium / dysprosium / terbium / indium
- Samsung / SK / Hanwha Ocean supply-chain risk

한미 관세:
- 15% tariff on Korean imports including autos
- Hyundai / Kia shares reaction
- semiconductor/pharma tariff cap at 15%
- policy relief vs margin damage

중국 fab 장비:
- Samsung / SK Hynix annual license for 2026
- validated end user status expiration
- temporary relief, not Green

재난:
- 2025 South Korea wildfires
- 32 deaths, 104,000 hectares, 5,000 buildings
- climate change made event twice as likely
```

---

# 4. 국장 신규 후보 case

## Case A — Martial law / Korea discount `political hard 4C reference`

```text
symbols = KOSPI / KRW / 005930 / 000660 / financial-market basket
case_type = 4C-thesis-break-reference
archetype = POLITICAL_SHOCK_KOREA_DISCOUNT_HARD_GATE
```

### stage date

```text
Stage 1:
2024-12-03
- President Yoon declares martial law
- political activity / media restriction attempted
- parliament overturns decree within hours

Stage 4C:
2024-12-04
- KOSPI down 1.4% in Reuters close context
- other global-market report: KOSPI down nearly 2%
- won near two-year low
- finance ministry prepared "unlimited" liquidity
- regulator ready to deploy 10T won stock-market stabilisation fund
- Korea discount risk premium re-priced

Stage 3:
N/A
```

Martial law shock는 R11의 정치 hard gate다. Reuters는 martial law가 해제됐음에도 KOSPI가 1.4% 하락했고, won이 2년 저점 부근에 머물렀으며, 금융당국이 10조 원 규모 stock-market stabilisation fund를 준비했다고 보도했다. 이 case는 “국장 valuation discount”가 단순한 말이 아니라 정치 event 하나로 FX·index·외국인 risk premium에 즉시 반영된다는 기준이다. ([Reuters][1])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters martial-law political-shock anchors",
  "stage3_price": null,
  "stage4c_date": "2024-12-04",
  "kospi_close_mae_pct": -1.4,
  "kospi_intraday_context_pct": -2.0,
  "kospi_ytd_loss_context_pct": -7.0,
  "won_context": "near_two_year_low",
  "won_ytd_decline_context_pct": -9.0,
  "stock_market_stabilisation_fund_krw_trn": 10.0,
  "liquidity_commitment": "unlimited_liquidity_if_needed",
  "martial_law_duration_hours": 6,
  "mfe": "N/A",
  "mae_30d_90d_180d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break_reference
rerating_result = political_risk_premium_hard_gate
stage_failure_type = Korea_discount_political_shock
```

---

## Case B — Iran / Middle East energy shock `macro hard 4C`

```text
symbols = KOSPI / KRW / 005930 / 000660 / 005380 / 003490
case_type = 4C-thesis-break
archetype = MIDDLE_EAST_ENERGY_FX_MACRO_HARD_4C
```

### stage date

```text
Stage 1:
2026-02-28
- Iran conflict begins
- oil / FX volatility rises
- Korea vulnerable due Middle East oil dependence

Stage 4C:
2026-03-04
- KOSPI -12.06% to 5,093.54
- intraday low -12.65%
- previous day -7.24%
- market cap wipeout 817.6T won / $553.82B over two days
- won hits 1,505.8/USD, weakest since March 2009
- Samsung -11.7%
- SK Hynix -9.6%
- Hyundai Motor -15.8%
- Korean Air -7.9%
- Korea sources about 70% of oil purchases from Middle East

Stage 4B/4C validation:
2026-03-26
- panic selloff later described as valuation reset rather than earnings collapse
- but energy-intensive sectors remain vulnerable if disruptions persist

Stage 3:
N/A
```

Iran conflict는 R11의 가장 강한 macro hard 4C다. Reuters는 2026년 3월 4일 KOSPI가 12.06% 급락해 5,093.54에 마감했고, 이틀 동안 817.6조 원, 약 $553.82B의 시총이 사라졌다고 보도했다. 한국은 세계 4위 oil buyer이고 oil purchase의 약 70%를 Middle East에서 조달하기 때문에, 이 event는 “유가·환율·공급망”이 국장 전체 beta를 한 번에 꺾는 hard gate다. ([Reuters][2])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters Iran conflict macro-market anchors",
  "stage3_price": null,
  "stage4c_date": "2026-03-04",
  "kospi_close": 5093.54,
  "kospi_close_mae_pct": -12.06,
  "kospi_intraday_mae_pct": -12.65,
  "kospi_previous_day_mae_pct": -7.24,
  "two_day_market_cap_wipeout_krw_trn": 817.6,
  "two_day_market_cap_wipeout_usd_bn": 553.82,
  "won_intraday_low_per_usd": 1505.8,
  "won_close_per_usd": 1485.7,
  "won_close_decline_pct": -3.1,
  "middle_east_oil_purchase_share_pct": 70,
  "samsung_event_mae_pct": -11.7,
  "sk_hynix_event_mae_pct": -9.6,
  "hyundai_motor_event_mae_pct": -15.8,
  "korean_air_event_mae_pct": -7.9,
  "mfe": "N/A",
  "mae_30d_90d_180d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = middle_east_energy_fx_macro_hard_4C
stage_failure_type = oil_FX_index_deleveraging
```

---

## Case C — AI bonus / windfall redistribution `policy event premium + 4B-watch`

```text
symbols = 005930 / 000660 / KOSPI
case_type = event_premium + 4B-watch
archetype = AI_WINDFALL_FISCAL_REDISTRIBUTION_EVENT
```

### stage date

```text
Stage 1:
2026-05-12
- presidential policy chief floats AI bonus / citizen dividend idea
- debate over excess tax revenues from semiconductor boom
- investor concern over anti-market or windfall-tax-like policy

Stage 4B/4C-watch:
2026-05-12
- Samsung -3.5%
- SK Hynix -1.4%
- KOSPI fell as much as -5%
- MarketWatch/Barron's context: KOSPI closed -2.3%
- official clarification later: discussion concerned excess tax revenue, not direct seizure of corporate profits

Stage 3:
N/A
```

AI bonus 논쟁은 R11의 “정책 말 한마디가 4B 이후 시장을 흔드는” case다. FT는 대통령 정책실장의 AI bonus 발언 이후 Samsung이 3.5%, SK Hynix가 1.4% 하락했고, KOSPI가 장중 최대 5% 밀렸다고 보도했다. MarketWatch/Barron’s는 같은 selloff를 KOSPI close -2.3%로 정리했다. 실제 정책은 초과세수 사용 논의였고 corporate profits 자체를 빼앗는 구조로 확인되지는 않았지만, 시장이 고점권일 때 분배·세금 언급은 즉시 4B-watch로 작동한다. ([Financial Times][3])

### 실제 가격경로 검증

```json
{
  "price_data_source": "FT / Barron's / MarketWatch AI bonus policy-reaction anchors",
  "stage3_price": null,
  "stage4b_date": "2026-05-12",
  "samsung_event_mae_pct": -3.5,
  "sk_hynix_event_mae_pct": -1.4,
  "kospi_intraday_mae_pct": -5.0,
  "kospi_close_mae_pct": -2.3,
  "policy_object": "excess_tax_revenue_from_AI_semiconductor_boom",
  "corporate_profit_seizure_confirmed": false,
  "ai_tax_or_windfall_tax_legislation_confirmed": false,
  "mfe": "N/A",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium_4B_watch
rerating_result = AI_windfall_fiscal_redistribution_policy_watch
stage_failure_type = policy_comment_not_production_EPS_green
```

---

## Case D — Samsung strike / emergency arbitration `systemic labor 4C-watch`

```text
symbol = 005930
case_type = 4C-watch
archetype = SYSTEMIC_LABOR_SUPPLY_CHAIN_INTERVENTION
```

### stage date

```text
Stage 1:
2026-04~05
- Samsung union demands removal of bonus cap
- union seeks 15% of operating profit in bonus pool
- pay gap with SK Hynix becomes social/political issue

Stage 4C-watch:
2026-05-17
- government says all options including emergency arbitration possible
- one-day semiconductor factory suspension may cause up to 1T won direct loss
- longer disruption could cause up to 100T won economic damage
- emergency arbitration would ban industrial action for 30 days
- Samsung accounts for 22.8% of Korea exports and 26% of domestic stock market
- Samsung employs more than 120,000 people and works with 1,700 suppliers

Stage 4C-watch market validation:
2026-05-19
- 45,000 workers threaten 18-day strike
- Samsung shares -2.5%
- KOSPI -3.2%
- court requires essential staffing during any strike

Stage 3:
N/A
```

Samsung strike는 R11에서 labor event가 단순 노사 이슈가 아니라 국가 공급망·수출·지수 안정성까지 연결되는 case다. Reuters는 하루 생산 중단 손실이 최대 1조 원, 장기 차질의 경제 피해가 최대 100조 원이 될 수 있다고 보도했다. 5월 19일 협상 재개일에는 45,000명 strike threat 속에 Samsung이 -2.5%, KOSPI가 -3.2% 하락했다. ([Reuters][4])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters Samsung strike / government intervention anchors",
  "stage3_price": null,
  "stage4c_watch_date": "2026-05-17/2026-05-19",
  "threatened_workers": 45000,
  "strike_duration_days": 18,
  "one_day_direct_loss_krw_trn": 1.0,
  "potential_economic_damage_krw_trn": 100,
  "emergency_arbitration_ban_days": 30,
  "samsung_export_share_pct": 22.8,
  "samsung_domestic_stock_market_share_pct": 26,
  "samsung_employees": 120000,
  "supplier_count": 1700,
  "samsung_event_mae_pct": -2.5,
  "kospi_same_context_mae_pct": -3.2,
  "court_essential_staffing_required": true,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = systemic_labor_supply_chain_4C_watch
stage_failure_type = AI_supercycle_profit_sharing_disruption
```

---

## Case E — China rare earth / end-use export controls `supply-chain 4C-watch`

```text
symbols = 005930 / 000660 / 042660 / defense-auto-semiconductor basket
case_type = 4C-watch
archetype = RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C
```

### stage date

```text
Stage 1:
2025-04
- China introduces rare-earth export controls in response to U.S. tariffs
- heavy rare earths become strategic leverage

Stage 4C-watch:
2025-10-09
- China tightens rare-earth export controls
- overseas defence users will not receive licences
- advanced semiconductor-related applications reviewed case-by-case
- China produces more than 90% of processed rare earths and rare-earth magnets
- foreign users of Chinese components/equipment may need export licences

Stage 4C-watch Korea validation:
2025-10-22
- South Korean trade envoy asks China to lift sanctions on Hanwha Ocean U.S. subsidiaries
- Korea also raises rare-earth export curbs
- curbs expected to affect Samsung and SK Hynix

Stage 4C-watch persistence:
2026-05
- heavy rare-earth exports yttrium, dysprosium, terbium still down about 50% since April 2025 controls
- latest White House statement acknowledges China export-control regime remains

Stage 3:
N/A
```

Rare-earth controls는 R11 supply-chain 4C-watch다. Reuters는 중국이 defence users에는 licences를 주지 않고 advanced semiconductor applications는 case-by-case review로 처리한다고 보도했다. 중국은 processed rare earths와 magnets의 90% 이상을 생산하며, 2026년 5월에도 yttrium·dysprosium·terbium exports는 controls 이후 약 50% 낮은 수준으로 남아 있었다. 한국 측은 Hanwha Ocean 제재와 rare-earth curbs를 같이 문제 삼았고, 해당 curbs가 Samsung과 SK Hynix에도 영향을 줄 수 있다고 밝혔다. ([Reuters][5])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters rare-earth export-control and Korea trade-envoy anchors",
  "stage3_price": null,
  "stage4c_watch_date": "2025-10-09/2025-10-22/2026-05",
  "processed_rare_earths_china_share_pct": 90,
  "rare_earth_magnets_china_share_pct": 90,
  "heavy_rare_earth_exports_decline_since_controls_pct": -50,
  "affected_elements": ["yttrium", "dysprosium", "terbium", "scandium", "indium"],
  "defence_user_license_policy": "not_granted",
  "advanced_semiconductor_license_policy": "case_by_case",
  "korea_affected_companies_context": ["Samsung Electronics", "SK Hynix", "Hanwha Ocean"],
  "direct_korean_stock_price_anchor": "price_data_unavailable_after_deep_search",
  "mfe_mae": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = rare_earth_export_control_supply_chain_gate
stage_failure_type = supply_chain_policy_risk_not_company_green
```

---

## Case F — U.S.-Korea tariffs / auto-policy shock `policy 4C-watch`

```text
symbols = 005380 / 000270 / 004020 / semiconductor-pharma basket
case_type = 4C-watch + policy_relief
archetype = US_KOREA_TARIFF_POLICY_4C_WATCH
```

### stage date

```text
Stage 1:
2025-03~04
- Trump imposes 25% auto tariffs
- Korean auto / steel / parts exports face margin shock

Stage 4C-watch:
2025-07-31
- U.S.-Korea trade deal sets 15% tariff on Korean imports including autos
- Hyundai Motor -4.5%
- Kia -6.6%
- 15% lower than prior 25%, but removes 2.5% advantage under Korea-U.S. FTA vs Japanese rivals
- South Korean negotiators wanted 12.5%, Trump wanted 15%

Stage 2 relief:
2025-12-01
- U.S. confirms 15% tariff retroactive to November 1
- airplane parts tariffs removed
- reciprocal rate un-stacked to match Japan/EU
- future national security tariffs on semiconductors and pharmaceuticals capped at 15%
- tied to Korea’s $350B strategic U.S. investment commitments

Stage 3:
없음
- tariff relief is not Green
- company Green requires gross margin, price pass-through, local production, incentive cost and FX bridge
```

한미 tariff deal은 relief이면서 동시에 4C-watch다. Reuters는 2025년 7월 31일 현대차가 -4.5%, 기아가 -6.6% 하락했다고 보도했다. 15% tariff는 25%보다 낮지만, 한미 FTA 아래 한국차가 일본차 대비 갖던 2.5% advantage를 없앴다. 12월에는 15% rate가 11월 1일부터 소급 적용되고 반도체·제약 국가안보 tariff cap도 15%로 정리됐지만, 기업 Stage 3는 margin과 pass-through가 확인된 후다. ([Reuters][6])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters U.S.-Korea tariff trade-deal anchors",
  "stage3_price": null,
  "stage4c_watch_date": "2025-07-31",
  "hyundai_event_mae_pct": -4.5,
  "kia_event_mae_pct": -6.6,
  "auto_tariff_new_pct": 15,
  "auto_tariff_prior_pct": 25,
  "tariff_reduction_pp": -10,
  "korea_fta_prior_advantage_vs_japan_pct": 2.5,
  "requested_tariff_pct_by_korea": 12.5,
  "retroactive_effective_date": "2025-11-01",
  "strategic_us_investment_commitment_usd_bn": 350,
  "future_semiconductor_pharma_tariff_cap_pct": 15,
  "airplane_parts_tariffs_removed": true,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break_watch_plus_policy_relief
rerating_result = US_Korea_tariff_policy_gate
stage_failure_type = tariff_relief_not_margin_green
```

---

## Case G — Samsung / SK Hynix China fab tool-license relief `policy relief, not Green`

```text
symbols = 005930 / 000660
case_type = success_candidate_policy_relief
archetype = CHINA_FAB_EXPORT_LICENSE_RELIEF
```

### stage date

```text
Stage 1:
2025-08~09
- U.S. revokes previous validated-end-user-style waivers
- Samsung / SK Hynix China fabs face uncertainty on U.S. chipmaking tools

Stage 2:
2025-12-30
- U.S. grants Samsung and SK Hynix annual licence to bring chipmaking equipment into China facilities for 2026
- temporary relief after earlier revocation of licence waivers
- Washington introduces annual approval system
- previous validated end user status expires Dec 31
- Samsung/SK China facilities remain key production bases, especially traditional memory

Stage 3:
없음
- annual license is relief
- Green requires multi-year visibility, capex execution, no license denial, China fab economics, margin continuity
```

China fab license는 R11 policy relief다. Reuters는 미국이 Samsung과 SK Hynix에 2026년 중국 fab 장비 반입 annual licence를 부여했다고 보도했다. 이는 relief지만, 기존 validated end user status가 끝나고 annual approval system으로 바뀌었다는 뜻이라 구조적 Green은 아니다. 매년 승인 리스크가 남으면 capex·생산전략·traditional memory margin에 계속 discount가 붙는다. ([Reuters][7])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters U.S. approval for Samsung/SK Hynix China tool shipments",
  "stage3_price": null,
  "stage2_date": "2025-12-30",
  "license_period": "2026_annual_license",
  "validated_end_user_status_expiry": "2025-12-31",
  "annual_approval_system": true,
  "company_context": ["Samsung Electronics", "SK Hynix"],
  "china_facility_role": "key_production_base_for_traditional_memory",
  "multi_year_visibility_confirmed": false,
  "license_denial_risk_removed": false,
  "price_validation_status": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_policy_relief
rerating_result = China_fab_tool_license_relief_stage2
stage_failure_type = annual_license_not_multiyear_green
```

---

## Case H — 2025 South Korea wildfires `climate disaster hard reference`

```text
symbols = insurers / construction / utilities / agriculture / logistics basket
case_type = disaster_hard_reference
archetype = CLIMATE_DISASTER_SUPPLY_CHAIN_REFERENCE
```

### stage date

```text
Stage 1:
2025-03-21
- multiple wildfires begin across southern South Korea
- dry conditions and strong winds
- disaster-zone designation

Stage 4C-reference:
2025-03~04
- Reuters climate attribution report: 32 people killed
- roughly 5,000 buildings destroyed
- fires consumed about 104,000 hectares
- four times prior record 25 years earlier
- climate change doubled likelihood and increased intensity by 15%
- initial Reuters/AP reports already showed 16~24 deaths, thousands evacuated, highest wildfire response level

Stage 3:
N/A
```

2025 wildfires는 R11 disaster hard reference다. Reuters는 World Weather Attribution study를 인용해 2025년 한국 산불이 32명을 사망하게 하고 약 5,000개 건물을 파괴했으며 104,000 hectares를 태웠다고 보도했다. 기후변화는 이런 event의 가능성을 두 배로 높이고 intensity를 15% 키운 것으로 평가됐다. 이 case는 보험·건설·농산물·전력망·물류를 평가할 때 “재난 복구 수혜”보다 먼저 **실제 피해비용·보험손해율·복구예산·공급망 차질**을 봐야 한다는 기준이다. ([Reuters][8])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters climate-attribution wildfire report + AP early disaster anchor",
  "stage3_price": null,
  "event_period": "2025-03_to_2025-04",
  "fatalities_final_context": 32,
  "buildings_destroyed_context": 5000,
  "area_burned_hectares": 104000,
  "prior_record_multiple": 4,
  "climate_change_likelihood_increase_multiple": 2,
  "climate_change_intensity_increase_pct": 15,
  "ap_early_fatalities": 24,
  "ap_early_injured": 26,
  "ap_early_evacuated": 28800,
  "ap_early_structures_destroyed": 300,
  "listed_stock_price_anchor": "price_data_unavailable_after_deep_search",
  "mfe_mae": "N/A_disaster_reference"
}
```

### alignment

```text
score_price_alignment = thesis_break_reference
rerating_result = climate_disaster_supply_chain_hard_reference
stage_failure_type = disaster_cost_before_rebuild_beneficiary
```

---

# 5. 이번 R11 case별 stage date 요약

| case                                   | Stage 1    | Stage 2                        | Stage 3 | Stage 4B   | Stage 4C                  |
| -------------------------------------- | ---------- | ------------------------------ | ------- | ---------- | ------------------------- |
| Martial law / Korea discount           | 2024-12-03 | liquidity relief               | N/A     | N/A        | 2024-12-04 hard reference |
| Iran / Middle East shock               | 2026-02-28 | N/A                            | N/A     | N/A        | 2026-03-04 hard           |
| AI bonus / fiscal redistribution       | 2026-05-12 | N/A                            | N/A     | 2026-05-12 | policy 4C-watch           |
| Samsung strike / emergency arbitration | 2026-04~05 | court/government relief        | N/A     | N/A        | 2026-05-17/19 watch       |
| China rare earth controls              | 2025-04    | limited truce/licensing relief | N/A     | N/A        | 2025-10 / 2026-05 watch   |
| U.S.-Korea tariff                      | 2025-03~07 | 2025-12 relief                 | N/A     | N/A        | 2025-07 auto shock        |
| China fab tool license                 | 2025-08~09 | 2025-12-30                     | N/A     | N/A        | annual-license watch      |
| South Korea wildfires                  | 2025-03-21 | disaster response              | N/A     | N/A        | disaster hard reference   |

---

# 6. 실제 가격경로 검증 총괄

| case                |                                                    anchor | MFE / MAE 해석                              | 판정                              |
| ------------------- | --------------------------------------------------------: | ----------------------------------------- | ------------------------------- |
| Martial law         |                        KOSPI -1.4%, won 2yr low, 10T fund | 정치 리스크 premium hard reference             | thesis_break_reference          |
| Iran shock          |             KOSPI -12.06%, Samsung -11.7%, Hyundai -15.8% | macro hard 4C                             | thesis_break                    |
| AI bonus            |               Samsung -3.5%, SK -1.4%, KOSPI intraday -5% | policy comment 4B/4C-watch                | event_premium                   |
| Samsung strike      |      Samsung -2.5%, KOSPI -3.2%, one-day loss 1T won risk | systemic labor 4C-watch                   | thesis_break_watch              |
| Rare earth controls | heavy rare earth exports -50%, China >90% processed share | no direct stock anchor, supply-chain gate | thesis_break_watch              |
| U.S.-Korea tariff   |                                  Hyundai -4.5%, Kia -6.6% | tariff relief still margin risk           | 4C-watch                        |
| China fab license   |                                       annual 2026 license | policy relief, not durable Green          | success_candidate_policy_relief |
| Wildfires           |                       32 deaths, 104k ha, 5,000 buildings | disaster cost reference                   | thesis_break_reference          |

---

# 7. score-price alignment 판정

```text
aligned:
- none as Stage 3 this round

success_candidate_policy_relief:
- China fab tool-license relief
- U.S.-Korea tariff retroactive 15% relief
- rare-earth licensing facilitation if confirmed by end-use

event_premium:
- AI bonus / fiscal redistribution proposal
- tariff relief if used before margin proof

price_moved_without_evidence:
- AI dividend / AI tax narrative if traded as direct corporate-profit grab before legislation
- tariff relief if stocks rerate before pass-through and local-production economics
- disaster rebuild beneficiaries if traded before insurance/loss/rebuild orders

thesis_break_watch:
- Samsung strike
- China rare-earth export controls
- U.S.-Korea tariff margin shock
- annual China fab tool-license regime

thesis_break_reference:
- martial law Korea-discount shock
- wildfires climate-disaster reference

thesis_break:
- Iran / Middle East macro energy FX shock

hard_4C_confirmed:
- Iran / Middle East energy-FX shock
- martial-law political shock reference
- climate disaster hard reference
```

---

# 8. 점수비중 교정

## 올릴 축

```text
political_risk_premium +5
FX_energy_sensitivity +5
supply_chain_license_visibility +5
tariff_pass_through +5
policy_to_EPS_bridge +5
labor_continuity +5
critical_material_inventory +5
disaster_loss_exposure +5
government_relief_actual_execution +4
sovereign_credit_stability +4
```

### 왜 올리나

Martial law와 Iran shock는 headline event가 아니라 index·FX·large-cap을 바로 꺾었다. Samsung strike는 특정 기업 노사문제가 한국 수출·반도체 공급망 issue로 확장됐다. Rare earth와 China fab license는 “수입 가능 여부”가 capex와 생산성의 전제다. U.S.-Korea tariff는 headline relief가 나와도 Hyundai/Kia가 빠졌듯 margin bridge가 핵심이다. Wildfire는 복구수혜보다 손해율·피해비용·공급망 차질을 먼저 봐야 한다.

## 내릴 축

```text
policy_headline_only -5
relief_package_without_execution -5
tariff_cut_without_margin_bridge -5
rare_earth_truce_without_actual_license -5
strike_risk_unresolved -5
AI_tax_or_bonus_comment_without_legislation -4
disaster_rebuild_story_without_loss_assessment -5
geopolitical_risk_ignored -5
```

### 왜 내리나

R11은 원래 “이야기”가 가장 잘 튀는 섹터다. 하지만 AI bonus 발언처럼 정책 아이디어만으로도 주가가 흔들리고, tariff relief처럼 좋은 뉴스도 margin에는 부정적일 수 있다. 정치·전쟁·노동·재난은 수혜주보다 먼저 downside gate로 처리해야 한다.

## Green gate 강화 조건

```text
R11 Stage 3-Green 필수:
1. 정책이 법안 / 예산 / 시행령 / 집행으로 확정
2. 기업별 EPS / FCF bridge 확인
3. 관세는 gross margin / pass-through / local-production economics 확인
4. 지정학은 원가 / 물량 / FX hedge 확인
5. 공급망은 actual license / inventory / alternative sourcing 확인
6. 노동 이슈는 production continuity 확인
7. 재난은 손해율 / 피해액 / 복구계약 / 보상구조 확인
8. 정치 event는 FX / 외국인 수급 / sovereign credibility 안정 확인
9. price path가 evidence 이후 따라옴

금지:
정책 발언 only
구두 truce only
지원책 headline only
재난 복구수혜 only
관세완화 headline only
AI 배당 / windfall tax rumor only
```

## 4B 조기감지 조건

```text
4B-watch:
AI chip rally 이후 분배/세금 발언으로 index 급락
정책지원 발표로 관련주 선반영
관세 완화 headline 후 margin proof 전 rerating
rare-earth truce headline 후 actual license proof 없음
disaster rebuild theme before loss assessment
government arbitration / strike relief before actual production continuity

4B-elevated:
index concentration extreme
foreign positioning crowded
FX volatility rising
oil price spike
policy details absent
supply-chain inventory thin
```

## 4C hard gate 조건

```text
martial law / political crisis
index circuit breaker / record market drawdown
FX disorderly move / won 1,500 breach
Middle East oil chokepoint shock
rare-earth license denial
semiconductor fab tool license denial
systemic strike halting production
tariff shock directly cutting OP margin
climate disaster causing large insured / uninsured losses
```

---

# 9. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
```

---

# 10. 레포 반영용 patch-ready 출력

## docs/round/round_208.md 요약

```md
# R11 Loop 13. Policy / Geopolitics / Disaster / Event Price Validation

이번 라운드는 R11 Loop 13 price-validation 라운드다.

핵심 결론:
- Martial law / Korea discount is political hard reference. KOSPI fell 1.4%, won stayed near a two-year low, authorities prepared unlimited liquidity and a 10T won stock-market stabilisation fund. Political risk premium is a hard gate.
- Iran / Middle East energy shock is macro hard 4C. KOSPI -12.06% to 5,093.54, market-cap wipeout 817.6T won / $553.82B over two days, won hit 1,505.8/USD, Samsung -11.7%, SK Hynix -9.6%, Hyundai -15.8%. Korea sources about 70% of oil purchases from Middle East.
- AI bonus / fiscal redistribution is event premium and 4B-watch. Samsung -3.5%, SK Hynix -1.4%, KOSPI fell as much as -5% intraday after AI dividend discussion. It was later clarified as excess tax revenue, not confirmed corporate-profit seizure.
- Samsung strike / emergency arbitration is systemic labor 4C-watch. 45,000 workers threatened an 18-day strike; one-day semiconductor factory halt could cost up to 1T won and wider economic damage up to 100T won. Samsung accounts for 22.8% of exports and 26% of the domestic stock market.
- China rare-earth export controls are supply-chain 4C-watch. China produces over 90% of processed rare earths and magnets; defence users are denied licences and advanced semiconductor applications are case-by-case. Heavy rare-earth exports are still down about 50% since April 2025 controls.
- U.S.-Korea tariff deal is policy relief plus 4C-watch. Hyundai -4.5% and Kia -6.6% after 15% tariff announcement. Later 15% was confirmed retroactive to Nov. 1 and future semiconductor/pharma national security tariffs capped at 15%, but company Green needs margin bridge.
- Samsung / SK Hynix China fab tool licence is policy relief, not Green. U.S. granted annual 2026 licence after waiver revocation, but annual approval system preserves future risk.
- 2025 South Korea wildfires are climate-disaster hard reference. 32 deaths, about 5,000 buildings destroyed, 104,000 hectares burned; climate change doubled likelihood and raised intensity by 15%.
```

## docs/checkpoints/checkpoint_28a_round208_r11_loop13.md 요약

```md
# Checkpoint 28A Round 208 R11 Loop 13 Policy Geopolitics Disaster Event Price Validation

## 반영 내용
- R11 Loop 13 price-validation 라운드를 추가했다.
- Martial law, Iran/Middle East shock, AI bonus policy comment, Samsung strike, China rare-earth export controls, U.S.-Korea tariff deal, China fab annual tool licence, 2025 wildfires를 비교했다.
- Reuters / FT / AP / WSJ / Barron's anchors로 가능한 event MFE/MAE, FX/index drawdown, policy amounts, supply-chain metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- political risk premium, FX/energy sensitivity, supply-chain licence visibility, tariff pass-through, policy-to-EPS bridge, labor continuity, critical-material inventory, disaster loss exposure 가중치 강화
- policy headline-only, relief package without execution, tariff cut without margin bridge, rare-earth truce without actual licence, strike risk unresolved, disaster rebuild story without loss assessment 감점 강화
```

## data/e2r_case_library/cases_r11_loop13_round208.jsonl 초안

```jsonl
{"case_id":"r11_loop13_martial_law_korea_discount_political_shock","symbol":"KOSPI/KRW/005930/000660","company_name":"Korea political shock / martial law reference","case_type":"4c_thesis_break_reference","primary_archetype":"POLITICAL_SHOCK_KOREA_DISCOUNT_HARD_GATE","stage1_date":"2024-12-03","stage4c_date":"2024-12-04","price_validation":{"price_data_source":"Reuters martial-law political-shock anchors","stage3_price":null,"kospi_close_mae_pct":-1.4,"kospi_intraday_context_pct":-2.0,"kospi_ytd_loss_context_pct":-7.0,"won_context":"near_two_year_low","won_ytd_decline_context_pct":-9.0,"stock_market_stabilisation_fund_krw_trn":10.0,"liquidity_commitment":"unlimited_liquidity_if_needed","martial_law_duration_hours":6,"price_validation_status":"reported_index_fx_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_reference","rerating_result":"political_risk_premium_hard_gate","notes":"Political shock immediately repriced KOSPI/won; use as Korea-discount hard reference."}
{"case_id":"r11_loop13_iran_middle_east_energy_fx_macro_hard_4c","symbol":"KOSPI/KRW/005930/000660/005380/003490","company_name":"Iran / Middle East energy and FX shock","case_type":"4c_thesis_break","primary_archetype":"MIDDLE_EAST_ENERGY_FX_MACRO_HARD_4C","stage1_date":"2026-02-28","stage4c_date":"2026-03-04","price_validation":{"price_data_source":"Reuters Iran conflict macro-market anchors","stage3_price":null,"kospi_close":5093.54,"kospi_close_mae_pct":-12.06,"kospi_intraday_mae_pct":-12.65,"kospi_previous_day_mae_pct":-7.24,"two_day_market_cap_wipeout_krw_trn":817.6,"two_day_market_cap_wipeout_usd_bn":553.82,"won_intraday_low_per_usd":1505.8,"won_close_per_usd":1485.7,"won_close_decline_pct":-3.1,"middle_east_oil_purchase_share_pct":70,"samsung_event_mae_pct":-11.7,"sk_hynix_event_mae_pct":-9.6,"hyundai_motor_event_mae_pct":-15.8,"korean_air_event_mae_pct":-7.9,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"middle_east_energy_fx_macro_hard_4C","notes":"Oil/FX macro shock caused record KOSPI drawdown; hard 4C."}
{"case_id":"r11_loop13_ai_bonus_fiscal_redistribution_event","symbol":"005930/000660/KOSPI","company_name":"AI windfall / citizen dividend policy discussion","case_type":"event_premium_4b_watch","primary_archetype":"AI_WINDFALL_FISCAL_REDISTRIBUTION_EVENT","stage4b_date":"2026-05-12","price_validation":{"price_data_source":"FT/Barron's/MarketWatch AI bonus policy-reaction anchors","stage3_price":null,"samsung_event_mae_pct":-3.5,"sk_hynix_event_mae_pct":-1.4,"kospi_intraday_mae_pct":-5.0,"kospi_close_mae_pct":-2.3,"policy_object":"excess_tax_revenue_from_AI_semiconductor_boom","corporate_profit_seizure_confirmed":false,"ai_tax_or_windfall_tax_legislation_confirmed":false,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_4B_watch","rerating_result":"AI_windfall_fiscal_redistribution_policy_watch","notes":"Policy comment triggered selloff before legislation; treat as 4B/policy-risk watch."}
{"case_id":"r11_loop13_samsung_strike_emergency_arbitration_supply_chain","symbol":"005930","company_name":"Samsung Electronics labor strike / government arbitration","case_type":"4c_watch","primary_archetype":"SYSTEMIC_LABOR_SUPPLY_CHAIN_INTERVENTION","stage4c_date":"2026-05-17/2026-05-19_watch","price_validation":{"price_data_source":"Reuters Samsung strike / government intervention anchors","stage3_price":null,"threatened_workers":45000,"strike_duration_days":18,"one_day_direct_loss_krw_trn":1.0,"potential_economic_damage_krw_trn":100,"emergency_arbitration_ban_days":30,"samsung_export_share_pct":22.8,"samsung_domestic_stock_market_share_pct":26,"samsung_employees":120000,"supplier_count":1700,"samsung_event_mae_pct":-2.5,"kospi_same_context_mae_pct":-3.2,"court_essential_staffing_required":true,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"systemic_labor_supply_chain_4C_watch","notes":"Samsung labor disruption is systemic export/supply-chain risk, not normal wage negotiation."}
{"case_id":"r11_loop13_china_rare_earth_export_control_supply_chain","symbol":"005930/000660/042660/supply_chain_basket","company_name":"China rare-earth export controls / Korean semiconductor and defence supply chain","case_type":"4c_watch","primary_archetype":"RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C","stage1_date":"2025-04","stage4c_date":"2025-10-09/2025-10-22/2026-05_watch","price_validation":{"price_data_source":"Reuters rare-earth export-control and Korea trade-envoy anchors","stage3_price":null,"processed_rare_earths_china_share_pct":90,"rare_earth_magnets_china_share_pct":90,"heavy_rare_earth_exports_decline_since_controls_pct":-50,"affected_elements":["yttrium","dysprosium","terbium","scandium","indium"],"defence_user_license_policy":"not_granted","advanced_semiconductor_license_policy":"case_by_case","korea_affected_companies_context":["Samsung Electronics","SK Hynix","Hanwha Ocean"],"direct_korean_stock_price_anchor":"price_data_unavailable_after_deep_search","price_validation_status":"supply_chain_policy_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"rare_earth_export_control_supply_chain_gate","notes":"Rare-earth truce is insufficient without actual licences, inventory and alternative sourcing."}
{"case_id":"r11_loop13_us_korea_tariff_auto_semis_pharma_policy","symbol":"005380/000270/004020/semiconductor_pharma_basket","company_name":"U.S.-Korea tariff policy shock and relief","case_type":"4c_watch_policy_relief","primary_archetype":"US_KOREA_TARIFF_POLICY_4C_WATCH","stage4c_date":"2025-07-31_watch","stage2_date":"2025-12-01_relief","price_validation":{"price_data_source":"Reuters U.S.-Korea tariff trade-deal anchors","stage3_price":null,"hyundai_event_mae_pct":-4.5,"kia_event_mae_pct":-6.6,"auto_tariff_new_pct":15,"auto_tariff_prior_pct":25,"tariff_reduction_pp":-10,"korea_fta_prior_advantage_vs_japan_pct":2.5,"requested_tariff_pct_by_korea":12.5,"retroactive_effective_date":"2025-11-01","strategic_us_investment_commitment_usd_bn":350,"future_semiconductor_pharma_tariff_cap_pct":15,"airplane_parts_tariffs_removed":true,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch_plus_policy_relief","rerating_result":"US_Korea_tariff_policy_gate","notes":"Tariff relief still needs company-level gross margin, pass-through and local-production bridge."}
{"case_id":"r11_loop13_samsung_sk_china_fab_tool_license_relief","symbol":"005930/000660","company_name":"Samsung Electronics / SK Hynix China fab tool license relief","case_type":"success_candidate_policy_relief","primary_archetype":"CHINA_FAB_EXPORT_LICENSE_RELIEF","stage2_date":"2025-12-30","price_validation":{"price_data_source":"Reuters U.S. approval for Samsung/SK Hynix China tool shipments","stage3_price":null,"license_period":"2026_annual_license","validated_end_user_status_expiry":"2025-12-31","annual_approval_system":true,"company_context":["Samsung Electronics","SK Hynix"],"china_facility_role":"key_production_base_for_traditional_memory","multi_year_visibility_confirmed":false,"license_denial_risk_removed":false,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_policy_relief","rerating_result":"China_fab_tool_license_relief_stage2","notes":"Annual licence is relief, not durable Green; multiyear tool access remains key gate."}
{"case_id":"r11_loop13_2025_south_korea_wildfires_disaster_reference","symbol":"insurers/construction/utilities/agriculture/logistics_basket","company_name":"2025 South Korea wildfires climate-disaster reference","case_type":"disaster_hard_reference","primary_archetype":"CLIMATE_DISASTER_SUPPLY_CHAIN_REFERENCE","stage1_date":"2025-03-21","stage4c_date":"2025-03_to_2025-04_reference","price_validation":{"price_data_source":"Reuters climate-attribution wildfire report + AP early disaster anchor","stage3_price":null,"fatalities_final_context":32,"buildings_destroyed_context":5000,"area_burned_hectares":104000,"prior_record_multiple":4,"climate_change_likelihood_increase_multiple":2,"climate_change_intensity_increase_pct":15,"ap_early_fatalities":24,"ap_early_injured":26,"ap_early_evacuated":28800,"ap_early_structures_destroyed":300,"listed_stock_price_anchor":"price_data_unavailable_after_deep_search","price_validation_status":"disaster_reference_not_full_ohlc"},"score_price_alignment":"thesis_break_reference","rerating_result":"climate_disaster_supply_chain_hard_reference","notes":"Disaster rebuild theme must wait for loss assessment, insurance burden and actual rebuilding contracts."}
```

## data/sector_taxonomy/score_weight_profiles_round208_r11_loop13_v1.csv 초안

```csv
archetype,political_risk_premium,fx_energy_sensitivity,supply_chain_license_visibility,tariff_pass_through,policy_to_eps_bridge,labor_continuity,critical_material_inventory,disaster_loss_exposure,government_relief_execution,sovereign_credit_stability,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
POLITICAL_SHOCK_KOREA_DISCOUNT_HARD_GATE,+5,+4,+1,+1,+3,+2,+1,+2,+5,+5,0,+4,+5,Martial law shows political shock can reprice KOSPI/won immediately.
MIDDLE_EAST_ENERGY_FX_MACRO_HARD_4C,+3,+5,+3,+4,+3,+2,+4,+3,+4,+5,0,+5,+5,Iran shock confirms energy/FX macro hard gate for Korea.
AI_WINDFALL_FISCAL_REDISTRIBUTION_EVENT,+4,+2,+1,+1,+5,+3,+1,+0,+4,+4,-4,+5,+4,AI bonus comment is policy event; legislation and EPS bridge required.
SYSTEMIC_LABOR_SUPPLY_CHAIN_INTERVENTION,+3,+2,+3,+1,+3,+5,+3,+0,+5,+4,0,+5,+5,Samsung strike risk affects exports, suppliers, index and chip supply.
RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C,+2,+2,+5,+3,+3,+1,+5,+0,+3,+4,0,+5,+5,China rare-earth controls require actual licences, inventory and alternative sourcing.
US_KOREA_TARIFF_POLICY_4C_WATCH,+2,+3,+2,+5,+5,+1,+1,+0,+4,+4,-5,+5,+4,Tariff cut is not Green without gross margin and pass-through.
CHINA_FAB_EXPORT_LICENSE_RELIEF,+1,+1,+5,+1,+4,+1,+3,+0,+4,+3,-4,+4,+4,Annual fab-tool licence is relief but not multiyear visibility.
CLIMATE_DISASTER_SUPPLY_CHAIN_REFERENCE,+1,+2,+1,+1,+2,+1,+2,+5,+5,+4,-5,+4,+5,Wildfire disaster shows loss exposure before rebuild-beneficiary scoring.
```

---

# 이번 R11 Loop 13 결론

```text
1. Martial law shock는 R11 정치 hard reference다.
   KOSPI -1.4%, won 2년 저점, 10T won stabilisation fund 준비가 가격경로로 확인됐다.

2. Iran / Middle East shock는 macro hard 4C다.
   KOSPI -12.06%, Samsung -11.7%, Hyundai -15.8%, won 1,505.8/USD는 에너지·FX gate의 위력을 보여준다.

3. AI bonus 논쟁은 policy event premium이다.
   Samsung -3.5%, SK Hynix -1.4%, KOSPI intraday -5%가 나왔지만, 실제 입법/세금 구조는 확인되지 않았다.

4. Samsung strike는 systemic labor 4C-watch다.
   노사 이슈가 22.8% export share, 26% stock-market share, 1T won/day 생산손실 리스크로 확장됐다.

5. China rare-earth controls는 supply-chain 4C-watch다.
   truce headline보다 actual license, inventory, alternative sourcing을 봐야 한다.

6. U.S.-Korea tariff deal은 relief이자 4C-watch다.
   Hyundai -4.5%, Kia -6.6% 반응은 tariff cut만으로 Green이 안 된다는 증거다.

7. Samsung/SK China fab annual licence는 policy relief다.
   2026년 장비반입은 가능하지만 annual approval regime은 discount 요인이다.

8. 2025 wildfires는 climate disaster hard reference다.
   재난 복구수혜보다 피해액, 보험손해율, 공급망 차질, 실제 복구계약을 먼저 봐야 한다.
```

한 문장으로 압축하면:

> **R11에서 진짜 Stage 3는 “정책·관세·휴전·지원책·재난복구 이야기가 있다”가 아니라, 그 event가 EPS·마진·공급망 license·FX 안정·생산연속성·피해비용으로 실제 숫자에 닫히는 순간이다.**

[1]: https://www.reuters.com/world/asia-pacific/south-korean-lawmakers-call-impeach-president-yoon-after-martial-law-rescinded-2024-12-04/?utm_source=chatgpt.com "South Korea's Yoon faces impeachment after martial law debacle"
[2]: https://www.reuters.com/world/asia-pacific/korean-stocks-dive-won-hits-17-year-low-iran-conflict-2026-03-04/?utm_source=chatgpt.com "Korean stocks record worst day, won sinks on Iran conflict"
[3]: https://www.ft.com/content/fefa0641-7fb0-4d78-81c8-0180f1b618ed?utm_source=chatgpt.com "South Koreans should all get an AI bonus, says presidential adviser"
[4]: https://www.reuters.com/business/world-at-work/south-korea-says-it-will-pursue-all-options-avoid-samsung-strike-2026-05-17/?utm_source=chatgpt.com "South Korea says it will pursue all options to avoid Samsung strike"
[5]: https://www.reuters.com/world/china/china-tightens-rare-earth-export-controls-2025-10-09/?utm_source=chatgpt.com "China tightens rare earth export controls, targets defence, semiconductor users"
[6]: https://www.reuters.com/business/autos-transportation/south-korea-automaker-shares-slip-after-us-trade-deal-2025-07-31/?utm_source=chatgpt.com "South Korea automaker shares slip after US trade deal"
[7]: https://www.reuters.com/world/china/samsung-wins-us-annual-approval-chipmaking-tool-shipments-china-source-says-2025-12-30/?utm_source=chatgpt.com "US approves Samsung, SK Hynix chipmaking tool shipments to China for 2026, sources say"
[8]: https://www.reuters.com/sustainability/cop/south-koreas-deadly-fires-made-twice-likely-by-climate-change-researchers-say-2025-04-30/?utm_source=chatgpt.com "South Korea's deadly fires made twice as likely by climate change, researchers say"
