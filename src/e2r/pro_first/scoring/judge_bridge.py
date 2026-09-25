"""Twenty-one evidence-only component judges with no search capability."""

from __future__ import annotations

from dataclasses import dataclass
import json
import os
from pathlib import Path
from typing import Any, Mapping, Protocol, Sequence

from e2r.research_brain.researcher_mode.schemas import (
    CANONICAL_COMPONENT_ORDER,
    ComponentAnchor,
    ComponentJudgeDecision,
    ComponentJudgeRole,
    ComponentResearchMemo,
    EvidenceFact,
)

from ..ids import canonical_hash, stable_id
from ..atomic_io import fsync_directory


PASS_BY_ROLE = {
    ComponentJudgeRole.ANALYST.value: "COMPONENT_ANALYST_JUDGE",
    ComponentJudgeRole.SKEPTIC.value: "COMPONENT_SKEPTIC_JUDGE",
    ComponentJudgeRole.CALIBRATION_JUDGE.value: "CALIBRATION_JUDGE",
}

_JUDGE_PROVIDER_SEMANTICS = "e2r_pro_evidence_only_judge_v2"


class EvidenceOnlyJudgeProvider(Protocol):
    provider_name: str

    def judge(self, request: Mapping[str, Any]) -> Mapping[str, Any]: ...


@dataclass(frozen=True)
class JudgeCallReceipt:
    judge_call_id: str
    component_id: str
    role: str
    prompt_hash: str
    response_hash: str | None
    provider_name: str
    status: str
    error: str | None = None
    provider_called: bool = True
    response_reused: bool = False

    def to_dict(self) -> Mapping[str, Any]:
        return {
            **self.__dict__,
            "mode": "EVIDENCE_ONLY_NO_SEARCH",
            "query_count": 0,
            "fetch_count": 0,
            "web_search_allowed": False,
            "source_fetch_allowed": False,
            "production_total_score_authority": False,
            "production_stage_authority": False,
        }


@dataclass(frozen=True)
class JudgeBridgeResult:
    status: str
    decisions: tuple[ComponentJudgeDecision, ...]
    call_receipts: tuple[JudgeCallReceipt, ...]
    pending_reasons: tuple[str, ...]

    @property
    def score_valid(self) -> bool:
        return self.status == "JUDGING_COMPLETE" and len(self.decisions) == 21

    @property
    def receipt_payload(self) -> Mapping[str, Any]:
        return {
            "schema_version": "e2r_pro_judge_bridge_receipt_v1",
            "status": self.status,
            "judge_decision_count": len(self.decisions),
            "judge_call_count": len(self.call_receipts),
            "provider_call_count": sum(
                row.provider_called for row in self.call_receipts
            ),
            "provider_response_reuse_count": sum(
                row.response_reused for row in self.call_receipts
            ),
            "expected_judge_count": 21,
            "pending_reasons": list(self.pending_reasons),
            "mode": "EVIDENCE_ONLY_NO_SEARCH",
            "query_count": 0,
            "fetch_count": 0,
            "web_search_allowed": False,
            "source_fetch_allowed": False,
            "score_valid": self.score_valid,
            "production_total_score_authority": False,
            "production_stage_authority": False,
        }


class ProEvidenceOnlyJudgeBridge:
    def __init__(self, provider: EvidenceOnlyJudgeProvider | None) -> None:
        self.provider = provider

    def run(
        self,
        *,
        memos: Sequence[ComponentResearchMemo],
        evidence_facts: Sequence[EvidenceFact],
        historical_anchors: Sequence[ComponentAnchor | Mapping[str, Any]],
        gap_decisions: Sequence[Mapping[str, Any]],
        component_ids: Sequence[str] | None = None,
        response_cache_root: str | Path | None = None,
    ) -> JudgeBridgeResult:
        if self.provider is None:
            return JudgeBridgeResult(
                status="JUDGING_PROVIDER_PENDING",
                decisions=(),
                call_receipts=(),
                pending_reasons=("JUDGE_PROVIDER_UNAVAILABLE",),
            )
        by_component = {row.component_id: row for row in memos}
        if set(by_component) != set(CANONICAL_COMPONENT_ORDER) or len(memos) != 7:
            raise ValueError("judge bridge requires exactly seven component memos")
        selected_components = (
            tuple(CANONICAL_COMPONENT_ORDER)
            if component_ids is None
            else tuple(dict.fromkeys(str(value) for value in component_ids))
        )
        if not selected_components or not set(selected_components).issubset(
            CANONICAL_COMPONENT_ORDER
        ):
            raise ValueError("judge bridge component subset is invalid")
        fact_by_id = {row.fact_id: row for row in evidence_facts}
        anchor_by_id = {
            _anchor_id(row): _anchor_dict(row)
            for row in historical_anchors
            if _anchor_id(row)
        }
        cache_root = (
            Path(response_cache_root).resolve()
            if response_cache_root is not None
            else None
        )
        decisions: list[ComponentJudgeDecision] = []
        receipts: list[JudgeCallReceipt] = []
        for component_id in CANONICAL_COMPONENT_ORDER:
            if component_id not in set(selected_components):
                continue
            memo = by_component[component_id]
            if not memo.research_complete:
                return JudgeBridgeResult(
                    status="JUDGING_PROVIDER_PENDING",
                    decisions=tuple(decisions),
                    call_receipts=tuple(receipts),
                    pending_reasons=(f"COMPONENT_RESEARCH_INCOMPLETE:{component_id}",),
                )
            memo_fact_ids = {
                *memo.positive_fact_ids,
                *memo.counter_fact_ids,
                *memo.resolution_fact_ids,
                *memo.context_fact_ids,
            }
            facts = [
                fact_by_id[fact_id].to_dict()
                for fact_id in sorted(memo_fact_ids)
                if fact_id in fact_by_id
            ]
            anchors = [
                anchor_by_id[anchor_id]
                for anchor_id in memo.historical_anchor_ids
                if anchor_id in anchor_by_id
            ]
            component_gaps = [
                dict(row)
                for row in gap_decisions
                if component_id
                in set(
                    ((row.get("assessment") or {}).get("affected_component_ids"))
                    or ()
                )
            ]
            for role in (
                ComponentJudgeRole.ANALYST.value,
                ComponentJudgeRole.SKEPTIC.value,
                ComponentJudgeRole.CALIBRATION_JUDGE.value,
            ):
                request = {
                    "schema_version": "e2r_pro_evidence_only_judge_request_v1",
                    "provider_semantics": _JUDGE_PROVIDER_SEMANTICS,
                    "mode": "EVIDENCE_ONLY_NO_SEARCH",
                    "role": role,
                    "component_memo": memo.to_dict(),
                    "verified_facts": facts,
                    "historical_anchors": anchors,
                    "gap_dispositions": component_gaps,
                    "forbidden_inputs": [
                        "WEB_SEARCH",
                        "SOURCE_FETCH",
                        "TOTAL_SCORE",
                        "CANONICAL_STAGE",
                    ],
                    "production_total_score_authority": False,
                    "production_stage_authority": False,
                }
                prompt_hash = canonical_hash(request)
                judge_call_id = stable_id(
                    "PROJUDGECALL",
                    {
                        "memo_id": memo.memo_id,
                        "role": role,
                        "prompt_hash": prompt_hash,
                    },
                )
                response_hash = None
                response_reused = False
                provider_called = False
                try:
                    response = _read_cached_judge_response(
                        cache_root=cache_root,
                        judge_call_id=judge_call_id,
                        prompt_hash=prompt_hash,
                    )
                    if response is not None:
                        response_hash = canonical_hash(response)
                        try:
                            decision = self._decision(
                                response=response,
                                memo=memo,
                                role=role,
                                judge_call_id=judge_call_id,
                                prompt_hash=prompt_hash,
                                response_hash=response_hash,
                            )
                        except (KeyError, TypeError, ValueError):
                            _quarantine_invalid_judge_response(
                                cache_root=cache_root,
                                judge_call_id=judge_call_id,
                                response_hash=response_hash,
                            )
                            response = None
                            response_hash = None
                        else:
                            response_reused = True
                    if response is None:
                        provider_called = True
                        response = dict(self.provider.judge(request))
                        response_hash = canonical_hash(response)
                        decision = self._decision(
                            response=response,
                            memo=memo,
                            role=role,
                            judge_call_id=judge_call_id,
                            prompt_hash=prompt_hash,
                            response_hash=response_hash,
                        )
                        _write_cached_judge_response(
                            cache_root=cache_root,
                            judge_call_id=judge_call_id,
                            prompt_hash=prompt_hash,
                            response_hash=response_hash,
                            provider_name=str(
                                getattr(
                                    self.provider,
                                    "provider_name",
                                    "UNKNOWN",
                                )
                            ),
                            response=response,
                        )
                except Exception as error:
                    receipts.append(
                        JudgeCallReceipt(
                            judge_call_id=judge_call_id,
                            component_id=component_id,
                            role=role,
                            prompt_hash=prompt_hash,
                            response_hash=response_hash,
                            provider_name=str(
                                getattr(self.provider, "provider_name", "UNKNOWN")
                            ),
                            status=(
                                "PROVIDER_ERROR"
                                if response_hash is None
                                else "RESPONSE_INVALID"
                            ),
                            error=f"{type(error).__name__}: {error}",
                            provider_called=provider_called,
                            response_reused=response_reused,
                        )
                    )
                    return JudgeBridgeResult(
                        status="JUDGING_PROVIDER_PENDING",
                        decisions=tuple(decisions),
                        call_receipts=tuple(receipts),
                        pending_reasons=(
                            f"JUDGE_PROVIDER_ERROR:{component_id}:{role}",
                        ),
                    )
                decisions.append(decision)
                receipts.append(
                    JudgeCallReceipt(
                        judge_call_id=judge_call_id,
                        component_id=component_id,
                        role=role,
                        prompt_hash=prompt_hash,
                        response_hash=response_hash,
                        provider_name=decision.provider_name,
                        status=(
                            "REUSED_COMPLETE"
                            if response_reused
                            else "COMPLETE"
                        ),
                        provider_called=provider_called,
                        response_reused=response_reused,
                    )
                )
        return JudgeBridgeResult(
            status=(
                "JUDGING_COMPLETE"
                if len(selected_components) == 7
                else "JUDGING_PARTIAL_COMPLETE"
            ),
            decisions=tuple(decisions),
            call_receipts=tuple(receipts),
            pending_reasons=(),
        )

    def _decision(
        self,
        *,
        response: Mapping[str, Any],
        memo: ComponentResearchMemo,
        role: str,
        judge_call_id: str,
        prompt_hash: str,
        response_hash: str,
    ) -> ComponentJudgeDecision:
        support_ids = tuple(str(value) for value in response.get("support_fact_ids") or ())
        counter_ids = tuple(str(value) for value in response.get("counter_fact_ids") or ())
        if not set(support_ids).issubset(memo.positive_fact_ids):
            raise ValueError("judge support facts are outside the verified memo")
        if not set(counter_ids).issubset(memo.counter_fact_ids):
            raise ValueError("judge counter facts are outside the verified memo")
        nearest = tuple(str(value) for value in response.get("nearest_anchor_ids") or ())
        if not set(nearest).issubset(memo.historical_anchor_ids):
            raise ValueError("judge anchor is outside the memo anchor roster")
        comparisons = tuple(
            str(value) for value in response.get("anchor_comparisons") or ()
        )
        if memo.historical_anchor_ids and (not nearest or not comparisons):
            raise ValueError(
                "judge must compare a supplied historical anchor when one exists"
            )
        proposed = float(response.get("proposed_points", 0.0))
        allowed = tuple(
            float(value)
            for value in response.get("allowed_range")
            or (proposed, proposed)
        )
        if (
            len(allowed) != 2
            or not 0 <= allowed[0] <= proposed <= allowed[1]
            or allowed[1] > memo.component_max_points
        ):
            raise ValueError("judge points or allowed range exceed the component contract")
        judge_id = stable_id(
            "PROJUDGE",
            {
                "judge_call_id": judge_call_id,
                "response_hash": response_hash,
            },
        )
        return ComponentJudgeDecision(
            judge_id=judge_id,
            judge_call_id=judge_call_id,
            memo_id=memo.memo_id,
            component_id=memo.component_id,
            component_max_points=memo.component_max_points,
            role=role,
            pass_name=PASS_BY_ROLE[role],
            prompt_hash=prompt_hash,
            response_hash=response_hash,
            provider_name=str(getattr(self.provider, "provider_name", "UNKNOWN")),
            anchor_comparisons=comparisons,
            proposed_points=proposed,
            allowed_range=allowed,  # type: ignore[arg-type]
            rationale=str(response.get("rationale") or "").strip(),
            disagreements=tuple(
                str(value) for value in response.get("disagreements") or ()
            ),
            support_fact_ids=support_ids,
            counter_fact_ids=counter_ids,
            nearest_anchor_ids=nearest,
            why_not_higher=str(response.get("why_not_higher") or "").strip(),
            why_not_lower=str(response.get("why_not_lower") or "").strip(),
        )


def _anchor_id(row: ComponentAnchor | Mapping[str, Any]) -> str:
    return str(row.anchor_id if isinstance(row, ComponentAnchor) else row.get("anchor_id") or "")


def _anchor_dict(row: ComponentAnchor | Mapping[str, Any]) -> Mapping[str, Any]:
    return row.to_dict() if isinstance(row, ComponentAnchor) else dict(row)


def _read_cached_judge_response(
    *,
    cache_root: Path | None,
    judge_call_id: str,
    prompt_hash: str,
) -> Mapping[str, Any] | None:
    if cache_root is None:
        return None
    path = cache_root / f"{judge_call_id}.json"
    if not path.is_file():
        return None
    payload = json.loads(path.read_text(encoding="utf-8"))
    response = payload.get("response")
    if (
        payload.get("judge_call_id") != judge_call_id
        or payload.get("prompt_hash") != prompt_hash
        or not isinstance(response, Mapping)
        or payload.get("response_hash") != canonical_hash(response)
    ):
        raise ValueError("durable Judge response cache failed hash validation")
    return dict(response)


def _write_cached_judge_response(
    *,
    cache_root: Path | None,
    judge_call_id: str,
    prompt_hash: str,
    response_hash: str,
    provider_name: str,
    response: Mapping[str, Any],
) -> None:
    if cache_root is None:
        return
    cache_root.mkdir(parents=True, exist_ok=True)
    path = cache_root / f"{judge_call_id}.json"
    part = path.with_suffix(".json.part")
    payload = {
        "schema_version": "e2r_pro_judge_response_cache_v1",
        "judge_call_id": judge_call_id,
        "prompt_hash": prompt_hash,
        "response_hash": response_hash,
        "provider_name": provider_name,
        "provider_original_call_count": 1,
        "query_count": 0,
        "fetch_count": 0,
        "response": response,
    }
    with part.open("w", encoding="utf-8") as stream:
        stream.write(json.dumps(payload, ensure_ascii=False, sort_keys=True))
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(part, path)
    fsync_directory(path.parent)


def _quarantine_invalid_judge_response(
    *,
    cache_root: Path | None,
    judge_call_id: str,
    response_hash: str,
) -> None:
    if cache_root is None:
        return
    source = cache_root / f"{judge_call_id}.json"
    if not source.is_file():
        return
    destination_root = cache_root / "invalid"
    destination_root.mkdir(parents=True, exist_ok=True)
    destination = destination_root / f"{judge_call_id}.{response_hash}.json"
    os.replace(source, destination)
    fsync_directory(destination_root)
    fsync_directory(cache_root)


__all__ = [
    "EvidenceOnlyJudgeProvider",
    "JudgeBridgeResult",
    "JudgeCallReceipt",
    "ProEvidenceOnlyJudgeBridge",
]
