"""Run post-Checkpoint20 Korea live-lite shadow validation."""

from __future__ import annotations

import argparse
import os
from dataclasses import dataclass, field, fields, is_dataclass
from datetime import date, datetime
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.cli.review_korea_run import KoreaRunReviewSummary, build_review_summary, render_review_summary
from e2r.pipeline.korea_live_lite import KoreaLiveLiteConfig, KoreaLiveLiteResult, KoreaLiveLiteRunner


UNDERSTOOD_SOURCE_MODES = {"fixture", "request_only", "live_executed", "fallback", "disabled_optional", "not_configured"}


@dataclass(frozen=True)
class ShadowGateResult:
    """Gate evaluation for one shadow validation step."""

    passed: bool
    reasons: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class ShadowStepResult:
    """One live-lite run plus its review and gate result."""

    name: str
    result: KoreaLiveLiteResult
    review: KoreaRunReviewSummary
    gate: ShadowGateResult


@dataclass(frozen=True)
class ShadowValidationSummary:
    """All steps from a shadow validation run."""

    as_of_date: date
    fixture_mode: bool
    live_enabled: bool
    standard_shadow_requested: bool
    standard_shadow_ran: bool
    steps: tuple[ShadowStepResult, ...]
    output_directory: Path
    summary_path: Path | None = None

    @property
    def passed(self) -> bool:
        return all(step.gate.passed for step in self.steps)


def run_shadow_validation(
    *,
    as_of_date: date,
    output_directory: str | Path = "output",
    live_enabled: bool = False,
    fixture_mode: bool = True,
    run_standard_shadow: bool = False,
    targeted_smoke_company: str = "삼성전자",
    targeted_smoke_symbol: str = "005930",
    targeted_smoke_queries: Sequence[str] = ("삼성전자 수주잔고",),
    runner: KoreaLiveLiteRunner | None = None,
    write_summary: bool = True,
) -> ShadowValidationSummary:
    """Run tiny, targeted smoke, small, and optionally standard_shadow.

    Live execution only happens when ``live_enabled=True`` and
    ``fixture_mode=False``.
    """

    live_runner = runner or KoreaLiveLiteRunner()
    output_root = Path(output_directory)
    validation_root = output_root / "korea_shadow_validation"
    steps: list[ShadowStepResult] = []

    tiny_output = validation_root / "tiny"
    tiny = live_runner.run(
        KoreaLiveLiteConfig.smoke_preset(
            "tiny",
            as_of_date=as_of_date,
            output_directory=tiny_output,
            fixture_mode=fixture_mode,
            live_enabled=live_enabled,
        )
    )
    steps.append(_step("tiny", tiny, tiny_output))

    smoke_output = validation_root / "targeted_smoke"
    smoke = live_runner.run(
        KoreaLiveLiteConfig.smoke_preset(
            "tiny",
            as_of_date=as_of_date,
            output_directory=smoke_output,
            fixture_mode=fixture_mode,
            live_enabled=live_enabled,
            targeted_smoke_enabled=True,
            targeted_smoke_company=targeted_smoke_company,
            targeted_smoke_symbol=targeted_smoke_symbol,
            targeted_smoke_queries=tuple(targeted_smoke_queries),
        )
    )
    steps.append(_step("targeted_smoke", smoke, smoke_output, require_smoke_excluded=True))

    if steps[-1].gate.passed and steps[0].gate.passed:
        small_output = validation_root / "small"
        small = live_runner.run(
            KoreaLiveLiteConfig.smoke_preset(
                "small",
                as_of_date=as_of_date,
                output_directory=small_output,
                fixture_mode=fixture_mode,
                live_enabled=live_enabled,
            )
        )
        steps.append(_step("small", small, small_output))

    standard_shadow_ran = False
    if run_standard_shadow and all(step.gate.passed for step in steps):
        standard_output = validation_root / "standard_shadow"
        standard = live_runner.run(
            KoreaLiveLiteConfig.smoke_preset(
                "standard_shadow",
                as_of_date=as_of_date,
                output_directory=standard_output,
                fixture_mode=fixture_mode,
                live_enabled=live_enabled,
            )
        )
        steps.append(_step("standard_shadow", standard, standard_output))
        standard_shadow_ran = True

    summary = ShadowValidationSummary(
        as_of_date=as_of_date,
        fixture_mode=fixture_mode,
        live_enabled=live_enabled,
        standard_shadow_requested=run_standard_shadow,
        standard_shadow_ran=standard_shadow_ran,
        steps=tuple(steps),
        output_directory=output_root,
    )
    if not write_summary:
        return summary
    summary_dir = validation_root
    summary_dir.mkdir(parents=True, exist_ok=True)
    summary_path = summary_dir / f"{as_of_date.isoformat()}_summary.md"
    summary_path.write_text(render_shadow_validation_summary(summary), encoding="utf-8")
    return ShadowValidationSummary(
        as_of_date=summary.as_of_date,
        fixture_mode=summary.fixture_mode,
        live_enabled=summary.live_enabled,
        standard_shadow_requested=summary.standard_shadow_requested,
        standard_shadow_ran=summary.standard_shadow_ran,
        steps=summary.steps,
        output_directory=summary.output_directory,
        summary_path=summary_path,
    )


def render_shadow_validation_summary(summary: ShadowValidationSummary) -> str:
    """Render markdown summary for checkpoint review."""

    lines = [
        "# Korea Shadow Validation",
        "",
        f"- as_of_date: {summary.as_of_date.isoformat()}",
        f"- fixture_mode: {summary.fixture_mode}",
        f"- live_enabled: {summary.live_enabled}",
        f"- standard_shadow_requested: {summary.standard_shadow_requested}",
        f"- standard_shadow_ran: {summary.standard_shadow_ran}",
        f"- overall_gate: {'pass' if summary.passed else 'fail'}",
        "",
    ]
    for step in summary.steps:
        lines.extend(
            [
                f"## {step.name}",
                "",
                f"- gate: {'pass' if step.gate.passed else 'fail'}",
                f"- gate_reasons: {', '.join(step.gate.reasons) if step.gate.reasons else 'none'}",
                f"- candidates: {step.review.total_candidates}",
                f"- event_search: {step.review.event_search_count}",
                f"- deep_research: {step.review.deep_research_count}",
                f"- live_requests_failed: {step.review.live_requests_failed}",
                f"- source_modes: {_mapping_text(step.review.source_modes)}",
                "",
                "```text",
                render_review_summary(step.review).strip(),
                "```",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run Korea live-lite shadow validation gates.")
    parser.add_argument("--date", required=True, help="Run date in YYYY-MM-DD format")
    parser.add_argument("--output-directory", default="output", help="Output root")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--fixture", action="store_true", help="Run fixture mode without live HTTP")
    mode.add_argument("--live", action="store_true", help="Run live-lite mode with credentials")
    parser.add_argument("--standard-shadow", action="store_true", help="Run standard_shadow only if earlier gates pass")
    parser.add_argument("--targeted-smoke-symbol", default="005930")
    parser.add_argument("--targeted-smoke-company", default="삼성전자")
    parser.add_argument("--targeted-smoke-query", action="append", default=None)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    live_enabled = bool(args.live)
    fixture_mode = not live_enabled if not args.fixture else True
    summary = run_shadow_validation(
        as_of_date=date.fromisoformat(args.date),
        output_directory=args.output_directory,
        live_enabled=live_enabled,
        fixture_mode=fixture_mode,
        run_standard_shadow=args.standard_shadow,
        targeted_smoke_company=args.targeted_smoke_company,
        targeted_smoke_symbol=args.targeted_smoke_symbol,
        targeted_smoke_queries=tuple(args.targeted_smoke_query or (f"{args.targeted_smoke_company} 수주잔고",)),
    )
    print(render_shadow_validation_summary(summary), end="")
    if summary.summary_path:
        print(f"summary: {summary.summary_path}")
    return 0 if summary.passed else 1


def _step(
    name: str,
    result: KoreaLiveLiteResult,
    output_root: Path,
    *,
    require_smoke_excluded: bool = False,
) -> ShadowStepResult:
    review = build_review_summary(output_root, result.as_of_date.isoformat())
    gate = evaluate_shadow_gate(result, output_root, require_smoke_excluded=require_smoke_excluded)
    return ShadowStepResult(name=name, result=result, review=review, gate=gate)


def evaluate_shadow_gate(
    result: KoreaLiveLiteResult,
    output_root: str | Path,
    *,
    require_smoke_excluded: bool = False,
) -> ShadowGateResult:
    reasons: list[str] = []
    run_log = result.run_log
    if _api_key_leaks(output_root):
        reasons.append("api_key_leak_detected")
    unknown_modes = sorted(set(run_log.source_modes.values()) - UNDERSTOOD_SOURCE_MODES)
    if unknown_modes:
        reasons.append(f"unknown_source_modes:{','.join(unknown_modes)}")
    if run_log.live_requests_failed > max(3, run_log.live_requests_executed * 0.10):
        reasons.append("live_requests_failed_excessive")
    if run_log.rate_limit_skips and not run_log.skipped_queries:
        reasons.append("rate_limit_skips_unexplained")
    routine_audit_count = int(run_log.audit_summary.get("routine_audit_count") or 0)
    if routine_audit_count > 100:
        reasons.append("routine_audit_count_flooding")
    high_signal_audit_count = int(run_log.audit_summary.get("high_signal_audit_count") or 0)
    if high_signal_audit_count > 500:
        reasons.append("high_signal_audit_count_unbounded")
    if require_smoke_excluded and not run_log.targeted_smoke_results:
        reasons.append("targeted_smoke_missing")
    if any(item.candidate_source_path == "targeted_smoke" for item in result.candidates):
        reasons.append("targeted_smoke_in_production_candidates")
    if any(stage.stage.value == "3-Green" and stage.grade in {"cross-evidence-required", "parser-audit-blocked"} for stage in result.stages):
        reasons.append("unsafe_stage3_green_present")
    hard_audit_symbols = {finding.symbol for finding in run_log.audit_findings if finding.severity == "hard" or finding.suggested_action == "block_green"}
    green_symbols = {stage.symbol for stage in result.stages if stage.stage.value == "3-Green"}
    if hard_audit_symbols & green_symbols:
        reasons.append("hard_audit_green_present")
    return ShadowGateResult(passed=not reasons, reasons=tuple(reasons))


def _api_key_leaks(output_root: str | Path) -> bool:
    secrets = tuple(value for value in _secret_values_from_env() if value and len(value) >= 6)
    if not secrets:
        return False
    root = Path(output_root)
    if not root.exists():
        return False
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".json", ".md", ".txt", ".xml"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if any(secret in text for secret in secrets):
            return True
    return False


def _secret_values_from_env() -> tuple[str, ...]:
    return tuple(
        os.environ.get(name, "")
        for name in (
            "OPENDART_API_KEY",
            "NAVER_CLIENT_ID",
            "NAVER_CLIENT_SECRET",
            "DATA_GO_KR_SERVICE_KEY",
            "KRX_OPENAPI_KEY",
        )
    )


def _mapping_text(value: Mapping[str, Any]) -> str:
    return ", ".join(f"{key}={item}" for key, item in value.items()) if value else "none"


def _jsonable(value: Any) -> Any:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, Path):
        return str(value)
    if is_dataclass(value):
        return {field.name: _jsonable(getattr(value, field.name)) for field in fields(value)}
    if isinstance(value, Mapping):
        return {str(key): _jsonable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, set, frozenset)):
        return [_jsonable(item) for item in value]
    return value


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "ShadowGateResult",
    "ShadowStepResult",
    "ShadowValidationSummary",
    "build_arg_parser",
    "evaluate_shadow_gate",
    "main",
    "render_shadow_validation_summary",
    "run_shadow_validation",
]
