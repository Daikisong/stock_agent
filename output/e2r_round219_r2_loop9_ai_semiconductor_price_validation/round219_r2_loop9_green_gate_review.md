# Round 219 R2 Green Gate Review

Do not apply these weights to production scoring yet.

## Required Fields

- company_level_customer_evidence
- product_specific_exposure
- order_shipment_contract_or_revenue_path_confirmed
- gross_margin_or_opm_improvement
- eps_fcf_revision_confirmed
- capacity_bottleneck_or_supply_allocation
- price_path_after_evidence
- export_control_china_fab_labor_accounting_trust_passed
- no_hard_redteam

## Forbidden Patterns

- ai_keyword_only
- server_theme_only
- unconfirmed_customer_media_report
- design_win_without_revenue
- policy_foundry_without_order
- openai_or_nvidia_headline_without_company_revenue
- customer_name_without_margin
- price_rally_before_confirmation
- labor_disruption_unpriced
- export_control_unpriced

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| eps_revision | raise | 5 | HBM 리더는 OP/EPS revision이 가격경로와 같이 움직일 때만 강하게 본다. |
| capacity_bottleneck | raise | 5 | HBM 세대 전환과 CAPA 배분은 구조적 visibility의 핵심이다. |
| hbm4_first_mover | raise | 5 | HBM4 first mover와 고객 인증은 단순 메모리 사이클보다 높은 신뢰도를 준다. |
| customer_visibility | raise | 5 | Nvidia/OpenAI급 고객 수요가 회사 매출 경로로 연결될 때 보상한다. |
| memory_price_upcycle | raise | 4 | 메모리 가격 상승은 EPS/FCF revision과 같이 있을 때 보상한다. |
| confirmed_customer_order | raise | 5 | 확인된 고객 주문은 미확정 media rumor와 분리한다. |
| order_to_revenue_conversion | raise | 4 | design win이나 장비 수주가 매출·마진으로 내려오는 경로를 보상한다. |
| price_path_alignment | raise | 5 | 증거 이후 가격경로가 따라오면 score-price alignment를 인정한다. |
| unconfirmed_media_report | lower | -5 | 미확정 고객 보도만으로 오른 구간은 4B-watch다. |
| design_win_without_revenue | lower | -5 | design win은 Stage 2 근거지만 양산·매출·마진 전 Green은 아니다. |
| policy_foundry_without_order | lower | -5 | 정책 foundry 협의는 회사 단위 order/utilization 전 event premium이다. |
| openai_or_nvidia_headline_without_company_revenue | lower | -4 | OpenAI/Nvidia headline만으로 후발주 Green을 만들면 안 된다. |
| customer_name_without_margin | lower | -3 | 고객 이름만 있고 margin이 없으면 Green 신뢰도를 막는다. |
| price_rally_before_confirmation | lower | -5 | 확인 전 가격 급등은 price-before-evidence로 본다. |
| labor_or_export_control_unpriced | lower | -5 | 노동/수출통제 리스크가 실적 차질로 이어질 수 있으면 4C-watch다. |

## Easy Examples
- `HBM4 + EPS revision + 고객 수요 + 가격경로`가 같이 있으면 강한 케이스다.
- `OpenAI headline + 후발주 급등`은 매출·마진 전 Green이 아니라 4B/event watch다.
- `design win`은 좋은 Stage 2 신호지만 tape-out, 양산, 매출, 마진 전 Green은 아니다.
- `수출통제/파업`은 실제 생산·매출 차질 전까지 hard 4C가 아니라 4C-watch다.
