import json
import tempfile
import unittest
from pathlib import Path

from e2r.research_brain.artifact_discovery import discover_research_artifacts
from e2r.research_brain.candidate_context import candidate_event_from_mapping
from e2r.research_brain.evidence_os_bridge import audit_plan_does_not_mutate_evidence_os
from e2r.research_brain.investigation_planner import build_research_brain_plan
from e2r.research_brain.memory_acceptance import build_planner_replay_results
from e2r.research_brain.memory_compiler import compile_research_memory
from e2r.research_brain.memory_leakage_audit import audit_memory_leakage
from e2r.research_brain.memory_store import ResearchMemoryStore
from e2r.research_brain.research_artifact_parser import parse_research_artifact
from e2r.research_brain.research_row_normalizer import normalize_research_rows
from e2r.research_brain.schemas import (
    MemoryType,
    ResearchMemoryRecord,
    SourceQualityClass,
    SourceTask,
    SourceTaskType,
    UsagePolicy,
    deterministic_id,
)
from e2r.research_brain.source_quality_classifier import classify_source_quality
from e2r.research_brain.source_task_bridge import audit_source_tasks


class ResearchBrainV1Tests(unittest.TestCase):
    def test_artifact_discovery_parser_and_normalizer_classify_source_proxy_safely(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            docs = root / "docs"
            docs.mkdir()
            path = docs / "C28_research.md"
            path.write_text(
                "\n".join(
                    [
                        "# C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
                        "",
                        "| canonical_archetype_id | source_proxy_only | evidence_url_pending | primitive_ids | note |",
                        "| --- | --- | --- | --- | --- |",
                        "| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | true | true | retention_or_renewal_bridge | security keyword only, ARR/RPO missing |",
                    ]
                ),
                encoding="utf-8",
            )
            inventory = discover_research_artifacts(root=root, discovery_roots=("docs",))
            self.assertEqual(len(inventory), 1)
            rows = parse_research_artifact(path, inventory[0])
            records = normalize_research_rows(rows)
            self.assertTrue(records)
            self.assertTrue(any(record.memory_type == MemoryType.SOURCE_GAP.value for record in records))
            self.assertEqual(sum(record.runtime_score_eligible for record in records), 0)
            self.assertEqual(sum(record.usage_policy.allowed_for_score_contribution for record in records), 0)
            self.assertTrue(
                all(
                    record.source_quality_class
                    in {
                        SourceQualityClass.C_SOURCE_PROXY_ONTOLOGY_ONLY.value,
                        SourceQualityClass.D_PRICE_PATH_ONLY_OR_FUTURE_LEAKAGE_RISK.value,
                    }
                    for record in records
                    if record.source_proxy_only or record.evidence_url_pending
                )
            )

    def test_memory_store_import_is_idempotent_and_profiles_exist(self):
        record = _record("C06_HBM_MEMORY_CUSTOMER_CAPACITY", MemoryType.SOURCE_ROUTE_PATTERN.value)
        with tempfile.TemporaryDirectory() as temp_dir:
            store = ResearchMemoryStore(Path(temp_dir) / "memory.jsonl")
            first = store.add_records((record,))
            second = store.add_records((record,))
            self.assertEqual(first["added_count"], 1)
            self.assertEqual(second["added_count"], 0)
            profile = store.get_archetype_profile("C06_HBM_MEMORY_CUSTOMER_CAPACITY")
            self.assertEqual(profile.memory_record_count, 1)
            self.assertIn("DART", profile.source_routes)

    def test_planner_outputs_bounded_source_tasks_and_no_score_or_stage_fields(self):
        records = (
            _record("C06_HBM_MEMORY_CUSTOMER_CAPACITY", MemoryType.SOURCE_ROUTE_PATTERN.value),
            _record("C06_HBM_MEMORY_CUSTOMER_CAPACITY", MemoryType.GREEN_BLOCKER.value),
        )
        with tempfile.TemporaryDirectory() as temp_dir:
            store = ResearchMemoryStore(Path(temp_dir) / "memory.jsonl")
            store.add_records(records)
            event = candidate_event_from_mapping(
                {
                    "symbol": "000660",
                    "company_name": "SK하이닉스",
                    "as_of_date": "2026-06-29",
                    "reason_codes": ["DISC_SUPPLY_CONTRACT"],
                    "candidate_source_path": "official_cheap_scan",
                    "production_candidate": True,
                }
            )
            plan = build_research_brain_plan(
                candidate_event=event,
                memory_store=store,
                archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            )
            bridge = audit_plan_does_not_mutate_evidence_os((plan,))
            source_audit = audit_source_tasks(plan.source_tasks)
            self.assertEqual(bridge["research_brain_score_output_key_count"], 0)
            self.assertEqual(bridge["research_brain_direct_feature_input_mutation_count"], 0)
            self.assertGreater(len(plan.source_tasks), 0)
            self.assertEqual(source_audit["unbounded_source_task_count"], 0)
            self.assertEqual(source_audit["FCF_gap_sent_to_news_count"], 0)

    def test_leakage_audit_blocks_future_outcomes_from_extractor(self):
        record = _record(
            "C24_BIO_TRIAL_DATA_EVENT_RISK",
            MemoryType.SCORE_WEIGHT_SUPPORT.value,
            source_quality_class=SourceQualityClass.D_PRICE_PATH_ONLY_OR_FUTURE_LEAKAGE_RISK.value,
        )
        audit = audit_memory_leakage(records=(record,), extraction_prompts=("current document only",))
        self.assertTrue(audit["summary"]["leakage_audit_pass"])
        self.assertEqual(audit["summary"]["future_outcome_in_extraction_prompt_count"], 0)
        bad = audit_memory_leakage(records=(record,), extraction_prompts=("MFE 90d was high",))
        self.assertFalse(bad["summary"]["leakage_audit_pass"])

    def test_compile_memory_builds_inventory_and_replay_acceptance_from_small_repo(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            docs = root / "docs"
            docs.mkdir()
            for archetype_id in (
                "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
                "C15_MATERIAL_SPREAD_SUPERCYCLE",
                "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
                "C24_BIO_TRIAL_DATA_EVENT_RISK",
                "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
            ):
                (docs / f"{archetype_id}.jsonl").write_text(
                    json.dumps(
                        {
                            "canonical_archetype_id": archetype_id,
                            "source_url": "https://example.com/source",
                            "quote": "official source route and green blocker",
                            "primitive_ids": ["source_quorum"],
                        },
                        ensure_ascii=False,
                    )
                    + "\n",
                    encoding="utf-8",
                )
            store_path = root / "memory.jsonl"
            manifest = compile_research_memory(
                repo_root=root,
                output_store_path=store_path,
                discovery_roots=("docs",),
                max_rows_per_artifact=10,
                max_total_compiled_rows=100,
            )
            self.assertEqual(manifest["summary"]["scanned_file_count"], 6)
            self.assertEqual(manifest["summary"]["frozen_import_duplicate_growth_count"], 0)
            store = ResearchMemoryStore(store_path)
            replay = build_planner_replay_results(store)
            self.assertTrue(replay["summary"]["planner_replay_pass"])

    def test_source_quality_classifier_respects_url_and_pending_rows(self):
        self.assertEqual(
            classify_source_quality({"source_url": "https://example.com/a", "quote": "anchor"}),
            SourceQualityClass.A_URL_BACKED_REPLAY_READY,
        )
        self.assertEqual(
            classify_source_quality({"source_proxy_only": True, "source_url": "https://example.com/a"}),
            SourceQualityClass.C_SOURCE_PROXY_ONTOLOGY_ONLY,
        )


def _record(
    archetype_id: str,
    memory_type: str,
    *,
    source_quality_class: str = SourceQualityClass.A_URL_BACKED_REPLAY_READY.value,
) -> ResearchMemoryRecord:
    payload = {"archetype_id": archetype_id, "memory_type": memory_type, "quality": source_quality_class}
    return ResearchMemoryRecord(
        record_id=deterministic_id("TESTMEM", payload),
        source_artifact_path="fixture.md",
        source_artifact_sha256="abc",
        source_artifact_type="md",
        source_line_or_span="L1",
        memory_type=memory_type,
        canonical_archetype_id=archetype_id,
        large_sector_id="L2_AI_SEMICONDUCTOR_ELECTRONICS",
        primitive_ids=("cash_or_revision_conversion", "source_quorum"),
        free_source_route_hints=("DART", "IR"),
        preferred_source_classes=("DART", "IR"),
        source_quality_class=source_quality_class,
        source_quality=source_quality_class.lower(),
        fixture_usable=source_quality_class == SourceQualityClass.A_URL_BACKED_REPLAY_READY.value,
        usage_policy=UsagePolicy(allowed_for_replay_fixture=True),
        dedupe_key=deterministic_id("TESTDEDUP", payload),
    )


class ResearchBrainSchemaGuardTests(unittest.TestCase):
    def test_source_task_rejects_unbounded_budget(self):
        with self.assertRaises(ValueError):
            SourceTask(
                task_id="bad",
                candidate_event_id="event",
                symbol="000000",
                company_name="bad",
                archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                primitive_gap="cash_or_revision_conversion",
                task_type=SourceTaskType.POSITIVE_VERIFY.value,
                preferred_source_classes=("DART",),
                max_fetches=0,
            )


if __name__ == "__main__":
    unittest.main()
