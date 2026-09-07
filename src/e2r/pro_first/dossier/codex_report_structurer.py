"""Codex-only structuring of a readable Pro report into ResearchDossierV3.

This is a dialect/representation recovery path, not a research or scoring
provider.  It may only copy claims, excerpts, URLs, and route information that
already exist in the captured Pro report.  Missing support remains an explicit
gap and all score/Stage authority stays false.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping, Protocol, Sequence

from e2r.research_brain.planning.provider_transport import (
    CodexStructuredProviderTransport,
)

from ..ids import canonical_hash, canonical_json


class StructuredReportTransport(Protocol):
    def complete(
        self,
        *,
        prompt: str,
        output_schema: Mapping[str, Any],
        schema_name: str,
    ) -> Any: ...


@dataclass(frozen=True)
class StructuredProReport:
    dossier: Mapping[str, Any]
    receipt: Mapping[str, Any]


class CodexProReportDossierStructurer:
    """Convert one completed marker-bound Pro report without new research."""

    provider_name = "CODEX_STRUCTURED_PRO_REPORT_TO_DOSSIER_V3"

    def __init__(
        self,
        transport: StructuredReportTransport,
        *,
        schema_path: str | Path,
    ) -> None:
        self.transport = transport
        self.schema_path = Path(schema_path).expanduser().resolve()
        self.validation_schema = json.loads(
            self.schema_path.read_text(encoding="utf-8")
        )
        if self.validation_schema.get("$id") is None:
            raise ValueError("ResearchDossierV3 schema must have a stable $id")
        # ResearchDossierV3 intentionally contains a few open metadata maps,
        # while OpenAI structured outputs require every object to be closed.
        # Keep the full tracked schema as the local authority and ask the
        # provider for one JSON string inside a minimal closed wrapper.
        self.output_schema = {
            "type": "object",
            "additionalProperties": False,
            "required": ["dossier_json"],
            "properties": {
                "dossier_json": {"type": "string", "minLength": 2}
            },
        }

    @classmethod
    def default(
        cls,
        *,
        repo_root: str | Path,
        working_directory: str | Path | None = None,
        timeout_seconds: float = 900.0,
    ) -> "CodexProReportDossierStructurer":
        root = Path(repo_root).expanduser().resolve()
        return cls(
            CodexStructuredProviderTransport(
                working_directory=working_directory or root,
                timeout_seconds=timeout_seconds,
            ),
            schema_path=root / "configs/e2r_pro_research_dossier_v3.schema.json",
        )

    def structure(
        self,
        *,
        report_text: str,
        packet: Mapping[str, Any],
        conversation_id: str,
        research_pass_id: str,
        prompt_hash: str,
        response_hash: str,
        mandatory_question_ids: Sequence[str],
    ) -> StructuredProReport:
        if not report_text.strip():
            raise ValueError("readable Pro report is required")
        if len(response_hash) != 64:
            raise ValueError("browser result hash must be sha256")
        report_text_sha256 = hashlib.sha256(report_text.encode("utf-8")).hexdigest()
        target = packet.get("target") or {}
        identity = {
            "job_id": str(packet.get("job_id") or ""),
            "run_id": str(packet.get("run_id") or ""),
            "conversation_id": conversation_id,
            "research_pass_id": research_pass_id,
            "parent_pass_id": None,
            "target": target,
            "as_of_date": str(packet.get("as_of_date") or ""),
            "candidate_archetypes": list(packet.get("candidate_archetypes") or ()),
            "mandatory_question_ids": list(mandatory_question_ids),
            "prompt_hash": prompt_hash,
            "response_hash": response_hash,
        }
        prompt = "\n".join(
            (
                "You are the E2R Codex report-to-dossier structuring agent.",
                "The supplied ChatGPT Pro report is complete readable research but omitted its required ResearchDossierV3 JSON block.",
                "Convert that existing report into exactly one ResearchDossierV3 JSON object matching the supplied full dossier schema.",
                "Do not browse, fetch, call tools, add research, improve the thesis, infer an unstated customer/product/contract/date/value, or calculate score/Stage.",
                "A material/counter/resolution fact is allowed only when the report itself contains one exact supporting excerpt and one explicit source URL for that atomic statement.",
                "Copy excerpts exactly from the report. Never create or paraphrase a quote. One fact must have one predicate and one source_document_id.",
                "If the report discusses a claim but lacks an exact excerpt or explicit source URL, keep it out of facts and record the missing support in unresolved_gaps/question_family_results.",
                "Create one question_family_result for every mandatory_question_id. Use a non-terminal status when the report does not close it; never fabricate closure.",
                "Preserve the exact identity fields supplied below. score_authority and stage_authority must be false.",
                "This provider only structures representation; deterministic local validation and source verification decide whether any fact is usable.",
                "Return the closed provider wrapper only. dossier_json must be a JSON-encoded string containing the complete ResearchDossierV3 object, with no Markdown fence.",
                "FULL_RESEARCH_DOSSIER_V3_SCHEMA:",
                canonical_json(self.validation_schema),
                "IDENTITY_AND_CONTRACT:",
                canonical_json(identity),
                "RESEARCH_PACKET_V3:",
                canonical_json(packet),
                "COMPLETED_PRO_REPORT:",
                report_text,
            )
        )
        response = self.transport.complete(
            prompt=prompt,
            output_schema=self.output_schema,
            schema_name="e2r_pro_report_to_dossier_v3",
        )
        wrapper = getattr(response, "payload", response)
        raw = str(getattr(response, "raw_response", canonical_json(wrapper)))
        if not isinstance(wrapper, Mapping) or set(wrapper) != {"dossier_json"}:
            raise ValueError("report structurer returned a non-object")
        dossier_text = wrapper.get("dossier_json")
        if not isinstance(dossier_text, str):
            raise ValueError("report structurer omitted dossier_json")
        try:
            parsed = json.loads(dossier_text)
        except json.JSONDecodeError as error:
            raise ValueError("report structurer returned invalid dossier_json") from error
        if not isinstance(parsed, Mapping):
            raise ValueError("report structurer dossier_json is not an object")
        dossier = dict(parsed)
        expected_identity = {
            "job_id": identity["job_id"],
            "run_id": identity["run_id"],
            "conversation_id": identity["conversation_id"],
            "research_pass_id": identity["research_pass_id"],
            "parent_pass_id": None,
            "as_of_date": identity["as_of_date"],
        }
        for field, expected in expected_identity.items():
            if dossier.get(field) != expected:
                raise ValueError(f"report structurer changed identity field: {field}")
        if dossier.get("score_authority") is not False or dossier.get(
            "stage_authority"
        ) is not False:
            raise ValueError("report structurer claimed score or Stage authority")
        actual_questions = {
            str(row.get("question_family_id") or "")
            for row in dossier.get("question_family_results") or ()
        }
        missing_questions = set(mandatory_question_ids) - actual_questions
        if missing_questions:
            raise ValueError("report structurer omitted mandatory question families")
        unsigned = {
            "schema_version": "e2r_codex_pro_report_structuring_receipt_v1",
            "status": "PASS",
            "provider_name": self.provider_name,
            "job_id": identity["job_id"],
            "run_id": identity["run_id"],
            "conversation_id": identity["conversation_id"],
            "research_pass_id": identity["research_pass_id"],
            "report_hash": response_hash,
            "browser_result_hash_bound": True,
            "report_text_sha256": report_text_sha256,
            "prompt_hash": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
            "provider_response_hash": hashlib.sha256(raw.encode("utf-8")).hexdigest(),
            "dossier_hash": canonical_hash(dossier),
            "source_document_count": len(tuple(dossier.get("source_documents") or ())),
            "material_fact_count": len(tuple(dossier.get("material_facts") or ())),
            "counterfact_count": len(tuple(dossier.get("counterfacts") or ())),
            "resolution_fact_count": len(tuple(dossier.get("resolution_facts") or ())),
            "mandatory_question_count": len(tuple(mandatory_question_ids)),
            "new_research_allowed": False,
            "score_authority": False,
            "stage_authority": False,
        }
        return StructuredProReport(
            dossier=dossier,
            receipt={**unsigned, "receipt_hash": canonical_hash(unsigned)},
        )


__all__ = [
    "CodexProReportDossierStructurer",
    "StructuredProReport",
    "StructuredReportTransport",
]
