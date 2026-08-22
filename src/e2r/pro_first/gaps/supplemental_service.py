"""Bounded material-gap-only execution after a verified Pro dossier.

This lane is deliberately narrower than Researcher Mode.  It asks an LLM for
literal target-scoped queries, applies the existing query validator, executes
only the durable bounded SourceTask roster, and accepts evidence only through
the existing Evidence OS acquisition/extraction bridge.  It never restarts the
full research graph and it never assigns points or a Stage.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from datetime import date
import hashlib
import json
import os
from pathlib import Path
from typing import Any, Mapping, Protocol, Sequence

from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2
from e2r.agentic.evidence_os import MappingStatus, SupportDirection
from e2r.production.claim_extraction import (
    CodexCLIExtractorProvider,
    LLMContractBlindRawAssertionExtractor,
)
from e2r.research_brain.intelligence_schema import CurrentEvidenceFact
from e2r.research_brain.planning import (
    QUERY_INTENT_OUTPUT_SCHEMA,
    SourceBudget,
    build_codex_question_query_provider,
    compile_question_task_context,
    decode_query_generation_output,
    validate_llm_literal_queries,
)
from e2r.research_brain.researcher_mode.evidence_fact_compiler import (
    EvidenceFactCompiler,
)
from e2r.research_brain.schemas import SourceTask
from e2r.research_brain.v2_schemas import CandidateEventV2
from e2r.research_brain.v4_evidence_extraction_bridge import (
    EvidenceOSExecutionBundleV4,
    execute_source_tasks_with_evidence_os_v4,
)
from e2r.research_brain.v4_schemas import SourceAcquisitionModeV4
from e2r.research_brain.v4_source_acquisition_runner import (
    SourceAcquisitionRunnerV4,
)

from ..atomic_io import fsync_directory
from ..ids import canonical_hash, canonical_json, stable_id
from ..job_store import ProFirstJobStore
from ..models import JobStatus, ProResearchJob
from ..state_machine import NoProgressDetected
from .source_family_policy import route_source_classes


_GENERAL_WEB_SOURCE_CLASSES = frozenset(
    {
        "GeneralWebSearch",
        "NaverSearch",
        "TrustedNews",
        "IndustryMedia",
        "CompanyNewsroom",
        "ReportPDF",
        "BrokerReportPublicPDF",
    }
)

_QUERY_PROMPT_SCHEMA_NAME = "e2r_pro_material_gap_queries"
SUPPLEMENTAL_EXECUTION_SEMANTICS_VERSION = "e2r_pro_supplemental_execution_v3"


@dataclass(frozen=True)
class SupplementalTaskResult:
    evidence_gap_key: str
    task_id: str
    status: str
    resolved: bool
    query_count: int
    candidate_count: int
    fetch_count: int
    queries: tuple[str, ...] = ()
    query_prompt_hashes: tuple[str, ...] = ()
    query_response_hashes: tuple[str, ...] = ()
    provider_name: str = ""
    selected_contract_primitive_id: str = ""
    provider_errors: tuple[str, ...] = ()
    stop_reason: str = ""
    dossier_facts: tuple[Mapping[str, Any], ...] = ()
    evidence_facts: tuple[Mapping[str, Any], ...] = ()
    claim_fact_links: tuple[Mapping[str, Any], ...] = ()
    source_verifications: tuple[Mapping[str, Any], ...] = ()
    source_pages: tuple[tuple[str, str], ...] = ()

    def __post_init__(self) -> None:
        if not self.evidence_gap_key or not self.task_id:
            raise ValueError("supplemental result requires exact gap/task identity")
        for label, value, maximum in (
            ("query_count", self.query_count, 3),
            ("candidate_count", self.candidate_count, 20),
            ("fetch_count", self.fetch_count, 6),
        ):
            if value < 0 or value > maximum:
                raise ValueError(f"supplemental {label} exceeds the bounded contract")
        if self.resolved and not self.evidence_facts:
            raise ValueError("a resolved material gap requires source-backed EvidenceFact")

    @property
    def provider_pending(self) -> bool:
        return self.status == "PROVIDER_PENDING"

    def to_receipt_row(self) -> Mapping[str, Any]:
        return {
            "schema_version": "e2r_pro_supplemental_task_result_v1",
            "evidence_gap_key": self.evidence_gap_key,
            "task_id": self.task_id,
            "status": self.status,
            "resolved": self.resolved,
            "query_count": self.query_count,
            "candidate_count": self.candidate_count,
            "fetch_count": self.fetch_count,
            "query_hashes": [
                hashlib.sha256(value.encode("utf-8")).hexdigest()
                for value in self.queries
            ],
            "query_prompt_hashes": list(self.query_prompt_hashes),
            "query_response_hashes": list(self.query_response_hashes),
            "provider_name": self.provider_name,
            "selected_contract_primitive_id": self.selected_contract_primitive_id,
            "provider_errors": list(self.provider_errors),
            "stop_reason": self.stop_reason,
            "dossier_fact_count": len(self.dossier_facts),
            "evidence_fact_count": len(self.evidence_facts),
            "claim_fact_link_count": len(self.claim_fact_links),
            "full_research_restart_count": 0,
            "production_score_authority": False,
            "production_stage_authority": False,
        }


@dataclass(frozen=True)
class SupplementalResearchRun:
    job: ProResearchJob
    task_results: tuple[SupplementalTaskResult, ...]
    receipt: Mapping[str, Any]
    supplemental_root: Path
    reused: bool = False


class SupplementalTaskExecutor(Protocol):
    def execute(
        self,
        *,
        job: ProResearchJob,
        task_binding: Mapping[str, Any],
        gap_decision: Mapping[str, Any],
        dossier: Mapping[str, Any],
        verified_facts: Sequence[Mapping[str, Any]],
        job_root: Path,
    ) -> SupplementalTaskResult: ...


class CodexBoundedSupplementalExecutor:
    """Execute one material gap through LLM query generation and Evidence OS."""

    def __init__(
        self,
        *,
        repo_root: str | Path = ".",
        query_provider: Any | None = None,
        source_runner: SourceAcquisitionRunnerV4 | None = None,
        claim_extractor: LLMContractBlindRawAssertionExtractor | None = None,
    ) -> None:
        self.repo_root = Path(repo_root).expanduser().resolve()
        provider_workdir = Path.home() if os.name == "nt" else self.repo_root
        self.query_provider = query_provider or build_codex_question_query_provider(
            working_directory=provider_workdir
        )
        self.source_runner = source_runner or SourceAcquisitionRunnerV4(
            mode=SourceAcquisitionModeV4.LIVE_FULL_BOUNDED.value,
            repo_root=self.repo_root,
        )
        self.claim_extractor = claim_extractor or LLMContractBlindRawAssertionExtractor(
            provider=CodexCLIExtractorProvider(
                repo_root=provider_workdir,
                timeout_seconds=180.0,
            )
        )

    def execute(
        self,
        *,
        job: ProResearchJob,
        task_binding: Mapping[str, Any],
        gap_decision: Mapping[str, Any],
        dossier: Mapping[str, Any],
        verified_facts: Sequence[Mapping[str, Any]],
        job_root: Path,
    ) -> SupplementalTaskResult:
        task = _source_task_from_mapping(task_binding.get("source_task") or {})
        gap_key = str(task_binding.get("evidence_gap_key") or "")
        if not gap_key or gap_key != str(gap_decision.get("evidence_gap_key") or ""):
            raise ValueError("supplemental task is detached from its exact gap decision")
        if task.candidate_event_id != job.candidate_id or task.symbol != job.symbol:
            raise ValueError("supplemental SourceTask belongs to another durable job")
        if not task.llm_query_allowed:
            raise ValueError("material-gap supplemental task must delegate queries to LLM")
        contracts = load_evidence_contracts_v2(require_all_archetypes=True)
        contract = contracts.get(task.archetype_id)
        if contract is None:
            return SupplementalTaskResult(
                evidence_gap_key=gap_key,
                task_id=task.task_id,
                status="PROVIDER_PENDING",
                resolved=False,
                query_count=0,
                candidate_count=0,
                fetch_count=0,
                provider_name=str(getattr(self.query_provider, "provider_name", "UNKNOWN")),
                provider_errors=("EVIDENCE_CONTRACT_NOT_FOUND",),
                stop_reason="selected_archetype_contract_missing",
            )
        allowed_primitives = _contract_primitive_ids(contract)
        (
            queries,
            selected_primitive,
            prompt_hashes,
            response_hashes,
            pending,
        ) = self._generate_queries(
            job=job,
            task=task,
            gap_decision=gap_decision,
            dossier=dossier,
            verified_facts=verified_facts,
            allowed_primitive_ids=allowed_primitives,
        )
        if pending is not None:
            return SupplementalTaskResult(
                evidence_gap_key=gap_key,
                task_id=task.task_id,
                status="PROVIDER_PENDING",
                resolved=False,
                query_count=0,
                candidate_count=0,
                fetch_count=0,
                query_prompt_hashes=prompt_hashes,
                query_response_hashes=response_hashes,
                provider_name=str(getattr(self.query_provider, "provider_name", "UNKNOWN")),
                selected_contract_primitive_id=selected_primitive or "",
                provider_errors=(pending,),
                stop_reason="llm_query_generation_pending",
            )

        routed = _routed_source_task(
            task,
            queries=queries,
            selected_primitive_id=str(selected_primitive),
        )
        event = CandidateEventV2(
            candidate_event_id=job.candidate_id,
            symbol=job.symbol,
            company_name=job.company_name,
            event_date=job.as_of_date,
            detected_at=job.created_at,
            source_family="PRO_RESEARCH_DOSSIER",
            source_id=str(job.dossier_id or job.job_id),
            event_type="PRO_MATERIAL_GAP_SUPPLEMENT",
            raw_reason_codes=(str(gap_decision.get("planner_label") or ""),),
            event_title=f"{job.company_name} material evidence gap",
            event_summary=str(
                ((gap_decision.get("key") or {}).get("objective_identity"))
                or task.primitive_gap
            ),
            issuer_directness="DIRECT",
        )
        bundle = execute_source_tasks_with_evidence_os_v4(
            event=event,
            tasks=(routed,),
            contract=contract,
            as_of_date=date.fromisoformat(job.as_of_date),
            source_runner=self.source_runner,
            claim_extractor=self.claim_extractor,
        )
        execution = bundle.executions[0]
        dossier_facts, evidence_facts, links, verifications, pages = (
            _compile_bundle_evidence(
                job=job,
                gap_decision=gap_decision,
                execution=execution,
                bundle=bundle,
                job_root=job_root,
            )
        )
        budget = dict(execution.budget_used)
        resolved = bool(execution.satisfies_source_task and evidence_facts)
        provider_pending = bool(execution.provider_errors) and not resolved
        status = (
            "RESOLVED"
            if resolved
            else "PROVIDER_PENDING"
            if provider_pending
            else "NO_EVIDENCE_FOUND"
        )
        return SupplementalTaskResult(
            evidence_gap_key=gap_key,
            task_id=task.task_id,
            status=status,
            resolved=resolved,
            query_count=min(len(queries), int(budget.get("queries") or len(queries))),
            candidate_count=int(budget.get("candidates") or 0),
            fetch_count=int(budget.get("fetches") or 0),
            queries=queries,
            query_prompt_hashes=prompt_hashes,
            query_response_hashes=response_hashes,
            provider_name=str(execution.provider_name or ""),
            selected_contract_primitive_id=str(selected_primitive),
            provider_errors=tuple(execution.provider_errors),
            stop_reason=str(execution.stop_reason or ""),
            dossier_facts=dossier_facts,
            evidence_facts=evidence_facts,
            claim_fact_links=links,
            source_verifications=verifications,
            source_pages=pages,
        )

    def _generate_queries(
        self,
        *,
        job: ProResearchJob,
        task: SourceTask,
        gap_decision: Mapping[str, Any],
        dossier: Mapping[str, Any],
        verified_facts: Sequence[Mapping[str, Any]],
        allowed_primitive_ids: Sequence[str],
    ) -> tuple[
        tuple[str, ...],
        str | None,
        tuple[str, ...],
        tuple[str, ...],
        str | None,
    ]:
        current = tuple(
            CurrentEvidenceFact(
                fact_id=str(row.get("fact_id") or stable_id("PROFACTCTX", row)),
                text=_fact_context_text(row),
                observed_date=job.as_of_date,
                target_relation="DIRECT",
                current_status=str(row.get("current_lifecycle") or "CURRENT"),
            )
            for row in verified_facts[:20]
            if _fact_context_text(row)
        )
        if not current:
            current = (
                CurrentEvidenceFact(
                    fact_id=stable_id(
                        "PROFACTCTX",
                        {"job_id": job.job_id, "gap_key": gap_decision.get("evidence_gap_key")},
                    ),
                    text=f"{job.company_name}의 검증된 현재 fact roster에 이 공백을 닫는 원문이 없다.",
                    observed_date=job.as_of_date,
                    target_relation="DIRECT",
                    current_status="UNKNOWN",
                ),
            )
        key = gap_decision.get("key") or {}
        context = compile_question_task_context(
            target_id=job.symbol,
            target_name=job.company_name,
            symbol=job.symbol,
            target_aliases=tuple(
                dict.fromkeys(
                    (
                        job.company_name,
                        job.symbol,
                        *(str(value) for value in (dossier.get("target") or {}).get("aliases") or ()),
                    )
                )
            ),
            as_of_date=job.as_of_date,
            current_facts=current,
            missing_information=(
                str(key.get("objective_identity") or task.primitive_gap),
                str(key.get("economic_mechanism_id") or ""),
                str(key.get("required_source_family") or ""),
            ),
            existing_queries=(),
        )
        budget = SourceBudget(
            max_queries=task.max_queries,
            max_candidates=task.max_candidates,
            max_fetches=task.max_fetches,
        )
        feedback: list[str] = []
        rejected: list[str] = []
        prompt_hashes: list[str] = []
        response_hashes: list[str] = []
        for attempt in range(1, 4):
            completion = None
            payload = {
                "schema_version": "e2r_pro_material_gap_query_input_v1",
                "input_id": stable_id(
                    "PROSUPQUERY",
                    {
                        "job_id": job.job_id,
                        "task_id": task.task_id,
                        "attempt": attempt,
                        "feedback": feedback,
                    },
                ),
                "target": {
                    "target_id": job.symbol,
                    "company_name": job.company_name,
                    "aliases": list(context.target_aliases),
                },
                "as_of_date": job.as_of_date,
                "current_facts": [row.to_dict() for row in current],
                "missing_information": list(context.missing_information),
                "source_route": {
                    "preferred_source_families": list(task.preferred_source_classes),
                    "general_search_allowed": task.general_search_allowed,
                },
                "allowed_contract_primitive_ids": list(allowed_primitive_ids),
                "budget": budget.to_dict(),
                "validation_feedback": list(feedback),
                "rejected_queries": list(dict.fromkeys(rejected)),
                "score_authority": False,
                "stage_authority": False,
            }
            prompt = "\n\n".join(
                (
                    "You generate literal source queries for one bounded E2R material evidence gap.",
                    "Use only the supplied current facts and missing information. Every query must name the target and use an explicit reporting year no later than as_of_date.",
                    "Select exactly one allowed_contract_primitive_id that best operationalizes the open-ended gap, and generate queries for that same primitive. Do not invent a primitive.",
                    "Do not output a score, Stage, investment instruction, canonical archetype label, or deterministic fallback query. Return exactly the requested JSON object.",
                    canonical_json(payload),
                )
            )
            prompt_hashes.append(hashlib.sha256(prompt.encode("utf-8")).hexdigest())
            try:
                completion = self.query_provider.complete(
                    prompt=prompt,
                    output_schema=_supplemental_query_output_schema(
                        allowed_primitive_ids
                    ),
                )
                decoded = _decode_supplemental_query_output(
                    completion.payload,
                    expected_input_id=str(payload["input_id"]),
                    allowed_primitive_ids=allowed_primitive_ids,
                )
                raw_response = str(getattr(completion, "raw_response", ""))
                response_hashes.append(
                    hashlib.sha256(raw_response.encode("utf-8")).hexdigest()
                )
                if decoded["abstain"]:
                    return (
                        (),
                        decoded["selected_contract_primitive_id"],
                        tuple(prompt_hashes),
                        tuple(response_hashes),
                        "QUERY_PROVIDER_ABSTAINED:" + str(decoded["abstention_reason"]),
                    )
                queries = validate_llm_literal_queries(
                    decoded["literal_queries"],
                    context=context,
                    primitive_id=decoded["selected_contract_primitive_id"],
                    budget=budget,
                    prior_rejected_queries=tuple(rejected),
                )
                return (
                    queries,
                    decoded["selected_contract_primitive_id"],
                    tuple(prompt_hashes),
                    tuple(response_hashes),
                    None,
                )
            except Exception as error:
                raw = getattr(completion, "payload", {})
                if isinstance(raw, Mapping):
                    rejected.extend(
                        str(value)
                        for value in raw.get("literal_queries") or ()
                        if str(value).strip()
                    )
                feedback.append(f"attempt_{attempt}:{type(error).__name__}:{error}")
        return (
            (),
            None,
            tuple(prompt_hashes),
            tuple(response_hashes),
            "QUERY_PROVIDER_OR_OUTPUT_ERROR:" + "|".join(feedback),
        )


class ProSupplementalResearchService:
    """Persist bounded task results and release only fully resolved gaps."""

    def __init__(
        self,
        store: ProFirstJobStore,
        *,
        executor: SupplementalTaskExecutor,
    ) -> None:
        self.store = store
        self.executor = executor

    def run_job(
        self,
        job_id: str,
        *,
        job_root: str | Path,
    ) -> SupplementalResearchRun:
        root = Path(job_root).resolve()
        supplemental_root = root / "supplemental"
        receipt_path = supplemental_root / "supplemental_execution_receipt.json"
        job = self.store.get_job(job_id)
        if job.status != JobStatus.SUPPLEMENTAL_RESEARCH.value:
            if job.status == JobStatus.COMPONENT_RESEARCH.value and receipt_path.is_file():
                receipt = _read_json(receipt_path)
                if receipt.get("status") != "SUPPLEMENTAL_RESEARCH_COMPLETE":
                    raise ValueError("completed supplemental state has a non-complete receipt")
                return SupplementalResearchRun(
                    job=job,
                    task_results=(),
                    receipt=receipt,
                    supplemental_root=supplemental_root,
                    reused=True,
                )
            raise ValueError("job is outside the supplemental research boundary")
        prior_receipt = _read_json(receipt_path) if receipt_path.is_file() else None
        tasks = _read_jsonl(root / "gaps/supplemental_tasks.jsonl")
        decisions = {
            str(row.get("evidence_gap_key") or ""): row
            for row in _read_jsonl(root / "gaps/gap_decisions.jsonl")
        }
        if not tasks or len(decisions) < len(tasks):
            raise ValueError("supplemental task roster is missing exact gap decisions")
        dossier = _read_json(root / "import/research_dossier.normalized.json")
        verified_facts = _read_jsonl(root / "verification/evidence_facts.jsonl")
        supplemental_input_hash = canonical_hash(
            {
                "job_id": job.job_id,
                "dossier_hash": canonical_hash(dossier),
                "verified_fact_roster_hash": canonical_hash(verified_facts),
                "tasks": tasks,
                "decisions": [
                    decisions[str(task.get("evidence_gap_key") or "")]
                    for task in tasks
                ],
            }
        )
        if (
            prior_receipt is not None
            and prior_receipt.get("status")
            in {
                "SUPPLEMENTAL_RESEARCH_PROVIDER_PENDING",
                "SUPPLEMENTAL_RESEARCH_UNRESOLVED",
            }
        ):
            prior_semantics = str(
                prior_receipt.get("execution_semantics_version") or ""
            )
            prior_input_hash = str(
                prior_receipt.get("supplemental_input_hash") or ""
            )
            if (
                prior_semantics == SUPPLEMENTAL_EXECUTION_SEMANTICS_VERSION
                and prior_input_hash == supplemental_input_hash
            ):
                raise NoProgressDetected(
                    "supplemental inputs and execution semantics are unchanged; repeat is forbidden"
                )
            _archive_prior_supplemental_attempt(
                supplemental_root=supplemental_root,
                receipt=prior_receipt,
            )
        task_results = tuple(
            self.executor.execute(
                job=job,
                task_binding=task,
                gap_decision=decisions[str(task.get("evidence_gap_key") or "")],
                dossier=dossier,
                verified_facts=verified_facts,
                job_root=root,
            )
            for task in tasks
        )
        if {row.task_id for row in task_results} != {
            str((row.get("source_task") or {}).get("task_id") or "") for row in tasks
        }:
            raise ValueError("supplemental executor result roster differs from the plan")
        _write_source_pages(supplemental_root, task_results)
        _write_jsonl_atomic(
            supplemental_root / "task_executions.jsonl",
            [row.to_receipt_row() for row in task_results],
        )
        _write_jsonl_atomic(
            supplemental_root / "dossier_facts.jsonl",
            [fact for row in task_results for fact in row.dossier_facts],
        )
        _write_jsonl_atomic(
            supplemental_root / "evidence_facts.jsonl",
            [fact for row in task_results for fact in row.evidence_facts],
        )
        _write_jsonl_atomic(
            supplemental_root / "claim_fact_links.jsonl",
            [link for row in task_results for link in row.claim_fact_links],
        )
        _write_jsonl_atomic(
            supplemental_root / "source_verifications.jsonl",
            [verification for row in task_results for verification in row.source_verifications],
        )
        resolved = tuple(sorted(row.evidence_gap_key for row in task_results if row.resolved))
        pending = tuple(sorted(row.evidence_gap_key for row in task_results if not row.resolved))
        provider_pending = tuple(
            sorted(row.evidence_gap_key for row in task_results if row.provider_pending)
        )
        receipt_status = (
            "SUPPLEMENTAL_RESEARCH_COMPLETE"
            if not pending
            else "SUPPLEMENTAL_RESEARCH_PROVIDER_PENDING"
            if provider_pending
            else "SUPPLEMENTAL_RESEARCH_UNRESOLVED"
        )
        receipt = {
            "schema_version": "e2r_pro_supplemental_execution_receipt_v1",
            "execution_semantics_version": SUPPLEMENTAL_EXECUTION_SEMANTICS_VERSION,
            "supplemental_input_hash": supplemental_input_hash,
            "execution_attempt": int(
                (prior_receipt or {}).get("execution_attempt") or 1
            )
            + (1 if prior_receipt is not None else 0),
            "status": receipt_status,
            "job_id": job.job_id,
            "dossier_id": job.dossier_id,
            "task_count": len(task_results),
            "resolved_gap_keys": list(resolved),
            "unresolved_gap_keys": list(pending),
            "provider_pending_gap_keys": list(provider_pending),
            "query_count": sum(row.query_count for row in task_results),
            "candidate_count": sum(row.candidate_count for row in task_results),
            "fetch_count": sum(row.fetch_count for row in task_results),
            "evidence_fact_count": sum(len(row.evidence_facts) for row in task_results),
            "full_research_restart_count": 0,
            "prohibited_gap_task_count": 0,
            "deterministic_query_template_count": 0,
            "query_generation_owner": "LLM",
            "production_score_authority": False,
            "production_stage_authority": False,
            "task_result_hash": canonical_hash(
                [row.to_receipt_row() for row in task_results]
            ),
        }
        _write_json_atomic(receipt_path, receipt)
        if pending:
            return SupplementalResearchRun(
                job=job,
                task_results=task_results,
                receipt=receipt,
                supplemental_root=supplemental_root,
            )
        # Validate the effective append-only roster before releasing the job to
        # component compilation.  A colliding fact/claim identity must fail
        # here, not surface later as an ambiguous scoring lineage.
        load_effective_verified_evidence(root)
        transitioned = self.store.transition(
            job_id,
            expected_version=job.state_version,
            to_status=JobStatus.COMPONENT_RESEARCH,
            actor="pro-material-gap-supplemental",
            idempotency_key=f"supplemental-complete:{canonical_hash(receipt)}",
            payload={
                "resolved_gap_count": len(resolved),
                "query_count": receipt["query_count"],
                "fetch_count": receipt["fetch_count"],
                "full_research_restart_count": 0,
            },
        )
        return SupplementalResearchRun(
            job=transitioned,
            task_results=task_results,
            receipt=receipt,
            supplemental_root=supplemental_root,
        )


def load_effective_verified_evidence(
    job_root: str | Path,
) -> tuple[
    tuple[Mapping[str, Any], ...],
    tuple[Mapping[str, Any], ...],
    tuple[Mapping[str, Any], ...],
]:
    """Return base plus completed supplemental evidence without mutating base receipts."""

    root = Path(job_root).resolve()
    facts = list(_read_jsonl(root / "verification/evidence_facts.jsonl"))
    links = list(_read_jsonl(root / "verification/claim_fact_links.jsonl"))
    verifications = list(_read_jsonl(root / "verification/source_verifications.jsonl"))
    receipt_path = root / "supplemental/supplemental_execution_receipt.json"
    if not receipt_path.is_file():
        return tuple(facts), tuple(links), tuple(verifications)
    receipt = _read_json(receipt_path)
    if receipt.get("status") != "SUPPLEMENTAL_RESEARCH_COMPLETE":
        return tuple(facts), tuple(links), tuple(verifications)
    facts.extend(_read_jsonl(root / "supplemental/evidence_facts.jsonl"))
    links.extend(_read_jsonl(root / "supplemental/claim_fact_links.jsonl"))
    verifications.extend(_read_jsonl(root / "supplemental/source_verifications.jsonl"))
    if len({str(row.get("fact_id") or "") for row in facts}) != len(facts):
        raise ValueError("base and supplemental EvidenceFact ids collide")
    if len({str(row.get("claim_id") or "") for row in links}) != len(links):
        raise ValueError("base and supplemental claim lineage ids collide")
    return tuple(facts), tuple(links), tuple(verifications)


def load_effective_dossier_facts(
    dossier: Mapping[str, Any],
    job_root: str | Path,
) -> tuple[Mapping[str, Any], ...]:
    root = Path(job_root).resolve()
    rows = [
        *(dossier.get("material_facts") or ()),
        *(dossier.get("counterfacts") or ()),
    ]
    receipt_path = root / "supplemental/supplemental_execution_receipt.json"
    if receipt_path.is_file() and _read_json(receipt_path).get("status") == "SUPPLEMENTAL_RESEARCH_COMPLETE":
        rows.extend(_read_jsonl(root / "supplemental/dossier_facts.jsonl"))
    return tuple(rows)


def resolved_supplemental_gap_keys(job_root: str | Path) -> frozenset[str]:
    path = Path(job_root).resolve() / "supplemental/supplemental_execution_receipt.json"
    if not path.is_file():
        return frozenset()
    receipt = _read_json(path)
    if receipt.get("status") != "SUPPLEMENTAL_RESEARCH_COMPLETE":
        return frozenset()
    return frozenset(str(value) for value in receipt.get("resolved_gap_keys") or ())


def _source_task_from_mapping(row: Mapping[str, Any]) -> SourceTask:
    fields = {
        "task_id",
        "candidate_event_id",
        "symbol",
        "company_name",
        "archetype_id",
        "primitive_gap",
        "task_type",
        "preferred_source_classes",
        "fallback_source_classes",
        "forbidden_source_classes",
        "allowed_domains",
        "date_window",
        "max_queries",
        "max_candidates",
        "max_fetches",
        "stop_condition",
        "query_intents",
        "llm_query_allowed",
        "general_search_allowed",
        "reason_from_memory",
        "memory_record_ids",
    }
    if not fields.issuperset(row) or not {
        "task_id",
        "candidate_event_id",
        "symbol",
        "company_name",
        "archetype_id",
        "primitive_gap",
        "task_type",
        "preferred_source_classes",
    }.issubset(row):
        raise ValueError("invalid durable supplemental SourceTask payload")
    payload = {key: row[key] for key in row if key in fields}
    for key in (
        "preferred_source_classes",
        "fallback_source_classes",
        "forbidden_source_classes",
        "allowed_domains",
        "query_intents",
        "memory_record_ids",
    ):
        if key in payload:
            payload[key] = tuple(payload[key] or ())
    return SourceTask(**payload)


def _supplemental_query_output_schema(
    allowed_primitive_ids: Sequence[str],
) -> Mapping[str, Any]:
    allowed = tuple(dict.fromkeys(str(value).strip() for value in allowed_primitive_ids))
    if not allowed or any(not value for value in allowed):
        raise ValueError("supplemental query schema requires contract primitives")
    properties = dict(QUERY_INTENT_OUTPUT_SCHEMA["properties"])
    properties["selected_contract_primitive_id"] = {
        "type": "string",
        "enum": list(allowed),
    }
    return {
        "type": "object",
        "additionalProperties": False,
        "properties": properties,
        "required": [
            *QUERY_INTENT_OUTPUT_SCHEMA["required"],
            "selected_contract_primitive_id",
        ],
    }


def _decode_supplemental_query_output(
    raw: Mapping[str, Any],
    *,
    expected_input_id: str,
    allowed_primitive_ids: Sequence[str],
) -> Mapping[str, Any]:
    base_keys = frozenset(str(value) for value in QUERY_INTENT_OUTPUT_SCHEMA["required"])
    expected_keys = base_keys | {"selected_contract_primitive_id"}
    actual_keys = frozenset(str(key) for key in raw)
    if actual_keys != expected_keys:
        raise ValueError(
            "supplemental query output keys differ: "
            f"missing={sorted(expected_keys - actual_keys)}, "
            f"unknown={sorted(actual_keys - expected_keys)}"
        )
    decoded = dict(
        decode_query_generation_output(
            {key: raw[key] for key in base_keys},
            expected_input_id=expected_input_id,
        )
    )
    selected = str(raw.get("selected_contract_primitive_id") or "").strip()
    allowed = frozenset(str(value).strip() for value in allowed_primitive_ids)
    if not selected or selected not in allowed:
        raise ValueError("query provider selected a primitive outside the contract")
    decoded["selected_contract_primitive_id"] = selected
    return decoded


def _contract_primitive_ids(contract: Any) -> tuple[str, ...]:
    primitive_ids = set(str(value).strip() for value in contract.required_primitives)
    primitive_ids.update(str(value).strip() for value in contract.green_gate.primitive_ids())
    primitive_ids.update(str(value).strip() for value in contract.alternative_primitives)
    primitive_ids.update(
        str(value).strip()
        for values in contract.alternative_primitives.values()
        for value in values
    )
    primitive_ids.update(str(value).strip() for value in contract.primitive_aliases)
    primitive_ids.update(
        str(value).strip()
        for values in contract.score_rubric.values()
        for value in values
    )
    return tuple(sorted(value for value in primitive_ids if value))


def _routed_source_task(
    task: SourceTask,
    *,
    queries: tuple[str, ...],
    selected_primitive_id: str,
) -> SourceTask:
    if not selected_primitive_id.strip():
        raise ValueError("supplemental SourceTask requires a selected contract primitive")
    routed: list[str] = []
    for family in task.preferred_source_classes:
        routed.extend(_router_source_classes(family))
    routed = list(dict.fromkeys(routed))
    official = [value for value in routed if value not in _GENERAL_WEB_SOURCE_CLASSES]
    external = [value for value in routed if value in _GENERAL_WEB_SOURCE_CLASSES]
    if official:
        # Mixed requests remain official-first.  General web is a later,
        # explicit fallback, not a companion to an official-solvable attempt.
        routed = official
        general = False
    elif external and task.general_search_allowed:
        routed = external
        general = True
    elif external:
        # A conceptual source such as CUSTOMER_OFFICIAL has no direct connector.
        # Do not silently widen it to general web without an official-gap lineage.
        routed = []
        general = False
    else:
        general = False
    if not routed:
        routed = list(task.preferred_source_classes)
    return replace(
        task,
        primitive_gap=selected_primitive_id,
        preferred_source_classes=tuple(routed),
        query_intents=queries,
        general_search_allowed=general,
    )


def _archive_prior_supplemental_attempt(
    *,
    supplemental_root: Path,
    receipt: Mapping[str, Any],
) -> None:
    identity = str(receipt.get("task_result_hash") or canonical_hash(receipt))
    archive_root = supplemental_root / "attempts" / identity
    archived_receipt = archive_root / "supplemental_execution_receipt.json"
    receipt_payload = canonical_json(receipt) + "\n"
    if archived_receipt.is_file():
        if archived_receipt.read_text(encoding="utf-8") != receipt_payload:
            raise ValueError("archived supplemental receipt identity collision")
    else:
        _write_atomic(archived_receipt, receipt_payload)
    for name in (
        "task_executions.jsonl",
        "dossier_facts.jsonl",
        "evidence_facts.jsonl",
        "claim_fact_links.jsonl",
        "source_verifications.jsonl",
    ):
        source = supplemental_root / name
        destination = archive_root / name
        if not source.is_file():
            continue
        payload = source.read_text(encoding="utf-8")
        if destination.is_file():
            if destination.read_text(encoding="utf-8") != payload:
                raise ValueError("archived supplemental artifact identity collision")
            continue
        _write_atomic(destination, payload)


def _router_source_classes(family: str) -> tuple[str, ...]:
    return route_source_classes(family)


def _compile_bundle_evidence(
    *,
    job: ProResearchJob,
    gap_decision: Mapping[str, Any],
    execution: Any,
    bundle: EvidenceOSExecutionBundleV4,
    job_root: Path,
) -> tuple[
    tuple[Mapping[str, Any], ...],
    tuple[Mapping[str, Any], ...],
    tuple[Mapping[str, Any], ...],
    tuple[Mapping[str, Any], ...],
    tuple[tuple[str, str], ...],
]:
    direct_ids = set(execution.direct_accepted_claim_ids)
    key = gap_decision.get("key") or {}
    affected = tuple(str(value) for value in key.get("affected_component_ids") or ())
    accepted_rows: list[Mapping[str, Any]] = []
    dossier_rows: list[Mapping[str, Any]] = []
    verification_by_claim: dict[str, Mapping[str, Any]] = {}
    pages: list[tuple[str, str]] = []
    mapping_by_claim = {
        mapping.claim_id: mapping
        for mapping in bundle.ledger.mappings.values()
        if mapping.mapping_status == MappingStatus.ACCEPTED
    }
    for claim_id in sorted(direct_ids):
        claim = bundle.ledger.claims.get(claim_id)
        raw = bundle.raw_assertions.get(claim.raw_assertion_id) if claim else None
        mapping = mapping_by_claim.get(claim_id)
        document = bundle.documents.get(claim.source_document_id) if claim else None
        anchor = bundle.anchors.get(claim.source_anchor_id) if claim else None
        if None in (claim, raw, mapping, document, anchor):
            continue
        direction = {
            SupportDirection.SUPPORT: "POSITIVE",
            SupportDirection.COUNTER: "COUNTER",
            SupportDirection.RESOLUTION: "RESOLUTION",
        }.get(mapping.support_direction)
        if direction is None:
            continue
        period = (
            str(raw.effective_period_text or "").strip()
            or (claim.effective_start.isoformat() if claim.effective_start else "")
            or (claim.event_date.isoformat() if claim.event_date else "")
            or job.as_of_date
        )
        source_group = str(document.source_lineage_id or document.document_id)
        accepted_rows.append(
            {
                "claim_id": claim_id,
                "accepted_by_evidence_os": True,
                "material": True,
                "target_id": job.symbol,
                "as_of_date": job.as_of_date,
                "subject": str(claim.subject_entity_id),
                "business_segment": "",
                "product_family": "",
                "economic_mechanism": str(key.get("economic_mechanism_id") or mapping.primitive_id),
                "predicate": str(raw.predicate),
                "value": raw.value if raw.value is not None else raw.object_text,
                "unit": raw.unit,
                "period": period,
                "direction": direction,
                "current_lifecycle": "CURRENT",
                "source_ids": [document.document_id],
                "quote_ids": [anchor.anchor_id],
                "source_independence_group": source_group,
                "confidence": 0.5,
                "primitive_tags": [mapping.primitive_id],
                "allowed_component_ids": list(affected),
                "structured_evidence_roles": ["SUPPLEMENTAL_MATERIAL_GAP"],
            }
        )
        dossier_fact_id = stable_id(
            "PROSUPFACT",
            {"job_id": job.job_id, "claim_id": claim_id, "gap_key": gap_decision.get("evidence_gap_key")},
        )
        published = document.published_date()
        dossier_row = {
            "dossier_fact_id": dossier_fact_id,
            "statement": str(raw.object_text or raw.exact_quote),
            "direction": direction,
            "subject": str(claim.subject_entity_id),
            "target_id": job.symbol,
            "issuer_scoped": True,
            "business_segment": "",
            "product_family": "",
            "economic_mechanism": str(key.get("economic_mechanism_id") or mapping.primitive_id),
            "predicate": str(raw.predicate),
            "value": raw.value if raw.value is not None else raw.object_text,
            "unit": raw.unit,
            "period": period,
            "event_date": claim.event_date.isoformat() if claim.event_date else job.as_of_date,
            "current_status": "CURRENT",
            "candidate_components": list(affected),
            "source_url": str(document.canonical_url or ""),
            "source_title": "supplemental material-gap source",
            "source_publisher": str(document.source_name or ""),
            "published_at": published.isoformat() if published else job.as_of_date,
            "supporting_excerpt": str(raw.exact_quote or anchor.exact_text),
            "confidence": 0.5,
            "origin": "PRO_SUPPLEMENTAL_MATERIAL_GAP",
        }
        dossier_rows.append(dossier_row)
        text = str(bundle.document_text_by_id.get(document.document_id) or "")
        relative = f"supplemental/source_pages/{document.document_id}.txt"
        pages.append((relative, text))
        verification_by_claim[claim_id] = {
            "dossier_fact_id": dossier_fact_id,
            "status": {
                "POSITIVE": "ACCEPTED_CURRENT",
                "COUNTER": "ACCEPTED_COUNTER",
                "RESOLUTION": "ACCEPTED_RESOLUTION",
            }[direction],
            "reason": "Evidence OS accepted bounded supplemental source",
            "source_url": str(document.canonical_url or ""),
            "source_id": document.document_id,
            "content_hash": document.content_hash,
            "document_path": relative,
            "full_document": True,
            "cache_reused": False,
            "effective_published_at": published.isoformat() if published else None,
            "quote_match_mode": "EVIDENCE_OS_ANCHOR_VERIFIED",
            "target_scope_status": str(claim.target_scope_status.value),
            "proposed_component_ids": list(affected),
            "allowed_component_ids": list(affected),
            "component_rejection_reasons": [],
            "compiled_claim_id": claim_id,
            "origin": "PRO_SUPPLEMENTAL_MATERIAL_GAP",
        }
    compilation = EvidenceFactCompiler().compile(
        target_id=job.symbol,
        as_of_date=job.as_of_date,
        accepted_claims=accepted_rows,
    )
    if not compilation.fact_graph_ready:
        return (), (), (), (), tuple(pages)
    return (
        tuple(dossier_rows),
        tuple(row.to_dict() for row in compilation.facts),
        tuple(row.to_dict() for row in compilation.claim_fact_links),
        tuple(
            verification_by_claim[row.claim_id]
            for row in compilation.claim_fact_links
            if row.claim_id in verification_by_claim
        ),
        tuple(pages),
    )


def _fact_context_text(row: Mapping[str, Any]) -> str:
    values = (
        row.get("subject"),
        row.get("business_segment"),
        row.get("product_family"),
        row.get("economic_mechanism"),
        row.get("predicate"),
        row.get("value"),
        row.get("period"),
        row.get("direction"),
    )
    return " | ".join(str(value) for value in values if str(value or "").strip())[:1000]


def _write_source_pages(
    supplemental_root: Path,
    results: Sequence[SupplementalTaskResult],
) -> None:
    for result in results:
        for relative, text in result.source_pages:
            path = (supplemental_root.parent / relative).resolve()
            allowed_root = supplemental_root.resolve()
            if path != allowed_root and allowed_root not in path.parents:
                raise ValueError("supplemental source page path escapes the job root")
            _write_atomic(path, text)


def _read_json(path: Path) -> Mapping[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        raise ValueError(f"expected JSON object: {path}")
    return payload


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    if not path.is_file():
        return ()
    return tuple(
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    )


def _write_json_atomic(path: Path, payload: Mapping[str, Any]) -> None:
    _write_atomic(path, canonical_json(payload) + "\n")


def _write_jsonl_atomic(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    _write_atomic(path, "".join(canonical_json(row) + "\n" for row in rows))


def _write_atomic(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    part = path.with_suffix(path.suffix + ".part")
    with part.open("w", encoding="utf-8") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(part, path)
    fsync_directory(path.parent)


__all__ = [
    "CodexBoundedSupplementalExecutor",
    "ProSupplementalResearchService",
    "SupplementalResearchRun",
    "SupplementalTaskExecutor",
    "SupplementalTaskResult",
    "load_effective_dossier_facts",
    "load_effective_verified_evidence",
    "resolved_supplemental_gap_keys",
]
