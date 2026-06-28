"""Gate production cutover for the Evidence OS preview chain."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping, Sequence


DEFAULT_CHAIN_AUDIT = (
    "output/0621_agentic_replay/"
    "c01_c36_combined_replacement_metadata_asof_source_recovery_v12_chain_audit.json"
)
DEFAULT_REPLAY_ACCEPTANCE = (
    "output/0621_agentic_replay/"
    "c01_c36_combined_replacement_metadata_asof_source_recovery_v13_replay_acceptance_acceptance.json"
)
DEFAULT_ADVERSARIAL_ACCEPTANCE = (
    "output/0621_agentic_replay/"
    "c01_c36_combined_replacement_metadata_asof_source_recovery_v13_adversarial_acceptance_acceptance.json"
)
DEFAULT_LIVE_SMOKE_ACCEPTANCE = (
    "output/0621_agentic_replay/"
    "samsung_cp199_hynix_cp198_live_smoke_acceptance_acceptance.json"
)
DEFAULT_FROZEN_REPEATABILITY_ACCEPTANCE = (
    "output/0621_agentic_replay/"
    "sk_hynix_c06_frozen_repeatability_acceptance_after_cp163_acceptance.json"
)
DEFAULT_OUTPUT_DIRECTORY = "output/0621_agentic_replay"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Gate Evidence OS production cutover readiness.")
    parser.add_argument("--chain-audit", default=DEFAULT_CHAIN_AUDIT)
    parser.add_argument("--replay-acceptance", default=DEFAULT_REPLAY_ACCEPTANCE)
    parser.add_argument("--adversarial-acceptance", default=DEFAULT_ADVERSARIAL_ACCEPTANCE)
    parser.add_argument("--live-smoke-acceptance", default=DEFAULT_LIVE_SMOKE_ACCEPTANCE)
    parser.add_argument("--frozen-repeatability-acceptance", default=DEFAULT_FROZEN_REPEATABILITY_ACCEPTANCE)
    parser.add_argument("--output-directory", default=DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument(
        "--output-prefix",
        default="c01_c36_v13_cp199_live_cutover_acceptance",
    )
    return parser


def run_cutover_acceptance(
    *,
    chain_audit_manifest_path: str | Path,
    replay_acceptance_manifest_path: str | Path,
    adversarial_acceptance_manifest_path: str | Path,
    output_directory: str | Path,
    live_smoke_acceptance_manifest_path: str | Path | None = None,
    frozen_repeatability_acceptance_manifest_path: str | Path | None = None,
    output_prefix: str = "c01_c36_v13_cp199_live_cutover_acceptance",
) -> Mapping[str, Path]:
    live_smoke_acceptance = (
        _read_json_mapping(Path(live_smoke_acceptance_manifest_path))
        if live_smoke_acceptance_manifest_path is not None
        else None
    )
    frozen_repeatability_acceptance = (
        _read_json_mapping(Path(frozen_repeatability_acceptance_manifest_path))
        if frozen_repeatability_acceptance_manifest_path is not None
        else None
    )
    manifest = build_cutover_acceptance_manifest(
        chain_audit_manifest=_read_json_mapping(Path(chain_audit_manifest_path)),
        replay_acceptance_manifest=_read_json_mapping(Path(replay_acceptance_manifest_path)),
        adversarial_acceptance_manifest=_read_json_mapping(Path(adversarial_acceptance_manifest_path)),
        live_smoke_acceptance_manifest=live_smoke_acceptance,
        frozen_repeatability_acceptance_manifest=frozen_repeatability_acceptance,
    )
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = {
        "acceptance_json": output_dir / f"{output_prefix}_acceptance.json",
        "acceptance_md": output_dir / f"{output_prefix}_acceptance.md",
    }
    _write_json(paths["acceptance_json"], manifest)
    paths["acceptance_md"].write_text(_render_acceptance_markdown(manifest), encoding="utf-8")
    return paths


def build_cutover_acceptance_manifest(
    *,
    chain_audit_manifest: Mapping[str, Any],
    replay_acceptance_manifest: Mapping[str, Any],
    adversarial_acceptance_manifest: Mapping[str, Any],
    live_smoke_acceptance_manifest: Mapping[str, Any] | None = None,
    frozen_repeatability_acceptance_manifest: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    chain_summary = _summary(chain_audit_manifest)
    replay_summary = _summary(replay_acceptance_manifest)
    adversarial_summary = _summary(adversarial_acceptance_manifest)
    live_smoke_summary = _summary(live_smoke_acceptance_manifest or {})
    frozen_repeatability_summary = _summary(frozen_repeatability_acceptance_manifest or {})
    blockers: list[Mapping[str, Any]] = []
    chain_ready = _chain_ready(chain_summary)
    replay_ready = _replay_ready(replay_summary)
    adversarial_ready = _adversarial_ready(adversarial_summary)
    live_smoke_ready = _live_smoke_ready(live_smoke_summary)
    frozen_repeatability_ready = _frozen_repeatability_ready(frozen_repeatability_summary)

    if not chain_ready:
        blockers.append(
            {
                "blocker_id": "chain_evidence_os_ready_false",
                "source": "chain_audit",
                "reason": chain_summary.get("blocked_reason")
                or "claim replay chain has not passed full production cutover acceptance",
            }
        )

    archetype_count = _int_or_zero(replay_summary.get("archetype_count"))
    stage_ready = _int_or_zero(replay_summary.get("stage_preview_ready_count"))
    unsupported = _int_or_zero(replay_summary.get("unsupported_source_gap_count"))
    present_not_ready = _int_or_zero(replay_summary.get("primitive_state_present_stage_not_ready_count"))
    missing_contracts = _int_or_zero(replay_summary.get("evidence_contract_missing_count"))

    if not replay_ready:
        blockers.append(
            {
                "blocker_id": "replay_acceptance_ready_false",
                "source": "replay_acceptance",
                "reason": "C01-C36 replay acceptance is not production-ready",
            }
        )
    if archetype_count and stage_ready < archetype_count:
        blockers.append(
            {
                "blocker_id": "replay_not_all_archetypes_stage_preview_ready",
                "source": "replay_acceptance",
                "reason": f"only {stage_ready}/{archetype_count} archetypes reached StageCourt preview",
            }
        )
    if unsupported:
        blockers.append(
            {
                "blocker_id": "replay_unsupported_source_gap_remaining",
                "source": "replay_acceptance",
                "reason": f"{unsupported} archetypes still have unsupported_source_gap coverage status",
            }
        )
    if present_not_ready:
        blockers.append(
            {
                "blocker_id": "replay_primitive_state_present_stage_not_ready",
                "source": "replay_acceptance",
                "reason": f"{present_not_ready} archetypes have primitive states but no StageCourt preview",
            }
        )
    if missing_contracts:
        blockers.append(
            {
                "blocker_id": "replay_evidence_contract_missing",
                "source": "replay_acceptance",
                "reason": f"{missing_contracts} archetypes are missing Evidence Contract v2",
            }
        )

    if not adversarial_ready:
        blockers.append(
            {
                "blocker_id": "adversarial_acceptance_ready_false",
                "source": "adversarial_acceptance",
                "reason": "global adversarial acceptance is still preview-only",
            }
        )
    if _int_or_zero(adversarial_summary.get("missing_representative_test_count")):
        blockers.append(
            {
                "blocker_id": "adversarial_missing_named_regression",
                "source": "adversarial_acceptance",
                "reason": "one or more adversarial cases are missing representative regression tests",
            }
        )

    if not live_smoke_acceptance_manifest:
        blockers.append(
            {
                "blocker_id": "live_smoke_acceptance_missing",
                "source": "live_smoke_acceptance",
                "reason": "Samsung/SK Hynix bounded live smoke acceptance manifest is missing",
            }
        )
    elif not live_smoke_ready:
        blockers.append(
            {
                "blocker_id": "live_smoke_acceptance_ready_false",
                "source": "live_smoke_acceptance",
                "reason": "Samsung/SK Hynix bounded live smoke is still pending or deprecated",
            }
        )

    if not frozen_repeatability_acceptance_manifest:
        blockers.append(
            {
                "blocker_id": "frozen_repeatability_acceptance_missing",
                "source": "frozen_repeatability_acceptance",
                "reason": "frozen-corpus three-run repeatability acceptance manifest is missing",
            }
        )
    elif not frozen_repeatability_ready:
        blockers.append(
            {
                "blocker_id": "frozen_repeatability_acceptance_ready_false",
                "source": "frozen_repeatability_acceptance",
                "reason": "frozen-corpus score/stage repeatability is not acceptance-ready",
            }
        )

    production_cutover_ready = not blockers
    return {
        "schema_version": "e2r_cutover_acceptance_manifest_v1",
        "source_chain_audit_schema_version": chain_audit_manifest.get("schema_version"),
        "source_replay_acceptance_schema_version": replay_acceptance_manifest.get("schema_version"),
        "source_adversarial_acceptance_schema_version": adversarial_acceptance_manifest.get("schema_version"),
        "source_live_smoke_acceptance_schema_version": (
            live_smoke_acceptance_manifest.get("schema_version") if live_smoke_acceptance_manifest else None
        ),
        "summary": {
            "production_cutover_ready": production_cutover_ready,
            "legacy_parser_direct_score_cutover_allowed": production_cutover_ready,
            "blocker_count": len(blockers),
            "chain_status": chain_summary.get("chain_status"),
            "chain_evidence_os_ready": chain_ready,
            "chain_production_cutover_ready": chain_summary.get("production_cutover_ready"),
            "replay_archetype_count": archetype_count,
            "replay_stage_preview_ready_count": stage_ready,
            "replay_unsupported_source_gap_count": unsupported,
            "replay_acceptance_ready": replay_ready,
            "replay_production_cutover_ready": replay_summary.get("production_cutover_ready"),
            "adversarial_case_count": adversarial_summary.get("case_count"),
            "adversarial_named_regression_covered_count": adversarial_summary.get(
                "named_regression_covered_count",
            ),
            "adversarial_missing_representative_test_count": adversarial_summary.get(
                "missing_representative_test_count",
            ),
            "adversarial_acceptance_ready": adversarial_ready,
            "adversarial_production_cutover_ready": adversarial_summary.get("production_cutover_ready"),
            "live_smoke_target_count": live_smoke_summary.get("smoke_target_count"),
            "live_smoke_pending_not_operational_stage_count": live_smoke_summary.get(
                "pending_not_operational_stage_count",
            ),
            "live_smoke_provider_failure_pending_count": live_smoke_summary.get(
                "provider_failure_pending_count",
            ),
            "live_smoke_provider_quota_exhausted_pending_count": live_smoke_summary.get(
                "provider_quota_exhausted_pending_count",
            ),
            "live_smoke_theme_review_timeout_pending_count": live_smoke_summary.get(
                "theme_review_timeout_pending_count",
            ),
            "live_smoke_theme_review_timeout_observed_count": live_smoke_summary.get(
                "theme_review_timeout_observed_count",
            ),
            "live_smoke_score_gap_no_progress_pending_count": live_smoke_summary.get(
                "score_gap_no_progress_pending_count",
            ),
            "live_smoke_score_gap_evidence_progress_pending_count": live_smoke_summary.get(
                "score_gap_evidence_progress_pending_count",
            ),
            "live_smoke_score_gap_rejected_mapping_pending_count": live_smoke_summary.get(
                "score_gap_rejected_mapping_pending_count",
            ),
            "live_smoke_cash_bridge_pending_count": live_smoke_summary.get(
                "cash_bridge_pending_count",
            ),
            "live_smoke_cash_bridge_source_quorum_without_signal_count": live_smoke_summary.get(
                "cash_bridge_source_quorum_without_signal_count",
            ),
            "live_smoke_legacy_parser_score_audit_missing_count": live_smoke_summary.get(
                "legacy_parser_score_audit_missing_count",
            ),
            "live_smoke_legacy_parser_score_claim_without_v2_current_row_count": live_smoke_summary.get(
                "legacy_parser_score_claim_without_v2_current_row_count",
            ),
            "live_smoke_deprecated_legacy_result_not_accepted_count": live_smoke_summary.get(
                "deprecated_legacy_result_not_accepted_count",
            ),
            "live_smoke_acceptance_ready": live_smoke_ready,
            "live_smoke_production_cutover_ready": live_smoke_summary.get("production_cutover_ready"),
            "frozen_repeatability_report_count": frozen_repeatability_summary.get("replay_report_count"),
            "frozen_repeatability_blocked_report_count": frozen_repeatability_summary.get("blocked_report_count"),
            "frozen_repeatability_score_relevant_ready_count": frozen_repeatability_summary.get(
                "score_relevant_repeatability_ready_count",
            ),
            "frozen_repeatability_score_stage_ready_count": frozen_repeatability_summary.get(
                "score_stage_repeatability_ready_count",
            ),
            "frozen_repeatability_acceptance_ready": frozen_repeatability_ready,
            "frozen_repeatability_production_cutover_ready": frozen_repeatability_summary.get(
                "production_cutover_ready",
            ),
        },
        "blockers": blockers,
    }


def _summary(manifest: Mapping[str, Any]) -> Mapping[str, Any]:
    summary = manifest.get("summary")
    return summary if isinstance(summary, Mapping) else {}


def _int_or_zero(value: Any) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def _chain_ready(chain_summary: Mapping[str, Any]) -> bool:
    if chain_summary.get("evidence_os_chain_ready") is True:
        return True
    return (
        chain_summary.get("chain_status") == "stage_preview_ready_not_production_cutover"
        and _int_or_zero(chain_summary.get("stage_court_ready_count")) > 0
        and _int_or_zero(chain_summary.get("production_score_fixture_total")) == 0
        and _int_or_zero(chain_summary.get("production_stage_fixture_total")) == 0
    )


def _replay_ready(replay_summary: Mapping[str, Any]) -> bool:
    if replay_summary.get("replay_acceptance_ready") is True:
        return True
    return (
        replay_summary.get("production_cutover_ready") is True
        and _int_or_zero(replay_summary.get("unsupported_source_gap_count")) == 0
        and _int_or_zero(replay_summary.get("primitive_state_present_stage_not_ready_count")) == 0
        and _int_or_zero(replay_summary.get("evidence_contract_missing_count")) == 0
    )


def _adversarial_ready(adversarial_summary: Mapping[str, Any]) -> bool:
    if adversarial_summary.get("adversarial_acceptance_ready") is True:
        return True
    return (
        adversarial_summary.get("production_cutover_ready") is True
        and _int_or_zero(adversarial_summary.get("missing_representative_test_count")) == 0
    )


def _live_smoke_ready(live_smoke_summary: Mapping[str, Any]) -> bool:
    legacy_parser_score_audit_ready = (
        "legacy_parser_score_audit_missing_count" in live_smoke_summary
        and _int_or_zero(live_smoke_summary.get("legacy_parser_score_audit_missing_count")) == 0
        and _int_or_zero(live_smoke_summary.get("legacy_parser_score_claim_without_v2_current_row_count")) == 0
    )
    if live_smoke_summary.get("live_smoke_acceptance_ready") is True:
        return legacy_parser_score_audit_ready
    target_count = _int_or_zero(live_smoke_summary.get("smoke_target_count"))
    return (
        live_smoke_summary.get("production_cutover_ready") is True
        and target_count > 0
        and _int_or_zero(live_smoke_summary.get("pending_not_operational_stage_count")) == 0
        and _int_or_zero(live_smoke_summary.get("invalid_live_smoke_result_count")) == 0
        and legacy_parser_score_audit_ready
    )


def _frozen_repeatability_ready(frozen_repeatability_summary: Mapping[str, Any]) -> bool:
    if frozen_repeatability_summary.get("frozen_repeatability_acceptance_ready") is True:
        return True
    report_count = _int_or_zero(frozen_repeatability_summary.get("replay_report_count"))
    return (
        frozen_repeatability_summary.get("production_cutover_ready") is True
        and report_count > 0
        and _int_or_zero(frozen_repeatability_summary.get("blocked_report_count")) == 0
        and _int_or_zero(frozen_repeatability_summary.get("score_stage_repeatability_ready_count")) == report_count
    )


def _read_json_mapping(path: Path) -> Mapping[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, Mapping):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def _write_json(path: Path, data: Mapping[str, Any]) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def _render_acceptance_markdown(manifest: Mapping[str, Any]) -> str:
    lines = ["# Evidence OS Cutover Acceptance", ""]
    summary = manifest.get("summary")
    if isinstance(summary, Mapping):
        lines.append("## Summary")
        for key in sorted(summary):
            lines.append(f"- {key}: `{summary[key]}`")
        lines.append("")
    lines.append("## Blockers")
    blockers = manifest.get("blockers") or ()
    if not blockers:
        lines.append("- none")
    for blocker in blockers:
        if not isinstance(blocker, Mapping):
            continue
        lines.append(f"- `{blocker.get('blocker_id')}`: {blocker.get('reason')}")
    lines.append("")
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    paths = run_cutover_acceptance(
        chain_audit_manifest_path=args.chain_audit,
        replay_acceptance_manifest_path=args.replay_acceptance,
        adversarial_acceptance_manifest_path=args.adversarial_acceptance,
        live_smoke_acceptance_manifest_path=args.live_smoke_acceptance,
        frozen_repeatability_acceptance_manifest_path=args.frozen_repeatability_acceptance,
        output_directory=args.output_directory,
        output_prefix=args.output_prefix,
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "DEFAULT_ADVERSARIAL_ACCEPTANCE",
    "DEFAULT_CHAIN_AUDIT",
    "DEFAULT_FROZEN_REPEATABILITY_ACCEPTANCE",
    "DEFAULT_LIVE_SMOKE_ACCEPTANCE",
    "DEFAULT_OUTPUT_DIRECTORY",
    "DEFAULT_REPLAY_ACCEPTANCE",
    "build_arg_parser",
    "build_cutover_acceptance_manifest",
    "main",
    "run_cutover_acceptance",
]
