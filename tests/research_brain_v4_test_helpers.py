import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.research_brain.schemas import SourceTask, SourceTaskType
from e2r.research_brain.v2_memory_cards import build_memory_cards_from_v1_matrix
from e2r.research_brain.v2_schemas import ArchetypeMemoryCard, CandidateEventV2, LLMPlannerOutputV2
from e2r.research_brain.v4_planner_runtime import FixturePlannerProviderV4, ResearchBrainPlannerProviderV4
from e2r.research_brain.v4_schemas import PlannerProviderModeV4


def load_v4_matrix() -> Mapping[str, Any]:
    return json.loads(Path("docs/operational/research_brain_v1_archetype_matrix.json").read_text(encoding="utf-8"))


def load_v4_cards() -> tuple[ArchetypeMemoryCard, ...]:
    return build_memory_cards_from_v1_matrix(load_v4_matrix())


def sample_v4_event(symbol: str = "005930", company_name: str = "삼성전자") -> CandidateEventV2:
    return CandidateEventV2(
        candidate_event_id=f"CEV4-TEST-{symbol}",
        symbol=symbol,
        company_name=company_name,
        event_date="2026-06-25",
        detected_at="2026-06-29",
        source_family="CompanyGuide",
        source_id=f"data/cache/company_guide/2026-06-28/{symbol}_recent_reports.json",
        event_type="report_radar",
        raw_reason_codes=("HBM", "MEMORY", "REVISION"),
        event_title="HBM 메모리 가격과 실적 전망",
        event_summary="HBM 고객 수요, 메모리 가격 상승, 추정EPS 상향을 확인해야 하는 리포트 이벤트",
        issuer_directness="DIRECT",
        research_brain_eligible=True,
    )


def c06_source_task(primitive: str = "medium_term_revision_visibility") -> SourceTask:
    event = sample_v4_event()
    return SourceTask(
        task_id=f"RSTASKV4-TEST-{primitive}",
        candidate_event_id=event.candidate_event_id,
        symbol=event.symbol,
        company_name=event.company_name,
        archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        primitive_gap=primitive,
        task_type=SourceTaskType.POSITIVE_VERIFY.value,
        preferred_source_classes=("CompanyGuide", "IR"),
        fallback_source_classes=("IssuerOfficial",),
        forbidden_source_classes=("unbounded_general_search",),
        date_window={"end": event.event_date, "lookback_days": 540},
        max_queries=1,
        max_candidates=10,
        max_fetches=3,
        stop_condition={"accepted_claim_count": 1},
        general_search_allowed=False,
        reason_from_memory="v4 test source-backed primitive",
    )


class RealStubPlannerProviderV4(ResearchBrainPlannerProviderV4):
    provider_name = "real_stub_planner_v4"
    provider_mode = PlannerProviderModeV4.REAL.value
    real_provider = True
    fake_provider = False
    model = "unit-test-real-stub"
    endpoint = "unit-test"

    def plan_many(
        self,
        *,
        events: Sequence[CandidateEventV2],
        memory_cards: Sequence[ArchetypeMemoryCard],
        existing_evidence_by_event_id: Mapping[str, Mapping[str, Any]] | None = None,
    ) -> Mapping[str, LLMPlannerOutputV2]:
        return FixturePlannerProviderV4().plan_many(
            events=events,
            memory_cards=memory_cards,
            existing_evidence_by_event_id=existing_evidence_by_event_id,
        )
