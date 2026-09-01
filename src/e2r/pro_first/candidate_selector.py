"""Blind-safe selector from the existing Korea cheap scan into the Pro queue."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Mapping, Sequence

from e2r.cheap_scan.korea_scanner import KoreaCheapScanResult
from e2r.cheap_scan.models import CheapScanCandidate, RecommendedNextLayer
from e2r.research_brain.candidate_context import candidate_event_from_mapping

from .ids import canonical_hash, stable_id
from .job_store import ProFirstJobStore
from .models import (
    CandidateRecord,
    CandidateSelectionReceipt,
    ProResearchJob,
    ResearchMode,
    ScanWindow,
)


ArchetypeResolver = Callable[[CheapScanCandidate], Sequence[str]]


@dataclass(frozen=True)
class ExistingDossierContext:
    dossier_id: str | None = None
    materially_stale: bool = False
    last_trigger_fingerprint: str | None = None
    last_source_delta_hash: str | None = None
    current_source_delta_hash: str | None = None
    force_validation_canary: bool = False


@dataclass(frozen=True)
class CandidateObservation:
    candidate: CheapScanCandidate
    scan_window: ScanWindow
    scan_run_id: str | None = None


@dataclass(frozen=True)
class SelectedProCandidate:
    candidate_id: str
    source_candidate: CheapScanCandidate
    scan_window: ScanWindow
    scan_run_id: str | None
    trigger_fingerprint: str
    research_mode: ResearchMode
    receipt: CandidateSelectionReceipt


@dataclass(frozen=True)
class CandidateSelectionBatch:
    selected: tuple[SelectedProCandidate, ...]
    rejection_counts: Mapping[str, int]


@dataclass(frozen=True)
class EnqueuedProCandidate:
    candidate: CandidateRecord
    job: ProResearchJob
    created: bool


class ProCandidateSelector:
    """Select only genuine production DEEP_RESEARCH candidates.

    The selector receives no full-E2R score or final Stage input by design. The
    cheap-scan score is retained only as queue priority metadata.
    """

    def __init__(
        self,
        *,
        archetype_resolver: ArchetypeResolver | None = None,
    ) -> None:
        self._archetype_resolver = archetype_resolver or (lambda _candidate: ())

    def select_result(
        self,
        result: KoreaCheapScanResult,
        *,
        scan_window: str | ScanWindow,
        scan_run_id: str | None = None,
        existing_by_symbol: Mapping[str, ExistingDossierContext] | None = None,
    ) -> CandidateSelectionBatch:
        if any(candidate.as_of_date != result.as_of_date for candidate in result.candidates):
            raise ValueError("cheap scan result contains a mismatched as_of_date")
        observations = tuple(
            CandidateObservation(
                candidate=candidate,
                scan_window=ScanWindow(scan_window),
                scan_run_id=scan_run_id,
            )
            for candidate in result.candidates
        )
        return self.select_observations(
            observations,
            existing_by_symbol=existing_by_symbol,
        )

    def select_observations(
        self,
        observations: Sequence[CandidateObservation],
        *,
        existing_by_symbol: Mapping[str, ExistingDossierContext] | None = None,
    ) -> CandidateSelectionBatch:
        existing_by_symbol = existing_by_symbol or {}
        rejection_counts: dict[str, int] = {}
        eligible: list[CandidateObservation] = []
        for observation in observations:
            candidate = observation.candidate
            rejection = self._rejection_reason(candidate)
            if rejection:
                rejection_counts[rejection] = rejection_counts.get(rejection, 0) + 1
                continue
            eligible.append(observation)

        grouped: dict[tuple[str, str], list[CandidateObservation]] = {}
        for observation in eligible:
            key = (observation.candidate.symbol, observation.candidate.as_of_date.isoformat())
            grouped.setdefault(key, []).append(observation)

        selected: list[SelectedProCandidate] = []
        for key in sorted(grouped):
            group = grouped[key]
            merged = self._merge_candidates(group)
            context = existing_by_symbol.get(merged.symbol, ExistingDossierContext())
            trigger_ids = self._trigger_ids(group)
            trigger_fingerprint = canonical_hash(
                {
                    "symbol": merged.symbol,
                    "as_of_date": merged.as_of_date.isoformat(),
                    "trigger_ids": trigger_ids,
                    "reason_codes": sorted(merged.reason_codes),
                    "evidence_ids": sorted(merged.evidence_ids),
                }
            )
            mode = self._research_mode(context)
            if self._no_material_delta(context, trigger_fingerprint, mode):
                rejection_counts["NO_MATERIAL_DELTA"] = (
                    rejection_counts.get("NO_MATERIAL_DELTA", 0) + 1
                )
                continue
            scan_window = self._merged_window(group)
            scan_run_id = self._merged_scan_run_id(group, scan_window)
            dedupe_identity = {
                "symbol": merged.symbol,
                "as_of_date": merged.as_of_date.isoformat(),
                "trigger_fingerprint": trigger_fingerprint,
                "research_mode": mode.value,
            }
            candidate_id = stable_id("PCAND", dedupe_identity)
            archetypes = tuple(
                sorted(
                    set(
                        archetype
                        for observation in group
                        for archetype in self._archetype_resolver(observation.candidate)
                    )
                )
            )
            receipt = CandidateSelectionReceipt(
                schema_version="e2r_pro_candidate_selection_v1",
                candidate_id=candidate_id,
                symbol=merged.symbol,
                company_name=merged.company_name,
                as_of_date=merged.as_of_date.isoformat(),
                scan_window=scan_window.value,
                trigger_ids=trigger_ids,
                reason_codes=merged.reason_codes,
                cheap_scan_total_score=merged.cheap_scan_total_score,
                candidate_archetypes=archetypes,
                existing_dossier_id=context.dossier_id,
                research_mode=mode.value,
                production_candidate=True,
                test_injected=False,
                final_score_visible_at_selection=False,
                final_stage_visible_at_selection=False,
            )
            selected.append(
                SelectedProCandidate(
                    candidate_id=candidate_id,
                    source_candidate=merged,
                    scan_window=scan_window,
                    scan_run_id=scan_run_id,
                    trigger_fingerprint=trigger_fingerprint,
                    research_mode=mode,
                    receipt=receipt,
                )
            )
        return CandidateSelectionBatch(
            selected=tuple(selected),
            rejection_counts=dict(sorted(rejection_counts.items())),
        )

    def enqueue(
        self,
        store: ProFirstJobStore,
        batch: CandidateSelectionBatch,
    ) -> tuple[EnqueuedProCandidate, ...]:
        enqueued: list[EnqueuedProCandidate] = []
        for selected in batch.selected:
            dedupe_key = canonical_hash(
                {
                    "symbol": selected.source_candidate.symbol,
                    "as_of_date": selected.source_candidate.as_of_date.isoformat(),
                    "trigger_fingerprint": selected.trigger_fingerprint,
                    "mode": selected.research_mode.value,
                }
            )
            candidate = store.create_candidate(
                candidate_id=selected.candidate_id,
                scan_run_id=selected.scan_run_id,
                symbol=selected.source_candidate.symbol,
                company_name=selected.source_candidate.company_name,
                as_of_date=selected.source_candidate.as_of_date.isoformat(),
                scan_window=selected.scan_window,
                trigger_fingerprint=selected.trigger_fingerprint,
                research_mode=selected.research_mode,
                dedupe_key=dedupe_key,
                selection_receipt=selected.receipt.to_dict(),
            )
            job = store.get_job_by_candidate(candidate.candidate_id)
            job_created = job is None
            if job is None:
                job = store.create_job(
                    candidate.candidate_id,
                    priority=int(round(selected.source_candidate.cheap_scan_total_score * 100)),
                    archetype_ids=selected.receipt.candidate_archetypes,
                )
            enqueued.append(
                EnqueuedProCandidate(candidate=candidate, job=job, created=job_created)
            )
        return tuple(enqueued)

    @staticmethod
    def _rejection_reason(candidate: CheapScanCandidate) -> str | None:
        if candidate.test_injected:
            return "TEST_INJECTED"
        if not candidate.production_candidate:
            return "NOT_PRODUCTION_CANDIDATE"
        if candidate.recommended_next_layer is RecommendedNextLayer.EVENT_SEARCH:
            return "EVENT_SEARCH_NOT_DIRECTLY_PROMOTED"
        if candidate.recommended_next_layer is not RecommendedNextLayer.DEEP_RESEARCH:
            return "NOT_DEEP_RESEARCH"
        return None

    @staticmethod
    def _research_mode(context: ExistingDossierContext) -> ResearchMode:
        if context.force_validation_canary:
            return ResearchMode.FORCED_VALIDATION_CANARY
        if context.dossier_id and not context.materially_stale:
            return ResearchMode.DELTA_RESEARCH
        return ResearchMode.FULL_RESEARCH

    @staticmethod
    def _no_material_delta(
        context: ExistingDossierContext,
        trigger_fingerprint: str,
        mode: ResearchMode,
    ) -> bool:
        if mode is not ResearchMode.DELTA_RESEARCH:
            return False
        if context.last_trigger_fingerprint == trigger_fingerprint:
            return True
        return bool(
            context.last_source_delta_hash
            and context.current_source_delta_hash
            and context.last_source_delta_hash == context.current_source_delta_hash
        )

    @staticmethod
    def _trigger_ids(group: Sequence[CandidateObservation]) -> tuple[str, ...]:
        trigger_ids: list[str] = []
        for observation in group:
            candidate = observation.candidate
            event = candidate_event_from_mapping(
                {
                    "symbol": candidate.symbol,
                    "company_name": candidate.company_name,
                    "as_of_date": candidate.as_of_date.isoformat(),
                    "reason_codes": candidate.reason_codes,
                    "candidate_source_path": candidate.candidate_source_path,
                    "evidence_ids": candidate.evidence_ids,
                    "cheap_scan_total_score": candidate.cheap_scan_total_score,
                },
                as_of_date=candidate.as_of_date,
            )
            trigger_ids.append(event.candidate_event_id)
        return tuple(sorted(set(trigger_ids)))

    @staticmethod
    def _merged_window(group: Sequence[CandidateObservation]) -> ScanWindow:
        if any(item.scan_window is ScanWindow.EVENING for item in group):
            return ScanWindow.EVENING
        return ScanWindow.MORNING

    @staticmethod
    def _merged_scan_run_id(
        group: Sequence[CandidateObservation], selected_window: ScanWindow
    ) -> str | None:
        for observation in reversed(group):
            if observation.scan_window is selected_window and observation.scan_run_id:
                return observation.scan_run_id
        return next((item.scan_run_id for item in group if item.scan_run_id), None)

    @staticmethod
    def _merge_candidates(group: Sequence[CandidateObservation]) -> CheapScanCandidate:
        ranked = sorted(
            (item.candidate for item in group),
            key=lambda item: (-item.cheap_scan_total_score, item.symbol),
        )
        representative = ranked[0]
        return CheapScanCandidate(
            symbol=representative.symbol,
            company_name=representative.company_name,
            market=representative.market,
            as_of_date=representative.as_of_date,
            reason_codes=tuple(
                sorted({code for item in group for code in item.candidate.reason_codes})
            ),
            price_event_score=max(item.candidate.price_event_score for item in group),
            disclosure_event_score=max(
                item.candidate.disclosure_event_score for item in group
            ),
            financial_event_score=max(
                item.candidate.financial_event_score for item in group
            ),
            risk_event_score=max(item.candidate.risk_event_score for item in group),
            cheap_scan_total_score=max(
                item.candidate.cheap_scan_total_score for item in group
            ),
            evidence_ids=tuple(
                sorted({evidence for item in group for evidence in item.candidate.evidence_ids})
            ),
            recommended_next_layer=RecommendedNextLayer.DEEP_RESEARCH,
            candidate_source_path=representative.candidate_source_path,
            test_injected=False,
            production_candidate=True,
        )


__all__ = [
    "CandidateObservation",
    "CandidateSelectionBatch",
    "EnqueuedProCandidate",
    "ExistingDossierContext",
    "ProCandidateSelector",
    "SelectedProCandidate",
]
