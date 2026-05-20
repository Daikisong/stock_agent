순서상 이번은 **R13 Loop 16 — Cross-archetype RedTeam / 4B / 4C / accounting trust / price validation 총정리 라운드**다.

R13은 새 섹터를 넓히는 라운드가 아니라, R1~R12에서 반복적으로 나온 오판 패턴을 도려내는 라운드다. 쉽게 말하면 점수표의 “눈”을 교정하는 구간이다. 좋은 뉴스가 좋아 보이는 것과, 실제로 좋은 entry가 되는 것은 다르다. 이번 라운드는 그 차이를 잡는다.

```text
round = R13 Loop 16
round_id = round_249
large_sector = CROSS_ARCHETYPE_REDTEAM_4B_4C_ACCOUNTING_TRUST_PRICE_VALIDATION
method = trigger_level_redteam_v1
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R1 Loop 17
```

이번 세션에서도 KRX/Naver/Yahoo/Stooq 수정주가 일봉 OHLC 30D/90D/180D/1Y/2Y window는 안정적으로 확보하지 못했다. 그래서 full MFE/MAE 숫자는 만들지 않는다. 대신 각 case마다 **reported event return / event price / contract value / selloff trigger / user metric / legal gate**를 가격 anchor로 사용한다. 즉 `MFE_30D/90D/180D/1Y/2Y = price_data_unavailable_after_deep_search`이고, 이번 R13의 목적은 **trigger별 상대 품질과 4B/4C gate 보정**이다.

---

# 1. 이번 라운드 대섹터

```text
R13 = Cross-archetype RedTeam / 4B / 4C / accounting trust / price validation
```

R13의 핵심 질문은 이거다.

```text
1. Stage2인데 사실상 좋은 entry였던 trigger는 무엇인가?
2. Stage3-Green으로 올리면 안 되는 headline은 무엇인가?
3. 좋은 evidence였지만 가격이 실패한 case는 무엇인가?
4. 4B overlay가 실제로 대시세를 막거나 drawdown을 만든 case는 무엇인가?
5. 4C가 큰 하락 전에 잡힌 case는 무엇인가?
6. production score에 바로 반영하지 말고 shadow-only로 어떤 weight를 바꿀 것인가?
```

---

# 2. 대상 canonical archetype

```text
CROSS_STAGE2_ACTIONABLE_CONFIRMED
GOOD_EVIDENCE_PRICE_FAILED
CONTRACT_VALUE_WITH_MARGIN_GATE
GROWTH_WITH_DILUTION_4B
EXPORT_ORDER_TO_COMBAT_VALIDATION_YELLOW
POLICY_OR_PREFERRED_BIDDER_WITH_LEGAL_4B
SECURITY_TRUST_BREAK_HARD_4C
TARIFF_RELIEF_THAT_STILL_SELLOFF
FOREIGN_STRATEGIC_CAPITAL_WITH_CB_4B
```

---

# 3. deep sub-archetype

```text
Stage2가 좋은 entry였던 유형:
- 대형 계약 + 즉시 가격반응 + market-relative outperformance
- 외국 전략자본 + 구체적 자금 + 자문/집행 경로
- 방산 수출 + 반복 operator 확장 + 실전 수요 검증
- value-up / buyback / hybrid strategy처럼 숫자가 닫힌 전략 발표

Stage3로 올리면 안 되는 유형:
- AI/cloud 매출 비중은 좋지만 IPO가 공모가를 하회
- preferred bidder지만 final contract/legal challenge가 남음
- 대형 수주지만 margin/cash conversion이 없음
- policy reform이지만 company-specific action이 없음
- 인수설/teaser letter일 뿐 final SPA/approval 없음

4B가 실제 가격을 꺾은 유형:
- 방산 성장주 dilution / capital raise
- 15% tariff “relief”인데 주가는 하락
- legal injunction / court block
- CB dilution / valuation overhang
- user shift는 있지만 revenue/margin 미확인

4C가 즉시 작동한 유형:
- 대규모 생활서비스 data breach
- 통신/플랫폼 cybersecurity breach
- 항공 fatal accident
- 정치 crisis / martial law
- PF liquidity shock
```

---

# 4. 선정 case 요약

| bucket                                                | case                                          | 핵심 판정                                                                         |
| ----------------------------------------------------- | --------------------------------------------- | ----------------------------------------------------------------------------- |
| structural_success / Stage2-Actionable                | **Samsung SDS / KKR**                         | $820M CB, +20.8%, KOSPI +3.0%. 외국 전략자본 trigger는 강하지만 CB/AI execution 4B       |
| structural_success / Stage2-Actionable                | **Samsung E&A / Fadhili**                     | $6B Saudi contract, +8.5%, KOSPI -1.4%. EPC 계약 trigger는 강하지만 margin/cash gate |
| Stage2 + 4B                                           | **Hanwha Aerospace / Romania K9 + dilution**  | $1B order, +5% record high, 이후 3.6T won capital raise 계획에 -13%                |
| Stage3-Yellow candidate                               | **LIG Nex1 / Iraq M-SAM + combat validation** | $2.8B order, +3.6%, 이후 missile-defense validation으로 +47% context              |
| false_positive_score / evidence_good_but_price_failed | **LG CNS IPO**                                | AI/cloud 매출 비중 높지만 공모가 61,900원 → 59,700원                                      |
| hard 4C + rival Stage2                                | **Coupang breach / Naver·CJ shift**           | Coupang -34%, MAU -3.5%, spending -6.3%, Naver users +23%, CJ volume +120%    |
| 4C + hedge                                            | **Hyundai/Kia tariff**                        | 15% tariff deal에도 Hyundai -4.5%, Kia -6.6%. headline relief가 실제 relief가 아니었음  |
| Stage2 + legal 4B                                     | **KHNP/Czech nuclear**                        | preferred bidder 후 원전 basket rally, 이후 Czech court/EDF legal block            |

---

# 5. 각 case별 trigger grid

## Case A — Samsung SDS / KKR strategic capital

```text
symbol = 018260
case_type = Stage2-Actionable + CB 4B
```

| trigger |              type | date       | 당시 공개 evidence                                                            | 가격 anchor                       | outcome |
| ------- | ----------------: | ---------- | ------------------------------------------------------------------------- | ------------------------------- | ------- |
| T0      |         awareness | 2025~2026  | Korea Discount reform, 외국 전략자본 관심 증가                                      | no entry                        | Stage1  |
| T1      | Stage2-Actionable | 2026-04-15 | KKR, Samsung SDS 신규 CB $820M 매입                                           | +20.8% intraday, +19.4% morning |         |
| T2      |        validation | 2026-04-15 | KKR가 M&A, capital allocation, AI expansion 자문; Samsung SDS cash 6.4T won  | KOSPI +3.0%                     |         |
| T3      |          4B-watch | 2026       | CB dilution, AI execution, M&A ROIC, physical AI/stablecoin overextension | no full OHLC                    |         |
| T4      |     Stage3-Yellow | N/A        | 실제 M&A/AI revenue/capital allocation execution 필요                         | 보류                              |         |

Samsung SDS는 R13에서 “좋은 Stage2-Actionable”의 가장 깨끗한 예시다. KKR의 $820M CB 투자는 단순 소문이 아니라 계약형 자금 유입이고, 주가는 장중 +20.8%, 오전 +19.4%로 KOSPI +3.0%를 크게 이겼다. KKR가 M&A, capital allocation, AI offering 확장에 6년간 자문한다는 구체성도 있다. 다만 CB는 dilution이고, AI/M&A는 아직 실행 전이다. 그래서 **Stage2-Actionable + 4B overlay**가 맞다. ([Reuters][1])

```json
{
  "case_id": "r13_loop16_samsung_sds_kkr_cross_redteam",
  "symbol": "018260",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable_foreign_strategic_capital",
  "trigger_date": "2026-04-15",
  "event_return_intraday_pct": 20.8,
  "event_return_morning_pct": 19.4,
  "kospi_same_context_pct": 3.0,
  "market_relative_morning_pp": 16.4,
  "cb_value_usd_mn": 820,
  "cash_balance_krw_trn": 6.4,
  "4B_overlay": ["CB_dilution", "AI_execution", "M&A_ROIC"],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "excellent_stage2_actionable_with_4B"
}
```

---

## Case B — Samsung E&A / Fadhili EPC contract

```text
symbol = 028050
case_type = Stage2-Actionable contract-value trigger
```

| trigger |              type | date       | 당시 공개 evidence                                                       | 가격 anchor                        | outcome |
| ------- | ----------------: | ---------- | -------------------------------------------------------------------- | -------------------------------- | ------- |
| T0      |   Stage2 evidence | 2024-04-02 | Aramco, Fadhili expansion EPC $7.7B contracts awarded                | no entry                         |         |
| T1      | Stage2-Actionable | 2024-04-03 | Samsung E&A 약 $6B contract share                                     | +8.5% to 26,750 won, KOSPI -1.4% |         |
| T2      |        validation | 2024-04-03 | Fadhili capacity +1.5B scf/day to 4B scf/day, completion Nov 2027    | same                             |         |
| T3      |          4B-watch | 2024~2027  | EPC margin, working capital, claims, cost escalation, execution risk | no full OHLC                     |         |
| T4      |     Stage3-Yellow | N/A        | margin/cash conversion 확인 필요                                         | 보류                               |         |

Samsung E&A는 “contract value + price reaction + market-relative return”이 같이 닫힌 Stage2-Actionable이다. Fadhili contract는 약 $6B이고, 주가는 +8.5%로 26,750원까지 올랐으며, 같은 구간 KOSPI는 -1.4%였다. 즉 trigger 자체는 매우 좋다. 하지만 EPC는 “수주=이익”이 아니다. 공사마진, 원가 상승, 공정률, claim, working capital이 Green gate다. ([월스트리트저널][2])

```json
{
  "case_id": "r13_loop16_samsung_ea_fadhili_cross_redteam",
  "symbol": "028050",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable_contract_value",
  "trigger_date": "2024-04-03",
  "contract_value_context_usd_bn": 6.0,
  "event_return_pct": 8.5,
  "event_price_krw": 26750,
  "kospi_same_context_pct": -1.4,
  "market_relative_return_pp": 9.9,
  "4B_overlay": ["EPC_margin", "working_capital", "cost_escalation", "execution_delay"],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "excellent_stage2_actionable_contract_with_margin_gate"
}
```

---

## Case C — Hanwha Aerospace / Romania K9 + dilution 4B

```text
symbol = 012450
case_type = Stage2 export success + 4B dilution
```

| trigger |              type | date       | 당시 공개 evidence                                                 | 가격 anchor          | outcome |
| ------- | ----------------: | ---------- | -------------------------------------------------------------- | ------------------ | ------- |
| T0      |            Stage1 | 2022~2024  | Russia-Ukraine 이후 Europe rearmament                            | no entry           |         |
| T1      | Stage2-Actionable | 2024-07-09 | Romania K9/K10 $1B order                                       | +5%+, record high  |         |
| T2      |        validation | 2024-07-09 | backlog 5.1T won → 30T won, global howitzer export share >50%  | same               |         |
| T3      |                4B | 2025-03~04 | 3.6T won capital raise plan, 이후 2.3T won 수정, 별도 1.3T won issue | -13% on first plan |         |
| T4      |     Stage3-Yellow | N/A        | delivery/margin/capacity/dilution absorption 필요                | 보류                 |         |

Hanwha Aerospace는 R13의 “좋은 성장주도 dilution 하나로 4B가 된다” case다. Romania K9 order는 $1B이고 주가는 +5% 이상 record high를 찍었다. backlog는 2021년 말 5.1T won에서 2024년 3월 약 30T won으로 커졌고, global howitzer export share도 50% 이상으로 보도됐다. 하지만 2025년 3.6T won capital increase plan 이후 주가는 -13% 급락했다. 이건 Stage2 success를 취소하는 4C가 아니라, **Stage2 + dilution 4B 병기**가 맞다. ([Reuters][3])

```json
{
  "case_id": "r13_loop16_hanwha_export_dilution_cross_redteam",
  "symbol": "012450",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2-Actionable_export_with_dilution_4B",
  "export_trigger_date": "2024-07-09",
  "contract_value_usd_bn": 1.0,
  "export_event_return_pct": ">5",
  "backlog_end_2021_krw_trn": 5.1,
  "backlog_mar_2024_krw_trn": 30,
  "dilution_trigger_date": "2025-03-21",
  "capital_raise_plan_krw_trn": 3.6,
  "dilution_event_return_pct": -13,
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_success_with_4B_dilution"
}
```

---

## Case D — LIG Nex1 / Iraq order + combat validation

```text
symbol = 079550
case_type = Stage3-Yellow candidate
```

| trigger |                    type | date       | 당시 공개 evidence                                                     | 가격 anchor                         | outcome |
| ------- | ----------------------: | ---------- | ------------------------------------------------------------------ | --------------------------------- | ------- |
| T0      |         Stage2 evidence | 2024-09-20 | Iraq M-SAM II / Cheongung-II order 3.71T won / $2.8B               | +3.6%, KOSPI +0.9%                |         |
| T1      |              validation | 2024-09-20 | Iraq becomes 4th operator after Korea, UAE, Saudi Arabia           | same                              |         |
| T2      | Stage3-Yellow candidate | 2026       | missile-defense combat validation / Middle East demand context     | +47% context from conflict period |         |
| T3      |                4B-watch | 2026       | war-event premium, production scale, delivery time, export finance | no full OHLC                      |         |
| T4      |            Stage3-Green | N/A        | delivery/margin/repeat orders 확인 필요                                | 보류                                |         |

LIG Nex1은 R13에서 Stage2를 Stage3-Yellow 후보로 올려야 하는 패턴이다. Iraq order는 3.71T won, $2.8B였고, 발표 당일 +3.6%로 KOSPI +0.9%를 이겼다. 중요한 건 여기서 끝이 아니라, Iraq가 Cheongung-II의 네 번째 operator가 되면서 export repeatability가 생겼다는 점이다. 다만 Green은 생산능력, 납기, 마진, 반복수주가 닫혀야 한다. ([Reuters][4])

```json
{
  "case_id": "r13_loop16_lig_nex1_export_yellow_cross_redteam",
  "symbol": "079550",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage3-Yellow_candidate_export_validation",
  "trigger_date": "2024-09-20",
  "contract_value_krw_trn": 3.71,
  "contract_value_usd_bn": 2.8,
  "event_return_pct": 3.6,
  "kospi_same_context_pct": 0.9,
  "market_relative_return_pp": 2.7,
  "operator_count_after_iraq": 4,
  "4B_overlay": ["production_capacity", "delivery_schedule", "war_event_premium", "export_finance"],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage3_Yellow_candidate_not_Green"
}
```

---

## Case E — LG CNS IPO / good evidence but price failed

```text
symbol = 064400
case_type = evidence_good_but_price_failed
```

| trigger |             type | date       | 당시 공개 evidence                                                         | 가격 anchor              | outcome |
| ------- | ---------------: | ---------- | ---------------------------------------------------------------------- | ---------------------- | ------- |
| T0      |  Stage2 evidence | 2025-02-05 | IPO 1.2T won / $827.1M, AI/cloud services over half of sales           | issue price 61,900 won |         |
| T1      | price validation | 2025-02-05 | debut open 60,500 won, later 59,700 won                                | below issue price      |         |
| T2      |         4B-watch | 2025       | IPO overhang, valuation, external AI/cloud revenue, margin uncertainty | no full OHLC           |         |
| T3      |    Stage3-Yellow | N/A        | post-listing strength and recurring revenue needed                     | 보류                     |         |

LG CNS는 “좋은 테마라도 가격이 검증하지 않으면 점수를 낮춰야 한다”의 대표 case다. AI/cloud services가 매출의 절반 이상이었고 IPO도 1.2T won 규모로 컸다. 그런데 주가는 공모가 61,900원을 밑도는 59,700원에 거래됐다. 이건 `evidence_good_but_price_failed`다. AI/cloud headline을 Green으로 올리면 false positive가 된다. ([Reuters][5])

```json
{
  "case_id": "r13_loop16_lg_cns_ipo_false_positive_cross_redteam",
  "symbol": "064400",
  "best_trigger": "T1",
  "best_trigger_type": "evidence_good_but_price_failed",
  "trigger_date": "2025-02-05",
  "ipo_raise_krw_trn": 1.2,
  "ipo_raise_usd_mn": 827.1,
  "issue_price_krw": 61900,
  "debut_open_krw": 60500,
  "debut_later_price_krw": 59700,
  "price_vs_issue": "below_issue_price",
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "false_positive_if_promoted_to_stage3"
}
```

---

## Case F — Coupang breach / everyday delivery trust break

```text
symbols = CPNG / 035420 / 000120 / 139480
case_type = hard 4C + rival Stage2
```

| trigger |          type | date       | 당시 공개 evidence                                                        | 가격 anchor               | outcome |
| ------- | ------------: | ---------- | --------------------------------------------------------------------- | ----------------------- | ------- |
| T0      |       hard 4C | 2025-11~12 | Coupang breach, 34M users affected                                    | stock drawdown starts   |         |
| T1      | 4C validation | 2026-02-25 | Coupang -34%, MAU -3.5%, daily spending -6.3% to 139.2B won           | -34%                    |         |
| T2      |  rival Stage2 | 2026-02-25 | Naver users +23%, CJ Logistics overnight/one-day volume +120% Q4      | rival price unavailable |         |
| T3      |      4B-watch | 2026       | hypermarket late-night rule easing, revenue/margin conversion unknown | no full OHLC            |         |
| T4      | Stage3-Yellow | N/A        | rival GMV/revenue/margin 확인 필요                                        | 보류                      |         |

Coupang은 R13 hard 4C로 확정할 수 있다. breach 이후 stock은 약 -34%, mobile MAU는 -3.5%, daily consumer spending은 -6.3%로 139.2B won까지 내려갔다. 동시에 Naver online users는 +23%, CJ Logistics overnight/one-day delivery volume은 +120%였다. 즉 4C가 단순 headline이 아니라 **user behavior와 spending에 실제로 침투**했다. 다만 rival Stage2를 Green으로 올리려면 Naver/CJ/E-Mart의 revenue/margin conversion이 필요하다. ([Reuters][6])

```json
{
  "case_id": "r13_loop16_coupang_security_delivery_cross_redteam",
  "symbols": "CPNG/035420/000120/139480",
  "best_trigger": "T0/T2",
  "best_trigger_type": "hard_4C_with_rival_Stage2",
  "affected_users_mn": 34,
  "coupang_return_since_breach_pct": -34,
  "mobile_mau_change_pct": -3.5,
  "daily_spending_change_pct": -6.3,
  "daily_spending_krw_bn": 139.2,
  "naver_user_change_pct": 23,
  "cj_logistics_volume_yoy_pct": 120,
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "hard_4C_success_with_rival_stage2"
}
```

---

## Case G — Hyundai/Kia tariff relief that still sold off

```text
symbols = 005380 / 000270
case_type = tariff 4C + localization hedge
```

| trigger |            type | date       | 당시 공개 evidence                                                            | 가격 anchor                | outcome |
| ------- | --------------: | ---------- | ------------------------------------------------------------------------- | ------------------------ | ------- |
| T0      |   4C background | 2025-04    | U.S. imported auto tariff 25%                                             | tariff margin damage     |         |
| T1      | apparent relief | 2025-07-31 | U.S.-Korea trade deal, auto tariff 15%                                    | Hyundai -4.5%, Kia -6.6% |         |
| T2      |    Stage2 hedge | 2025       | Hyundai Group U.S. investment $21B, steel plant $5.8B, Georgia expansion  | hedge, not Green         |         |
| T3      |        4B-watch | 2025~2026  | localization utilization, tariff savings, U.S. sales mix, margin recovery | no full OHLC             |         |
| T4      |   Stage3-Yellow | N/A        | actual tariff absorption needed                                           | 보류                       |         |

Hyundai/Kia tariff case는 “relief headline인데 가격은 팔았다”는 RedTeam 핵심이다. 15% tariff는 25%보다 낮지만, 기존 KORUS zero-tariff advantage를 없앴고, Hyundai는 -4.5%, Kia는 -6.6% 하락했다. 즉 “관세 완화”라는 단어만 보고 Stage2-Actionable로 올리면 틀린다. 실제 시장은 **margin loss와 경쟁우위 상실**을 봤다. ([Reuters][7])

```json
{
  "case_id": "r13_loop16_hyundai_kia_tariff_redteam",
  "symbols": "005380/000270",
  "best_trigger": "T1/T3",
  "best_trigger_type": "4C_tariff_relief_that_still_sold_off",
  "trigger_date": "2025-07-31",
  "tariff_rate_after_deal_pct": 15,
  "prior_tariff_context_pct": 25,
  "hyundai_event_return_pct": -4.5,
  "kia_event_return_pct": -6.6,
  "4B_overlay": ["margin_damage", "KORUS_advantage_loss", "US_plant_utilization", "tariff_savings_uncertain"],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "tariff_4C_not_relief"
}
```

---

## Case H — KHNP / Czech nuclear preferred bidder with legal 4B

```text
symbols = 034020 / 052690 / 051600 / 015760
case_type = Stage2 nuclear export + legal 4B
```

| trigger |            type | date       | 당시 공개 evidence                                       | 가격 anchor              | outcome |
| ------- | --------------: | ---------- | ---------------------------------------------------- | ---------------------- | ------- |
| T0      | Stage2 evidence | 2024-07    | KHNP selected preferred bidder for Dukovany reactors | nuclear basket rallied |         |
| T1      |      validation | 2024       | two reactors, roughly $18B total project context     | no direct OHLC         |         |
| T2      |        legal 4B | 2025-05-06 | Czech court blocks final signing after EDF complaint | contract halted        |         |
| T3      |        4B-watch | 2025~      | appeal, final contract, financing, workshare, margin | no full OHLC           |         |
| T4      |   Stage3-Yellow | N/A        | final signing and legal clearance required           | 보류                     |         |

Czech nuclear case는 “preferred bidder는 Green이 아니다”를 보여준다. KHNP가 선택됐다는 Stage2는 강했지만, 2025년 5월 Czech court가 EDF complaint를 이유로 final contract signing을 막았다. 즉 원전 수출은 preferred bidder → final contract → legal clearance → workshare → margin 순서로 닫혀야 한다. 중간에 법원이 개입하면 바로 4B다. ([Reuters][8])

```json
{
  "case_id": "r13_loop16_czech_nuclear_legal_gate_cross_redteam",
  "symbols": "034020/052690/051600/015760",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage2_preferred_bidder_with_legal_4B",
  "preferred_bidder_date": "2024-07",
  "project_value_context_usd_bn": 18,
  "legal_4B_date": "2025-05-06",
  "legal_4B_event": "Czech_court_blocks_contract_signing_after_EDF_complaint",
  "stage3_gate_missing": ["final_contract", "legal_resolution", "workshare", "financing", "margin"],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "preferred_bidder_not_green_legal_4B"
}
```

---

# 6. Trigger별 실제 가격경로 검증

이번 R13은 full OHLC가 없으므로, 아래 표는 **reported event anchor 기준**이다. MFE/MAE window는 전부 `price_data_unavailable_after_deep_search`로 둔다.

| case                  | trigger |            event price / return |        market-relative | full MFE/MAE | 판정                             |
| --------------------- | ------- | ------------------------------: | ---------------------: | ------------ | ------------------------------ |
| Samsung SDS / KKR     | T1      | +20.8% intraday, +19.4% morning | +16.4pp vs KOSPI +3.0% | unavailable  | excellent Stage2-Actionable    |
| Samsung E&A / Fadhili | T1      |             +8.5% to 26,750 won |  +9.9pp vs KOSPI -1.4% | unavailable  | excellent Stage2-Actionable    |
| Hanwha / Romania K9   | T1      |               +5%+, record high |   market -0.1% context | unavailable  | good Stage2                    |
| Hanwha dilution       | T3      |                            -13% |            unavailable | unavailable  | 4B success                     |
| LIG Nex1 / Iraq       | T0      |                           +3.6% |  +2.7pp vs KOSPI +0.9% | unavailable  | good Stage2 / Yellow candidate |
| LG CNS IPO            | T1      |             61,900 → 59,700 won |      below issue price | unavailable  | evidence_good_but_price_failed |
| Coupang breach        | T1      |               -34% since breach |            unavailable | unavailable  | hard 4C                        |
| Hyundai/Kia tariff    | T1      |        Hyundai -4.5%, Kia -6.6% |            unavailable | unavailable  | tariff 4C                      |
| Czech nuclear         | T2      |           final signing blocked |        no direct price | unavailable  | legal 4B                       |

---

# 7. Case별 trigger 비교

## Stage2 entry 성과

```text
가장 좋은 Stage2:
1. Samsung SDS / KKR
2. Samsung E&A / Fadhili
3. Hanwha Aerospace / Romania K9
4. LIG Nex1 / Iraq M-SAM

좋지만 Green 금지:
1. Samsung SDS: CB dilution, AI/M&A execution 필요
2. Samsung E&A: EPC margin/cash conversion 필요
3. Hanwha: capital raise/dilution 4B 필요
4. LIG: delivery, production capacity, margin 필요
```

## Stage2-Actionable entry 성과

```text
Stage2-Actionable로 유지:
- Samsung SDS / KKR
- Samsung E&A / Fadhili
- Hanwha Aerospace / Romania, but with dilution 4B
- LIG Nex1 / Iraq, but Yellow candidate only after combat/export validation

Stage2로만 유지:
- Czech nuclear preferred bidder
- Hyundai localization/tariff hedge
- Coupang rival share-shift names

Actionable 금지:
- LG CNS IPO
- preferred bidder without final contract
- policy reform without company-specific action
- user shift without revenue/margin conversion
```

## Stage3-Yellow entry 성과

```text
Yellow 후보:
- LIG Nex1: export order + operator expansion + combat-validation context.
- Samsung SDS: foreign capital + advisory + price reaction, if M&A/AI execution begins.
- Samsung E&A: if project margin/cash conversion becomes visible.
- Hanwha: if dilution absorbed and delivery/margin remain intact.
```

## Stage3-Green

```text
이번 R13 Loop 16에서 확정 Green 없음.

이유:
- 대부분의 좋은 case가 아직 margin/cash/revenue/final-contract/execution gate를 남긴다.
- R13 목적은 Green 확정보다 false positive 제거다.
```

---

# 8. score-price alignment 판정

```text
aligned:
- Samsung SDS / KKR
- Samsung E&A / Fadhili
- Hanwha export + dilution overlay
- LIG Nex1 export validation
- Coupang hard 4C
- Hyundai/Kia tariff 4C
- LG CNS IPO price-failed
- Czech nuclear legal 4B

false_positive_score:
- LG CNS를 AI/cloud Stage3로 올리는 경우
- Czech nuclear를 final contract 전 Green으로 올리는 경우
- Hyundai tariff deal을 relief로만 보고 매수 신호를 주는 경우

missed_structural:
- LIG Nex1을 단순 Stage2로만 두고 combat/export validation을 반영하지 않는 경우
- Samsung SDS/KKR을 단순 CB dilution으로만 보고 strategic capital score를 주지 않는 경우

Stage2_promote_candidate:
- Samsung SDS / KKR
- Samsung E&A / Fadhili
- LIG Nex1 / Iraq-MSAM
- Hanwha Aerospace / Romania, 단 dilution 병기

evidence_good_but_price_failed:
- LG CNS IPO

event_premium:
- Hanwha defense rally
- Samsung SDS foreign capital rally
- nuclear preferred-bidder rally

thesis_break:
- Coupang trust breach
- Czech legal block if prolonged
- tariff margin damage if localization fails

hard_4C_success:
- Coupang breach
```

---

# 9. 점수비중 교정

## 올릴 축

```csv
axis,delta,reason,cases
reported_event_return,+5,"event return이 +5% 이상이고 market-relative도 강하면 Stage2-Actionable 후보","Samsung SDS, Samsung E&A, Hanwha"
market_relative_return,+5,"시장 대비 초과수익은 trigger quality의 핵심","Samsung SDS, Samsung E&A"
contract_value_visibility,+5,"계약금액이 확정되면 headline보다 강한 evidence","Samsung E&A, Hanwha, LIG"
strategic_capital_quality,+5,"외국 전략자본+자문+자금용도는 Stage2-Actionable","Samsung SDS"
delivery_margin_conversion,+5,"방산/EPC는 delivery와 margin이 Green gate","Hanwha, LIG, Samsung E&A"
security_trust_break,+5,"생활서비스 data breach는 hard 4C","Coupang"
legal_finality,+5,"preferred bidder는 final contract/legal clearance 전 Green 금지","Czech nuclear"
tariff_margin_reality,+5,"tariff relief headline보다 실제 margin reaction 우선","Hyundai/Kia"
```

## 내릴 축

```csv
axis,delta,reason,cases
theme_label_without_price_validation,-5,"AI/cloud 같은 테마명만으로 Stage3 금지","LG CNS"
ipo_demand_without_post_listing_strength,-5,"IPO 수요가 좋아도 공모가 하회하면 Actionable 금지","LG CNS"
preferred_bidder_without_contract,-5,"preferred bidder는 final contract 전까지 Stage2","Czech nuclear"
growth_with_dilution_ignored,-5,"증자/dilution 무시하면 4B를 놓침","Hanwha"
contract_without_margin,-4,"대형 수주만으로 Green 금지","Samsung E&A, Hanwha, LIG"
user_shift_without_revenue,-4,"MAU/user 이동은 revenue/margin 전환 전 Stage2","Coupang rivals"
policy_or_trade_relief_headline,-4,"relief headline인데 가격이 팔리면 4C를 우선","Hyundai/Kia"
```

---

# 10. Stage 2-Actionable 승격 조건

R13 cross-rule:

```text
Stage2-Actionable 승격:
아래 중 4개 이상이면 Stage2-Actionable로 올린다.

1. event return +5% 이상
2. market-relative return +5pp 이상
3. contract/deal/funding value 명확
4. trigger source가 Reuters/공시/계약/법원/정부처럼 hard source
5. trigger가 revenue/backlog/capital allocation으로 연결될 수 있음
6. 4B가 있더라도 식별 가능하고 size가 제한적
7. 가격이 공모가/직전 기대치를 명확히 이김
```

적용:

```text
Samsung SDS:
1,2,3,4,5 충족 → Stage2-Actionable.

Samsung E&A:
1,2,3,4,5 충족 → Stage2-Actionable.

Hanwha:
1,3,4,5 충족 → Stage2-Actionable, 그러나 dilution 4B.

LIG:
3,4,5 충족, 1은 약함. combat validation까지 들어오면 Yellow candidate.

LG CNS:
3,4,5 일부 충족하지만 7 실패 → Actionable 금지.

Czech nuclear:
3,4,5 충족하지만 final contract/legal 4B → Stage2 only.
```

---

# 11. Stage 3-Yellow 조건

R13 shadow rule:

```text
Stage3-Yellow:
Stage2-Actionable 이후 다음 중 2개 이상이 추가로 닫히면 Yellow.

1. delivery / execution schedule이 현실화
2. margin / cash conversion visibility
3. repeat orders or adoption evidence
4. legal/final contract clearance
5. dilution absorption or capital raise 목적 명확화
6. revenue or GMV conversion
7. 4B가 관리 가능한 수준으로 축소
```

Yellow 후보:

```text
LIG Nex1:
repeat operator + combat validation → Yellow 후보.

Samsung SDS:
KKR 자문이 실제 M&A/AI 매출/ROIC로 연결되면 Yellow.

Samsung E&A:
Fadhili margin/cash conversion 확인 시 Yellow.

Hanwha:
dilution absorption + delivery/margin 유지 시 Yellow.

Czech nuclear:
final contract signing + legal challenge resolution 시 Yellow.
```

---

# 12. Stage3-Green 조건

```text
Stage3-Green:
- Stage2-Actionable trigger 이후 margin/revenue/cash conversion이 확인된다.
- 4B overlay가 해소되거나 관리 가능해진다.
- 법적/승인/계약 finality가 닫힌다.
- 가격이 event 이후에도 구조적으로 버틴다.
- full OHLC 기준 MFE는 크고 MAE는 얕다.
```

이번 R13에서는 Green 확정 없음.

```text
stage3_green_confirmed = false
reason = full OHLC unavailable + conversion/finality gates not closed
```

---

# 13. 4B 조기감지 조건

R13에서 가장 중요한 보정이다.

```text
4B early-warning:
1. 좋은 수주 뒤 대규모 증자/CB/dilution
2. preferred bidder 뒤 법원/경쟁사 appeal
3. AI/cloud headline 뒤 IPO 공모가 하회
4. tariff relief headline 뒤 주가 하락
5. user shift 뒤 revenue/margin 미확인
6. policy reform 뒤 company-specific action 부재
7. contract value는 크지만 margin/cash conversion 부재
```

적용:

```text
Hanwha:
수주 Stage2 + dilution 4B.

Czech nuclear:
preferred bidder Stage2 + legal 4B.

LG CNS:
AI/cloud evidence + price-failed 4B/false positive.

Hyundai/Kia:
tariff relief headline + selloff = 4C/4B.

Samsung E&A:
excellent contract but margin/cash 4B.

Samsung SDS:
excellent foreign capital but CB dilution/AI execution 4B.
```

---

# 14. 4C hard gate 조건

```text
R13 hard 4C:
- customer trust breach with user/spending deterioration
- fatal accident / safety collapse
- political crisis / market-wide confidence break
- PF default / liquidity freeze
- final contract legally blocked for long period
- regulatory sanction that changes business model
```

이번 R13 hard 4C 확정:

```text
Coupang breach = hard_4C_success
```

Strong 4C-watch:

```text
Hyundai/Kia tariff margin damage
Czech nuclear legal block if prolonged
Hanwha dilution if repeated or opaque
LG CNS if post-listing weakness persists
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

R13 production 설계 원칙:

```text
1. reported_event_return을 trigger quality score에 반영한다.
2. market_relative_return을 Stage2-Actionable 승격 조건에 넣는다.
3. 좋은 headline도 price-failed이면 감점한다.
4. preferred bidder는 final contract 전까지 Green 금지한다.
5. contract value는 margin/cash conversion 전까지 Green 금지한다.
6. dilution/CB/capital raise는 4B overlay로 즉시 병기한다.
7. data breach는 user/spending deterioration이 있으면 hard 4C로 둔다.
8. tariff/policy relief headline은 가격반응이 반대면 4C로 우선 분류한다.
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_249.md 요약

```md
# R13 Loop 16. Cross-archetype RedTeam / 4B / 4C / Accounting Trust / Price Validation

이번 라운드는 R13 Loop 16 cross-archetype redteam 라운드다.

핵심 결론:
- Samsung SDS / KKR is excellent Stage2-Actionable. $820M CB, Samsung SDS +20.8% intraday and +19.4% morning vs KOSPI +3.0%. CB dilution and AI/M&A execution remain 4B.
- Samsung E&A / Fadhili is excellent Stage2-Actionable. Around $6B Saudi EPC contract, +8.5% to 26,750 won, while KOSPI -1.4%. Green requires EPC margin and cash conversion.
- Hanwha Aerospace shows Stage2 success plus 4B dilution. Romania K9/K10 $1B order and +5% record high were good, but later 3.6T won capital raise plan caused -13%.
- LIG Nex1 is Stage3-Yellow candidate. Iraq M-SAM II 3.71T won / $2.8B order, +3.6% vs KOSPI +0.9%, plus repeat operator expansion. Green requires delivery, production capacity and margin.
- LG CNS IPO is evidence_good_but_price_failed. AI/cloud services were over half of sales and IPO raised 1.2T won, but debut traded below 61,900 won issue price at 59,700 won.
- Coupang breach is hard 4C and rival Stage2. Coupang shares -34%, MAU -3.5%, daily spending -6.3%; Naver users +23% and CJ Logistics overnight/one-day volume +120%.
- Hyundai/Kia tariff is 4C despite relief headline. 15% U.S.-Korea tariff deal still drove Hyundai -4.5% and Kia -6.6%, showing margin damage and lost tariff advantage.
- Czech nuclear is Stage2 plus legal 4B. KHNP preferred-bidder status is not Green because Czech court blocked final signing after EDF complaint.

Main calibration:
- Raise reported_event_return, market_relative_return, contract_value_visibility, strategic_capital_quality, delivery_margin_conversion, security_trust_break, legal_finality, tariff_margin_reality.
- Lower theme_label_without_price_validation, ipo_demand_without_post_listing_strength, preferred_bidder_without_contract, growth_with_dilution_ignored, contract_without_margin, user_shift_without_revenue, policy_or_trade_relief_headline.
```

## docs/checkpoints/checkpoint_28a_round249_r13_loop16.md 요약

```md
# Checkpoint 28A Round 249 R13 Loop 16 Cross-RedTeam Calibration

## 반영 내용
- R13 Loop 16 cross-archetype trigger redteam을 수행했다.
- Samsung SDS/KKR, Samsung E&A/Fadhili, Hanwha Aerospace export+dilution, LIG Nex1 export validation, LG CNS IPO, Coupang breach, Hyundai/Kia tariff, KHNP Czech nuclear legal gate를 비교했다.
- full adjusted OHLC는 확보하지 못했으므로 Reuters/WSJ/FT reported event return과 event price anchor를 사용했다.
- MFE/MAE는 조작하지 않고 price_data_unavailable_after_deep_search로 분리했다.

## 핵심 보정
- Stage2-Actionable 승격에는 reported event return과 market-relative return을 반영한다.
- 좋은 headline이라도 price-failed이면 감점한다.
- preferred bidder, IPO demand, policy relief, contract value alone은 Green이 아니다.
- dilution/CB/legal block/tariff margin/user trust break는 4B/4C overlay로 즉시 병기한다.
```

## data/e2r_case_library/cases_r13_loop16_round249.jsonl 초안

```jsonl
{"case_id":"r13_loop16_samsung_sds_kkr_cross_redteam","symbol":"018260","company_name":"Samsung SDS","case_type":"Stage2_Actionable_foreign_strategic_capital_with_CB_4B","best_trigger":"T1/T2","price_validation":{"trigger_date":"2026-04-15","event_return_intraday_pct":20.8,"event_return_morning_pct":19.4,"kospi_same_context_pct":3.0,"market_relative_morning_pp":16.4,"cb_value_usd_mn":820,"cash_balance_krw_trn":6.4,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_actionable_with_4B","notes":"Strong strategic-capital trigger; CB dilution and AI/M&A execution remain 4B."}
{"case_id":"r13_loop16_samsung_ea_fadhili_cross_redteam","symbol":"028050","company_name":"Samsung E&A","case_type":"Stage2_Actionable_contract_value_with_margin_gate","best_trigger":"T1/T2","price_validation":{"trigger_date":"2024-04-03","contract_value_context_usd_bn":6.0,"event_return_pct":8.5,"event_price_krw":26750,"kospi_same_context_pct":-1.4,"market_relative_return_pp":9.9,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_actionable_contract_with_margin_gate","notes":"Contract and price aligned; EPC margin/cash conversion required for Yellow/Green."}
{"case_id":"r13_loop16_hanwha_export_dilution_cross_redteam","symbol":"012450","company_name":"Hanwha Aerospace","case_type":"Stage2_Actionable_export_with_dilution_4B","best_trigger":"T1/T3","price_validation":{"export_trigger_date":"2024-07-09","contract_value_usd_bn":1.0,"export_event_return_pct":">5","backlog_end_2021_krw_trn":5.1,"backlog_mar_2024_krw_trn":30,"dilution_trigger_date":"2025-03-21","capital_raise_plan_krw_trn":3.6,"dilution_event_return_pct":-13,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_success_with_4B_dilution","notes":"Export success is real, but capital raise dilution is real 4B."}
{"case_id":"r13_loop16_lig_nex1_export_yellow_cross_redteam","symbol":"079550","company_name":"LIG Nex1","case_type":"Stage3_Yellow_candidate_export_validation","best_trigger":"T0/T2","price_validation":{"trigger_date":"2024-09-20","contract_value_krw_trn":3.71,"contract_value_usd_bn":2.8,"event_return_pct":3.6,"kospi_same_context_pct":0.9,"market_relative_return_pp":2.7,"operator_count_after_iraq":4,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage3_Yellow_candidate_not_Green","notes":"Export order plus operator expansion supports Yellow candidate; production/margin needed for Green."}
{"case_id":"r13_loop16_lg_cns_ipo_false_positive_cross_redteam","symbol":"064400","company_name":"LG CNS","case_type":"evidence_good_but_price_failed","best_trigger":"T1","price_validation":{"trigger_date":"2025-02-05","ipo_raise_krw_trn":1.2,"ipo_raise_usd_mn":827.1,"issue_price_krw":61900,"debut_open_krw":60500,"debut_later_price_krw":59700,"price_vs_issue":"below_issue_price","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"false_positive_if_promoted_to_stage3","notes":"AI/cloud evidence was good but price failed; Actionable promotion prohibited."}
{"case_id":"r13_loop16_coupang_security_delivery_cross_redteam","symbol":"CPNG/035420/000120/139480","company_name":"Coupang / Naver / CJ Logistics / E-Mart","case_type":"hard_4C_with_rival_Stage2","best_trigger":"T0/T2","price_validation":{"affected_users_mn":34,"coupang_return_since_breach_pct":-34,"mobile_mau_change_pct":-3.5,"daily_spending_change_pct":-6.3,"daily_spending_krw_bn":139.2,"naver_user_change_pct":23,"cj_logistics_volume_yoy_pct":120,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"hard_4C_success_with_rival_stage2","notes":"Customer trust break drove stock/user/spending decline and created rival opportunity."}
{"case_id":"r13_loop16_hyundai_kia_tariff_redteam","symbol":"005380/000270","company_name":"Hyundai Motor / Kia","case_type":"4C_tariff_relief_that_still_sold_off","best_trigger":"T1/T3","price_validation":{"trigger_date":"2025-07-31","tariff_rate_after_deal_pct":15,"prior_tariff_context_pct":25,"hyundai_event_return_pct":-4.5,"kia_event_return_pct":-6.6,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"tariff_4C_not_relief","notes":"Relief headline still sold off because margin damage and tariff-advantage loss mattered."}
{"case_id":"r13_loop16_czech_nuclear_legal_gate_cross_redteam","symbol":"034020/052690/051600/015760","company_name":"KHNP / Doosan Enerbility / KEPCO E&C / KEPCO Plant S&E","case_type":"Stage2_preferred_bidder_with_legal_4B","best_trigger":"T0/T2","price_validation":{"preferred_bidder_date":"2024-07","project_value_context_usd_bn":18,"legal_4b_date":"2025-05-06","legal_4b_event":"Czech_court_blocks_contract_signing_after_EDF_complaint","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"preferred_bidder_not_green_legal_4B","notes":"Preferred bidder status remains Stage2 until final contract and legal clearance."}
```

## data/e2r_trigger_calibration/triggers_r13_loop16_round249.jsonl 초안

```jsonl
{"trigger_id":"r13l16_samsung_sds_kkr_T1","case_id":"r13_loop16_samsung_sds_kkr_cross_redteam","trigger_type":"Stage2-Actionable","trigger_date":"2026-04-15","event_return_pct":20.8,"market_relative_pp":16.4,"trigger_outcome_label":"excellent_entry_with_CB_4B","promote_to":"Stage2-Actionable"}
{"trigger_id":"r13l16_samsung_ea_fadhili_T1","case_id":"r13_loop16_samsung_ea_fadhili_cross_redteam","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-03","event_return_pct":8.5,"market_relative_pp":9.9,"trigger_outcome_label":"excellent_entry_contract_value_margin_gate","promote_to":"Stage2-Actionable"}
{"trigger_id":"r13l16_hanwha_romania_T1","case_id":"r13_loop16_hanwha_export_dilution_cross_redteam","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-09","event_return_pct":">5","trigger_outcome_label":"good_entry_defense_export","promote_to":"Stage2-Actionable"}
{"trigger_id":"r13l16_hanwha_dilution_T3","case_id":"r13_loop16_hanwha_export_dilution_cross_redteam","trigger_type":"4B_dilution","trigger_date":"2025-03-21","event_return_pct":-13,"trigger_outcome_label":"4B_success_dilution","promote_to":"4B-watch"}
{"trigger_id":"r13l16_lig_iraq_T0","case_id":"r13_loop16_lig_nex1_export_yellow_cross_redteam","trigger_type":"Stage3-Yellow_candidate","trigger_date":"2024-09-20","event_return_pct":3.6,"market_relative_pp":2.7,"trigger_outcome_label":"good_stage2_to_yellow_candidate","promote_to":"Stage3-Yellow_candidate"}
{"trigger_id":"r13l16_lg_cns_ipo_T1","case_id":"r13_loop16_lg_cns_ipo_false_positive_cross_redteam","trigger_type":"false_positive_price_failed","trigger_date":"2025-02-05","event_return_pct":"below_issue_price","trigger_outcome_label":"evidence_good_but_price_failed","promote_to":"no_actionable"}
{"trigger_id":"r13l16_coupang_breach_T1","case_id":"r13_loop16_coupang_security_delivery_cross_redteam","trigger_type":"hard_4C","trigger_date":"2025-11_to_2026-02","event_return_pct":-34,"trigger_outcome_label":"hard_4C_success_customer_trust_break","promote_to":"4C"}
{"trigger_id":"r13l16_hyundai_kia_tariff_T1","case_id":"r13_loop16_hyundai_kia_tariff_redteam","trigger_type":"4C_tariff_margin","trigger_date":"2025-07-31","event_return_pct":"Hyundai_-4.5_Kia_-6.6","trigger_outcome_label":"tariff_relief_headline_failed","promote_to":"4C-watch"}
{"trigger_id":"r13l16_czech_nuclear_legal_T2","case_id":"r13_loop16_czech_nuclear_legal_gate_cross_redteam","trigger_type":"4B_legal_gate","trigger_date":"2025-05-06","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"preferred_bidder_legal_4B","promote_to":"4B-watch"}
```

## data/sector_taxonomy/score_weight_profiles_round249_r13_loop16_v1.csv 초안

```csv
archetype,reported_event_return,market_relative_return,contract_value_visibility,strategic_capital_quality,delivery_margin_conversion,security_trust_break,legal_finality,tariff_margin_reality,theme_label_without_price_validation_penalty,ipo_demand_without_post_listing_strength_penalty,preferred_bidder_without_contract_penalty,growth_with_dilution_ignored_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
CROSS_STAGE2_ACTIONABLE_CONFIRMED,+5,+5,+4,+4,+3,+0,+1,+1,-2,-2,-2,-2,event return and relative return closed,conversion gate remains,margin/revenue/cash conversion,Samsung SDS/Samsung E&A.
GOOD_EVIDENCE_PRICE_FAILED,+0,-5,+2,+1,+0,+0,+0,+0,-5,-5,-2,-1,good evidence but price failed,no Actionable,post-listing strength required,LG CNS.
CONTRACT_VALUE_WITH_MARGIN_GATE,+5,+5,+5,+0,+5,+0,+1,+0,-2,-1,-1,-1,contract value strong,margin/cash missing,margin+cash conversion,Samsung E&A.
GROWTH_WITH_DILUTION_4B,+4,+2,+5,+0,+4,+0,+1,+0,-1,-1,-1,-5,growth order strong,dilution overlay,delivery+margin+dilution absorption,Hanwha.
EXPORT_ORDER_TO_COMBAT_VALIDATION_YELLOW,+4,+3,+5,+0,+5,+0,+1,+0,-1,-1,-1,-1,export order plus validation,production/margin missing,repeat orders+delivery+margin,LIG Nex1.
POLICY_OR_PREFERRED_BIDDER_WITH_LEGAL_4B,+2,+1,+3,+0,+2,+0,+5,+0,-2,-1,-5,-1,preferred bidder/policy stage2,legal finality missing,final contract+legal resolution,Czech nuclear.
SECURITY_TRUST_BREAK_HARD_4C,+0,+0,+0,+0,+0,+5,+0,+0,-1,-1,-1,-1,data breach with user/spending decline,hard 4C,N/A,Coupang.
TARIFF_RELIEF_THAT_STILL_SELLOFF,+0,-5,+0,+0,+3,+0,+1,+5,-1,-1,-1,-1,relief headline sold off,margin reality first,tariff savings+localization margin,Hyundai/Kia.
```

---

# 이번 R13 Loop 16 결론

```text
1. Stage2-Actionable은 “좋은 뉴스”가 아니라 “가격이 검증한 좋은 뉴스”다.
   Samsung SDS, Samsung E&A가 대표다.

2. Stage3-Green은 아직 너무 이르다.
   대부분 margin, cash conversion, final contract, revenue conversion, dilution absorption이 남아 있다.

3. LG CNS는 false positive 방지용 핵심 case다.
   AI/cloud evidence가 좋아도 공모가를 밑돌면 Actionable 금지다.

4. Hanwha는 growth + dilution 병기 case다.
   수주 success는 유지하되 4B overlay를 반드시 붙인다.

5. LIG Nex1은 Stage2에서 Yellow 후보로 올릴 수 있는 case다.
   order + operator expansion + combat validation이 붙으면 기존 Stage2보다 높은 tier가 맞다.

6. Coupang은 hard 4C다.
   단순 breach headline이 아니라 주가, MAU, spending이 실제로 깨졌다.

7. Hyundai/Kia tariff는 “relief headline”을 믿으면 안 되는 case다.
   15%로 낮아져도 주가가 팔리면 market은 margin damage를 본 것이다.

8. Czech nuclear는 preferred bidder를 Green으로 올리면 안 되는 case다.
   final contract와 legal clearance가 닫혀야 한다.
```

한 문장으로 압축하면:

> **R13 Loop 16에서 배운 핵심은 “뉴스의 크기”가 아니라 “가격이 검증한 trigger인지, 그리고 그 trigger 뒤에 dilution·legal·margin·trust·tariff gate가 남아 있는지”다. Stage2를 무조건 보수적으로 죽이면 LIG·Samsung SDS 같은 후보를 놓치고, headline만 믿고 Green을 주면 LG CNS·Czech nuclear·Hyundai tariff 같은 false positive에 걸린다.**

다음 순서는 **R1 Loop 17 — 산업재·수주·인프라**로 돌아간다.

* [Reuters](https://www.reuters.com/world/asia-pacific/kkr-buy-820-million-samsung-sds-convertible-bonds-shares-jump-20-2026-04-15/?utm_source=chatgpt.com)
* [월스트리트저널](https://www.wsj.com/articles/samsung-e-a-shares-rise-on-6-billion-saudi-contract-win-10a5b2f4?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/aerospace-defense/south-koreas-hanwha-aerospace-wins-1-bln-order-romania-k9-howitzers-2024-07-09/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/aerospace-defense/south-koreas-lig-nex1-wins-28-bln-deal-with-iraq-export-missile-systems-2024-09-19/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/technology/skorean-tech-services-firm-lg-cns-falls-stock-market-debut-2025-02-05/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/retail-consumer/coupang-braces-increased-competition-amid-fallout-south-korea-data-breach-2026-02-25/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/autos-transportation/south-korea-automaker-shares-slip-after-us-trade-deal-2025-07-31/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/sustainability/boards-policy-regulation/czech-court-halts-nuclear-plant-signing-with-khnp-after-last-minute-appeal-2025-05-06/?utm_source=chatgpt.com)

[1]: https://www.reuters.com/world/asia-pacific/kkr-buy-820-million-samsung-sds-convertible-bonds-shares-jump-20-2026-04-15/?utm_source=chatgpt.com "KKR to buy $820 million of Samsung SDS convertible bonds, shares jump 20%"
[2]: https://www.wsj.com/articles/samsung-e-a-shares-rise-on-6-billion-saudi-contract-win-10a5b2f4?utm_source=chatgpt.com "Samsung E&A Shares Rise on $6 Billion Saudi Contract Win"
[3]: https://www.reuters.com/business/aerospace-defense/south-koreas-hanwha-aerospace-wins-1-bln-order-romania-k9-howitzers-2024-07-09/?utm_source=chatgpt.com "South Korea's Hanwha Aerospace wins $1 bln order from Romania for self-propelled howitzers"
[4]: https://www.reuters.com/business/aerospace-defense/south-koreas-lig-nex1-wins-28-bln-deal-with-iraq-export-missile-systems-2024-09-19/?utm_source=chatgpt.com "South Korea's LIG Nex1 wins $2.8 bln Iraq deal to export missile systems"
[5]: https://www.reuters.com/technology/skorean-tech-services-firm-lg-cns-falls-stock-market-debut-2025-02-05/?utm_source=chatgpt.com "South Korean tech services firm LG CNS drops in market debut"
[6]: https://www.reuters.com/business/retail-consumer/coupang-braces-increased-competition-amid-fallout-south-korea-data-breach-2026-02-25/?utm_source=chatgpt.com "Coupang braces for increased competition amid fallout from South Korea data breach"
[7]: https://www.reuters.com/business/autos-transportation/south-korea-automaker-shares-slip-after-us-trade-deal-2025-07-31/?utm_source=chatgpt.com "South Korea automaker shares slip after US trade deal"
[8]: https://www.reuters.com/sustainability/boards-policy-regulation/czech-court-halts-nuclear-plant-signing-with-khnp-after-last-minute-appeal-2025-05-06/?utm_source=chatgpt.com "Czech court halts nuclear plant signing with KHNP after last-minute appeal"
