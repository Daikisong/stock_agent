"""Build adversarial acceptance coverage for the Evidence OS preview chain."""

from __future__ import annotations

import argparse
import ast
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
DEFAULT_OUTPUT_DIRECTORY = "output/0621_agentic_replay"
DEFAULT_TESTS_ROOT = "tests"


ADVERSARIAL_CASES: tuple[Mapping[str, Any], ...] = (
    {
        "case_id": "01_other_company_clean_audit_target_customer_mention",
        "case_number": 1,
        "description": "Other company clean audit opinion with target mentioned as customer.",
        "required_behavior": "Do not attach another company's normal audit status to the target or create 4C.",
        "evidence_os_stages": (
            "claim_extraction",
            "target_temporal_adjudication",
            "primitive_mapping",
            "eligibility",
            "stage_court",
        ),
        "cli_path_segments": (
            "run_agentic_claim_extraction",
            "run_agentic_adjudication",
            "run_agentic_primitive_mapping",
            "run_agentic_eligibility",
            "run_agentic_stage_court",
        ),
        "representative_tests": (
            "test_worldex_audit_opinion_with_samsung_customer_mention_does_not_create_samsung_4c",
        ),
    },
    {
        "case_id": "02_target_historical_problem_latest_resolution",
        "case_number": 2,
        "description": "Target historical problem with later resolution evidence.",
        "required_behavior": "Resolved historical risk cannot become a current hard break.",
        "evidence_os_stages": ("target_temporal_adjudication", "lifecycle", "stage_court"),
        "cli_path_segments": ("run_agentic_adjudication", "run_agentic_stage_court"),
        "representative_tests": ("test_resolved_target_risk_claim_does_not_create_current_hard_break_or_4c",),
    },
    {
        "case_id": "03_target_historical_problem_current_open",
        "case_number": 3,
        "description": "Target historical problem with current OPEN official confirmation.",
        "required_behavior": "Current OPEN direct target risk with quorum may create a hard-break overlay.",
        "evidence_os_stages": ("target_temporal_adjudication", "source_quorum", "stage_court"),
        "cli_path_segments": ("run_agentic_adjudication", "run_agentic_stage_court"),
        "representative_tests": ("test_current_open_target_risk_with_quorum_can_create_hard_break_overlay",),
    },
    {
        "case_id": "04_subsidiary_parent_separation",
        "case_number": 4,
        "description": "Subsidiary and parent issue separation.",
        "required_behavior": "Do not default subsidiary or parent claims to target-direct score eligibility.",
        "evidence_os_stages": ("entity_registry", "target_temporal_adjudication", "eligibility"),
        "cli_path_segments": ("run_agentic_adjudication", "run_agentic_eligibility"),
        "representative_tests": (
            "test_subsidiary_and_parent_claims_are_not_default_score_eligible_for_target",
        ),
    },
    {
        "case_id": "05_customer_supplier_capa_separation",
        "case_number": 5,
        "description": "Customer or supplier CAPA confused with issuer CAPA.",
        "required_behavior": "Indirect customer or supplier CAPA is not issuer capacity or order support.",
        "evidence_os_stages": ("entity_relation", "primitive_mapping", "eligibility"),
        "cli_path_segments": ("run_agentic_primitive_mapping", "run_agentic_eligibility"),
        "representative_tests": (
            "test_customer_supplier_and_industry_claims_do_not_become_issuer_capacity_or_order_support",
        ),
    },
    {
        "case_id": "06_industry_demand_not_issuer_order",
        "case_number": 6,
        "description": "Industry demand confused with issuer order.",
        "required_behavior": "Industry demand is not issuer-level backlog, order, or capacity allocation.",
        "evidence_os_stages": ("entity_relation", "primitive_mapping", "eligibility"),
        "cli_path_segments": ("run_agentic_primitive_mapping", "run_agentic_eligibility"),
        "representative_tests": (
            "test_customer_supplier_and_industry_claims_do_not_become_issuer_capacity_or_order_support",
        ),
    },
    {
        "case_id": "07_claim_and_company_rebuttal",
        "case_number": 7,
        "description": "Positive or negative claim appears with company rebuttal.",
        "required_behavior": "Keep both sides and mark unresolved contradiction instead of scoring as clean support.",
        "evidence_os_stages": ("lifecycle_graph", "primitive_aggregation", "stage_court"),
        "cli_path_segments": ("run_agentic_primitive_aggregation", "run_agentic_stage_court"),
        "representative_tests": ("test_company_rebuttal_and_positive_claim_make_primitive_contradicted",),
    },
    {
        "case_id": "08_negated_contract_statement",
        "case_number": 8,
        "description": "Negated contract statement.",
        "required_behavior": "A statement that the company did not contract cannot support a positive contract primitive.",
        "evidence_os_stages": ("semantic_adjudication", "primitive_mapping", "eligibility"),
        "cli_path_segments": ("run_agentic_adjudication", "run_agentic_primitive_mapping", "run_agentic_eligibility"),
        "representative_tests": ("test_mapper_rejects_negated_contract_claim_as_positive_primitive_support",),
    },
    {
        "case_id": "09_clean_audit_but_going_concern_mixed",
        "case_number": 9,
        "description": "Clean audit and going-concern mixed wording.",
        "required_behavior": "Normal audit opinion is not risk, but mixed going-concern emphasis may map to risk.",
        "evidence_os_stages": ("semantic_adjudication", "primitive_mapping"),
        "cli_path_segments": ("run_agentic_adjudication", "run_agentic_primitive_mapping"),
        "representative_tests": (
            "test_mapper_rejects_normal_audit_opinion_as_accounting_risk_support",
            "test_mapper_allows_mixed_going_concern_audit_claim_as_accounting_risk_support",
        ),
    },
    {
        "case_id": "10_forecast_guidance_not_actual",
        "case_number": 10,
        "description": "Forecast or guidance confused with actual performance.",
        "required_behavior": "Forecast claims cannot support actual-profit primitives.",
        "evidence_os_stages": ("semantic_adjudication", "primitive_mapping"),
        "cli_path_segments": ("run_agentic_adjudication", "run_agentic_primitive_mapping"),
        "representative_tests": ("test_mapper_rejects_forecast_claim_as_actual_profit_support",),
    },
    {
        "case_id": "11_article_date_vs_event_date",
        "case_number": 11,
        "description": "Article publication date differs from event date.",
        "required_behavior": "Use event/effective date and as-of policy, not just article date.",
        "evidence_os_stages": ("anchor_validation", "lifecycle", "primitive_aggregation"),
        "cli_path_segments": ("run_agentic_claim_replay", "run_agentic_primitive_aggregation"),
        "representative_tests": ("test_primitive_aggregator_applies_contract_freshness_max_age",),
    },
    {
        "case_id": "12_latest_article_recounts_old_event",
        "case_number": 12,
        "description": "Recent article recounts an old event.",
        "required_behavior": "A recent article does not refresh an expired historical event by itself.",
        "evidence_os_stages": ("anchor_validation", "lifecycle", "primitive_aggregation"),
        "cli_path_segments": ("run_agentic_claim_replay", "run_agentic_primitive_aggregation"),
        "representative_tests": ("test_primitive_aggregator_applies_contract_freshness_max_age",),
    },
    {
        "case_id": "13_corrected_or_withdrawn_disclosure",
        "case_number": 13,
        "description": "Corrected or withdrawn disclosure.",
        "required_behavior": "Withdrawn or corrected disclosures are not current score-eligible support.",
        "evidence_os_stages": ("source_anchor_validation", "lifecycle", "eligibility"),
        "cli_path_segments": ("run_agentic_claim_replay", "run_agentic_eligibility"),
        "representative_tests": ("test_withdrawn_or_corrected_disclosure_is_not_score_eligible",),
    },
    {
        "case_id": "14_twenty_reuters_reposts",
        "case_number": 14,
        "description": "Twenty reposts of the same Reuters story.",
        "required_behavior": "Syndicated reposts count as one source family for quorum and score.",
        "evidence_os_stages": ("source_lineage_dedupe", "primitive_aggregation", "score_contribution"),
        "cli_path_segments": ("run_agentic_primitive_aggregation", "run_agentic_score_contribution"),
        "representative_tests": ("test_twenty_reuters_reposts_count_as_one_source_family",),
    },
    {
        "case_id": "15_same_url_modified_document",
        "case_number": 15,
        "description": "Same URL with modified document content.",
        "required_behavior": "Different content revisions get distinct document anchors and deterministic claim ids.",
        "evidence_os_stages": ("document_store", "anchor_validation", "claim_id_idempotency"),
        "cli_path_segments": ("run_agentic_claim_replay", "run_agentic_claim_extraction"),
        "representative_tests": ("test_same_url_revised_content_gets_new_document_anchor_and_claim_ids",),
    },
    {
        "case_id": "16_tampered_exact_quote",
        "case_number": 16,
        "description": "Tampered exact quote.",
        "required_behavior": "A quote not found at the anchor is quarantined before the ledger.",
        "evidence_os_stages": ("anchor_validation", "claim_replay"),
        "cli_path_segments": ("run_agentic_claim_replay",),
        "representative_tests": ("test_v2_orchestrator_quarantines_tampered_exact_quote_before_ledger",),
    },
    {
        "case_id": "17_snippet_only_fetch_failed",
        "case_number": 17,
        "description": "Snippet only with original fetch failure.",
        "required_behavior": "Snippet-only evidence is not score-eligible source support.",
        "evidence_os_stages": ("source_acquisition", "anchor_validation", "eligibility"),
        "cli_path_segments": ("run_agentic_claim_replay", "run_agentic_eligibility"),
        "representative_tests": (
            "test_agentic_document_inputs_do_not_promote_fetch_failed_snippet_only_result",
            "test_search_snippet_only_document_is_not_score_eligible",
        ),
    },
    {
        "case_id": "18_after_as_of_date_document",
        "case_number": 18,
        "description": "Document or availability after as_of_date.",
        "required_behavior": "Future-published or future-available evidence cannot support current scoring.",
        "evidence_os_stages": ("as_of_validation", "eligibility"),
        "cli_path_segments": ("run_agentic_claim_replay", "run_agentic_eligibility"),
        "representative_tests": (
            "test_future_source_is_not_score_eligible_even_if_claim_is_current",
            "test_future_available_at_is_not_score_eligible_even_if_published_date_is_past",
        ),
    },
    {
        "case_id": "19_reprocess_same_document_idempotent",
        "case_number": 19,
        "description": "Same document reprocessed twice.",
        "required_behavior": "Reprocessing identical input must not duplicate claims or change preview scoring.",
        "evidence_os_stages": ("append_only_ledger", "idempotency"),
        "cli_path_segments": ("run_agentic_claim_replay", "run_agentic_score_contribution", "run_agentic_stage_court"),
        "representative_tests": ("test_v2_orchestrator_reprocessing_same_document_is_idempotent",),
    },
    {
        "case_id": "20_llm_invented_primitive",
        "case_number": 20,
        "description": "LLM invents a primitive name.",
        "required_behavior": "Unknown primitive names are rejected by contract validation.",
        "evidence_os_stages": ("primitive_mapping", "contract_validation"),
        "cli_path_segments": ("run_agentic_primitive_mapping",),
        "representative_tests": ("test_mapper_rejects_new_primitive_name_from_llm",),
    },
    {
        "case_id": "21_source_proxy_only_not_score",
        "case_number": 21,
        "description": "source_proxy_only research row.",
        "required_behavior": "Proxy-only research rows can guide ontology but cannot become production score support.",
        "evidence_os_stages": ("source_replay_policy", "eligibility"),
        "cli_path_segments": ("run_agentic_claim_replay", "run_agentic_eligibility"),
        "representative_tests": (
            "test_source_proxy_only_document_is_not_score_eligible",
            "test_v2_orchestrator_quarantines_source_proxy_only_mapping_before_ledger",
        ),
    },
    {
        "case_id": "22_past_negative_without_current_hard_break",
        "case_number": 22,
        "description": "Past negative claim without current hard-break proof.",
        "required_behavior": "Historical or resolved negative claims cannot create current hard break or 4C.",
        "evidence_os_stages": ("lifecycle", "primitive_aggregation", "stage_court"),
        "cli_path_segments": ("run_agentic_primitive_aggregation", "run_agentic_stage_court"),
        "representative_tests": (
            "test_primitive_aggregator_does_not_promote_non_current_indirect_or_future_claims",
            "test_resolved_target_risk_claim_does_not_create_current_hard_break_or_4c",
        ),
    },
    {
        "case_id": "23_positive_claim_expired_or_superseded",
        "case_number": 23,
        "description": "Positive claim expired or superseded.",
        "required_behavior": "Expired or superseded positive claims cannot keep contributing points.",
        "evidence_os_stages": ("lifecycle", "primitive_aggregation", "score_contribution"),
        "cli_path_segments": ("run_agentic_primitive_aggregation", "run_agentic_score_contribution"),
        "representative_tests": (
            "test_primitive_aggregator_does_not_promote_non_current_indirect_or_future_claims",
            "test_primitive_aggregator_applies_contract_freshness_max_age",
        ),
    },
    {
        "case_id": "24_prompt_injection_document",
        "case_number": 24,
        "description": "Prompt injection text inside an untrusted document.",
        "required_behavior": "Document instructions stay untrusted data and generated follow-up queries are validated.",
        "evidence_os_stages": ("claim_extraction", "follow_up_planner", "query_validator"),
        "cli_path_segments": ("run_agentic_claim_extraction", "run_agentic_claim_replay"),
        "representative_tests": (
            "test_prompt_injection_markers_are_detected_as_untrusted_document_text",
            "test_follow_up_planner_validation_filters_duplicates_and_blocks_prompt_injection",
        ),
    },
)


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Evidence OS global adversarial acceptance coverage.")
    parser.add_argument("--chain-audit", default=DEFAULT_CHAIN_AUDIT)
    parser.add_argument("--replay-acceptance", default=DEFAULT_REPLAY_ACCEPTANCE)
    parser.add_argument("--tests-root", default=DEFAULT_TESTS_ROOT)
    parser.add_argument("--output-directory", default=DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument(
        "--output-prefix",
        default="c01_c36_combined_replacement_metadata_asof_source_recovery_v13_adversarial_acceptance",
    )
    return parser


def run_adversarial_acceptance(
    *,
    chain_audit_manifest_path: str | Path,
    replay_acceptance_manifest_path: str | Path,
    output_directory: str | Path,
    output_prefix: str = "c01_c36_combined_replacement_metadata_asof_source_recovery_v13_adversarial_acceptance",
    tests_root: str | Path | None = DEFAULT_TESTS_ROOT,
) -> Mapping[str, Path]:
    chain_audit = _read_json_mapping(Path(chain_audit_manifest_path))
    replay_acceptance = _read_json_mapping(Path(replay_acceptance_manifest_path))
    test_methods = discover_test_methods(Path(tests_root)) if tests_root else frozenset()
    manifest = build_adversarial_acceptance_manifest(
        chain_audit_manifest=chain_audit,
        replay_acceptance_manifest=replay_acceptance,
        test_methods=test_methods,
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


def build_adversarial_acceptance_manifest(
    *,
    chain_audit_manifest: Mapping[str, Any],
    replay_acceptance_manifest: Mapping[str, Any],
    test_methods: set[str] | frozenset[str],
) -> Mapping[str, Any]:
    rows: list[Mapping[str, Any]] = []
    missing_total = 0
    stage_names: set[str] = set()
    cli_segments: set[str] = set()

    for case in ADVERSARIAL_CASES:
        required_tests = tuple(str(name) for name in case["representative_tests"])
        missing_tests = tuple(name for name in required_tests if name not in test_methods)
        missing_total += len(missing_tests)
        evidence_os_stages = tuple(str(stage) for stage in case["evidence_os_stages"])
        cli_path_segments = tuple(str(segment) for segment in case["cli_path_segments"])
        stage_names.update(evidence_os_stages)
        cli_segments.update(cli_path_segments)
        row_ready = not missing_tests
        rows.append(
            {
                "case_id": case["case_id"],
                "case_number": case["case_number"],
                "description": case["description"],
                "required_behavior": case["required_behavior"],
                "evidence_os_stages": list(evidence_os_stages),
                "cli_path_segments": list(cli_path_segments),
                "representative_tests": list(required_tests),
                "representative_tests_present": not missing_tests,
                "missing_representative_tests": list(missing_tests),
                "acceptance_status": (
                    "blocked_missing_named_regression"
                    if missing_tests
                    else "covered_by_named_regression"
                ),
                "adversarial_case_ready": row_ready,
                "production_score_fixture": False,
                "production_stage_fixture": False,
            }
        )

    chain_summary = chain_audit_manifest.get("summary")
    if not isinstance(chain_summary, Mapping):
        chain_summary = {}
    replay_summary = replay_acceptance_manifest.get("summary")
    if not isinstance(replay_summary, Mapping):
        replay_summary = {}
    mapped_count = sum(1 for row in rows if row["representative_tests_present"])
    chain_ready = _chain_ready(chain_summary)
    replay_ready = _replay_ready(replay_summary)
    adversarial_acceptance_ready = (
        missing_total == 0
        and mapped_count == len(rows)
        and all(row["cli_path_segments"] for row in rows)
        and chain_ready
        and replay_ready
    )
    return {
        "schema_version": "e2r_adversarial_acceptance_manifest_v1",
        "source_chain_audit_schema_version": chain_audit_manifest.get("schema_version"),
        "source_replay_acceptance_schema_version": replay_acceptance_manifest.get("schema_version"),
        "summary": {
            "case_count": len(rows),
            "named_regression_covered_count": mapped_count,
            "missing_representative_test_count": missing_total,
            "evidence_os_stage_count": len(stage_names),
            "cli_path_segment_count": len(cli_segments),
            "all_cases_linked_to_cli_path": all(row["cli_path_segments"] for row in rows),
            "adversarial_acceptance_ready": adversarial_acceptance_ready,
            "production_cutover_ready": adversarial_acceptance_ready,
            "adversarial_acceptance_status": (
                "blocked_missing_named_regression"
                if missing_total
                else (
                    "adversarial_acceptance_ready"
                    if adversarial_acceptance_ready
                    else "covered_by_named_regression_pending_chain_or_replay_acceptance"
                )
            ),
            "chain_status": chain_summary.get("chain_status"),
            "chain_evidence_os_ready": chain_ready,
            "chain_production_cutover_ready": chain_summary.get("production_cutover_ready"),
            "replay_stage_preview_ready_count": replay_summary.get("stage_preview_ready_count"),
            "replay_unsupported_source_gap_count": replay_summary.get("unsupported_source_gap_count"),
            "replay_acceptance_ready": replay_ready,
            "replay_production_cutover_ready": replay_summary.get("production_cutover_ready"),
            "production_score_fixture_total": chain_summary.get("production_score_fixture_total", 0),
            "production_stage_fixture_total": chain_summary.get("production_stage_fixture_total", 0),
        },
        "rows": rows,
    }


def discover_test_methods(tests_root: Path) -> frozenset[str]:
    methods: set[str] = set()
    for path in tests_root.glob("test_*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        methods.update(
            node.name
            for node in ast.walk(tree)
            if isinstance(node, ast.FunctionDef) and node.name.startswith("test_")
        )
    return frozenset(methods)


def _read_json_mapping(path: Path) -> Mapping[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, Mapping):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def _write_json(path: Path, data: Mapping[str, Any]) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def _render_acceptance_markdown(manifest: Mapping[str, Any]) -> str:
    lines = ["# Evidence OS Adversarial Acceptance", ""]
    summary = manifest.get("summary")
    if isinstance(summary, Mapping):
        lines.append("## Summary")
        for key in sorted(summary):
            lines.append(f"- {key}: `{summary[key]}`")
        lines.append("")
    lines.append("## Cases")
    for row in manifest.get("rows") or ():
        if not isinstance(row, Mapping):
            continue
        lines.append(
            f"- `{row.get('case_id')}`: `{row.get('acceptance_status')}` "
            f"via `{', '.join(row.get('cli_path_segments') or [])}`"
        )
    lines.append("")
    lines.append("Production cutover is allowed only when chain, replay, adversarial, and live-smoke gates are all ready.")
    lines.append("")
    return "\n".join(lines)


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


def _int_or_zero(value: Any) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    paths = run_adversarial_acceptance(
        chain_audit_manifest_path=args.chain_audit,
        replay_acceptance_manifest_path=args.replay_acceptance,
        tests_root=args.tests_root,
        output_directory=args.output_directory,
        output_prefix=args.output_prefix,
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "ADVERSARIAL_CASES",
    "DEFAULT_CHAIN_AUDIT",
    "DEFAULT_OUTPUT_DIRECTORY",
    "DEFAULT_REPLAY_ACCEPTANCE",
    "DEFAULT_TESTS_ROOT",
    "build_adversarial_acceptance_manifest",
    "build_arg_parser",
    "discover_test_methods",
    "main",
    "run_adversarial_acceptance",
]
