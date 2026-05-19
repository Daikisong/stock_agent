# Round-205 R1 Loop-8 Green Gate Review

## Green Required Evidence

- `contract_amount_confirmed`
- `contract_duration_or_delivery_schedule_confirmed`
- `actual_delivery_or_revenue_recognition_confirmed`
- `opm_or_eps_revision_confirmed`
- `backlog_quality_confirmed`
- `price_path_after_evidence`
- `sanction_financing_dilution_margin_risk_passed`

## Green Forbidden Patterns

- `order_headline_only`
- `ipo_first_day_rally`
- `mou_or_preliminary_policy_event`
- `record_high_on_policy_event`
- `contract_without_margin_visibility`
- `policy_theme_only`

## Shadow Score Adjustments

| axis | direction | points | reason |
| --- | --- | ---: | --- |
| `contract_amount_to_sales` | raise | 4 | 계약금액/매출 비율이 확인된 수주형 사례를 더 강하게 본다. |
| `delivery_schedule` | raise | 4 | 납품 일정이 있어야 수주가 매출로 이어질 수 있다. |
| `order_to_revenue_conversion` | raise | 5 | 수주 헤드라인보다 실제 매출 전환을 보상한다. |
| `op_eps_revision` | raise | 5 | 수주가 OP/EPS 상향으로 연결될 때 Stage 3 근거가 된다. |
| `government_backlog` | raise | 4 | 정부 고객과 다년 backlog는 방산 visibility를 높인다. |
| `combat_validation` | raise | 3 | 실전 검증은 방공/요격체계 수요 확률을 높인다. |
| `local_production_or_technology_transfer` | raise | 3 | 현지생산/기술이전은 방산 수주 지속성을 높인다. |
| `price_path_alignment` | raise | 5 | Stage 2/3 증거 이후 가격경로가 맞는지 검증한다. |
| `order_headline_only` | lower | -4 | 수주 기사만 있고 마진·납품·EPS가 없으면 Green 금지다. |
| `ipo_first_day_rally` | lower | -5 | IPO 첫날 급등은 수주/FCF 증거가 아니므로 4B-watch다. |
| `mou_or_preliminary_policy_event` | lower | -4 | MOU·정책 예비 이벤트는 매출 전환 전까지 Stage 1/2에 둔다. |
| `record_high_on_policy_event` | lower | -3 | 정책/합병 이벤트 신고가는 evidence-before-price가 아닐 수 있다. |
| `contract_without_margin_visibility` | lower | -3 | 계약이 있어도 마진 visibility가 없으면 Green을 막는다. |
| `geopolitical_exposure_unpriced` | lower | -3 | 제재·지정학 리스크가 매출을 흔들 수 있으면 RedTeam에 반영한다. |

## What Not To Change

- Do not apply these weights to production scoring yet.
- Do not use Round205 cases as candidate-generation input.
- Do not lower Stage 3-Green thresholds to force promotion.
- Do not invent full OHLC, stage prices, or MFE/MAE when only reported anchors exist.
- Do not treat order headlines, IPO rallies, MOU/policy events, or record-high event moves as Green evidence alone.
