"""Immutable recovery for a full dossier emitted as a visible JSON artifact.

ChatGPT can keep a compact, schema-shaped transport manifest in the response
body while attaching the complete ResearchDossierV3 as a user-visible JSON
file.  The original capture bundle remains immutable.  This module writes a
separate hash-bound supplemental bundle and never uses the browser composer or
send control.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import json
import os
from pathlib import Path, PurePosixPath
from typing import Any, Callable, Mapping
from urllib.parse import urlsplit

from ..atomic_io import fsync_directory
from ..browser.protocol import (
    BrowserJsonAttachmentRequest,
    ChatGPTWebAdapter,
)
from ..dossier.parser import ResearchDossierParser
from ..ids import canonical_hash, canonical_json
from .receipt import (
    CaptureReceipt,
    file_sha256,
    verify_capture_bundle,
)


EXPANDED_RECOVERY_RECEIPT_SCHEMA = (
    "e2r_pro_expanded_dossier_recovery_receipt_v1"
)
EXPANDED_RECOVERY_READY_SCHEMA = "e2r_pro_expanded_dossier_ready_v1"
EXPANDED_RECOVERY_EVENT = "PRO_RESEARCH_EXPANDED_DOSSIER_RECOVERED"
EXPANDED_DOSSIER_PATH = (
    "capture/supplemental/expanded_research_dossier.json"
)
EXPANDED_RECEIPT_PATH = (
    "capture/supplemental/expanded_dossier_recovery_receipt.json"
)
EXPANDED_READY_PATH = "capture/supplemental/READY.json"

_COUNT_FIELDS = {
    "expanded_source_document_count": "source_documents",
    "expanded_derived_metric_count": "derived_metrics",
    "expanded_question_family_count": "question_family_results",
    "expanded_search_route_receipt_count": "search_route_receipts",
    "expanded_unresolved_gap_count": "unresolved_gaps",
}
_FACT_COLLECTIONS = ("material_facts", "counterfacts", "resolution_facts")


@dataclass(frozen=True)
class ExpandedDossierReference:
    filename: str
    artifact_uri: str
    inline_dossier_hash: str
    inline_dossier: Mapping[str, Any]
    expected_counts: Mapping[str, int]


@dataclass(frozen=True)
class ExpandedDossierBundle:
    dossier_path: Path
    dossier: Mapping[str, Any]
    receipt: Mapping[str, Any]
    reference: ExpandedDossierReference


def load_expanded_dossier_reference(
    job_root: str | Path,
    capture_receipt: CaptureReceipt,
) -> ExpandedDossierReference | None:
    """Return an exact attachment reference only for an explicit V3 manifest."""

    root = Path(job_root).resolve()
    inline_path = (root / capture_receipt.dossier_json_path).resolve()
    if root not in inline_path.parents or not inline_path.is_file():
        raise ValueError("inline dossier is missing or outside the job root")
    if file_sha256(inline_path) != capture_receipt.dossier_json_hash:
        raise ValueError("inline dossier hash differs from the capture receipt")
    parsed = ResearchDossierParser().parse(downloaded_json_path=inline_path)
    inline = parsed.payload
    saturation = inline.get("research_saturation")
    if not isinstance(saturation, Mapping):
        return None
    required = saturation.get("expanded_artifact_required_for_verification")
    is_manifest = saturation.get("inline_transport_manifest")
    if required is not True and is_manifest is not True:
        return None
    if required is not True or is_manifest is not True:
        raise ValueError(
            "expanded dossier transport flags must both be true or both absent"
        )
    if inline.get("schema_version") != "e2r_pro_research_dossier_v3":
        raise ValueError("expanded dossier transport is supported only for V3")
    business_model = inline.get("business_model")
    if not isinstance(business_model, Mapping):
        raise ValueError("expanded dossier manifest is missing business_model")
    artifact_uri = str(business_model.get("expanded_dossier_artifact") or "").strip()
    parsed_uri = urlsplit(artifact_uri)
    path = PurePosixPath(parsed_uri.path)
    filename = path.name
    if (
        parsed_uri.scheme != "sandbox"
        or parsed_uri.netloc
        or parsed_uri.query
        or parsed_uri.fragment
        or path.parent.as_posix() != "/mnt/data"
        or not filename.casefold().endswith(".json")
        or filename in {".", ".."}
    ):
        raise ValueError("expanded dossier artifact must be one sandbox JSON basename")
    expected_counts: dict[str, int] = {}
    for manifest_key in (*_COUNT_FIELDS, "expanded_accepted_fact_count"):
        value = saturation.get(manifest_key)
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError(f"expanded transport count is invalid: {manifest_key}")
        expected_counts[manifest_key] = value
    for manifest_key in (
        "expanded_dossier_schema_error_count",
        "expanded_post_cutoff_source_count",
        "expanded_duplicate_lineage_credit_count",
    ):
        value = saturation.get(manifest_key)
        if value != 0:
            raise ValueError(f"expanded transport safety count is not zero: {manifest_key}")
        expected_counts[manifest_key] = 0
    inline_fact_count = sum(len(tuple(inline.get(name) or ())) for name in _FACT_COLLECTIONS)
    if expected_counts["expanded_accepted_fact_count"] <= inline_fact_count:
        raise ValueError(
            "expanded dossier manifest does not describe evidence omitted from inline transport"
        )
    return ExpandedDossierReference(
        filename=filename,
        artifact_uri=artifact_uri,
        inline_dossier_hash=capture_receipt.dossier_json_hash,
        inline_dossier=inline,
        expected_counts=expected_counts,
    )


class ExpandedDossierArtifactService:
    def __init__(
        self,
        *,
        now: Callable[[], datetime] | None = None,
    ) -> None:
        self._now = now or (lambda: datetime.now(timezone.utc))

    async def recover(
        self,
        *,
        job_root: str | Path,
        capture_receipt: CaptureReceipt,
        adapter: ChatGPTWebAdapter,
    ) -> ExpandedDossierBundle | None:
        root = Path(job_root).resolve()
        verify_capture_bundle(root, capture_receipt)
        reference = load_expanded_dossier_reference(root, capture_receipt)
        if reference is None:
            return None
        ready_path = root / EXPANDED_READY_PATH
        if ready_path.is_file():
            return verify_expanded_dossier_bundle(root, capture_receipt)
        if not capture_receipt.conversation_id:
            raise ValueError("expanded dossier recovery requires a conversation id")

        staging = root / "capture/supplemental/.staging"
        supplemental = root / "capture/supplemental"
        staging.mkdir(parents=True, exist_ok=True)
        supplemental.mkdir(parents=True, exist_ok=True)
        raw = await adapter.download_json_attachment_without_submit(
            BrowserJsonAttachmentRequest(
                job_id=capture_receipt.job_id,
                run_id=capture_receipt.run_id,
                conversation_id=capture_receipt.conversation_id,
                assistant_turn_id=capture_receipt.assistant_turn_id,
                expected_filename=reference.filename,
                staging_directory=staging,
            )
        )
        if raw.submit_count != 0:
            raise ValueError("expanded dossier browser recovery submitted unexpectedly")
        if (
            raw.conversation_id != capture_receipt.conversation_id
            or raw.assistant_turn_id != capture_receipt.assistant_turn_id
            or raw.downloaded_filename != reference.filename
            or raw.attachment_key.conversation_id != capture_receipt.conversation_id
            or raw.attachment_key.turn_id != capture_receipt.assistant_turn_id
            or raw.attachment_key.button_text != reference.filename
        ):
            raise ValueError("expanded dossier browser attachment identity mismatch")
        dossier = _load_and_validate_expanded_payload(
            raw.json_part_path,
            capture_receipt=capture_receipt,
            reference=reference,
        )
        dossier_final = root / EXPANDED_DOSSIER_PATH
        os.replace(raw.json_part_path, dossier_final)
        fsync_directory(supplemental)

        recovered_at = self._now_value().isoformat().replace("+00:00", "Z")
        unsigned_receipt: Mapping[str, Any] = {
            "schema_version": EXPANDED_RECOVERY_RECEIPT_SCHEMA,
            "event_type": EXPANDED_RECOVERY_EVENT,
            "job_id": capture_receipt.job_id,
            "run_id": capture_receipt.run_id,
            "target_id": capture_receipt.target_id,
            "as_of_date": capture_receipt.as_of_date,
            "conversation_id": raw.conversation_id,
            "assistant_turn_id": raw.assistant_turn_id,
            "capture_receipt_hash": capture_receipt.receipt_hash,
            "report_md_hash": capture_receipt.report_md_hash,
            "inline_dossier_hash": reference.inline_dossier_hash,
            "artifact_uri": reference.artifact_uri,
            "expected_filename": reference.filename,
            "downloaded_filename": raw.downloaded_filename,
            "attachment_key": {
                "conversation_id": raw.attachment_key.conversation_id,
                "turn_id": raw.attachment_key.turn_id,
                "button_text": raw.attachment_key.button_text,
                "stable_key": raw.attachment_key.stable_key,
            },
            "expanded_dossier_path": EXPANDED_DOSSIER_PATH,
            "expanded_dossier_hash": file_sha256(dossier_final),
            "expanded_counts": _expanded_counts(dossier),
            "original_submit_count": capture_receipt.submit_count,
            "original_capture_count": capture_receipt.capture_count,
            "browser_submit_delta": 0,
            "attachment_recovery_count": 1,
            "recovered_at": recovered_at,
            "recovery_source": "CHATGPT_VISIBLE_SAME_TURN_JSON_ATTACHMENT",
        }
        receipt = {
            **unsigned_receipt,
            "receipt_hash": canonical_hash(unsigned_receipt),
        }
        receipt_part = staging / "expanded_dossier_recovery_receipt.json.part"
        receipt_final = root / EXPANDED_RECEIPT_PATH
        _write_json_durable(receipt_part, receipt)
        os.replace(receipt_part, receipt_final)
        fsync_directory(supplemental)

        unsigned_ready: Mapping[str, Any] = {
            "schema_version": EXPANDED_RECOVERY_READY_SCHEMA,
            "job_id": capture_receipt.job_id,
            "run_id": capture_receipt.run_id,
            "capture_receipt_hash": capture_receipt.receipt_hash,
            "expanded_recovery_receipt_hash": receipt["receipt_hash"],
            "expanded_recovery_receipt_path": EXPANDED_RECEIPT_PATH,
            "written_last": True,
        }
        ready = {**unsigned_ready, "ready_hash": canonical_hash(unsigned_ready)}
        ready_part = staging / "READY.json.part"
        _write_json_durable(ready_part, ready)
        os.replace(ready_part, ready_path)
        fsync_directory(supplemental)
        return verify_expanded_dossier_bundle(root, capture_receipt)

    def _now_value(self) -> datetime:
        value = self._now()
        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError("expanded dossier recovery clock must be timezone-aware")
        return value.astimezone(timezone.utc)


def verify_expanded_dossier_bundle(
    job_root: str | Path,
    capture_receipt: CaptureReceipt,
) -> ExpandedDossierBundle | None:
    root = Path(job_root).resolve()
    verify_capture_bundle(root, capture_receipt)
    reference = load_expanded_dossier_reference(root, capture_receipt)
    ready_path = root / EXPANDED_READY_PATH
    if reference is None:
        if ready_path.exists():
            raise ValueError("supplemental dossier exists without an inline transport manifest")
        return None
    if not ready_path.is_file():
        raise FileNotFoundError("required expanded dossier recovery READY is missing")
    ready = _read_json(ready_path)
    if ready.get("schema_version") != EXPANDED_RECOVERY_READY_SCHEMA:
        raise ValueError("invalid expanded dossier READY schema")
    unsigned_ready = dict(ready)
    ready_hash = unsigned_ready.pop("ready_hash", None)
    if ready_hash != canonical_hash(unsigned_ready):
        raise ValueError("expanded dossier READY hash mismatch")
    if (
        ready.get("job_id") != capture_receipt.job_id
        or ready.get("run_id") != capture_receipt.run_id
        or ready.get("capture_receipt_hash") != capture_receipt.receipt_hash
        or ready.get("expanded_recovery_receipt_path") != EXPANDED_RECEIPT_PATH
        or ready.get("written_last") is not True
    ):
        raise ValueError("expanded dossier READY identity mismatch")

    receipt_path = root / EXPANDED_RECEIPT_PATH
    receipt = _read_json(receipt_path)
    unsigned_receipt = dict(receipt)
    receipt_hash = unsigned_receipt.pop("receipt_hash", None)
    if (
        receipt_hash != canonical_hash(unsigned_receipt)
        or ready.get("expanded_recovery_receipt_hash") != receipt_hash
    ):
        raise ValueError("expanded dossier recovery receipt hash mismatch")
    required_values = {
        "schema_version": EXPANDED_RECOVERY_RECEIPT_SCHEMA,
        "event_type": EXPANDED_RECOVERY_EVENT,
        "job_id": capture_receipt.job_id,
        "run_id": capture_receipt.run_id,
        "target_id": capture_receipt.target_id,
        "as_of_date": capture_receipt.as_of_date,
        "conversation_id": capture_receipt.conversation_id,
        "assistant_turn_id": capture_receipt.assistant_turn_id,
        "capture_receipt_hash": capture_receipt.receipt_hash,
        "report_md_hash": capture_receipt.report_md_hash,
        "inline_dossier_hash": reference.inline_dossier_hash,
        "artifact_uri": reference.artifact_uri,
        "expected_filename": reference.filename,
        "downloaded_filename": reference.filename,
        "expanded_dossier_path": EXPANDED_DOSSIER_PATH,
        "original_submit_count": 1,
        "original_capture_count": 1,
        "browser_submit_delta": 0,
        "attachment_recovery_count": 1,
        "recovery_source": "CHATGPT_VISIBLE_SAME_TURN_JSON_ATTACHMENT",
    }
    for key, expected in required_values.items():
        if receipt.get(key) != expected:
            raise ValueError(f"expanded dossier receipt identity mismatch: {key}")
    attachment_key = receipt.get("attachment_key")
    if not isinstance(attachment_key, Mapping) or (
        attachment_key.get("conversation_id") != capture_receipt.conversation_id
        or attachment_key.get("turn_id") != capture_receipt.assistant_turn_id
        or attachment_key.get("button_text") != reference.filename
    ):
        raise ValueError("expanded dossier attachment key identity mismatch")
    stable_key = "|".join(
        (
            str(capture_receipt.conversation_id or ""),
            capture_receipt.assistant_turn_id,
            reference.filename,
        )
    )
    if attachment_key.get("stable_key") != stable_key:
        raise ValueError("expanded dossier attachment stable key mismatch")

    dossier_path = (root / EXPANDED_DOSSIER_PATH).resolve()
    if root not in dossier_path.parents or not dossier_path.is_file():
        raise ValueError("expanded dossier artifact is missing or outside job root")
    if receipt.get("expanded_dossier_hash") != file_sha256(dossier_path):
        raise ValueError("expanded dossier artifact hash mismatch")
    dossier = _load_and_validate_expanded_payload(
        dossier_path,
        capture_receipt=capture_receipt,
        reference=reference,
    )
    if receipt.get("expanded_counts") != _expanded_counts(dossier):
        raise ValueError("expanded dossier receipt count mismatch")
    return ExpandedDossierBundle(dossier_path, dossier, receipt, reference)


def resolve_import_dossier_path(
    job_root: str | Path,
    capture_receipt: CaptureReceipt,
) -> Path:
    """Resolve the only evidence-bearing dossier allowed for import.

    An explicit compact transport manifest is never silently imported as a
    zero-fact dossier.  Its full same-turn JSON artifact must have a valid
    supplemental READY/receipt bundle first.
    """

    root = Path(job_root).resolve()
    reference = load_expanded_dossier_reference(root, capture_receipt)
    if reference is None:
        return root / capture_receipt.dossier_json_path
    bundle = verify_expanded_dossier_bundle(root, capture_receipt)
    if bundle is None:  # pragma: no cover - reference makes this unreachable
        raise ValueError("expanded dossier bundle resolution failed")
    return bundle.dossier_path


def expanded_dossier_recovery_required(
    job_root: str | Path,
    capture_receipt: CaptureReceipt,
) -> bool:
    root = Path(job_root).resolve()
    reference = load_expanded_dossier_reference(root, capture_receipt)
    return reference is not None and not (root / EXPANDED_READY_PATH).is_file()


def _load_and_validate_expanded_payload(
    path: Path,
    *,
    capture_receipt: CaptureReceipt,
    reference: ExpandedDossierReference,
) -> Mapping[str, Any]:
    dossier = _read_json(path)
    inline = reference.inline_dossier
    target = dossier.get("target")
    if not isinstance(target, Mapping):
        raise ValueError("expanded dossier target must be an object")
    expected_identity = {
        "schema_version": "e2r_pro_research_dossier_v3",
        "job_id": capture_receipt.job_id,
        "run_id": capture_receipt.run_id,
        "as_of_date": capture_receipt.as_of_date,
        "research_pass_id": inline.get("research_pass_id"),
        "parent_pass_id": inline.get("parent_pass_id"),
    }
    for key, expected in expected_identity.items():
        if dossier.get(key) != expected:
            raise ValueError(f"expanded dossier identity mismatch: {key}")
    if str(target.get("target_id") or "") != capture_receipt.target_id:
        raise ValueError("expanded dossier target differs from capture receipt")
    if dossier.get("conversation_id") not in {
        capture_receipt.conversation_id,
        "PENDING_INITIAL_CONVERSATION",
        "PENDING_NEW_CONVERSATION",
    }:
        raise ValueError("expanded dossier conversation identity is not bindable")
    if dossier.get("score_authority") is not False or dossier.get(
        "stage_authority"
    ) is not False:
        raise ValueError("expanded Pro dossier cannot own score or Stage authority")
    actual_counts = _expanded_counts(dossier)
    for key, expected in reference.expected_counts.items():
        if actual_counts.get(key) != expected:
            raise ValueError(f"expanded dossier count differs from manifest: {key}")
    saturation = dossier.get("research_saturation")
    if not isinstance(saturation, Mapping):
        raise ValueError("expanded dossier is missing research_saturation")
    saturation_checks = {
        "source_document_count": actual_counts["expanded_source_document_count"],
        "accepted_fact_count": actual_counts["expanded_accepted_fact_count"],
        "search_route_receipt_count": actual_counts[
            "expanded_search_route_receipt_count"
        ],
        "unresolved_gap_count": actual_counts["expanded_unresolved_gap_count"],
        "post_cutoff_source_count": 0,
        "duplicate_lineage_credit_count": 0,
    }
    for key, expected in saturation_checks.items():
        if saturation.get(key) != expected:
            raise ValueError(f"expanded dossier saturation count mismatch: {key}")
    schema_validation = saturation.get("schema_validation")
    if not isinstance(schema_validation, Mapping) or (
        schema_validation.get("schema_error_count") != 0
        or schema_validation.get("json_roundtrip_equal") is not True
    ):
        raise ValueError("expanded dossier self-declared schema validation did not pass")
    return dossier


def _expanded_counts(dossier: Mapping[str, Any]) -> Mapping[str, int]:
    counts = {
        manifest_key: len(tuple(dossier.get(collection) or ()))
        for manifest_key, collection in _COUNT_FIELDS.items()
    }
    counts["expanded_accepted_fact_count"] = sum(
        len(tuple(dossier.get(collection) or ()))
        for collection in _FACT_COLLECTIONS
    )
    saturation = dossier.get("research_saturation")
    schema_validation = (
        saturation.get("schema_validation")
        if isinstance(saturation, Mapping)
        else None
    )
    counts["expanded_dossier_schema_error_count"] = int(
        schema_validation.get("schema_error_count")
        if isinstance(schema_validation, Mapping)
        else -1
    )
    counts["expanded_post_cutoff_source_count"] = int(
        saturation.get("post_cutoff_source_count", -1)
        if isinstance(saturation, Mapping)
        else -1
    )
    counts["expanded_duplicate_lineage_credit_count"] = int(
        saturation.get("duplicate_lineage_credit_count", -1)
        if isinstance(saturation, Mapping)
        else -1
    )
    return counts


def _read_json(path: Path) -> Mapping[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(payload, dict):
        raise ValueError(f"JSON artifact must be an object: {path.name}")
    return payload


def _write_json_durable(path: Path, value: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as stream:
        stream.write((canonical_json(value) + "\n").encode("utf-8"))
        stream.flush()
        os.fsync(stream.fileno())


__all__ = [
    "EXPANDED_DOSSIER_PATH",
    "EXPANDED_READY_PATH",
    "ExpandedDossierArtifactService",
    "ExpandedDossierBundle",
    "ExpandedDossierReference",
    "expanded_dossier_recovery_required",
    "load_expanded_dossier_reference",
    "resolve_import_dossier_path",
    "verify_expanded_dossier_bundle",
]
