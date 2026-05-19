# Round-196 R5 Loop-7 Green Gate Review

## Green Required Evidence

- `repeat_purchase_evidence`
- `overseas_sales_mix_growth`
- `channel_sell_through_confirmed`
- `opm_improvement`
- `inventory_and_receivables_stable`
- `asp_or_product_mix_improvement`
- `single_product_dependence_not_excessive`
- `tariff_regulation_recall_passed`
- `price_path_after_evidence`

## Green Forbidden Patterns

- `tiktok_viral_only`
- `retail_talks_only`
- `ipo_first_month_rally`
- `influencer_endorsement_only`
- `mna_event_only`
- `private_affiliate_value_only`
- `china_decline_without_offset`

## Shadow Score Adjustments

| axis | direction | points | reason |
| --- | --- | ---: | --- |
| `repeat_demand` | raise | 4 | 유행이 아니라 반복구매가 확인될 때 R5 visibility가 올라간다. |
| `channel_sell_through` | raise | 4 | 입점이 아니라 매장 회전과 반복 발주가 확인되어야 한다. |
| `overseas_sales_mix` | raise | 3 | 미국/유럽/글로벌 매출 비중 증가는 내수 프레임 제거 근거다. |
| `us_retail_channel_confirmed` | raise | 3 | Costco/Ulta/Target/Sephora/Walmart 등 실제 채널 확인은 Stage 2 이상 근거다. |
| `opm_improvement` | raise | 4 | 수출 성장이나 브랜드 열기가 OPM으로 내려와야 EPS/FCF 체급 변화다. |
| `inventory_quality` | raise | 3 | 재고가 안정적이면 channel stuffing 위험이 낮아진다. |
| `receivables_quality` | raise | 3 | 매출채권이 안정적이면 매출 성장의 현금화 품질이 올라간다. |
| `brand_portfolio_breadth` | raise | 2 | 단일 제품보다 포트폴리오가 넓으면 fad 위험이 낮다. |
| `odm_customer_diversification` | raise | 3 | ODM은 고객 다변화와 주문 visibility가 핵심이다. |
| `localized_manufacturing` | raise | 2 | 현지 생산은 관세/물류 리스크를 줄이는 보조 근거다. |
| `viral_product_only` | lower | -5 | 틱톡/viral만으로는 반복수요와 FCF를 확인할 수 없다. |
| `brand_heat_only` | lower | -4 | 브랜드 열기만 있고 실적 품질이 없으면 Green 근거가 아니다. |
| `ipo_first_month_rally` | lower | -4 | 상장 직후 주가 급등은 가격경로 경고이지 구조 증거가 아니다. |
| `retail_talks_without_sell_through` | lower | -3 | 입점 논의는 Stage 2 attention이고 sell-through 전에는 제한한다. |
| `influencer_endorsement_only` | lower | -3 | 인플루언서 endorsement만으로 반복구매를 만들지 않는다. |
| `single_sku_dependence` | lower | -4 | 단일 SKU 의존도는 fad normalization과 4C 위험을 키운다. |
| `china_exposure_without_offset` | lower | -3 | 중국 둔화를 미국/유럽 성장으로 상쇄하지 못하면 제한한다. |
| `holdco_or_private_link_cap` | lower | -3 | 비상장 자회사 가치와 상장 모회사 수익률은 분리해야 한다. |
| `mna_event_premium` | lower | -4 | M&A/ROFR/법적 분쟁은 본업 브랜드 리레이팅 증거가 아니다. |
| `tariff_margin_uncertainty` | lower | -2 | 관세 부담을 판가에 전가하지 못하면 OPM 품질이 낮아진다. |
| `inventory_or_receivables_build` | lower | -4 | 재고/채권 증가는 channel stuffing과 현금화 리스크다. |

## What Not To Change

- Do not apply these weights to production scoring yet.
- Do not use Round196 cases as candidate-generation input.
- Do not lower Stage 3-Green thresholds to force promotion.
- Do not invent sell-through, reorder, OPM, inventory, receivables, stage prices, or MFE/MAE.
