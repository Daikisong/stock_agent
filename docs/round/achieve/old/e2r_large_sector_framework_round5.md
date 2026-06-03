# Round 5 Large-Sector Framework

Round 5 adds a large-sector layer before production scoring changes.

The goal is:

```text
company -> large sector -> E2R archetype -> peer normalization -> stage evidence
```

Easy example:

```text
전력기기
-> large sector: 산업재/수주
-> archetype: CONTRACT_BACKLOG_INDUSTRIAL
-> key evidence: contract quality, backlog, lead time, OPM, EPS revision

해운
-> large sector: 사이클/스프레드
-> archetype: SHIPPING_FREIGHT_CYCLE
-> key evidence: freight rate, contract vs spot, vessel supply
-> Green is restricted because cycle normalization can be fast
```

## Ten Large Sectors

| Large sector | Korean name | Green posture |
|---|---|---|
| `INDUSTRIAL_ORDERS` | 산업재/수주 | High, with contract/margin/legal checks |
| `EXPORT_CONSUMER` | 수출 소비재 | High, with repeat demand/channel/OPM checks |
| `SEMICONDUCTOR_AI_INFRA` | 반도체/AI 인프라 | High, with HBM/order/CAPEX checks |
| `CYCLICAL_SPREAD` | 사이클/스프레드 | Low, cycle cap required |
| `FINANCIAL_CAPITAL_ALLOCATION` | 금융/자본배분 | Medium, ROE/PBR/return execution required |
| `BIOTECH_HEALTHCARE` | 바이오/헬스케어 | Low, pre-revenue Green-blocked |
| `PLATFORM_IP_SERVICES` | 플랫폼/IP/서비스 | Medium, monetization/OPM/FCF required |
| `DOMESTIC_REOPENING` | 내수/리오프닝 | Low, rebound and structural improvement separated |
| `REAL_ESTATE_CREDIT_REGULATED` | 부동산/신용/규제자산 | Restricted |
| `THEME_EVENT_GUARDRAIL` | 테마/이벤트 | Restricted |

## New Or Confirmed Extension Archetypes

- `AI_DATA_CENTER_INFRASTRUCTURE`
- `NUCLEAR_SMR_GRID_POLICY`
- `TRAVEL_LEISURE_REOPENING`
- `EDUCATION_SPECIALTY_SERVICES`
- `RARE_METALS_STRATEGIC_MATERIALS`
- `CDMO_HEALTHCARE_CONTRACT`
- `VALUE_UP_SHAREHOLDER_RETURN`

## Green Policy

Round 5 keeps Green strict.

- Platform MAU alone is not enough.
- Robotics strategic investment is Stage 1/2 unless revenue conversion exists.
- Construction order news cannot override PF and cash-flow risk.
- Utilities need tariff, debt, and regulatory regime improvement.
- Pre-revenue biotech is Green-blocked unless commercialization and cash-flow conversion are visible.

## Guardrails

- Do not use large-sector labels as candidate-generation input.
- Do not hardcode stock names into scoring.
- Do not lower Stage 3-Green thresholds from this framework.
- Use the framework to decide which cases, price paths, and counterexamples must be filled next.

## Round 6 Overlay

Round 6 adds a cross-sector correction layer:

```text
Round 5 large sector -> Round 6 overlay -> archetype evidence checklist
```

Example:

```text
AI/전력/인프라
-> transformers, grid, cooling, PCB, HBM, and data-center CAPEX can move together
-> score validation must check actual orders, CAPEX visibility, and EPS revision
```

See `docs/e2r_missing_sector_correction_round6.md` for the overlay matrix.
