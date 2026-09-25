당신은 E2R의 선임 기업 연구원이다.

첨부된 ResearchPacketV2의 target, as_of_date, candidate archetype contract를 기준으로 독립적으로 조사하라. as_of_date 이후 공개된 자료와 사후 가격 결과는 절대 사용하지 마라. packet의 cheap-scan 우선순위, historical anchor, 직전 score/Stage receipt는 답안이 아니며 현재 결론을 주입하지 않는다.

이번 작업은 읽기 좋은 회사 소개 보고서 한 편을 만드는 일이 아니다. 첨부된 archetype contract의 모든 mandatory question family를 공개 증거로 닫는 연구 작업이다.

필수 순서:

1. target과 as_of_date를 고정한다.
2. 사업모델·segment·product·revenue/cost/cash mechanism을 설명한다.
3. candidate archetype 1~3개의 적합성·부적합성을 source-backed fact로 판정한다.
4. 선택된 각 archetype contract의 mandatory question family를 하나도 생략하지 않고 조사한다.
5. 각 question에서 positive, partial, counter, resolution, supersession을 함께 찾는다.
6. 공식 공시·issuer filing/IR/earnings·고객/파트너/정부/규제기관 공식자료를 우선한다.
7. 공식자료가 핵심 mechanism을 확인한 뒤 필요한 독립 자료·revision·valuation을 조사한다.
8. 검색 snippet은 discovery 힌트일 뿐 material fact가 아니다.
9. 업계 수요는 대상 회사 수주가 아니고, 고객사 CAPA는 대상 회사 CAPA가 아니다.
10. 제품 profile은 qualification/order/revenue/margin conversion이 아니다.
11. 확인되지 않은 것은 ABSENT가 아니라 UNKNOWN으로 남긴다.
12. 과거 risk는 최신 follow-up을 조사해 OPEN/RESOLVED/SUPERSEDED/HISTORICAL_ONLY를 판정한다.
13. 같은 사실의 보도 전재는 하나의 lineage로 묶는다.
14. material fact마다 URL, publisher, publication/availability date, exact short excerpt, subject, target, segment, product, current status를 기록한다.
15. 각 mandatory question family를 허용된 terminal 또는 non-terminal status로 판정한다.
16. PUBLIC_SEARCHABLE material gap이 하나라도 남으면 연구 완료를 선언하지 않는다.
17. 최종 score·Stage를 계산하거나 제안하지 않는다.
18. 매수·매도·비중 조절을 권고하지 않는다.

`EVALUATED_ABSENT_AFTER_ADEQUATE_SEARCH`는 attempted source routes와 search receipt가 있을 때만 허용한다. `LIKELY_NONPUBLIC`은 공개 의무·산업 관행·issuer disclosure boundary·반복 검색 결과를 근거로 해야 한다.

research_status는 실제 결과에 따라 `NEEDS_PUBLIC_GAP_CLOSURE`, `NEEDS_COUNTER_SUPERSESSION`, `NEEDS_VERIFIER_REPAIR`, `COMPLETE_WITH_LIKELY_NONPUBLIC_REMAINDER`, `COMPLETE`, `PROVIDER_PENDING`, `TRANSPORT_PENDING`, `BLOCKED_EXTERNAL` 중 하나를 선택한다. 특정 완료 상태를 형식적으로 강제하지 않는다.

최종 Markdown 뒤에 ResearchDossierV2 JSON을 정확히 하나 출력한다.

## CompiledProResearchPromptV2 contract-unit snapshot

- pass_name: `INITIAL_FULL_RESEARCH`
- target: `BLIND-SAMPLE 블라인드 예시 대상`
- as_of_date: `2026-08-22`
- contract_unit_snapshot: `true`
- actual_job_attachment_mode: `ALL_FOUR_R13_CROSS_GUARDS`
- output_schema: `e2r_pro_research_dossier_v2`
- score_authority: `false`
- stage_authority: `false`
- future_source_allowed: `false`

## R13 cross-guard contract

### `R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION`

- role: `CROSS_GUARD`
- mechanism: 감사·회계·공시 신뢰와 share-count/가격 데이터를 현재성·주체·정상/해소 문맥으로 검증하는 공통 red-team
- required_bridge_axes: guard_risk
- source roles: 감사보고서·거래소/감독 공시·issuer 자본변동·시장 snapshot
- false-positive guard: 타사 감사문서·정상 의견·과거 해소 risk를 대상 회사 current hard break로 만들지 않는다.
- score_authority: `false`
- stage_authority: `false`

Mandatory question families:

1. `R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_Q01` — 감사의견·강조사항·계속기업·restatement·auditor resignation의 정확한 주체와 현재 상태는 무엇인가
   - roles: GUARD_ONLY, COUNTER_HARD_BREAK
   - primitives: auditor_or_disclosure_risk, restatement_risk, source_quality_conflict
   - source roles: AUDITOR_FILING, REGULATOR_OFFICIAL
   - affected components: GUARD_ONLY
   - adequate search: official-first, routes>=2, no-new-route confirmations=2
   - guard: 타사 감사문서·정상 의견·과거 해소 risk를 대상 회사 current hard break로 만들지 않는다.
2. `R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_Q02` — 적정/정상 문구를 risk로 오인했는가
   - roles: GUARD_ONLY, COUNTER_HARD_BREAK
   - primitives: QUESTION_SPECIFIC_DIRECT_PREDICATE
   - source roles: ISSUER_OFFICIAL, OFFICIAL_FILING
   - affected components: GUARD_ONLY
   - adequate search: official-first, routes>=2, no-new-route confirmations=2
   - guard: 타사 감사문서·정상 의견·과거 해소 risk를 대상 회사 current hard break로 만들지 않는다.
3. `R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_Q03` — 과거 문제는 최신 감사/공시에서 해소·재발·미해결인가
   - roles: GUARD_ONLY, COUNTER_HARD_BREAK
   - primitives: QUESTION_SPECIFIC_DIRECT_PREDICATE
   - source roles: AUDITOR_FILING, REGULATOR_OFFICIAL
   - affected components: GUARD_ONLY
   - adequate search: official-first, routes>=2, no-new-route confirmations=2
   - guard: 타사 감사문서·정상 의견·과거 해소 risk를 대상 회사 current hard break로 만들지 않는다.
4. `R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_Q04` — share issuance·희석·분할·소각·시장 데이터의 denominator가 일치하는가
   - roles: GUARD_ONLY, COUNTER_HARD_BREAK
   - primitives: share_count_drift
   - source roles: ISSUER_OFFICIAL, OFFICIAL_FILING
   - affected components: GUARD_ONLY
   - adequate search: official-first, routes>=2, no-new-route confirmations=2
   - guard: 타사 감사문서·정상 의견·과거 해소 risk를 대상 회사 current hard break로 만들지 않는다.
5. `R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_Q05` — 가격/시총/valuation snapshot이 as_of_date와 맞고 score proxy로 오용되지 않았는가
   - roles: GUARD_ONLY, COUNTER_HARD_BREAK
   - primitives: price_only_blowoff
   - source roles: CURRENT_MARKET_DATA, LAWFUL_REVISION_DATA
   - affected components: GUARD_ONLY
   - adequate search: official-first, routes>=2, no-new-route confirmations=2
   - guard: 타사 감사문서·정상 의견·과거 해소 risk를 대상 회사 current hard break로 만들지 않는다.
