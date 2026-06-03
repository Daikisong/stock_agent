# Sector Structural Visibility

Checkpoint 28 adds sector-aware structural visibility scoring.

The problem was simple: the old Stage 3 gate treated almost every rerating like a transformer or defense backlog case. That works for power equipment, but it under-scores cases where the real visibility comes from exports, channels, repeat demand, memory pricing, HBM bottlenecks, or consensus revisions.

## Core Rule

`contract_quality` is still scored, but Stage 3-Green now checks `structural_visibility_quality`.

Example:

- HD현대일렉트릭: structural visibility should mostly come from contract quality, backlog, lead time, CAPA, ASP, and supply shortage.
- 삼양식품: structural visibility can come from export ratio, overseas channel expansion, repeat consumer demand, OPM expansion, FY1/FY2 EPS growth, and ASP/pricing power.
- 삼성전자/SK하이닉스 memory: structural visibility can come from HBM demand, memory price increases, supply discipline, HBM capacity bottlenecks, and medium-term revisions.

Green is not easier. It is just less sector-wrong.

## Profiles

The implemented profiles are:

- `POWER_EQUIPMENT`
- `DEFENSE`
- `K_FOOD_EXPORT`
- `K_BEAUTY_EXPORT`
- `MEMORY_HBM`
- `CYCLICAL_SHIPPING`
- `BATTERY_OVERHEAT`
- `GENERIC`

Profile inference uses available company/source context, report text, disclosure text, and parsed fields. It does not read benchmark labels.

## Scoring Fields

New diagnostics:

- `sector_profile_id`
- `structural_visibility_quality`
- `sector_visibility_score`
- `sector_bottleneck_score`
- `recurring_demand_visibility`
- `export_channel_visibility`
- `medium_term_revision_visibility`
- `domain_specific_evidence_score`
- `contract_required_for_green`

Evidence-family diagnostics were also added:

- `evidence_family_price`
- `evidence_family_financial_actual`
- `evidence_family_disclosure`
- `evidence_family_research_report`
- `evidence_family_consensus`
- `evidence_family_consensus_revision`
- `evidence_family_news`
- `cross_evidence_family_count`

## Qualitative Evidence

Parsers now emit bounded qualitative fields only when explicitly mentioned.

Examples:

- `리드타임 장기화` -> `lead_time_extended=True`
- `ASP 상승` or `판가 상승` -> `pricing_power_mentioned=True`
- `수출 비중 확대` -> `export_channel_expansion=True`
- `해외 채널 확장` -> `overseas_channel_expansion=True`
- `불닭 수출` with channel/repeat demand text -> `recurring_consumer_demand=True`
- `HBM 수요 증가` -> `hbm_demand_mentioned=True`
- `메모리 가격 상승` -> `memory_price_increase_mentioned=True`
- `공급조절` -> `supply_discipline_mentioned=True`

These fields never fabricate numeric values. They provide bounded score credit and cannot create Stage 3-Green by themselves without EPS/FCF, revision support, visibility, valuation, and Red Team safety.

## Promotion Band

Checkpoint 28 also adds `promotion_band`, a report-facing diagnostic label.

It does not replace the deterministic stage.

Example:

- deterministic stage: `Stage 2`
- promotion band: `Stage 2-High`

This means the candidate is stronger than a normal Stage 2 candidate, but Green gates are still incomplete.

Promotion bands:

- `Stage 1`
- `Stage 2`
- `Stage 2-High`
- `Stage 3-Watch`
- `Stage 3-Yellow`
- `Stage 3-Green`

## Stage 3 Discipline

Stage 3-Green still requires:

- high total score
- EPS/FCF explosion
- earnings visibility
- bottleneck/pricing evidence
- market mispricing
- valuation rerating
- meaningful revision score
- structural visibility quality
- low one-off risk
- low Red Team risk

For power equipment and defense, contract quality still matters. For K-food, K-beauty, and memory/HBM, structural visibility can be proven through sector-appropriate evidence instead of generic supply contracts.
