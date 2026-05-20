# Round 282 R13 Green Gate Review

Do not apply these weights to production scoring yet.

R13 Stage 3-Green is not `customer name`, `IPO size`, `control premium`, `M&A synergy`, or `mega order`. It requires conversion into revenue, margin, cashflow, trust, governance, and post-evidence price validation.

## Required Fields

- actual_calloff_revenue_recognition_confirmed
- shipment_or_delivery_conversion_confirmed
- project_margin_cash_conversion_confirmed
- working_capital_unbilled_receivables_confirmed
- aftermarket_ipo_demand_confirmed
- parent_ROI_bridge_confirmed
- M&A_closing_regulatory_integration_confirmed
- data_trust_internal_control_confirmed
- custody_and_digital_asset_control_confirmed
- fatal_safety_event_absent_or_resolved
- dilution_and_governance_risk_cleared
- accounting_investigation_absent_or_resolved
- price_path_after_evidence

## Forbidden Patterns

- customer_name_headline_only
- order_backlog_headline_only
- IPO_size_or_oversubscription_only
- control_premium_only
- M&A_synergy_before_trust
- AI_cloud_keyword_without_aftermarket_demand
- governance_fight_or_dilution
- accounting_fraud_review
- safety_or_data_trust_unresolved

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| trust_and_internal_control | raise | 5 | 보안·개인정보·내부통제 훼손은 EPS보다 먼저 Green을 막는다. |
| fatal_safety_event | raise | 5 | 항공·건설·배터리·의료기기에서는 사망사고가 hard 4C gate다. |
| actual_calloff_vs_contract | raise | 5 | 고객명 계약 headline은 call-off, shipment, revenue로 닫혀야 한다. |
| custody_and_digital_asset_control | raise | 5 | 디지털자산 M&A는 수탁·인출·규제 통제가 확인되어야 한다. |
| aftermarket_IPO_demand | raise | 5 | IPO 수요예측보다 상장 후 가격·거래 수요가 품질 검증이다. |
| governance_dilution_control | raise | 5 | 경영권 분쟁 프리미엄은 신주발행·희석·지배구조 리스크와 함께 본다. |
| accounting_investigation_flag | raise | 5 | 회계조사·공시통제 실패는 구조적 rerating을 차단한다. |
| project_margin_cash_conversion | raise | 5 | 대형 EPC 수주는 프로젝트 마진과 현금회수가 보여야 한다. |
| working_capital_unbilled_receivables | raise | 5 | 미청구공사·운전자본 stress는 수주 headline보다 중요하다. |
| parent_ROI_bridge | raise | 4 | 자회사 IPO는 모회사 ROIC/FCF/환원 bridge가 있어야 한다. |
| customer_name_headline_only | lower | -5 | 고객명이 유명하다는 이유만으로 Green을 만들지 않는다. |
| order_backlog_headline_only | lower | -5 | 수주잔고 headline만 있고 마진·현금화가 없으면 제한한다. |
| IPO_size_or_oversubscription_only | lower | -5 | IPO 규모와 청약경쟁률은 상장 후 수요 검증 전에는 부족하다. |
| control_premium_only | lower | -5 | 경영권 프리미엄은 운영 EPS/FCF 변화가 아니다. |
| M&A_synergy_before_trust | lower | -5 | M&A synergy는 신뢰·수탁·규제 이슈보다 뒤에 본다. |
| AI_cloud_keyword_without_aftermarket_demand | lower | -5 | AI/cloud 키워드만으로 IPO 품질을 인정하지 않는다. |
| governance_fight_or_dilution | lower | -5 | 분쟁·희석은 자본배분 질을 훼손한다. |
| accounting_fraud_review | lower | -5 | 회계부정 검토 flag는 hard RedTeam 입력이다. |
| safety_or_data_trust_unresolved | lower | -5 | 안전·데이터 신뢰가 열려 있으면 Green은 차단한다. |

## Easy Examples
- `Tesla customer name` is Stage 2 evidence at most until call-off and revenue recognition are confirmed.
- `large IPO oversubscription` needs aftermarket price validation before it supports rerating.
- `mega EPC order` needs project margin, working capital, and cash collection before Green.
