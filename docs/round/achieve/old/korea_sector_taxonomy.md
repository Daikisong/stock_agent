# Korea Sector Taxonomy

Checkpoint 28A adds a taxonomy layer before changing sector-aware scores.

The taxonomy answers a simple question:

```text
이 회사는 어떤 섹터이고, 어떤 E2R 사업모델 유형에 가까운가?
```

Example:

```text
HD현대일렉트릭
-> 전력기기/전선
-> CONTRACT_BACKLOG_INDUSTRIAL
-> 계약금액, 계약기간, 수주잔고, 리드타임이 핵심

삼양식품
-> 식품수출
-> EXPORT_RECURRING_CONSUMER
-> 수출비중, 해외 채널, 반복 소비, OPM 레버리지가 핵심
```

This file is metadata for analysis and future score-weight design. It is not a
candidate-generation answer key, and it does not change StageClassifier
thresholds.

## Data Sources

The builder is designed for the full Korea market, but fixture mode also works.

Source priority:

- KRX listed universe / issue base info
- data.go.kr KRX listed item info
- data.go.kr company basic info
- OpenDART company metadata
- local `data/historical_official/universe/universe.csv`
- manual overrides only as a fallback

## Output Fields

`data/sector_taxonomy/korea_sector_map.csv` contains:

- `symbol`
- `company_name`
- `market`
- `exchange`
- `listed_date`
- `sector_raw`
- `industry_raw`
- `sector_custom`
- `sector_source`
- `sector_confidence`
- `primary_archetype`
- `secondary_archetypes`
- `business_keywords`
- `product_keywords`
- `mapping_reason`

## Archetype Examples

- `CONTRACT_BACKLOG_INDUSTRIAL`: 전력기기, 전선, 변압기
- `DEFENSE_GOVERNMENT_BACKLOG`: 방산, 정부 고객, 수출 계약
- `EXPORT_RECURRING_CONSUMER`: 식품 수출, 반복 소비, 해외 채널
- `K_BEAUTY_EXPORT_DISTRIBUTION`: K-뷰티, 해외 플랫폼, 반복 주문
- `MEMORY_HBM_CAPACITY`: HBM, 메모리 가격, 공급 규율
- `ONE_OFF_EVENT_DEMAND`: 팬데믹 진단키트 같은 일회성 수요
- `THEME_VALUATION_OVERHEAT`: 근거보다 가격/테마가 앞선 과열

## Round 5 Large-Sector Layer

Round 5 adds a broad-sector layer above archetypes:

```text
대섹터 -> E2R Archetype -> Stage evidence -> peer normalization
```

Example:

```text
산업재/수주
-> CONTRACT_BACKLOG_INDUSTRIAL, DEFENSE_GOVERNMENT_BACKLOG, SHIPBUILDING_OFFSHORE_BACKLOG
-> contract quality, backlog, delivery schedule, margin path

플랫폼/IP/서비스
-> PLATFORM_SOFTWARE_INTERNET, GAME_CONTENT_IP, EDUCATION_SPECIALTY_SERVICES
-> ARPU, repeat monetization, OPM/FCF, regulation/IP risk
```

The report-only matrix can be rebuilt with:

```bash
PYTHONPATH=src python -m e2r.cli.build_round5_large_sector_report \
  --cases data/e2r_case_library/cases_v02.jsonl \
  --output-directory output/e2r_round5_large_sector_framework
```

This layer still does not change StageClassifier thresholds.

## Build Command

```bash
PYTHONPATH=src python -m e2r.cli.build_korea_sector_taxonomy \
  --as-of-date 2026-05-14 \
  --market KR \
  --output data/sector_taxonomy/korea_sector_map.csv
```

The summary is written to:

```text
output/sector_taxonomy/sector_taxonomy_summary.md
```

## Guardrails

- Do not use benchmark labels as taxonomy input.
- Do not hardcode individual winners into scoring rules.
- Do not apply final score weights until case coverage is reviewed.
- If a sector is unmapped, keep it explicit instead of inventing detail.
