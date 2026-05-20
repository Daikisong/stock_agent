# Round 284 R2 Green Gate Review

Do not apply these weights to production scoring yet.

R2 Stage 3-Green is not `AI`, `HBM`, `Nvidia`, `OpenAI`, `Apple AI`, `OLED`, or `AI chip startup` as a label. It requires allocation, delivery, ASP/mix, PO-to-revenue, sell-through, utilization, component margin and labor continuity.

## Required Fields

- actual_hbm_allocation_confirmed
- customer_delivery_and_calloff_confirmed
- HBM_ASP_mix_margin_confirmed
- capacity_utilization_confirmed
- equipment_PO_to_revenue_confirmed
- customer_diversification_confirmed
- device_sellthrough_confirmed
- component_mix_margin_confirmed
- OLED_utilization_confirmed
- labor_supply_continuity_confirmed
- price_path_after_evidence

## Forbidden Patterns

- AI_keyword_only
- HBM_theme_without_customer_delivery
- LOI_or_MOU_without_binding_contract
- rumored_customer_PO
- on_device_AI_expectation_only
- capacity_capex_without_utilization
- unlisted_AI_chip_readthrough
- consumer_OEM_exposed_to_memory_cost
- labor_disruption_risk

## Shadow Score Adjustments

| axis | direction | points | reason |
|---|---|---:|---|
| actual_hbm_allocation | raise | 5 | HBM은 고객 allocation과 실제 납품이 확인될 때 강하다. |
| customer_delivery_and_calloff | raise | 5 | 고객 수요는 call-off와 delivery로 닫혀야 한다. |
| HBM_ASP_mix_margin | raise | 5 | HBM ASP와 mix margin이 OP로 내려오는지 확인한다. |
| capacity_utilization | raise | 5 | 증설과 capex는 utilization이 있어야 FCF로 연결된다. |
| equipment_PO_to_revenue | raise | 5 | 장비주는 PO, 납품, revenue recognition이 핵심이다. |
| customer_diversification | raise | 4 | 장비·부품주는 단일 고객 루머보다 고객 다변화가 중요하다. |
| device_sellthrough | raise | 5 | on-device AI는 실제 기기 판매와 교체수요가 필요하다. |
| component_mix_margin | raise | 5 | 부품 탑재량과 mix가 margin으로 이어져야 한다. |
| OLED_utilization | raise | 5 | OLED capex는 utilization과 현금흐름으로 검증한다. |
| labor_supply_continuity | raise | 5 | 파업·셧다운은 memory 공급 안정성 hard gate다. |
| AI_keyword_only | lower | -5 | AI 단어만으로 매출·마진을 만들지 않는다. |
| HBM_theme_without_customer_delivery | lower | -5 | HBM 테마는 고객 납품 전에는 제한한다. |
| LOI_or_MOU_without_binding_contract | lower | -5 | LOI/MOU는 binding take-or-pay가 아니다. |
| rumored_customer_PO | lower | -5 | 고객 루머는 PO/revenue가 아니다. |
| on_device_AI_expectation_only | lower | -5 | Apple AI 기대는 sell-through와 부품 margin 전에는 부족하다. |
| capacity_capex_without_utilization | lower | -5 | capex만 있고 utilization이 없으면 현금소모일 수 있다. |
| unlisted_AI_chip_readthrough | lower | -5 | 비상장 AI chip 성과를 상장사 EPS로 바로 연결하지 않는다. |
| consumer_OEM_exposed_to_memory_cost | lower | -4 | 메모리 shortage는 OEM에는 부품비 부담일 수 있다. |
| labor_disruption_risk | lower | -5 | 파업·공급차질은 HBM catch-up narrative를 막는다. |

## Easy Examples
- `HBM sold out` becomes stronger when OP, ASP/mix and shipment evidence appear together.
- `OpenAI LOI` is a demand signal, but Green waits for binding call-off, margin and shipment schedule.
- `Apple Intelligence` helps a component thesis only if device sell-through and component margin confirm.
