# Round-6 Missing-Sector Correction Framework

Source round: `docs/round/round_06.md`

This is calibration material. It does not change production scoring.

## Overlay Sectors

| overlay | Korean name | posture | archetypes |
|---|---|---|---:|
| AI_POWER_INFRA | AI/전력/인프라 | STRUCTURAL_GREEN_POSSIBLE | 4 |
| NATIONAL_STRATEGY_POLICY | 정책/국가전략 | WATCH_YELLOW_FIRST | 3 |
| CAPITAL_ALLOCATION_VALUEUP | 자본배분/밸류업 | WATCH_YELLOW_FIRST | 4 |
| CYCLE_MACRO_CREDIT | 경기/사이클 | CYCLE_OR_EVENT_CAPPED | 6 |
| THEME_TECH_EXPECTATION | 테마/기술 기대 | REDTEAM_FIRST | 8 |
| RECURRING_EXPORT_BRAND | 반복수출/브랜드 | STRUCTURAL_GREEN_POSSIBLE | 4 |

## Interpretation
- Overlays are cross-sector corrections. They do not replace Round-5 large sectors.
- Example: AI data-center infrastructure can touch transformers, PCB, cooling, and memory/HBM.
- Example: construction and utilities can look cheap, but PF, debt, tariff, and cash-flow risk dominate.

## Guardrails
- Do not use overlay labels as candidate-generation input.
- Do not lower Stage 3-Green thresholds from this report.
- Fill price paths before applying any score-weight changes.
