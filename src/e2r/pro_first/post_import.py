"""Automatic post-import progression with explicit deterministic authority inputs."""

from __future__ import annotations

from dataclasses import dataclass
import json
import os
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

from e2r.research.page_fetcher import PageFetcher
from e2r.research_brain.researcher_mode.schemas import (
    CANONICAL_COMPONENT_ORDER,
    ComponentAnchor,
)
from e2r.research_brain.runtime.scoring_contracts import (
    load_archetype_scoring_contract,
)
from e2r.research_brain.scoring import (
    CodexEvidenceImpactProvider,
    CreditValidatedImpact,
    EventOverlayInput,
    FullScoreValidityEvidenceV2,
)

from .gaps.adjudicator import DeterministicGapContext
from .gaps.service import ProGapAdjudicationService
from .gaps.supplemental_service import (
    CodexBoundedSupplementalExecutor,
    ProSupplementalResearchService,
)
from .ids import stable_id
from .job_store import ProFirstJobStore
from .models import JobStatus, ProResearchJob
from .publication import ProResultPublisher
from .scoring.judge_bridge import EvidenceOnlyJudgeProvider
from .scoring.codex_judge_provider import CodexEvidenceOnlyJudgeProvider
from .scoring.impact_compiler import ProValidatedImpactCompiler
from .scoring.service import ProScoringPipelineService
from .verification import ProSourceVerificationService, ProSourceVerifier


_GENERAL_WEB_FAMILIES = frozenset(
    {"GENERAL_WEB_DISCOVERY", "NAVER_DISCOVERY", "TRUSTED_BUSINESS_MEDIA"}
)

GapContextProvider = Callable[
    [ProResearchJob, Mapping[str, Any], Path],
    Mapping[str, DeterministicGapContext],
]
ScoringInputProvider = Callable[
    [ProResearchJob, Mapping[str, Any], Path],
    "ProPostImportScoringInputs",
]


@dataclass(frozen=True)
class ProPostImportScoringInputs:
    selected_archetype_id: str
    judge_provider: EvidenceOnlyJudgeProvider | None
    historical_anchors: tuple[ComponentAnchor | Mapping[str, Any], ...] = ()
    validated_impacts: tuple[CreditValidatedImpact, ...] = ()
    terminal_evidence: Mapping[str, Mapping[str, Any]] | None = None
    validity_evidence: FullScoreValidityEvidenceV2 | None = None
    event_overlay_input: EventOverlayInput | None = None
    hard_break_claim_ids: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.selected_archetype_id.strip():
            raise ValueError("post-import scoring requires one selected archetype")
        if self.terminal_evidence is None:
            object.__setattr__(self, "terminal_evidence", {})
        if self.validity_evidence is None:
            object.__setattr__(
                self,
                "validity_evidence",
                _pending_validity_evidence("POST_IMPORT_SCORING_INPUT_PENDING"),
            )


@dataclass(frozen=True)
class ProPostImportAdvance:
    job_id: str
    before_status: str
    after_status: str
    action: str
    wait_reason: str | None = None
    published: bool = False

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "schema_version": "e2r_pro_post_import_advance_v1",
            "job_id": self.job_id,
            "before_status": self.before_status,
            "after_status": self.after_status,
            "action": self.action,
            "wait_reason": self.wait_reason,
            "published": self.published,
        }


class ProFirstPostImportCoordinator:
    """Advance durable post-import states without inventing score authority.

    The default path performs live verification of the finite URL roster in the
    imported dossier, deterministic gap classification, and seven-component
    compilation.  It deliberately stops at provider pending when no evidence-
    only Judge provider exists.  Tests and production integration may inject
    fully validated scoring inputs to close score, StageCourt, and publication.
    """

    def __init__(
        self,
        store: ProFirstJobStore,
        *,
        runtime_root: str | Path,
        repo_root: str | Path = ".",
        source_verification_service: ProSourceVerificationService | None = None,
        gap_context_provider: GapContextProvider | None = None,
        scoring_input_provider: ScoringInputProvider | None = None,
        supplemental_service: ProSupplementalResearchService | None = None,
    ) -> None:
        self.store = store
        self.runtime_root = Path(runtime_root).expanduser().resolve()
        self.repo_root = Path(repo_root).expanduser().resolve()
        self.source_verification_service = (
            source_verification_service
            or ProSourceVerificationService(
                store,
                verifier=ProSourceVerifier(
                    page_fetcher=PageFetcher(live_enabled=True, max_text_chars=None)
                ),
            )
        )
        self.gap_context_provider = (
            gap_context_provider or compile_conservative_gap_contexts
        )
        self.scoring_input_provider = scoring_input_provider or (
            OperationalProScoringInputProvider(repo_root=self.repo_root)
        )
        self.supplemental_service = supplemental_service or (
            ProSupplementalResearchService(
                store,
                executor=CodexBoundedSupplementalExecutor(
                    repo_root=self.repo_root,
                ),
            )
        )

    @property
    def judge_provider_available(self) -> bool:
        """Whether the configured scoring input path is known to be actionable.

        Custom providers may decide per job, so the runtime still invokes a
        JUDGING job once when explicitly requested via ``process_job_once``.
        The default provider is statically pending and is excluded from the
        background actionable roster to avoid an unbounded no-progress loop.
        """

        return self.scoring_input_provider is not compile_provider_pending_scoring_inputs

    def advance_once(self, job_id: str) -> ProPostImportAdvance:
        before = self.store.get_job(job_id)
        root = self.runtime_root / "jobs" / job_id
        if before.status in {
            JobStatus.DOSSIER_IMPORTED.value,
            JobStatus.VERIFYING_SOURCES.value,
        }:
            run = self.source_verification_service.verify_job(job_id, job_root=root)
            return ProPostImportAdvance(
                job_id,
                before.status,
                run.job.status,
                "VERIFY_SOURCES",
            )
        if before.status == JobStatus.GAP_ADJUDICATION.value:
            dossier = _read_json(root / "import/research_dossier.normalized.json")
            contexts = self.gap_context_provider(before, dossier, root)
            run = ProGapAdjudicationService(self.store).adjudicate_job(
                job_id,
                job_root=root,
                deterministic_contexts=contexts,
            )
            wait = (
                "MATERIAL_GAP_SUPPLEMENTAL_RESEARCH_REQUIRED"
                if run.job.status == JobStatus.SUPPLEMENTAL_RESEARCH.value
                else None
            )
            return ProPostImportAdvance(
                job_id,
                before.status,
                run.job.status,
                "ADJUDICATE_GAPS",
                wait_reason=wait,
            )
        if before.status == JobStatus.SUPPLEMENTAL_RESEARCH.value:
            run = self.supplemental_service.run_job(job_id, job_root=root)
            unresolved = tuple(run.receipt.get("unresolved_gap_keys") or ())
            reason = None
            if unresolved:
                reason = (
                    "MATERIAL_GAP_PROVIDER_PENDING:"
                    if run.receipt.get("provider_pending_gap_keys")
                    else "MATERIAL_GAP_UNRESOLVED:"
                ) + ",".join(unresolved)
            return ProPostImportAdvance(
                job_id,
                before.status,
                run.job.status,
                "EXECUTE_BOUNDED_SUPPLEMENTAL",
                wait_reason=reason,
            )
        if before.status in {
            JobStatus.COMPONENT_RESEARCH.value,
            JobStatus.JUDGING.value,
            JobStatus.SCORING.value,
            JobStatus.STAGECOURT.value,
        }:
            dossier = _read_json(root / "import/research_dossier.normalized.json")
            inputs = self.scoring_input_provider(before, dossier, root)
            if inputs.selected_archetype_id not in set(before.archetype_ids):
                raise ValueError("scoring input archetype is outside the durable job")
            run = ProScoringPipelineService(self.store).run_job(
                job_id,
                job_root=root,
                selected_archetype_id=inputs.selected_archetype_id,
                judge_provider=inputs.judge_provider,
                historical_anchors=inputs.historical_anchors,
                validated_impacts=inputs.validated_impacts,
                terminal_evidence=inputs.terminal_evidence or {},
                validity_evidence=inputs.validity_evidence,
                event_overlay_input=inputs.event_overlay_input,
                hard_break_claim_ids=inputs.hard_break_claim_ids,
            )
            if run.job.status == JobStatus.FINAL.value:
                ProResultPublisher(self.store).publish(job_id, job_root=root)
                return ProPostImportAdvance(
                    job_id,
                    before.status,
                    run.job.status,
                    "SCORE_STAGECOURT_PUBLISH",
                    published=True,
                )
            pending = tuple(
                run.judge_result.pending_reasons
                if run.judge_result is not None
                else ()
            )
            return ProPostImportAdvance(
                job_id,
                before.status,
                run.job.status,
                "COMPONENT_AND_JUDGE",
                wait_reason=(";".join(pending) or "JUDGING_PROVIDER_PENDING"),
            )
        if before.status == JobStatus.FINAL.value:
            published = ProResultPublisher(self.store).publish(job_id, job_root=root)
            return ProPostImportAdvance(
                job_id,
                before.status,
                published.job.status,
                "PUBLISH",
                published=True,
            )
        return ProPostImportAdvance(
            job_id,
            before.status,
            before.status,
            "NONE",
        )

    def advance_until_wait(
        self,
        job_id: str,
        *,
        maximum_steps: int = 8,
    ) -> tuple[ProPostImportAdvance, ...]:
        if not 1 <= maximum_steps <= 32:
            raise ValueError("post-import maximum_steps must be between 1 and 32")
        advances: list[ProPostImportAdvance] = []
        for _step in range(maximum_steps):
            advance = self.advance_once(job_id)
            advances.append(advance)
            if (
                advance.published
                or advance.wait_reason is not None
                or advance.after_status == advance.before_status
            ):
                return tuple(advances)
        raise RuntimeError("post-import progression exceeded its deterministic step bound")


def compile_conservative_gap_contexts(
    job: ProResearchJob,
    dossier: Mapping[str, Any],
    _job_root: Path,
) -> Mapping[str, DeterministicGapContext]:
    """Compile maximum component bounds without trusting Pro gap labels."""

    contexts: dict[str, DeterministicGapContext] = {}
    for gap in dossier.get("unresolved_gaps") or ():
        gap_id = str(gap.get("dossier_gap_id") or "")
        archetype_id = str(gap.get("archetype_id") or "")
        affected = tuple(str(value) for value in gap.get("affected_component_ids") or ())
        if not gap_id or archetype_id not in set(job.archetype_ids):
            raise ValueError("dossier gap is outside the durable job archetype roster")
        contract = load_archetype_scoring_contract(archetype_id)
        if not set(affected).issubset(contract.component_max_points):
            raise ValueError("dossier gap affects a component outside the scoring contract")
        required = tuple(str(value).upper() for value in gap.get("required_source_families") or ())
        general_web_requested = bool(set(required) & _GENERAL_WEB_FAMILIES)
        route_signatures = tuple(
            stable_id(
                "PROSOURCE_ROUTE",
                {
                    "job_id": job.job_id,
                    "dossier_gap_id": gap_id,
                    "source_family": family,
                },
            )
            for family in required
        )
        contexts[gap_id] = DeterministicGapContext(
            dossier_gap_id=gap_id,
            component_lower_delta={component_id: 0.0 for component_id in affected},
            component_upper_delta={
                component_id: float(contract.component_max_points[component_id])
                for component_id in affected
            },
            deterministic_lower_stage=None,
            deterministic_upper_stage=None,
            executable_new_source_route_signatures=route_signatures,
            could_change_score=True,
            official_first_attempted=not general_web_requested,
            rationale=(
                "verified fact roster and scoring-contract component maximum bound; "
                "Pro-proposed gap class and Stage flags are not authoritative"
            ),
        )
    return contexts


def compile_provider_pending_scoring_inputs(
    job: ProResearchJob,
    _dossier: Mapping[str, Any],
    job_root: Path,
) -> ProPostImportScoringInputs:
    if len(job.archetype_ids) != 1:
        raise ValueError(
            "automatic scoring requires one deterministic selected archetype; "
            "multi-archetype jobs remain pending"
        )
    archetype_id = job.archetype_ids[0]
    packet = _read_json(job_root / "packet/research_packet.json")
    anchors = tuple(
        dict(row)
        for row in packet.get("historical_anchor_digest") or ()
        if isinstance(row, Mapping)
        and row.get("digest_kind") == "COMPONENT_ANCHOR"
        and str(row.get("archetype_id") or "") == archetype_id
    )
    terminal = {
        component_id: {
            "status": "PROVIDER_PENDING",
            "reason": "validated impact adjudication is not configured",
        }
        for component_id in CANONICAL_COMPONENT_ORDER
    }
    return ProPostImportScoringInputs(
        selected_archetype_id=archetype_id,
        judge_provider=None,
        historical_anchors=anchors,
        validated_impacts=(),
        terminal_evidence=terminal,
        validity_evidence=_pending_validity_evidence(
            "VALIDATED_IMPACT_AND_JUDGE_PROVIDER_PENDING"
        ),
    )


class OperationalProScoringInputProvider:
    """Compile score inputs from durable verified leaves using Codex proposals.

    Codex can propose semantic impact and Judge rows, but the existing
    deterministic validators, scorer, and StageCourt retain every production
    authority.  A missing or invalid proposal returns provider pending rather
    than manufacturing a zero score.
    """

    def __init__(self, *, repo_root: str | Path = ".") -> None:
        self.repo_root = Path(repo_root).expanduser().resolve()
        provider_workdir = Path.home() if os.name == "nt" else self.repo_root
        self.impact_provider = CodexEvidenceImpactProvider.default(
            working_directory=provider_workdir,
            timeout_seconds=180.0,
        )
        self.judge_provider = CodexEvidenceOnlyJudgeProvider.default(
            working_directory=provider_workdir,
            timeout_seconds=180.0,
        )
        self.impact_compiler = ProValidatedImpactCompiler(
            self.impact_provider,
            repo_root=self.repo_root,
        )

    def __call__(
        self,
        job: ProResearchJob,
        _dossier: Mapping[str, Any],
        job_root: Path,
    ) -> ProPostImportScoringInputs:
        if len(job.archetype_ids) != 1:
            return compile_provider_pending_scoring_inputs(job, _dossier, job_root)
        archetype_id = job.archetype_ids[0]
        packet = _read_json(job_root / "packet/research_packet.json")
        anchors = tuple(
            dict(row)
            for row in packet.get("historical_anchor_digest") or ()
            if isinstance(row, Mapping)
            and row.get("digest_kind") == "COMPONENT_ANCHOR"
            and str(row.get("archetype_id") or "") == archetype_id
        )
        compilation = self.impact_compiler.compile(
            job=job,
            dossier=_dossier,
            job_root=job_root,
            selected_archetype_id=archetype_id,
        )
        return ProPostImportScoringInputs(
            selected_archetype_id=archetype_id,
            judge_provider=(
                self.judge_provider if compilation.ready_for_judging else None
            ),
            historical_anchors=anchors,
            validated_impacts=compilation.impacts,
            terminal_evidence=compilation.terminal_evidence,
            validity_evidence=compilation.validity_evidence,
        )


def _pending_validity_evidence(source_audit_id: str) -> FullScoreValidityEvidenceV2:
    return FullScoreValidityEvidenceV2(
        schema_totality_status="SCORING_SCHEMA_TOTALITY_PENDING",
        scoring_schema_critical_count=1,
        silent_zero_default_count=0,
        positive_impact_zeroed_by_missing_cap_count=0,
        counter_impact_zeroed_by_missing_cap_count=0,
        mechanism_scope_failure_count=0,
        question_component_reconciliation_critical_count=0,
        unresolved_contradiction_count=0,
        pending_state_count=len(CANONICAL_COMPONENT_ORDER),
        absence_without_adequacy_count=0,
        gold_critical_fact_miss_count=0,
        cross_business_question_closure_count=0,
        same_fact_duplicate_credit_count=0,
        same_document_duplicate_credit_count=0,
        source_audit_ids=(source_audit_id,),
    )


def _read_json(path: Path) -> Mapping[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        raise ValueError(f"expected JSON object: {path}")
    return payload


__all__ = [
    "GapContextProvider",
    "ProFirstPostImportCoordinator",
    "ProPostImportAdvance",
    "ProPostImportScoringInputs",
    "ScoringInputProvider",
    "OperationalProScoringInputProvider",
    "compile_conservative_gap_contexts",
    "compile_provider_pending_scoring_inputs",
]
