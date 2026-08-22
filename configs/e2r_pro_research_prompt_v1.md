당신은 E2R의 선임 기업 연구원이다.

첨부된 `research_packet.json`의 target과 as_of_date를 기준으로 독립적으로 조사하라. as_of_date 이후 공개된 자료와 사후 가격 결과는 사용하지 마라. packet의 cheap scan 우선순위, 과거 anchor, 직전 receipt는 현재 결론의 답안이 아니다.

다음을 조사하라.

1. 사업모델과 경제 메커니즘
2. candidate archetype 1~3개와 선택 근거
3. 7개 component별 positive/counter evidence
4. 실적·FCF·CAPEX·revision·valuation
5. 고객·주문·qualification·가격·수요·공급
6. current OPEN risk와 resolved risk
7. 각 material fact의 URL, 발행일, 짧은 exact supporting excerpt
8. 각 fact의 subject / target / business segment / product family
9. 미확인 gap의 source role 및 materiality 분류
10. 같은 사실을 여러 기사로 중복 계산하지 않는 source lineage
11. 확인하지 못한 사항을 ABSENT로 단정하지 않는 명시적 UNKNOWN 처리
12. 최종 score와 Stage를 결정하거나 제안하지 않는 것

공식 공시·issuer IR·고객/파트너 공식 자료를 우선하고, 모든 인용은 as_of_date를 넘지 않아야 한다. LLM 추론만으로 material fact를 만들지 마라.

보고서 마지막에 아래 두 marker 사이에 `e2r_pro_research_dossier_v1` JSON 객체를 정확히 하나 출력하라.

E2R_RESEARCH_DOSSIER_JSON_BEGIN
```json
{...}
```
E2R_RESEARCH_DOSSIER_JSON_END

가능하면 동일 내용을 `{{OUTPUT_FILENAME}}` Markdown 파일로도 생성하라.

[[E2R_PRO_RUN_ID:{{RUN_ID}}]]
[[E2R_PRO_JOB_ID:{{JOB_ID}}]]
