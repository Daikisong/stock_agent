import json
import shutil
import tempfile
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.research_brain.schemas import SourceTask, SourceTaskType
from e2r.research_brain.v2_memory_cards import build_memory_cards_from_v1_matrix
from e2r.research_brain.v2_schemas import ArchetypeMemoryCard, CandidateEventV2, LLMPlannerOutputV2
from e2r.research_brain.v4_planner_runtime import FixturePlannerProviderV4, ResearchBrainPlannerProviderV4
from e2r.research_brain.v4_schemas import PlannerProviderModeV4


_REPO_ROOT = Path(__file__).resolve().parents[1]
_FIXTURE_TEMP_DIR: tempfile.TemporaryDirectory[str] | None = None


def load_v4_matrix() -> Mapping[str, Any]:
    return json.loads(Path("docs/operational/research_brain_v1_archetype_matrix.json").read_text(encoding="utf-8"))


def load_v4_cards() -> tuple[ArchetypeMemoryCard, ...]:
    return build_memory_cards_from_v1_matrix(load_v4_matrix())


def sample_v4_event(symbol: str = "005930", company_name: str = "삼성전자") -> CandidateEventV2:
    fixture_root = research_brain_v4_fixture_root()
    return CandidateEventV2(
        candidate_event_id=f"CEV4-TEST-{symbol}",
        symbol=symbol,
        company_name=company_name,
        event_date="2026-06-25",
        detected_at="2026-06-29",
        source_family="CompanyGuide",
        source_id=str(fixture_root / f"data/cache/company_guide/2026-06-28/{symbol}_recent_reports.json"),
        event_type="report_radar",
        raw_reason_codes=("HBM", "MEMORY", "REVISION"),
        event_title="HBM 메모리 가격과 실적 전망",
        event_summary="HBM 고객 수요, 메모리 가격 상승, 추정EPS 상향을 확인해야 하는 리포트 이벤트",
        issuer_directness="DIRECT",
        research_brain_eligible=True,
    )


def research_brain_v4_fixture_root() -> Path:
    global _FIXTURE_TEMP_DIR
    if _FIXTURE_TEMP_DIR is None:
        _FIXTURE_TEMP_DIR = tempfile.TemporaryDirectory()
        root = Path(_FIXTURE_TEMP_DIR.name)
        shutil.copytree(_REPO_ROOT / "fixtures" / "historical", root / "fixtures" / "historical")
        shutil.copytree(_REPO_ROOT / "data" / "raw", root / "data" / "raw")
        _write_companyguide_fixture(root, symbol="005930", company_name="삼성전자")
        _write_companyguide_fixture(root, symbol="000660", company_name="SK하이닉스")
        _write_companyguide_fixture(root, symbol="111111", company_name="테스트픽스처")
        _write_live_candidate_fixture(root)
    return Path(_FIXTURE_TEMP_DIR.name)


def _write_companyguide_fixture(root: Path, *, symbol: str, company_name: str) -> None:
    path = root / "data" / "cache" / "company_guide" / "2026-06-28" / f"{symbol}_recent_reports.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(
            {
                "lists": [
                    {
                        "RPT_ID": int(symbol) if symbol.isdigit() else 1,
                        "ANL_DT": "26/06/25",
                        "RPT_TITLE": "HBM 고객 수요와 중기 실적 가시성",
                        "CMP_CD": symbol,
                        "CMP_NM_KOR": company_name,
                        "COMMENT": (
                            f"{company_name}({symbol}) HBM 고객 수요와 고객 배정 물량이 확인됐고 "
                            "HBM 매출 비중 확대, 생산능력 선점, 중기 추정EPS 상향이 이어진다."
                        ),
                        "EPS_ACTION_TYP_NM": "추정EPS 상향",
                        "PRC_ACTION_TYP_NM": "목표주가 상향",
                        "TARGET_PRC": "100,000",
                        "EPS": 10000,
                        "BRK_NM_KOR": "테스트증권",
                    }
                ]
            },
            ensure_ascii=False,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )


def _write_live_candidate_fixture(root: Path) -> None:
    day_root = root / "output" / "production_cutover_v3" / "2026-06-29"
    day_root.mkdir(parents=True, exist_ok=True)
    symbols = (("267260", "HD현대일렉트릭"), ("298040", "효성중공업"))
    rows = []
    for index in range(30):
        symbol, company_name = symbols[index % len(symbols)]
        rows.append(
            {
                "candidate_event_id": f"CE-LIVE-DART-{symbol}-20260629{index:04d}",
                "symbol": symbol,
                "company_name": company_name,
                "event_date": "2026-06-29",
                "detected_at": "2026-06-29",
                "source_family": "DART",
                "source_id": f"https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260629{index:04d}",
                "event_type": "단일판매ㆍ공급계약체결",
                "event_title": f"{company_name} 단일판매ㆍ공급계약체결",
                "event_summary": f"{company_name} 공식 공급계약 공시 {index}",
                "raw_reason_codes": ["OFFICIAL_CONTRACT"],
                "issuer_directness": "DIRECT",
                "research_brain_eligible": True,
            }
        )
    (day_root / "candidate_events.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
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
