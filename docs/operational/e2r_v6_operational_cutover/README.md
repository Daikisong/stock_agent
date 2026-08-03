# E2R v6 운영 인수 증거

이 디렉터리는 Phase 101~109 운영 인수 결과를 추적 가능한 작은 영수증으로 보관한다.

핵심 원칙은 원본 `output/`을 커밋하는 것이 아니라 최종 점수에 실제 사용된 fact, source, judge, anchor와 Stage 입력을 결박하는 것이다. 검증기는 영수증과 현재 코드·설정만 사용하며 `output/`, cache, `.env`, 협업 journal을 읽지 않는다.

현재 상태는 [starting_state.json](starting_state.json)과 [provider_lineage_blocker_audit.json](provider_lineage_blocker_audit.json)에 기록했다. Phase 101 canonical receipt는 Codex-only 재생성 및 독립 검증 PASS 후 `canary_receipts/2026-07-12/`에 공개한다.

검증 명령:

```bash
PYTHONPATH=src python -m e2r.cli.verify_e2r_v6_tracked_receipts \
  --receipt-root docs/operational/e2r_v6_operational_cutover/canary_receipts/2026-07-12 \
  --offline true
```

쉬운 예: 삼성전자 점수가 `66.8`이라는 숫자만 보관하지 않는다. 7개 component 합이 실제로 `66.8`인지, 세 judge의 제안으로 각 component 점수가 다시 나오는지, 사용된 fact가 source와 짧은 검수 인용 및 hash로 이어지는지, 그 점수 벡터로 Stage `2`가 다시 나오는지를 한 번에 확인한다.
