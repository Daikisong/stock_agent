# Round-206 R2 Loop-8 Green Gate Review

## Green Required Evidence

- `company_level_customer_evidence`
- `product_specific_exposure`
- `order_shipment_contract_or_revenue_path_confirmed`
- `gross_margin_or_opm_improvement`
- `eps_fcf_revision_confirmed`
- `capacity_bottleneck_or_supply_allocation`
- `price_path_after_evidence`
- `export_control_china_fab_accounting_trust_passed`

## Green Forbidden Patterns

- `ai_keyword_only`
- `server_theme_only`
- `unconfirmed_customer_media_report`
- `design_win_without_revenue`
- `policy_foundry_without_order`
- `openai_or_nvidia_headline_without_company_revenue`

## Shadow Score Adjustments

| axis | direction | points | reason |
| --- | --- | ---: | --- |
| `eps_revision` | raise | 5 | HBM/메모리 rerating은 EPS 상향이 동반될 때 가격경로와 맞았다. |
| `capacity_bottleneck` | raise | 5 | HBM 공급 배분과 CAPA 병목은 R2 구조적 visibility의 핵심이다. |
| `customer_visibility` | raise | 5 | 고객 주문과 수요 visibility가 없는 AI 이름표는 부족하다. |
| `confirmed_customer_order` | raise | 5 | 확인된 고객 주문과 미확정 media report를 분리한다. |
| `hbm_product_specificity` | raise | 4 | HBM/TSV-TC bonder처럼 제품 노출이 특정될수록 신뢰도가 높다. |
| `order_to_revenue_conversion` | raise | 4 | 수주와 design win은 매출 전환 경로가 있을 때 Stage 3 후보가 된다. |
| `gross_margin_visibility` | raise | 4 | R2 Green에는 gross margin 또는 OPM 개선이 필요하다. |
| `price_path_alignment` | raise | 5 | 증거 이후 가격경로가 따라온 케이스를 보상한다. |
| `ai_keyword_only` | lower | -5 | AI 이름만으로는 EPS/FCF 체급 변화를 증명하지 못한다. |
| `server_theme_only` | lower | -4 | 서버 테마만 있고 고객·제품·마진이 없으면 Green 금지다. |
| `design_win_without_revenue` | lower | -4 | design win은 Stage 2 근거지만 양산·매출 전 Green은 아니다. |
| `policy_foundry_without_order` | lower | -4 | 정책 foundry 협의는 회사 단위 order/utilization 전까지 이벤트다. |
| `unconfirmed_media_report` | lower | -5 | 미확정 고객 보도 급등은 4B-watch로 분리한다. |
| `openai_or_nvidia_event_without_company_revenue` | lower | -3 | OpenAI/Nvidia headline은 회사 매출 경로 전까지 Green 충분조건이 아니다. |
| `customer_name_without_margin` | lower | -3 | 고객 이름만 있고 margin이 없으면 고신뢰 Green을 막는다. |
| `price_rally_before_confirmation` | lower | -5 | 확인 전 가격 급등은 price-before-evidence로 본다. |

## What Not To Change

- Do not apply these weights to production scoring yet.
- Do not use Round206 cases as candidate-generation input.
- Do not lower Stage 3-Green thresholds to force promotion.
- Do not invent full OHLC, stage prices, or MFE/MAE when only reported anchors exist.
- Do not treat AI keyword, server theme, design win, policy foundry, unconfirmed customer report, or OpenAI/Nvidia headline as Green evidence alone.
