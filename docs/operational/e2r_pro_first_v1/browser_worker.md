# Browser Worker

기본 연결은 `CDP_ATTACH`이며 `http://127.0.0.1:9222`의 전용 Chrome에 붙는다. 기본 Chrome을 강제로 종료하거나 profile을 복사하지 않는다.

준비 단계는 다음까지만 한다.

```text
로그인 상태 확인
→ Deep Research UI 확인
→ packet 업로드
→ prompt 입력
→ send button 활성 확인
→ submit_count=0
```

실제 전송은 `ExactlyOnceSubmitCoordinator`만 호출할 수 있다. adapter도 장부에서 생성된 `ConsumedApprovalProof`와 packet/prompt/browser binding이 모두 맞아야 클릭한다.

완료 후 현재 run의 새 `.md`만 찾고, preview가 열리면 visible/enabled 실제 다운로드 버튼을 사용한다. MD가 없을 때는 현재 assistant turn의 직접 보고서만 fallback으로 쓴다. 예전 대화의 파일 버튼은 pre-submit snapshot과 비교해 제외한다.

금지: 로그인 자동화, private ChatGPT API, cookie export, Tampermonkey runtime 의존, 자동 재전송.
