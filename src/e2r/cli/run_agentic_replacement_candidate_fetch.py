"""Run bounded replacement-candidate fetch attempts.

This CLI executes only the fetch-attempt layer for replacement candidates. A
successful fetch is still not a score fixture; same-event and as-of verification
must happen later.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import date
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.agentic import (
    build_claim_replay_task_manifest,
    build_replacement_candidate_fetch_status_manifest,
    build_replacement_evidence_document_fixture_manifest,
    build_replacement_snapshot_request_manifest,
    build_replacement_snapshot_verification_manifest,
)
from e2r.research.page_fetcher import PageFetcher


DEFAULT_ACQUISITION_QUEUE = (
    "output/0621_agentic_replay/c01_c36_provider_low_full_replacement_candidate_acquisition_queue_from_run.json"
)
DEFAULT_OUTPUT_DIRECTORY = "output/0621_agentic_replay"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run bounded replacement candidate fetch attempts without scoring.",
    )
    parser.add_argument("--acquisition-queue", default=DEFAULT_ACQUISITION_QUEUE)
    parser.add_argument("--output-directory", default=DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--output-prefix", default="c01_c36_provider_low_full")
    parser.add_argument(
        "--fixture-map",
        default=None,
        help="Optional JSON mapping from candidate URL to text or local text path.",
    )
    parser.add_argument(
        "--live-fetch",
        action="store_true",
        help="Enable bounded live HTTP fetches. Default is fixture-only and does not scrape live web.",
    )
    parser.add_argument("--timeout-seconds", type=float, default=10.0)
    parser.add_argument("--max-tasks", type=int, default=None)
    parser.add_argument(
        "--snapshot-verifications",
        default=None,
        help="Optional JSON/JSONL rows proving same-event replacement and as-of snapshot status.",
    )
    parser.add_argument(
        "--target-identity-map",
        default=None,
        help=(
            "Optional JSON map with by_candidate_id/by_fixture_seed_id entries containing "
            "target_entity_id and target_names for contract-blind claim replay tasks."
        ),
    )
    return parser


def run_replacement_candidate_fetch(
    *,
    acquisition_queue_path: str | Path,
    output_directory: str | Path,
    output_prefix: str = "c01_c36_provider_low_full",
    fixture_map_path: str | Path | None = None,
    live_fetch: bool = False,
    timeout_seconds: float = 10.0,
    max_tasks: int | None = None,
    snapshot_verifications_path: str | Path | None = None,
    target_identity_map_path: str | Path | None = None,
) -> Mapping[str, Path]:
    queue = _read_json_mapping(Path(acquisition_queue_path))
    tasks = _selected_tasks(queue, max_tasks=max_tasks)
    fetcher = PageFetcher(
        fixture_text_by_url=_read_fixture_map(Path(fixture_map_path)) if fixture_map_path else None,
        live_enabled=live_fetch,
        timeout_seconds=timeout_seconds,
        cache_directory=Path(output_directory) / "replacement_candidate_fetch_cache",
    )
    attempts = tuple(_fetch_attempt_for_task(task, fetcher=fetcher) for task in tasks)
    scoped_queue = dict(queue)
    scoped_queue["tasks"] = tasks
    scoped_queue["fetch_input_filter"] = {
        "input_task_count": len(queue.get("tasks") or ()),
        "selected_task_count": len(tasks),
        "max_tasks": max_tasks,
        "live_fetch": live_fetch,
    }
    fetch_status = build_replacement_candidate_fetch_status_manifest(
        acquisition_queue=scoped_queue,
        fetch_rows=attempts,
    )
    snapshot_verification = build_replacement_snapshot_verification_manifest(
        fetch_status_manifest=fetch_status,
        verification_rows=_read_rows(Path(snapshot_verifications_path)) if snapshot_verifications_path else (),
    )
    snapshot_requests = build_replacement_snapshot_request_manifest(
        snapshot_verification_manifest=snapshot_verification,
    )
    evidence_document_fixtures = build_replacement_evidence_document_fixture_manifest(
        snapshot_verification_manifest=snapshot_verification,
    )
    identity_by_candidate_id, identity_by_fixture_seed_id = _read_target_identity_maps(
        Path(target_identity_map_path)
    ) if target_identity_map_path else ({}, {})
    claim_replay_tasks = build_claim_replay_task_manifest(
        replacement_evidence_document_fixture_manifest=evidence_document_fixtures,
        target_identity_by_candidate_id=identity_by_candidate_id,
        target_identity_by_fixture_seed_id=identity_by_fixture_seed_id,
    )

    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = {
        "fetch_attempts_jsonl": output_dir / f"{output_prefix}_replacement_candidate_fetch_attempts.jsonl",
        "fetch_status_json": output_dir / f"{output_prefix}_replacement_candidate_fetch_status_from_attempts.json",
        "fetch_status_md": output_dir / f"{output_prefix}_replacement_candidate_fetch_status_from_attempts.md",
        "snapshot_verification_json": output_dir
        / f"{output_prefix}_replacement_snapshot_verification_from_attempts.json",
        "snapshot_verification_md": output_dir
        / f"{output_prefix}_replacement_snapshot_verification_from_attempts.md",
        "snapshot_requests_json": output_dir / f"{output_prefix}_replacement_snapshot_requests.json",
        "snapshot_requests_md": output_dir / f"{output_prefix}_replacement_snapshot_requests.md",
        "evidence_document_fixtures_json": output_dir
        / f"{output_prefix}_replacement_evidence_document_fixtures.json",
        "evidence_document_fixtures_md": output_dir
        / f"{output_prefix}_replacement_evidence_document_fixtures.md",
        "claim_replay_tasks_json": output_dir / f"{output_prefix}_replacement_claim_replay_tasks.json",
        "claim_replay_tasks_md": output_dir / f"{output_prefix}_replacement_claim_replay_tasks.md",
    }
    _write_jsonl(paths["fetch_attempts_jsonl"], attempts)
    _write_json(paths["fetch_status_json"], fetch_status)
    _write_json(paths["snapshot_verification_json"], snapshot_verification)
    _write_json(paths["snapshot_requests_json"], snapshot_requests)
    _write_json(paths["evidence_document_fixtures_json"], evidence_document_fixtures)
    _write_json(paths["claim_replay_tasks_json"], claim_replay_tasks)
    paths["fetch_status_md"].write_text(
        _render_summary_markdown("Replacement Candidate Fetch Status", fetch_status),
        encoding="utf-8",
    )
    paths["snapshot_verification_md"].write_text(
        _render_summary_markdown("Replacement Snapshot Verification", snapshot_verification),
        encoding="utf-8",
    )
    paths["snapshot_requests_md"].write_text(
        _render_summary_markdown("Replacement Snapshot Requests", snapshot_requests),
        encoding="utf-8",
    )
    paths["evidence_document_fixtures_md"].write_text(
        _render_summary_markdown("Replacement EvidenceDocument Fixtures", evidence_document_fixtures),
        encoding="utf-8",
    )
    paths["claim_replay_tasks_md"].write_text(
        _render_summary_markdown("Replacement Claim Replay Tasks", claim_replay_tasks),
        encoding="utf-8",
    )
    return paths


def _fetch_attempt_for_task(task: Mapping[str, Any], *, fetcher: PageFetcher) -> Mapping[str, Any]:
    candidate_url = str(task.get("candidate_url") or "").strip()
    as_of_date = _parse_date(task.get("as_of_date"))
    if not candidate_url:
        return _attempt_base(task) | {
            "ok": False,
            "reason": "candidate_url_missing",
        }
    if as_of_date is None:
        return _attempt_base(task) | {
            "ok": False,
            "reason": "invalid_or_missing_as_of_date",
        }
    result = fetcher.fetch(candidate_url, as_of_date=as_of_date)
    base = _attempt_base(task) | {
        "ok": result.ok,
        "fetched_at": result.fetched_at.isoformat() if result.fetched_at else None,
        "content_type": result.content_type,
        "reason": result.reason,
    }
    if not result.ok or not (result.text or "").strip():
        return base
    text = result.text or ""
    return base | {
        "current_text_path": result.source_path,
        "current_text_hash": hashlib.sha256(text.encode("utf-8")).hexdigest(),
        "current_text_chars": len(text),
    }


def _attempt_base(task: Mapping[str, Any]) -> Mapping[str, Any]:
    return {
        "task_id": str(task.get("task_id") or ""),
        "replacement_candidate_id": str(task.get("replacement_candidate_id") or ""),
        "request_id": str(task.get("request_id") or ""),
        "fixture_seed_id": str(task.get("fixture_seed_id") or ""),
        "candidate_id": str(task.get("candidate_id") or ""),
        "archetype_id": str(task.get("archetype_id") or ""),
        "original_source_anchor": str(task.get("original_source_anchor") or ""),
        "candidate_url": str(task.get("candidate_url") or ""),
        "as_of_date": task.get("as_of_date"),
        "source_replacement_verified": False,
        "asof_snapshot_verified": False,
        "evidence_document_fixture_ready": False,
        "production_score_fixture": False,
    }


def _selected_tasks(queue: Mapping[str, Any], *, max_tasks: int | None) -> tuple[Mapping[str, Any], ...]:
    if max_tasks is not None and max_tasks < 1:
        raise ValueError("max_tasks must be positive when provided")
    raw_tasks = queue.get("tasks") or ()
    if not isinstance(raw_tasks, Sequence) or isinstance(raw_tasks, (str, bytes, bytearray)):
        raise ValueError("acquisition queue tasks must be a sequence")
    tasks = tuple(task for task in raw_tasks if isinstance(task, Mapping))
    return tasks[:max_tasks] if max_tasks is not None else tasks


def _read_json_mapping(path: Path) -> Mapping[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, Mapping):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def _read_fixture_map(path: Path) -> Mapping[str, str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, Mapping):
        raise ValueError(f"{path} must contain a JSON object")
    return {str(key): str(value) for key, value in data.items()}


def _read_rows(path: Path) -> tuple[Mapping[str, Any], ...]:
    if path.suffix.lower() == ".jsonl":
        rows: list[Mapping[str, Any]] = []
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            item = json.loads(line)
            if isinstance(item, Mapping):
                rows.append(item)
        return tuple(rows)
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, Mapping):
        raw_rows = (
            data.get("rows")
            or data.get("accepted_verification_rows")
            or data.get("attempts")
            or data.get("verifications")
            or data.get("results")
            or ()
        )
    else:
        raw_rows = data
    if not isinstance(raw_rows, Sequence) or isinstance(raw_rows, (str, bytes, bytearray)):
        raise ValueError(f"{path} must contain a JSON array or an object with rows/attempts/verifications")
    return tuple(row for row in raw_rows if isinstance(row, Mapping))


def _read_target_identity_maps(path: Path) -> tuple[Mapping[str, Mapping[str, Any]], Mapping[str, Mapping[str, Any]]]:
    data = _read_json_mapping(path)
    raw_by_candidate = data.get("by_candidate_id")
    raw_by_seed = data.get("by_fixture_seed_id")
    by_candidate = _string_keyed_mapping(raw_by_candidate if isinstance(raw_by_candidate, Mapping) else data)
    by_seed = _string_keyed_mapping(raw_by_seed if isinstance(raw_by_seed, Mapping) else {})
    return by_candidate, by_seed


def _string_keyed_mapping(value: Mapping[str, Any]) -> Mapping[str, Mapping[str, Any]]:
    result: dict[str, Mapping[str, Any]] = {}
    for key, item in value.items():
        if isinstance(item, Mapping):
            result[str(key)] = item
    return result


def _parse_date(value: Any) -> date | None:
    try:
        return date.fromisoformat(str(value or "").strip())
    except ValueError:
        return None


def _write_json(path: Path, data: Mapping[str, Any]) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def _write_jsonl(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True))
            handle.write("\n")


def _render_summary_markdown(title: str, manifest: Mapping[str, Any]) -> str:
    lines = [f"# {title}", ""]
    schema_version = manifest.get("schema_version")
    if schema_version:
        lines.extend((f"- schema_version: `{schema_version}`", ""))
    summary = manifest.get("summary")
    if isinstance(summary, Mapping):
        lines.append("## Summary")
        for key in sorted(summary):
            lines.append(f"- {key}: `{summary[key]}`")
        lines.append("")
    counts = manifest.get("fetch_status_counts")
    if isinstance(counts, Mapping) and counts:
        lines.append("## Counts")
        for key in sorted(counts):
            lines.append(f"- {key}: `{counts[key]}`")
        lines.append("")
    lines.append(
        "A fetched replacement candidate is not score evidence until source replacement, as-of snapshot, "
        "EvidenceDocument/EvidenceAnchor, and claim replay verification pass."
    )
    lines.append("")
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    paths = run_replacement_candidate_fetch(
        acquisition_queue_path=args.acquisition_queue,
        output_directory=args.output_directory,
        output_prefix=args.output_prefix,
        fixture_map_path=args.fixture_map,
        live_fetch=bool(args.live_fetch),
        timeout_seconds=args.timeout_seconds,
        max_tasks=args.max_tasks,
        snapshot_verifications_path=args.snapshot_verifications,
        target_identity_map_path=args.target_identity_map,
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "DEFAULT_ACQUISITION_QUEUE",
    "DEFAULT_OUTPUT_DIRECTORY",
    "build_arg_parser",
    "main",
    "run_replacement_candidate_fetch",
]
