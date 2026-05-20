# Round 283 R1 Green Gate Review

Do not apply these weights to production scoring yet.

R1 Stage 3-Green is not `order`, `defense`, `grid`, `shipbuilding`, `robotics`, or `IPO` as a label. It requires delivery, revenue recognition, margin, working capital, capacity utilization, financing, dilution-adjusted EPS, and price validation.

## Required Fields

- actual_delivery_revenue_confirmed
- backlog_to_revenue_conversion_confirmed
- order_margin_visibility_confirmed
- working_capital_control_confirmed
- local_production_execution_confirmed
- capacity_utilization_confirmed
- customer_financing_visibility_confirmed
- dilution_adjusted_EPS_confirmed
- contract_cancellation_risk_cleared
- aftermarket_IPO_demand_confirmed
- price_path_after_evidence

## Forbidden Patterns

- order_headline_only
- customer_or_parent_name_only
- strategic_stake_only
- capacity_expansion_without_backlog
- IPO_first_day_pop_only
- merger_theme_without_synergy
- defence_order_expectation_without_funding
- dilutive_share_issue
- geopolitical_contract_execution_risk

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| actual_delivery_revenue | raise | 5 | 수주가 실제 납품과 매출 인식으로 닫혀야 Stage 3 후보가 된다. |
| backlog_to_revenue_conversion | raise | 5 | 수주잔고가 매출로 내려오는 경로를 더 강하게 본다. |
| order_margin_visibility | raise | 5 | 대형 수주는 원가율과 OP margin이 확인되어야 한다. |
| working_capital_control | raise | 5 | 운전자본·미청구·현금회수 문제가 없을 때만 수주 품질을 인정한다. |
| local_production_execution | raise | 4 | 방산 현지생산 조건은 납품 일정과 마진의 핵심 gate다. |
| capacity_utilization | raise | 5 | 증설은 가동률과 주문이 같이 있어야 EPS/FCF로 연결된다. |
| customer_financing_visibility | raise | 4 | 정부·고객 financing이 확인되지 않은 주문 기대는 제한한다. |
| dilution_adjusted_EPS | raise | 5 | 증자 이후 EPS 체급이 유지되는지를 별도 확인한다. |
| contract_cancellation_risk | raise | 5 | 수주 산업재는 계약취소·제재·arbitration 리스크를 hard gate로 본다. |
| aftermarket_IPO_demand | raise | 4 | IPO 첫날 수요보다 상장 후 수요와 실적 지속성이 중요하다. |
| order_headline_only | lower | -5 | 수주했다는 말만으로 Green을 만들지 않는다. |
| customer_or_parent_name_only | lower | -5 | 유명 고객/모회사 이름은 납품·매출·마진의 대체물이 아니다. |
| strategic_stake_only | lower | -5 | 전략적 지분투자는 로봇 출하량과 마진이 아니다. |
| capacity_expansion_without_backlog | lower | -5 | 증설만 있고 수주잔고와 가동률이 없으면 제한한다. |
| IPO_first_day_pop_only | lower | -5 | IPO 첫날 급등은 4B-watch이지 Stage 3 근거가 아니다. |
| merger_theme_without_synergy | lower | -5 | 합병/MASGA 테마는 실제 주문·시너지 전에는 event premium이다. |
| defence_order_expectation_without_funding | lower | -4 | 방산 기대는 정부 예산·financing·납품 일정이 필요하다. |
| dilutive_share_issue | lower | -5 | 테마 랠리 뒤 희석 증자는 EPS/FCF 경로를 훼손한다. |
| geopolitical_contract_execution_risk | lower | -5 | 전쟁·제재·선주 리스크가 있으면 backlog를 그대로 인정하지 않는다. |

## Easy Examples
- `K2 export` is stronger when delivered tanks are recognized in revenue, not only when a contract is announced.
- `US grid demand` is Stage 2 until backlog, capacity utilization and margin are confirmed.
- `IPO +97% debut` is a 4B-watch signal until aftermarket demand and earnings durability are proven.
