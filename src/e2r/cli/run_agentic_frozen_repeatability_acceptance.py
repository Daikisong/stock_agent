"""Build frozen-corpus repeatability acceptance for Evidence OS runs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.agentic import PrimitiveStateV2, PrimitiveStatus, ScoreInterval, load_evidence_contracts_v2
from e2r.agentic.stage_court import StageCourtInput, decide_stage_court


DEFAULT_REPLAY_REPORTS: tuple[str, ...] = (
    "output/0621_agentic_replay/sk_hynix_c06_codex_provider_replay.json",
)
DEFAULT_OUTPUT_DIRECTORY = "output/0621_agentic_replay"
DEFAULT_OUTPUT_PREFIX = "sk_hynix_c06_frozen_repeatability_acceptance"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build frozen-corpus repeatability acceptance manifest.")
    parser.add_argument("--replay-report", action="append", default=None)
    parser.add_argument("--output-directory", default=DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--output-prefix", default=DEFAULT_OUTPUT_PREFIX)
    return parser


def run_frozen_repeatability_acceptance(
    *,
    replay_report_paths: Sequence[str | Path],
    output_directory: str | Path,
    output_prefix: str = DEFAULT_OUTPUT_PREFIX,
) -> Mapping[str, Path]:
    reports = [_read_json_mapping(Path(path)) for path in replay_report_paths]
    manifest = build_frozen_repeatability_acceptance_manifest(replay_reports=reports)
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = {
        "acceptance_json": output_dir / f"{output_prefix}_acceptance.json",
        "acceptance_md": output_dir / f"{output_prefix}_acceptance.md",
    }
    _write_json(paths["acceptance_json"], manifest)
    paths["acceptance_md"].write_text(_render_acceptance_markdown(manifest), encoding="utf-8")
    return paths


def build_frozen_repeatability_acceptance_manifest(
    *,
    replay_reports: Sequence[Mapping[str, Any]],
    required_run_count: int = 3,
) -> Mapping[str, Any]:
    rows = [_row_from_replay_report(report, required_run_count=required_run_count) for report in replay_reports]
    blocker_rows = [row for row in rows if row.get("acceptance_status") != "repeatability_ready"]
    score_relevant_ready_count = sum(1 for row in rows if row.get("score_relevant_repeatability_ready"))
    score_stage_ready_count = sum(1 for row in rows if row.get("score_stage_repeatability_ready"))
    strict_ready_count = sum(1 for row in rows if row.get("strict_identity_stable"))
    frozen_repeatability_ready = bool(rows) and not blocker_rows
    return {
        "schema_version": "e2r_frozen_repeatability_acceptance_manifest_v1",
        "summary": {
            "replay_report_count": len(rows),
            "required_run_count": required_run_count,
            "score_relevant_repeatability_ready_count": score_relevant_ready_count,
            "score_stage_repeatability_ready_count": score_stage_ready_count,
            "strict_identity_stable_count": strict_ready_count,
            "blocked_report_count": len(blocker_rows),
            "frozen_repeatability_acceptance_ready": frozen_repeatability_ready,
            "production_cutover_ready": frozen_repeatability_ready,
        },
        "rows": rows,
        "blockers": [blocker for row in rows for blocker in row.get("blockers", ())],
    }


def _row_from_replay_report(
    report: Mapping[str, Any],
    *,
    required_run_count: int,
) -> Mapping[str, Any]:
    variance = _preferred_variance(report)
    stable_axes = variance.get("stable_axes") if isinstance(variance.get("stable_axes"), Mapping) else {}
    run_count = _int_or_zero(variance.get("run_count") or report.get("successful_run_count"))
    score_relevant_stable = bool(variance.get("score_relevant_stable"))
    accepted_primitives_stable = bool(stable_axes.get("accepted_primitives"))
    source_primitives_stable = bool(stable_axes.get("score_relevant_source_primitives"))
    strict_stable = bool(variance.get("stable"))
    score_stage = _score_stage_repeatability(report)

    blockers: list[Mapping[str, Any]] = []
    row_id = _row_id(report)
    if run_count < required_run_count:
        blockers.append(
            {
                "blocker_id": "frozen_repeatability_run_count_below_required",
                "row_id": row_id,
                "reason": f"only {run_count}/{required_run_count} frozen replay runs are present",
            }
        )
    if not score_relevant_stable:
        blockers.append(
            {
                "blocker_id": "frozen_repeatability_score_relevant_evidence_unstable",
                "row_id": row_id,
                "reason": "score-relevant source primitive evidence is not stable across frozen runs",
            }
        )
    if not score_stage["ready"]:
        blockers.append(
            {
                "blocker_id": score_stage["blocker_id"],
                "row_id": row_id,
                "reason": score_stage["reason"],
            }
        )

    acceptance_status = "repeatability_ready" if not blockers else "repeatability_not_ready"
    return {
        "row_id": row_id,
        "target_entity_id": report.get("target_entity_id"),
        "archetype_id": report.get("archetype_id"),
        "as_of_date": report.get("as_of_date"),
        "document_id": report.get("document_id"),
        "anchor_id": report.get("anchor_id"),
        "run_count": run_count,
        "required_run_count": required_run_count,
        "acceptance_status": acceptance_status,
        "score_relevant_repeatability_ready": score_relevant_stable,
        "accepted_primitives_stable": accepted_primitives_stable,
        "score_relevant_source_primitives_stable": source_primitives_stable,
        "score_stage_repeatability_ready": score_stage["ready"],
        "score_values": score_stage["score_values"],
        "stage_values": score_stage["stage_values"],
        "strict_identity_stable": strict_stable,
        "unstable_axes": tuple(variance.get("unstable_axes") or ()),
        "blockers": tuple(blockers),
    }


def _preferred_variance(report: Mapping[str, Any]) -> Mapping[str, Any]:
    deduped = report.get("variance_after_source_assertion_and_duplicate_dedupe")
    if isinstance(deduped, Mapping):
        return deduped
    variance = report.get("variance")
    return variance if isinstance(variance, Mapping) else {}


def _score_stage_repeatability(report: Mapping[str, Any]) -> Mapping[str, Any]:
    runs = [row for row in report.get("runs") or () if isinstance(row, Mapping) and row.get("ok", True)]
    score_values: list[Any] = []
    stage_values: list[Any] = []
    for row in runs:
        score_value = _score_fingerprint(row)
        stage_value = _stage_fingerprint(row, report=report, score_value=score_value)
        if score_value is not None:
            score_values.append(score_value)
        if stage_value is not None:
            stage_values.append(stage_value)
    if not runs:
        return {
            "ready": False,
            "score_values": (),
            "stage_values": (),
            "blocker_id": "frozen_repeatability_no_successful_runs",
            "reason": "no successful frozen replay runs are available",
        }
    if len(score_values) != len(runs) or len(stage_values) != len(runs):
        return {
            "ready": False,
            "score_values": tuple(score_values),
            "stage_values": tuple(stage_values),
            "blocker_id": "frozen_repeatability_score_stage_fingerprint_missing",
            "reason": "frozen replay report does not include score and stage fingerprints for every run",
        }
    score_stable = len({json.dumps(value, ensure_ascii=False, sort_keys=True) for value in score_values}) == 1
    stage_stable = len({json.dumps(value, ensure_ascii=False, sort_keys=True) for value in stage_values}) == 1
    if not score_stable or not stage_stable:
        return {
            "ready": False,
            "score_values": tuple(score_values),
            "stage_values": tuple(stage_values),
            "blocker_id": "frozen_repeatability_score_stage_unstable",
            "reason": "score or stage fingerprints differ across frozen replay runs",
        }
    return {
        "ready": True,
        "score_values": tuple(score_values),
        "stage_values": tuple(stage_values),
        "blocker_id": None,
        "reason": None,
    }


def _score_fingerprint(row: Mapping[str, Any]) -> Any:
    explicit = _first_present(row, ("verified_score", "score", "raw_score", "total_score"))
    if explicit is not None:
        return explicit
    contributions = row.get("score_contributions")
    if not isinstance(contributions, Sequence) or isinstance(contributions, (str, bytes)):
        return None
    total = 0.0
    found = False
    for contribution in contributions:
        if not isinstance(contribution, Mapping):
            continue
        try:
            total += float(contribution.get("raw_points") or 0.0)
            found = True
        except (TypeError, ValueError):
            return None
    if not found:
        return None
    return round(total, 4)


def _stage_fingerprint(
    row: Mapping[str, Any],
    *,
    report: Mapping[str, Any],
    score_value: Any,
) -> Any:
    explicit = _first_present(row, ("stage", "base_stage", "runtime_stage"))
    if explicit is not None:
        return explicit
    if score_value is None:
        return None
    archetype_id = str(report.get("archetype_id") or "")
    contract = load_evidence_contracts_v2().get(archetype_id)
    if contract is None:
        return None
    primitive_states = _primitive_states_from_run(row)
    if not primitive_states:
        return None
    try:
        score = float(score_value)
    except (TypeError, ValueError):
        return None
    output = decide_stage_court(
        StageCourtInput(
            score_interval=ScoreInterval(verified_score=score, potential_score_upper_bound=score),
            primitive_states=primitive_states,
            contract=contract,
        )
    )
    return {
        "base_stage": output.decision.base_stage.value,
        "investigation_status": output.decision.investigation_status.value,
        "transition_overlay": output.decision.transition_overlay.value,
        "score_status": output.score_status.value,
        "present_green_primitives": tuple(output.present_green_primitives),
        "missing_green_primitives": tuple(output.missing_green_primitives),
    }


def _primitive_states_from_run(row: Mapping[str, Any]) -> Mapping[str, PrimitiveStateV2]:
    raw_states = row.get("primitive_states")
    if not isinstance(raw_states, Mapping):
        return {}
    states: dict[str, PrimitiveStateV2] = {}
    for primitive_id, raw_state in raw_states.items():
        if not isinstance(raw_state, Mapping):
            continue
        try:
            status = PrimitiveStatus(str(raw_state.get("status") or PrimitiveStatus.UNKNOWN.value))
        except ValueError:
            status = PrimitiveStatus.UNKNOWN
        states[str(primitive_id)] = PrimitiveStateV2(
            primitive_id=str(raw_state.get("primitive_id") or primitive_id),
            status=status,
            normalized_value=raw_state.get("normalized_value"),
            support_claim_ids=_tuple_field(raw_state.get("support_claim_ids")),
            counter_claim_ids=_tuple_field(raw_state.get("counter_claim_ids")),
            support_source_family_ids=_tuple_field(raw_state.get("support_source_family_ids")),
            counter_source_family_ids=_tuple_field(raw_state.get("counter_source_family_ids")),
            confidence_for_review=_float_or_zero(raw_state.get("confidence_for_review")),
            freshness_days=_int_or_none(raw_state.get("freshness_days")),
            materiality_remaining_points=_float_or_zero(raw_state.get("materiality_remaining_points")),
            support_mapping_ids=_tuple_field(raw_state.get("support_mapping_ids")),
            counter_mapping_ids=_tuple_field(raw_state.get("counter_mapping_ids")),
        )
    return states


def _first_present(row: Mapping[str, Any], keys: Sequence[str]) -> Any:
    for key in keys:
        if key in row and row[key] is not None:
            return row[key]
    return None


def _row_id(report: Mapping[str, Any]) -> str:
    parts = (
        str(report.get("target_entity_id") or "unknown_target"),
        str(report.get("archetype_id") or "unknown_archetype"),
        str(report.get("document_id") or "unknown_document"),
        str(report.get("anchor_id") or "unknown_anchor"),
    )
    return "|".join(parts)


def _read_json_mapping(path: Path) -> Mapping[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, Mapping):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def _write_json(path: Path, data: Mapping[str, Any]) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def _render_acceptance_markdown(manifest: Mapping[str, Any]) -> str:
    lines = ["# Evidence OS Frozen Repeatability Acceptance", ""]
    summary = manifest.get("summary")
    if isinstance(summary, Mapping):
        lines.append("## Summary")
        for key in sorted(summary):
            lines.append(f"- {key}: `{summary[key]}`")
        lines.append("")
    lines.append("## Rows")
    for row in manifest.get("rows") or ():
        if not isinstance(row, Mapping):
            continue
        lines.append(
            f"- `{row.get('row_id')}`: `{row.get('acceptance_status')}`, "
            f"score_relevant=`{row.get('score_relevant_repeatability_ready')}`, "
            f"score_stage=`{row.get('score_stage_repeatability_ready')}`"
        )
    lines.append("")
    lines.append("## Blockers")
    blockers = manifest.get("blockers") or ()
    if not blockers:
        lines.append("- none")
    for blocker in blockers:
        if isinstance(blocker, Mapping):
            lines.append(f"- `{blocker.get('blocker_id')}`: {blocker.get('reason')}")
    lines.append("")
    return "\n".join(lines)


def _int_or_zero(value: Any) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def _int_or_none(value: Any) -> int | None:
    if value is None:
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _float_or_zero(value: Any) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def _tuple_field(value: Any) -> tuple[str, ...]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes)):
        return ()
    return tuple(str(item) for item in value if str(item).strip())


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    paths = run_frozen_repeatability_acceptance(
        replay_report_paths=args.replay_report or DEFAULT_REPLAY_REPORTS,
        output_directory=args.output_directory,
        output_prefix=args.output_prefix,
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "DEFAULT_OUTPUT_DIRECTORY",
    "DEFAULT_OUTPUT_PREFIX",
    "DEFAULT_REPLAY_REPORTS",
    "build_arg_parser",
    "build_frozen_repeatability_acceptance_manifest",
    "main",
    "run_frozen_repeatability_acceptance",
]
