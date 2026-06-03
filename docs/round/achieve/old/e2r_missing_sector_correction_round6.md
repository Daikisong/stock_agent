# Round 6 Missing-Sector Correction

Round 6 adds a cross-sector overlay above the Round 5 large-sector framework.

The reason is simple:

```text
AI data-center infrastructure is not just one sector.
It can touch transformers, grid, cooling, PCB, servers, HBM, and IDC.
```

So Round 6 creates six overlays:

| Overlay | Korean name | Posture |
|---|---|---|
| `AI_POWER_INFRA` | AI/전력/인프라 | Structural Green possible |
| `NATIONAL_STRATEGY_POLICY` | 정책/국가전략 | Watch/Yellow first |
| `CAPITAL_ALLOCATION_VALUEUP` | 자본배분/밸류업 | Watch/Yellow first |
| `CYCLE_MACRO_CREDIT` | 경기/사이클 | Cycle/event capped |
| `THEME_TECH_EXPECTATION` | 테마/기술 기대 | RedTeam first |
| `RECURRING_EXPORT_BRAND` | 반복수출/브랜드 | Structural Green possible |

## Easy Examples

AI/전력/인프라:

```text
데이터센터 전력 부족 뉴스
-> 전력기기/전선/냉각/PCB 여러 업종이 같이 움직일 수 있음
-> 실제 수주, CAPEX, EPS revision이 없으면 Theme Overheat로 내려야 함
```

경기/사이클:

```text
HMM 2020~2021
-> 운임 급등과 EPS 폭발
-> 하지만 운임 정상화 후 EPS가 꺾이면 structural Green이 아니라 cycle_boom_bust
```

테마/기술 기대:

```text
로봇 대기업 투자 뉴스
-> Stage 1/2 신호는 될 수 있음
-> 실제 매출, 수주, OP 전환 전에는 Green 금지
```

## Price-Path Contract

Round 6 requires forward validation fields:

- `mfe_30d`
- `mfe_90d`
- `mfe_180d`
- `mfe_1y`
- `mfe_2y`
- `mae_30d`
- `mae_90d`
- `mae_180d`
- `mae_1y`
- `mae_2y`
- `time_to_50pct`
- `time_to_100pct`
- `drawdown_after_peak`

## Guardrails

- Do not use overlay labels as candidate-generation input.
- Do not lower Stage 3-Green thresholds.
- Do not treat price-only movement as EPS/FCF evidence.
- Fill price paths before applying score-weight changes.
