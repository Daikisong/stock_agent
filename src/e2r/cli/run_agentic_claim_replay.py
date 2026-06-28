"""Build claim replay result manifests without scoring."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.agentic import (
    DEFAULT_EVIDENCE_CONTRACT_V2_PATH,
    build_adjudication_result_manifest,
    build_adjudication_task_manifest,
    build_claim_replay_result_manifest,
    build_claim_replay_task_manifest,
    build_claim_replay_chain_audit_manifest,
    build_eligibility_result_manifest,
    build_claim_replay_readiness_audit_manifest,
    build_eligibility_task_manifest,
    build_primitive_mapping_result_manifest,
    build_primitive_mapping_task_manifest,
    build_score_contribution_task_manifest,
    build_score_contribution_result_manifest,
    build_score_snapshot_task_manifest,
    build_score_snapshot_result_manifest,
    build_stage_court_task_manifest,
    build_stage_court_result_manifest,
    build_replacement_fetch_failure_audit_manifest,
    build_replacement_snapshot_verifier_task_manifest,
    build_replacement_snapshot_verifier_result_manifest,
    build_replacement_snapshot_verification_manifest,
    build_replacement_evidence_document_fixture_manifest,
    load_evidence_contracts_v2,
)


DEFAULT_CLAIM_REPLAY_TASKS = (
    "output/0621_agentic_replay/"
    "c01_c36_provider_low_full_fixture_only_fetch_replacement_claim_replay_tasks.json"
)
DEFAULT_OUTPUT_DIRECTORY = "output/0621_agentic_replay"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build contract-blind claim replay result status without scoring.",
    )
    parser.add_argument("--claim-replay-tasks", default=DEFAULT_CLAIM_REPLAY_TASKS)
    parser.add_argument("--extraction-results", default=None)
    parser.add_argument("--adjudication-results", default=None)
    parser.add_argument("--primitive-mapping-results", default=None)
    parser.add_argument("--eligibility-results", default=None)
    parser.add_argument("--score-contribution-results", default=None)
    parser.add_argument("--score-snapshot-results", default=None)
    parser.add_argument("--evidence-contracts-v2", default=None)
    parser.add_argument("--replacement-evidence-document-fixtures", default=None)
    parser.add_argument("--replacement-snapshot-verification", default=None)
    parser.add_argument("--replacement-candidate-fetch-status", default=None)
    parser.add_argument("--replacement-snapshot-requests", default=None)
    parser.add_argument("--replacement-snapshot-verifier-results", default=None)
    parser.add_argument(
        "--target-identity-map",
        default=None,
        help=(
            "Optional JSON map with by_candidate_id/by_fixture_seed_id entries containing "
            "target_entity_id and target_names for post-verifier claim replay tasks."
        ),
    )
    parser.add_argument(
        "--source-backed-fixture-seeds",
        default=None,
        help=(
            "Optional source-backed fixture seed manifest. candidate_id/fixture_seed_id symbol and company_name "
            "are used only to derive target identity for contract-blind claim replay tasks."
        ),
    )
    parser.add_argument(
        "--canonical-primitive-registry",
        default=None,
        help="Optional JSON map from archetype_id to allowed primitive ids for mapper output validation.",
    )
    parser.add_argument("--output-directory", default=DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--output-prefix", default="c01_c36_provider_low_full_fixture_only_fetch")
    return parser


def run_claim_replay_status(
    *,
    claim_replay_tasks_path: str | Path,
    output_directory: str | Path,
    output_prefix: str = "c01_c36_provider_low_full_fixture_only_fetch",
    extraction_results_path: str | Path | None = None,
    adjudication_results_path: str | Path | None = None,
    primitive_mapping_results_path: str | Path | None = None,
    canonical_primitive_registry_path: str | Path | None = None,
    eligibility_results_path: str | Path | None = None,
    score_contribution_results_path: str | Path | None = None,
    score_snapshot_results_path: str | Path | None = None,
    evidence_contracts_v2_path: str | Path | None = None,
    replacement_evidence_document_fixtures_path: str | Path | None = None,
    replacement_snapshot_verification_path: str | Path | None = None,
    replacement_candidate_fetch_status_path: str | Path | None = None,
    replacement_snapshot_requests_path: str | Path | None = None,
    replacement_snapshot_verifier_results_path: str | Path | None = None,
    target_identity_map_path: str | Path | None = None,
    source_backed_fixture_seeds_path: str | Path | None = None,
) -> Mapping[str, Path]:
    task_manifest = _read_json_mapping(Path(claim_replay_tasks_path))
    replacement_candidate_fetch_status_manifest = _read_json_mapping(
        Path(replacement_candidate_fetch_status_path)
    ) if replacement_candidate_fetch_status_path else None
    replacement_snapshot_request_manifest = _read_json_mapping(
        Path(replacement_snapshot_requests_path)
    ) if replacement_snapshot_requests_path else None
    claim_replay_readiness_audit = build_claim_replay_readiness_audit_manifest(
        claim_replay_task_manifest=task_manifest,
        replacement_evidence_document_fixture_manifest=_read_json_mapping(
            Path(replacement_evidence_document_fixtures_path)
        ) if replacement_evidence_document_fixtures_path else None,
        replacement_snapshot_verification_manifest=_read_json_mapping(
            Path(replacement_snapshot_verification_path)
        ) if replacement_snapshot_verification_path else None,
        replacement_candidate_fetch_status_manifest=replacement_candidate_fetch_status_manifest,
        replacement_snapshot_request_manifest=replacement_snapshot_request_manifest,
    )
    replacement_fetch_failure_audit = build_replacement_fetch_failure_audit_manifest(
        replacement_candidate_fetch_status_manifest=replacement_candidate_fetch_status_manifest,
    )
    replacement_snapshot_verifier_tasks = build_replacement_snapshot_verifier_task_manifest(
        snapshot_request_manifest=replacement_snapshot_request_manifest or {},
    )
    replacement_snapshot_verifier_results = build_replacement_snapshot_verifier_result_manifest(
        verifier_task_manifest=replacement_snapshot_verifier_tasks,
        verifier_rows=_read_rows(
            Path(replacement_snapshot_verifier_results_path)
        ) if replacement_snapshot_verifier_results_path else (),
    )
    post_verifier_snapshot_verification = build_replacement_snapshot_verification_manifest(
        fetch_status_manifest=replacement_candidate_fetch_status_manifest or {},
        verification_rows=replacement_snapshot_verifier_results.get("accepted_verification_rows") or (),
    )
    post_verifier_evidence_document_fixtures = build_replacement_evidence_document_fixture_manifest(
        snapshot_verification_manifest=post_verifier_snapshot_verification,
    )
    identity_by_candidate_id, identity_by_fixture_seed_id = _combined_target_identity_maps(
        target_identity_map_path=Path(target_identity_map_path) if target_identity_map_path else None,
        source_backed_fixture_seeds_path=(
            Path(source_backed_fixture_seeds_path) if source_backed_fixture_seeds_path else None
        ),
    )
    post_verifier_claim_replay_tasks = build_claim_replay_task_manifest(
        replacement_evidence_document_fixture_manifest=post_verifier_evidence_document_fixtures,
        target_identity_by_candidate_id=identity_by_candidate_id,
        target_identity_by_fixture_seed_id=identity_by_fixture_seed_id,
    )
    result_manifest = build_claim_replay_result_manifest(
        claim_replay_task_manifest=task_manifest,
        extraction_rows=_read_rows(Path(extraction_results_path)) if extraction_results_path else (),
    )
    adjudication_tasks = build_adjudication_task_manifest(
        claim_replay_result_manifest=result_manifest,
    )
    adjudication_results = build_adjudication_result_manifest(
        adjudication_task_manifest=adjudication_tasks,
        adjudication_rows=_read_rows(Path(adjudication_results_path)) if adjudication_results_path else (),
    )
    primitive_mapping_tasks = build_primitive_mapping_task_manifest(
        adjudication_result_manifest=adjudication_results,
    )
    primitive_mapping_results = build_primitive_mapping_result_manifest(
        primitive_mapping_task_manifest=primitive_mapping_tasks,
        mapping_rows=_read_rows(Path(primitive_mapping_results_path)) if primitive_mapping_results_path else (),
        canonical_primitive_ids_by_archetype=_read_primitive_registry(
            Path(canonical_primitive_registry_path)
        ) if canonical_primitive_registry_path else {},
    )
    eligibility_tasks = build_eligibility_task_manifest(
        primitive_mapping_result_manifest=primitive_mapping_results,
    )
    eligibility_results = build_eligibility_result_manifest(
        eligibility_task_manifest=eligibility_tasks,
        eligibility_rows=_read_rows(Path(eligibility_results_path)) if eligibility_results_path else (),
    )
    score_contribution_tasks = build_score_contribution_task_manifest(
        eligibility_result_manifest=eligibility_results,
    )
    score_contribution_results = build_score_contribution_result_manifest(
        score_contribution_task_manifest=score_contribution_tasks,
        contribution_rows=_read_rows(Path(score_contribution_results_path)) if score_contribution_results_path else (),
    )
    score_snapshot_tasks = build_score_snapshot_task_manifest(
        score_contribution_result_manifest=score_contribution_results,
    )
    score_snapshot_results = build_score_snapshot_result_manifest(
        score_snapshot_task_manifest=score_snapshot_tasks,
        score_contribution_result_manifest=score_contribution_results,
        snapshot_rows=_read_rows(Path(score_snapshot_results_path)) if score_snapshot_results_path else (),
    )
    contracts_by_archetype = load_evidence_contracts_v2(
        path=Path(evidence_contracts_v2_path) if evidence_contracts_v2_path else DEFAULT_EVIDENCE_CONTRACT_V2_PATH,
    )
    stage_court_tasks = build_stage_court_task_manifest(
        score_snapshot_result_manifest=score_snapshot_results,
        score_contribution_result_manifest=score_contribution_results,
        contracts_by_archetype=contracts_by_archetype,
    )
    stage_court_results = build_stage_court_result_manifest(
        stage_court_task_manifest=stage_court_tasks,
        score_contribution_result_manifest=score_contribution_results,
        contracts_by_archetype=contracts_by_archetype,
    )
    chain_audit = build_claim_replay_chain_audit_manifest(
        claim_replay_result_manifest=result_manifest,
        adjudication_result_manifest=adjudication_results,
        primitive_mapping_result_manifest=primitive_mapping_results,
        eligibility_result_manifest=eligibility_results,
        score_contribution_result_manifest=score_contribution_results,
        score_snapshot_result_manifest=score_snapshot_results,
        stage_court_result_manifest=stage_court_results,
    )

    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = {
        "claim_replay_results_json": output_dir / f"{output_prefix}_claim_replay_results.json",
        "claim_replay_results_md": output_dir / f"{output_prefix}_claim_replay_results.md",
        "adjudication_tasks_json": output_dir / f"{output_prefix}_adjudication_tasks.json",
        "adjudication_tasks_md": output_dir / f"{output_prefix}_adjudication_tasks.md",
        "adjudication_results_json": output_dir / f"{output_prefix}_adjudication_results.json",
        "adjudication_results_md": output_dir / f"{output_prefix}_adjudication_results.md",
        "primitive_mapping_tasks_json": output_dir / f"{output_prefix}_primitive_mapping_tasks.json",
        "primitive_mapping_tasks_md": output_dir / f"{output_prefix}_primitive_mapping_tasks.md",
        "primitive_mapping_results_json": output_dir / f"{output_prefix}_primitive_mapping_results.json",
        "primitive_mapping_results_md": output_dir / f"{output_prefix}_primitive_mapping_results.md",
        "eligibility_tasks_json": output_dir / f"{output_prefix}_eligibility_tasks.json",
        "eligibility_tasks_md": output_dir / f"{output_prefix}_eligibility_tasks.md",
        "eligibility_results_json": output_dir / f"{output_prefix}_eligibility_results.json",
        "eligibility_results_md": output_dir / f"{output_prefix}_eligibility_results.md",
        "score_contribution_tasks_json": output_dir / f"{output_prefix}_score_contribution_tasks.json",
        "score_contribution_tasks_md": output_dir / f"{output_prefix}_score_contribution_tasks.md",
        "score_contribution_results_json": output_dir / f"{output_prefix}_score_contribution_results.json",
        "score_contribution_results_md": output_dir / f"{output_prefix}_score_contribution_results.md",
        "score_snapshot_tasks_json": output_dir / f"{output_prefix}_score_snapshot_tasks.json",
        "score_snapshot_tasks_md": output_dir / f"{output_prefix}_score_snapshot_tasks.md",
        "score_snapshot_results_json": output_dir / f"{output_prefix}_score_snapshot_results.json",
        "score_snapshot_results_md": output_dir / f"{output_prefix}_score_snapshot_results.md",
        "stage_court_tasks_json": output_dir / f"{output_prefix}_stage_court_tasks.json",
        "stage_court_tasks_md": output_dir / f"{output_prefix}_stage_court_tasks.md",
        "stage_court_results_json": output_dir / f"{output_prefix}_stage_court_results.json",
        "stage_court_results_md": output_dir / f"{output_prefix}_stage_court_results.md",
        "chain_audit_json": output_dir / f"{output_prefix}_chain_audit.json",
        "chain_audit_md": output_dir / f"{output_prefix}_chain_audit.md",
        "claim_replay_readiness_audit_json": output_dir / f"{output_prefix}_claim_replay_readiness_audit.json",
        "claim_replay_readiness_audit_md": output_dir / f"{output_prefix}_claim_replay_readiness_audit.md",
        "replacement_fetch_failure_audit_json": output_dir / f"{output_prefix}_replacement_fetch_failure_audit.json",
        "replacement_fetch_failure_audit_md": output_dir / f"{output_prefix}_replacement_fetch_failure_audit.md",
        "replacement_snapshot_verifier_tasks_json": output_dir
        / f"{output_prefix}_replacement_snapshot_verifier_tasks.json",
        "replacement_snapshot_verifier_tasks_md": output_dir
        / f"{output_prefix}_replacement_snapshot_verifier_tasks.md",
        "replacement_snapshot_verifier_results_json": output_dir
        / f"{output_prefix}_replacement_snapshot_verifier_results.json",
        "replacement_snapshot_verifier_results_md": output_dir
        / f"{output_prefix}_replacement_snapshot_verifier_results.md",
        "post_verifier_snapshot_verification_json": output_dir
        / f"{output_prefix}_post_verifier_snapshot_verification.json",
        "post_verifier_snapshot_verification_md": output_dir
        / f"{output_prefix}_post_verifier_snapshot_verification.md",
        "post_verifier_evidence_document_fixtures_json": output_dir
        / f"{output_prefix}_post_verifier_evidence_document_fixtures.json",
        "post_verifier_evidence_document_fixtures_md": output_dir
        / f"{output_prefix}_post_verifier_evidence_document_fixtures.md",
        "post_verifier_claim_replay_tasks_json": output_dir
        / f"{output_prefix}_post_verifier_claim_replay_tasks.json",
        "post_verifier_claim_replay_tasks_md": output_dir
        / f"{output_prefix}_post_verifier_claim_replay_tasks.md",
    }
    _write_json(paths["claim_replay_readiness_audit_json"], claim_replay_readiness_audit)
    _write_json(paths["replacement_fetch_failure_audit_json"], replacement_fetch_failure_audit)
    _write_json(paths["replacement_snapshot_verifier_tasks_json"], replacement_snapshot_verifier_tasks)
    _write_json(paths["replacement_snapshot_verifier_results_json"], replacement_snapshot_verifier_results)
    _write_json(paths["post_verifier_snapshot_verification_json"], post_verifier_snapshot_verification)
    _write_json(paths["post_verifier_evidence_document_fixtures_json"], post_verifier_evidence_document_fixtures)
    _write_json(paths["post_verifier_claim_replay_tasks_json"], post_verifier_claim_replay_tasks)
    _write_json(paths["claim_replay_results_json"], result_manifest)
    _write_json(paths["adjudication_tasks_json"], adjudication_tasks)
    _write_json(paths["adjudication_results_json"], adjudication_results)
    _write_json(paths["primitive_mapping_tasks_json"], primitive_mapping_tasks)
    _write_json(paths["primitive_mapping_results_json"], primitive_mapping_results)
    _write_json(paths["eligibility_tasks_json"], eligibility_tasks)
    _write_json(paths["eligibility_results_json"], eligibility_results)
    _write_json(paths["score_contribution_tasks_json"], score_contribution_tasks)
    _write_json(paths["score_contribution_results_json"], score_contribution_results)
    _write_json(paths["score_snapshot_tasks_json"], score_snapshot_tasks)
    _write_json(paths["score_snapshot_results_json"], score_snapshot_results)
    _write_json(paths["stage_court_tasks_json"], stage_court_tasks)
    _write_json(paths["stage_court_results_json"], stage_court_results)
    _write_json(paths["chain_audit_json"], chain_audit)
    paths["claim_replay_results_md"].write_text(
        _render_summary_markdown("Claim Replay Results", result_manifest),
        encoding="utf-8",
    )
    paths["adjudication_tasks_md"].write_text(
        _render_summary_markdown("Adjudication Tasks", adjudication_tasks),
        encoding="utf-8",
    )
    paths["adjudication_results_md"].write_text(
        _render_summary_markdown("Adjudication Results", adjudication_results),
        encoding="utf-8",
    )
    paths["primitive_mapping_tasks_md"].write_text(
        _render_summary_markdown("Primitive Mapping Tasks", primitive_mapping_tasks),
        encoding="utf-8",
    )
    paths["primitive_mapping_results_md"].write_text(
        _render_summary_markdown("Primitive Mapping Results", primitive_mapping_results),
        encoding="utf-8",
    )
    paths["eligibility_tasks_md"].write_text(
        _render_summary_markdown("Eligibility Tasks", eligibility_tasks),
        encoding="utf-8",
    )
    paths["eligibility_results_md"].write_text(
        _render_summary_markdown("Eligibility Results", eligibility_results),
        encoding="utf-8",
    )
    paths["score_contribution_tasks_md"].write_text(
        _render_summary_markdown("Score Contribution Tasks", score_contribution_tasks),
        encoding="utf-8",
    )
    paths["score_contribution_results_md"].write_text(
        _render_summary_markdown("Score Contribution Results", score_contribution_results),
        encoding="utf-8",
    )
    paths["score_snapshot_tasks_md"].write_text(
        _render_summary_markdown("Score Snapshot Tasks", score_snapshot_tasks),
        encoding="utf-8",
    )
    paths["score_snapshot_results_md"].write_text(
        _render_summary_markdown("Score Snapshot Results", score_snapshot_results),
        encoding="utf-8",
    )
    paths["stage_court_tasks_md"].write_text(
        _render_summary_markdown("Stage Court Tasks", stage_court_tasks),
        encoding="utf-8",
    )
    paths["stage_court_results_md"].write_text(
        _render_summary_markdown("Stage Court Results", stage_court_results),
        encoding="utf-8",
    )
    paths["chain_audit_md"].write_text(
        _render_summary_markdown("Claim Replay Chain Audit", chain_audit),
        encoding="utf-8",
    )
    paths["claim_replay_readiness_audit_md"].write_text(
        _render_summary_markdown("Claim Replay Readiness Audit", claim_replay_readiness_audit),
        encoding="utf-8",
    )
    paths["replacement_fetch_failure_audit_md"].write_text(
        _render_summary_markdown("Replacement Fetch Failure Audit", replacement_fetch_failure_audit),
        encoding="utf-8",
    )
    paths["replacement_snapshot_verifier_tasks_md"].write_text(
        _render_summary_markdown("Replacement Snapshot Verifier Tasks", replacement_snapshot_verifier_tasks),
        encoding="utf-8",
    )
    paths["replacement_snapshot_verifier_results_md"].write_text(
        _render_summary_markdown("Replacement Snapshot Verifier Results", replacement_snapshot_verifier_results),
        encoding="utf-8",
    )
    paths["post_verifier_snapshot_verification_md"].write_text(
        _render_summary_markdown("Post-Verifier Snapshot Verification", post_verifier_snapshot_verification),
        encoding="utf-8",
    )
    paths["post_verifier_evidence_document_fixtures_md"].write_text(
        _render_summary_markdown("Post-Verifier EvidenceDocument Fixtures", post_verifier_evidence_document_fixtures),
        encoding="utf-8",
    )
    paths["post_verifier_claim_replay_tasks_md"].write_text(
        _render_summary_markdown("Post-Verifier Claim Replay Tasks", post_verifier_claim_replay_tasks),
        encoding="utf-8",
    )
    return paths


def _read_json_mapping(path: Path) -> Mapping[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, Mapping):
        raise ValueError(f"{path} must contain a JSON object")
    return data


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
        raw_rows = data.get("rows") or data.get("results") or data.get("extractions") or ()
    else:
        raw_rows = data
    if not isinstance(raw_rows, Sequence) or isinstance(raw_rows, (str, bytes, bytearray)):
        raise ValueError(f"{path} must contain a JSON array or an object with rows/results/extractions")
    return tuple(row for row in raw_rows if isinstance(row, Mapping))


def _read_primitive_registry(path: Path) -> Mapping[str, Sequence[str]]:
    data = _read_json_mapping(path)
    raw = data.get("by_archetype") if isinstance(data.get("by_archetype"), Mapping) else data
    result: dict[str, Sequence[str]] = {}
    for key, value in raw.items():
        if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
            result[str(key)] = tuple(str(item) for item in value)
    return result


def _read_target_identity_maps(path: Path) -> tuple[Mapping[str, Mapping[str, Any]], Mapping[str, Mapping[str, Any]]]:
    data = _read_json_mapping(path)
    raw_by_candidate = data.get("by_candidate_id")
    raw_by_fixture_seed = data.get("by_fixture_seed_id")
    by_candidate = {
        str(key): value
        for key, value in (raw_by_candidate or {}).items()
        if isinstance(value, Mapping)
    } if isinstance(raw_by_candidate, Mapping) else {}
    by_fixture_seed = {
        str(key): value
        for key, value in (raw_by_fixture_seed or {}).items()
        if isinstance(value, Mapping)
    } if isinstance(raw_by_fixture_seed, Mapping) else {}
    return by_candidate, by_fixture_seed


def _combined_target_identity_maps(
    *,
    target_identity_map_path: Path | None,
    source_backed_fixture_seeds_path: Path | None,
) -> tuple[Mapping[str, Mapping[str, Any]], Mapping[str, Mapping[str, Any]]]:
    by_candidate: dict[str, Mapping[str, Any]] = {}
    by_seed: dict[str, Mapping[str, Any]] = {}
    if source_backed_fixture_seeds_path is not None:
        seed_by_candidate, seed_by_seed = _target_identity_maps_from_source_backed_fixture_seeds(
            source_backed_fixture_seeds_path
        )
        by_candidate.update(seed_by_candidate)
        by_seed.update(seed_by_seed)
    if target_identity_map_path is not None:
        explicit_by_candidate, explicit_by_seed = _read_target_identity_maps(target_identity_map_path)
        by_candidate.update(explicit_by_candidate)
        by_seed.update(explicit_by_seed)
    return by_candidate, by_seed


def _target_identity_maps_from_source_backed_fixture_seeds(
    path: Path,
) -> tuple[Mapping[str, Mapping[str, Any]], Mapping[str, Mapping[str, Any]]]:
    data = _read_json_mapping(path)
    raw_rows = data.get("seeds") or data.get("rows") or data.get("candidates") or ()
    if not isinstance(raw_rows, Sequence) or isinstance(raw_rows, (str, bytes, bytearray)):
        raise ValueError(f"{path} must contain seeds/rows/candidates")
    by_candidate: dict[str, Mapping[str, Any]] = {}
    by_seed: dict[str, Mapping[str, Any]] = {}
    for row in raw_rows:
        if not isinstance(row, Mapping):
            continue
        identity = _target_identity_from_source_backed_seed(row)
        if not identity:
            continue
        candidate_id = str(row.get("candidate_id") or "").strip()
        fixture_seed_id = str(row.get("fixture_seed_id") or "").strip()
        if candidate_id:
            by_candidate[candidate_id] = identity
        if fixture_seed_id:
            by_seed[fixture_seed_id] = identity
    return by_candidate, by_seed


def _target_identity_from_source_backed_seed(row: Mapping[str, Any]) -> Mapping[str, Any] | None:
    symbol = str(row.get("symbol") or "").strip()
    company_name = str(row.get("company_name") or "").strip()
    if not symbol and not company_name:
        return None
    target_names = tuple(dict.fromkeys(item for item in (company_name, symbol) if item))
    target_entity_id = f"KRX:{symbol}" if symbol else company_name
    return {
        "target_entity_id": target_entity_id,
        "target_names": target_names,
        "symbol": symbol or None,
        "company_name": company_name or None,
        "identity_source": "source_backed_fixture_seed_manifest",
    }


def _write_json(path: Path, data: Mapping[str, Any]) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


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
    lines.append(
        "Claim replay output is not score evidence until adjudication, primitive mapping, "
        "eligibility checks, and ScoreContribution construction pass."
    )
    lines.append("")
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    paths = run_claim_replay_status(
        claim_replay_tasks_path=args.claim_replay_tasks,
        extraction_results_path=args.extraction_results,
        adjudication_results_path=args.adjudication_results,
        primitive_mapping_results_path=args.primitive_mapping_results,
        canonical_primitive_registry_path=args.canonical_primitive_registry,
        eligibility_results_path=args.eligibility_results,
        score_contribution_results_path=args.score_contribution_results,
        score_snapshot_results_path=args.score_snapshot_results,
        evidence_contracts_v2_path=args.evidence_contracts_v2,
        replacement_evidence_document_fixtures_path=args.replacement_evidence_document_fixtures,
        replacement_snapshot_verification_path=args.replacement_snapshot_verification,
        replacement_candidate_fetch_status_path=args.replacement_candidate_fetch_status,
        replacement_snapshot_requests_path=args.replacement_snapshot_requests,
        replacement_snapshot_verifier_results_path=args.replacement_snapshot_verifier_results,
        target_identity_map_path=args.target_identity_map,
        source_backed_fixture_seeds_path=args.source_backed_fixture_seeds,
        output_directory=args.output_directory,
        output_prefix=args.output_prefix,
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "DEFAULT_CLAIM_REPLAY_TASKS",
    "DEFAULT_OUTPUT_DIRECTORY",
    "build_arg_parser",
    "main",
    "run_claim_replay_status",
]
