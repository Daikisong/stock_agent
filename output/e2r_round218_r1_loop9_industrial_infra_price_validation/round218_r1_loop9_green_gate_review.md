# Round 218 R1 Green Gate Review

Do not apply these weights to production scoring yet.

## Required Fields

- company_order_or_contract_confirmed
- contract_amount_customer_delivery_visible
- actual_delivery_or_revenue_recognition_confirmed
- margin_and_cost_control_confirmed
- backlog_to_revenue_conversion_confirmed
- eps_revision_or_fcf_path_confirmed
- price_path_after_evidence_confirmed
- geopolitical_financing_dilution_risk_passed
- no_hard_redteam

## Forbidden Patterns

- policy_news_only
- mou_or_merger_policy_only
- contract_headline_without_margin
- epc_order_without_cost_control
- transformer_sector_data_without_company_order
- nuclear_preferred_bidder_without_equipment_backlog
- shipbuilding_policy_theme_without_funded_order
- sanctions_or_geopolitical_trust_break
- ipo_event_premium_only
- record_high_event_rally
- high_score_without_price_validation

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| confirmed_contract_amount | raise | 5 | 계약금액이 고객·납기와 같이 확인되면 Stage 2 품질이 올라간다. |
| order_to_revenue_conversion | raise | 5 | 수주가 납품·매출·OP/EPS로 내려오는 경로를 보상한다. |
| delivery_schedule | raise | 4 | 납기와 공정이 있어야 backlog가 실제 실적으로 변한다. |
| backlog_margin_visibility | raise | 5 | 수주잔고가 마진과 FCF로 이어질 때만 Green에 가까워진다. |
| customer_quality | raise | 4 | 전력망·정부·Aramco처럼 고객 질이 높으면 visibility가 좋아진다. |
| capacity_bottleneck | raise | 4 | 변압기 lead time, CAPA 병목, 선박 슬롯 부족은 구조적 신호다. |
| us_grid_exposure | raise | 4 | 미국 grid/data-center exposure는 R1 구조 신호지만 회사별 주문 확인이 필요하다. |
| price_path_alignment | raise | 5 | 증거 이후 가격경로가 따라오면 score-price alignment를 인정한다. |
| contract_headline_without_margin | lower | -5 | 계약 headline만 있고 마진·현금회수가 없으면 Green 금지다. |
| policy_or_mou_without_order | lower | -5 | 정책·MOU·합병 이벤트는 funded order 전 event premium이다. |
| ipo_first_day_rally | lower | -5 | IPO 첫날 급등은 구조적 Stage 3가 아니라 4B-watch다. |
| record_high_on_policy_event | lower | -4 | 정책/합병 신고가는 가격이 증거보다 앞섰을 수 있다. |
| geopolitical_sanction_unpriced | lower | -4 | 제재·지정학 리스크는 4C-watch로 별도 분리한다. |
| epc_backlog_without_cashflow | lower | -4 | EPC 대형수주는 원가율·cash collection 전 Green이 아니다. |

## Easy Examples
- `계약금액 + 납기 + 마진 + EPS revision`이 같이 있어야 Stage 3 후보가 된다.
- `정책/MOU/합병 뉴스 + 신고가`는 funded order 전 4B-watch다.
- `IPO 첫날 +96.5%`는 운영 증거가 아니라 event premium이다.
- `중국 제재`는 실제 매출 차질 확인 전 4C-watch로 기록한다.
