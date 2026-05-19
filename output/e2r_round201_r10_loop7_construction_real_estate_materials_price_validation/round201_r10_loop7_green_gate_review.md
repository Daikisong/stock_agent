# Round-201 R10 Loop-7 Green Gate Review

## Green Required Evidence

- `company_level_order_or_tenant_confirmed`
- `cash_flow_after_working_capital_confirmed`
- `epc_margin_or_noi_affo_confirmed`
- `pf_and_funding_cost_risk_passed`
- `cost_ratio_or_project_progress_stable`
- `tenant_occupancy_or_utilization_confirmed`
- `capex_per_share_or_dilution_passed`
- `safety_quality_trust_passed`
- `price_path_after_cash_flow_evidence`

## Green Forbidden Patterns

- `contract_headline_only`
- `pf_relief_policy_only`
- `real_estate_rebound_theme_only`
- `data_center_theme_without_tenant`
- `asset_headline_without_noi_affo`
- `reit_yield_headline_only`
- `epc_backlog_without_margin`
- `low_margin_order_risk`
- `capex_per_share_dilution`
- `quality_safety_incident`
- `workplace_fatality_repeated`
- `working_capital_worsening`

## Shadow Score Adjustments

| axis | direction | points | reason |
| --- | --- | ---: | --- |
| `cash_flow_after_working_capital` | raise | 5 | R10 Green은 수주가 현금흐름으로 닫힐 때 강하다. |
| `epc_margin_visibility` | raise | 5 | 대형 EPC는 계약 크기보다 마진 가시성이 Stage 3의 핵심이다. |
| `project_cost_control` | raise | 4 | 공정률과 원가율이 안정되어야 저마진 수주 위험을 줄인다. |
| `handover_milestone` | raise | 3 | 완공·인도 milestone은 수주 headline보다 강한 Stage 2 증거다. |
| `pf_credit_cleanup` | raise | 5 | PF 부실 정리와 우량 프로젝트 분리가 확인될 때만 credit relief를 올린다. |
| `funding_cost_control` | raise | 4 | 리츠·부동산은 조달비용이 배당과 AFFO를 결정한다. |
| `tenant_contract_quality` | raise | 5 | 데이터센터 real asset은 임차계약이 있어야 현금흐름 후보가 된다. |
| `noi_affo_visibility` | raise | 5 | 자산 headline보다 NOI/AFFO와 배당 커버리지가 중요하다. |
| `occupancy_or_utilization` | raise | 4 | 공실률·가동률이 숫자로 확인되어야 자산 수익성이 보인다. |
| `power_water_permitting_secured` | raise | 4 | AI 데이터센터는 전력·물·인허가가 병목이다. |
| `safety_quality_trust` | raise | 5 | 건설주는 안전·품질 신뢰가 Green의 전제다. |
| `contract_headline_only` | lower | -4 | 수주 headline만으로 Stage 3-Green을 만들지 않는다. |
| `pf_relief_policy_only` | lower | -5 | PF 지원책은 relief이지 체급 변화 증거가 아니다. |
| `real_estate_rebound_theme_only` | lower | -4 | 부동산 반등 테마만으로 현금흐름을 발명하지 않는다. |
| `data_center_theme_without_tenant` | lower | -5 | 임차인 없는 데이터센터 테마는 Green 금지다. |
| `asset_headline_without_noi_affo` | lower | -5 | 자산 보유 headline은 NOI/AFFO 전까지 제한한다. |
| `epc_backlog_without_margin` | lower | -4 | 수주잔고가 많아도 마진이 없으면 Stage 3가 아니다. |
| `low_margin_order_risk` | lower | -4 | 저마진 EPC는 수주가 오히려 현금흐름 부담이 될 수 있다. |
| `capex_per_share_dilution` | lower | -4 | CAPEX가 주당 AFFO/FCF를 희석하면 Green을 막는다. |
| `quality_safety_incident` | lower | -5 | 아파트 붕괴·품질 사고는 hard RedTeam이다. |
| `workplace_fatality_repeated` | lower | -5 | 반복 사망사고와 현장중단은 operational trust 4C gate다. |

## What Not To Change

- Do not apply these weights to production scoring yet.
- Do not use Round201 cases as candidate-generation input.
- Do not lower Stage 3-Green thresholds to force promotion.
- Do not invent cash flow, EPC margin, NOI/AFFO, tenant contracts, power/water, funding cost, capex per share, stage prices, or MFE/MAE.
- Do not treat contract headline, PF support, real-estate rebound, AI data-center headline, REIT yield, or disaster rebuild as Green evidence alone.
