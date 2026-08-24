"""Compile grouped compact repair prompts without replaying a full dossier."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from ..ids import canonical_hash, stable_id
from .models_v3 import (
    CompactRepairGroupV3,
    CompiledCompactRepairPromptV3,
    PRO_REPAIRABLE_ROOT_CAUSES,
    REPAIR_ACTION_CONTRACT,
)


COMPACT_REPAIR_TEMPLATE = "e2r_pro_v3_compact_verifier_repair.md"
TARGET_REPAIR_PROMPT_CHARS = 60_000
HARD_MAX_REPAIR_PROMPT_CHARS = 100_000
DEFAULT_GROUP_SOURCE_TEXT_CHARS = 12_000


class CompactRepairPromptCompilerV3:
    def __init__(
        self,
        *,
        template_path: str | Path | None = None,
        schema_path: str | Path | None = None,
    ) -> None:
        repo_root = Path(__file__).resolve().parents[4]
        self.template_path = (
            Path(template_path).resolve()
            if template_path
            else repo_root / "configs/prompts" / COMPACT_REPAIR_TEMPLATE
        )
        self.schema_path = (
            Path(schema_path).resolve()
            if schema_path
            else repo_root / "configs/e2r_pro_repair_delta_v3.schema.json"
        )

    def compile(
        self,
        *,
        dossier: Mapping[str, Any],
        rejection_classifications: Sequence[Mapping[str, Any]],
        verification_rows: Sequence[Mapping[str, Any]],
        job_root: str | Path,
        research_pass_id: str,
        parent_pass_id: str,
        repair_pass_ordinal: int = 1,
        maximum_group_source_text_chars: int = DEFAULT_GROUP_SOURCE_TEXT_CHARS,
    ) -> CompiledCompactRepairPromptV3:
        if dossier.get("schema_version") != "e2r_pro_research_dossier_v3":
            raise ValueError("compact RepairDeltaV3 requires ResearchDossierV3")
        if repair_pass_ordinal != 1:
            raise ValueError("SECOND_REPAIR_PASS_BLOCKS_OPERATIONAL_READY")
        if not research_pass_id or not parent_pass_id:
            raise ValueError("compact repair requires pass and parent lineage")
        if maximum_group_source_text_chars < 512:
            raise ValueError("group source text bound is too small")

        facts = {
            str(row.get("dossier_fact_id") or ""): row
            for collection in ("material_facts", "counterfacts", "resolution_facts")
            for row in dossier.get(collection) or ()
        }
        sources = {
            str(row.get("source_document_id") or ""): row
            for row in dossier.get("source_documents") or ()
        }
        verification_by_candidate = {
            str(row.get("dossier_fact_id") or ""): row
            for row in verification_rows
        }
        repairable: list[Mapping[str, Any]] = []
        seen: set[str] = set()
        for row in rejection_classifications:
            candidate_id = str(row.get("candidate_id") or "")
            cause = str(row.get("cause_class") or "")
            sent_allowed = row.get("send_to_pro_allowed") is True
            if cause in {
                "LOCAL_NORMALIZABLE",
                "SOURCE_REPRESENTATION_RESOLVABLE",
            } and sent_allowed:
                raise ValueError("local/source-representation defect cannot route to Pro")
            if not sent_allowed:
                continue
            if cause not in PRO_REPAIRABLE_ROOT_CAUSES:
                raise ValueError("only initial-output or genuine defects may route to Pro")
            if row.get("material") is not True:
                raise ValueError("nonmaterial rejection cannot enter compact repair")
            if not candidate_id or candidate_id in seen:
                raise ValueError("compact repair candidate identity is missing or duplicated")
            if candidate_id not in facts:
                raise ValueError("compact repair classification references an unknown fact")
            seen.add(candidate_id)
            repairable.append(row)
        if not repairable:
            raise ValueError("no Pro-repairable rejection remains after local preflight")

        grouped: dict[tuple[str, str, tuple[str, ...]], list[Mapping[str, Any]]] = {}
        for classification in repairable:
            candidate_id = str(classification["candidate_id"])
            fact = facts[candidate_id]
            source_document_id = str(fact.get("source_document_id") or "")
            question_ids = tuple(
                sorted(str(value) for value in fact.get("question_family_ids") or ())
            )
            key = (
                source_document_id,
                str(classification["cause_class"]),
                question_ids,
            )
            grouped.setdefault(key, []).append(classification)

        root = Path(job_root).resolve()
        groups: list[CompactRepairGroupV3] = []
        for key in sorted(grouped):
            source_document_id, cause, question_ids = key
            source_document = sources.get(source_document_id)
            if source_document is None:
                raise ValueError("repair fact references an unknown source document")
            classifications = grouped[key]
            candidate_ids = tuple(
                sorted(str(row["candidate_id"]) for row in classifications)
            )
            source_text, source_text_hash = _load_group_source_text(
                root=root,
                candidate_ids=candidate_ids,
                verification_by_candidate=verification_by_candidate,
                maximum_chars=maximum_group_source_text_chars,
            )
            candidates: list[Mapping[str, Any]] = []
            classification_by_id = {
                str(row["candidate_id"]): row for row in classifications
            }
            for candidate_id in candidate_ids:
                fact = facts[candidate_id]
                classification = classification_by_id[candidate_id]
                verification = verification_by_candidate.get(candidate_id) or {}
                candidates.append(
                    {
                        "candidate_id": candidate_id,
                        "question_family_ids": list(question_ids),
                        "rejection_category": cause,
                        "rejection_code": classification.get("cause_code"),
                        "verifier_status": classification.get("verifier_status"),
                        "verifier_reason": verification.get("reason")
                        or classification.get("detail"),
                        "original_statement": fact.get("statement"),
                        "source_document_id": source_document_id,
                        "canonical_url": source_document.get("canonical_url"),
                        "fetched_excerpt": _literal_candidate_source_excerpt(
                            fact,
                            source_text,
                        ),
                        "allowed_action": REPAIR_ACTION_CONTRACT,
                        "original_atomic_fact": dict(fact),
                    }
                )
            group_id = stable_id(
                "PROREPAIRGROUP",
                {
                    "job_id": dossier.get("job_id"),
                    "source_document_id": source_document_id,
                    "cause": cause,
                    "question_ids": question_ids,
                    "candidate_ids": candidate_ids,
                },
            )
            groups.append(
                CompactRepairGroupV3(
                    group_id=group_id,
                    source_document_id=source_document_id,
                    rejection_category=cause,
                    question_family_ids=question_ids,
                    canonical_url=str(source_document.get("canonical_url") or ""),
                    fetched_source_text=source_text,
                    fetched_source_text_hash=source_text_hash,
                    candidates=tuple(candidates),
                )
            )

        schema = json.loads(self.schema_path.read_text(encoding="utf-8"))
        context = {
            "authority": {
                "schema_version": "e2r_compact_repair_prompt_context_v3",
                "job_id": dossier.get("job_id"),
                "run_id": dossier.get("run_id"),
                "research_pass_id": research_pass_id,
                "parent_pass_id": parent_pass_id,
                "target": dossier.get("target"),
                "as_of_date": dossier.get("as_of_date"),
                "repair_pass_ordinal": repair_pass_ordinal,
                "full_dossier_reoutput_allowed": False,
                "accepted_fact_deletion_allowed": False,
                "deterministic_reverification_required": True,
                "score_authority": False,
                "stage_authority": False,
            },
            "repair_groups": [row.to_prompt_dict() for row in groups],
            "output_schema": schema,
        }
        template = self.template_path.read_text(encoding="utf-8")
        if template.count("{{COMPILED_CONTEXT}}") != 1:
            raise ValueError("compact repair template requires one context slot")
        prompt = template.replace(
            "{{COMPILED_CONTEXT}}",
            "## Compact repair context\n\n```json\n"
            + json.dumps(context, ensure_ascii=False, indent=2, sort_keys=True)
            + "\n```",
        ).rstrip() + "\n"
        lineage_markers = "\n".join(
            (
                f"[[E2R_PRO_RUN_ID:{dossier.get('run_id')}]]",
                f"[[E2R_PRO_JOB_ID:{dossier.get('job_id')}]]",
                f"[[E2R_PRO_PASS_ID:{research_pass_id}]]",
                f"[[E2R_PRO_PARENT_PASS_ID:{parent_pass_id}]]",
            )
        )
        prompt = lineage_markers + "\n\n" + prompt
        if "{{" in prompt or "}}" in prompt:
            raise ValueError("compact repair prompt has an unresolved template variable")
        if len(prompt) > HARD_MAX_REPAIR_PROMPT_CHARS:
            raise ValueError(
                "COMPACT_REPAIR_PROMPT_HARD_LIMIT_EXCEEDED: classify/compress first"
            )
        candidate_ids = tuple(
            candidate_id for group in groups for candidate_id in group.candidate_ids
        )
        return CompiledCompactRepairPromptV3(
            job_id=str(dossier.get("job_id") or ""),
            run_id=str(dossier.get("run_id") or ""),
            research_pass_id=research_pass_id,
            parent_pass_id=parent_pass_id,
            target=dict(dossier.get("target") or {}),
            as_of_date=str(dossier.get("as_of_date") or ""),
            prompt_text=prompt,
            prompt_hash=canonical_hash({"prompt": prompt}),
            schema_hash=canonical_hash(schema),
            groups=tuple(groups),
            candidate_ids=candidate_ids,
            prompt_char_count=len(prompt),
            target_char_limit=TARGET_REPAIR_PROMPT_CHARS,
            hard_char_limit=HARD_MAX_REPAIR_PROMPT_CHARS,
            repair_pass_ordinal=repair_pass_ordinal,
        )


def _load_group_source_text(
    *,
    root: Path,
    candidate_ids: Sequence[str],
    verification_by_candidate: Mapping[str, Mapping[str, Any]],
    maximum_chars: int,
) -> tuple[str, str | None]:
    paths = {
        str((verification_by_candidate.get(candidate_id) or {}).get("document_path") or "")
        for candidate_id in candidate_ids
        if str((verification_by_candidate.get(candidate_id) or {}).get("document_path") or "")
    }
    hashes = {
        str((verification_by_candidate.get(candidate_id) or {}).get("content_hash") or "")
        for candidate_id in candidate_ids
        if str((verification_by_candidate.get(candidate_id) or {}).get("content_hash") or "")
    }
    if not paths:
        return "", None
    if len(paths) != 1 or len(hashes) != 1:
        raise ValueError("one repair source group resolved to conflicting documents")
    path = (root / next(iter(paths))).resolve()
    try:
        path.relative_to(root)
    except ValueError as error:
        raise ValueError("repair source document escapes the job root") from error
    payload = path.read_bytes()
    expected = next(iter(hashes))
    if hashlib.sha256(payload).hexdigest() != expected:
        raise ValueError("repair source document hash differs from verifier receipt")
    text = payload.decode("utf-8")
    if len(text) > maximum_chars:
        half = maximum_chars // 2
        text = (
            text[:half].rstrip()
            + "\n[...SOURCE_TEXT_COMPACTED...]\n"
            + text[-half:].lstrip()
        )
    return text, canonical_hash({"source_text": text})


def _literal_candidate_source_excerpt(
    fact: Mapping[str, Any], source_text: str
) -> str:
    """Return only a literal source span; never synthesize a semantic match."""

    if not source_text:
        return ""
    claimed = str(fact.get("supporting_excerpt") or "").strip()
    if claimed and claimed in source_text:
        return claimed
    locator = str(fact.get("source_locator") or "").strip()
    if not locator:
        return ""
    index = source_text.find(locator)
    if index < 0:
        return ""
    left_boundaries = [
        source_text.rfind(mark, 0, index) for mark in (".", "!", "?", "。")
    ]
    left = max(left_boundaries) + 1
    right_candidates = [
        position
        for mark in (".", "!", "?", "。")
        for position in (source_text.find(mark, index + len(locator)),)
        if position >= 0
    ]
    right = min(right_candidates) + 1 if right_candidates else len(source_text)
    excerpt = source_text[left:right].strip()
    return excerpt if len(excerpt) <= 600 else excerpt[:600].rstrip()


__all__ = [
    "COMPACT_REPAIR_TEMPLATE",
    "CompactRepairPromptCompilerV3",
    "DEFAULT_GROUP_SOURCE_TEXT_CHARS",
    "HARD_MAX_REPAIR_PROMPT_CHARS",
    "TARGET_REPAIR_PROMPT_CHARS",
]
