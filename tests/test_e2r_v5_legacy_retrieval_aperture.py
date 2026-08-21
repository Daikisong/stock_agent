from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from e2r.research_brain.researcher_mode import (
    LEGACY_FACT_CLASSIFICATIONS,
    PHASE92_CAPABILITY_TRANSFERS,
    PHASE92_PASS,
    PHASE92_THRESHOLDS,
    build_legacy_aperture_feedback,
    build_legacy_retrieval_shadow_snapshot,
    build_legacy_shadow_source_graph,
    compile_phase92_legacy_retrieval_parity_audit,
    legacy_score_authority_leakage_paths,
    load_legacy_retrieval_shadow_snapshot,
    write_phase92_legacy_retrieval_parity_audit,
)


class E2RV5LegacyRetrievalApertureTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    @classmethod
    def setUpClass(cls) -> None:
        cls.snapshot = load_legacy_retrieval_shadow_snapshot(cls.ROOT)
        cls.audit = compile_phase92_legacy_retrieval_parity_audit(cls.ROOT)
        cls.targets = {
            str(row["target_id"]): row for row in cls.snapshot["targets"]
        }

    def test_committed_snapshot_and_audit_rebuild_or_fail_closed(self) -> None:
        committed = json.loads(
            (
                self.ROOT
                / "docs/operational/e2r_v5_legacy_retrieval_parity.json"
            ).read_text(encoding="utf-8")
        )
        try:
            rebuilt = build_legacy_retrieval_shadow_snapshot(self.ROOT)
        except FileNotFoundError as exc:
            # Clean packaging intentionally excludes the legacy raw output tree.
            # In that environment the committed audit is a historical receipt,
            # and the raw rebuild must fail closed instead of being reported as
            # a fresh clean-clone reproduction.
            self.assertIn("legacy shadow source artifacts missing", str(exc))
            self.assertIn("output/", str(exc))
            self.assertNotEqual(self.audit["status"], PHASE92_PASS)
            self.assertEqual(self.audit["critical_count_sum"], 1)
            self.assertEqual(
                self.audit["critical_counts"][
                    "shadow_snapshot_rebuild_mismatch_count"
                ],
                1,
            )
            self.assertEqual(committed["status"], PHASE92_PASS)
            self.assertEqual(committed["critical_count_sum"], 0)
            return
        self.assertEqual(rebuilt, self.snapshot)
        self.assertEqual(self.audit, committed)
        self.assertEqual(self.audit["status"], PHASE92_PASS)
        self.assertEqual(self.audit["critical_count_sum"], 0)
        self.assertEqual(
            self.audit["critical_counts"][
                "shadow_snapshot_rebuild_mismatch_count"
            ],
            0,
        )

    def test_both_required_shadow_targets_are_compared(self) -> None:
        self.assertEqual(set(self.targets), {"005930", "000660"})
        self.assertEqual(self.targets["005930"]["target_name"], "삼성전자")
        self.assertEqual(self.targets["000660"]["target_name"], "SK하이닉스")
        self.assertTrue(
            all(row["as_of_date"] == "2026-06-28" for row in self.targets.values())
        )
        self.assertTrue(all(row["shadow_mode"] for row in self.targets.values()))
        self.assertTrue(all(row["evaluation_only"] for row in self.targets.values()))

    def test_generated_queries_reconcile_without_becoming_templates(self) -> None:
        expected = {"005930": 20, "000660": 25}
        for target_id, target in self.targets.items():
            with self.subTest(target_id=target_id):
                queries = target["generated_queries"]
                self.assertEqual(len(queries), expected[target_id])
                self.assertEqual(
                    len(queries), target["phase_accounting"]["final_query_count"]
                )
                origins = Counter(row["query_origin"] for row in queries)
                self.assertEqual(
                    origins["LEGACY_DETERMINISTIC_TARGETED_SMOKE"], 6
                )
                self.assertEqual(
                    sum(row["llm_generated_in_legacy_run"] for row in queries),
                    expected[target_id] - 6,
                )
                self.assertTrue(all(row["shadow_only"] for row in queries))
                self.assertTrue(
                    all(not row["production_execution_allowed"] for row in queries)
                )
                self.assertTrue(
                    all(not row["query_template_authority"] for row in queries)
                )
                self.assertTrue(
                    all(not row["deterministic_fallback_query_used"] for row in queries)
                )

    def test_production_feedback_contains_failures_but_no_donor_query(self) -> None:
        for target_id, target in self.targets.items():
            with self.subTest(target_id=target_id):
                feedback = build_legacy_aperture_feedback(target)
                payload = json.dumps(
                    feedback.to_dict(), ensure_ascii=False, sort_keys=True
                )
                self.assertTrue(feedback.llm_query_regeneration_required)
                self.assertFalse(feedback.production_score_authority)
                self.assertEqual(feedback.literal_donor_queries, ())
                self.assertEqual(feedback.deterministic_query_templates, ())
                self.assertTrue(
                    feedback.score_gap_context["new_query_must_be_generated_by_llm"]
                )
                for query in target["generated_queries"]:
                    self.assertNotIn(query["literal_query"], payload)

    def test_search_result_and_fetch_aperture_are_accounted(self) -> None:
        expected = {
            "005930": {
                "observations": 1244,
                "maximum": 1250,
                "final": 1250,
                "fetches": 102,
                "reads": 19,
            },
            "000660": {
                "observations": 1800,
                "maximum": 1769,
                "final": 1667,
                "fetches": 81,
                "reads": 14,
            },
        }
        for target_id, target in self.targets.items():
            with self.subTest(target_id=target_id):
                values = expected[target_id]
                accounting = target["phase_accounting"]
                self.assertEqual(
                    len(target["search_result_observations"]), values["observations"]
                )
                self.assertEqual(
                    accounting["maximum_ranked_search_result_count"], values["maximum"]
                )
                self.assertEqual(
                    accounting["final_ranked_search_result_count"], values["final"]
                )
                self.assertEqual(
                    accounting["final_fetched_document_count"], values["fetches"]
                )
                self.assertEqual(
                    accounting["material_document_read_count"], values["reads"]
                )
                self.assertTrue(
                    all(
                        row["snippet_discovery_only"]
                        and not row["evidence_eligible"]
                        and not row["score_authority"]
                        for row in target["search_result_observations"]
                    )
                )

    def test_full_documents_require_body_or_structured_content_hash(self) -> None:
        expected = {
            "005930": {"evidence": 97, "verified": 50, "selected_verified": 14},
            "000660": {"evidence": 102, "verified": 59, "selected_verified": 11},
        }
        for target_id, target in self.targets.items():
            with self.subTest(target_id=target_id):
                documents = target["documents"]
                selected = target["selected_material_documents"]
                self.assertEqual(len(documents), expected[target_id]["evidence"])
                self.assertEqual(
                    sum(row["full_document_verified"] for row in documents),
                    expected[target_id]["verified"],
                )
                self.assertEqual(
                    sum(row["full_document_verified"] for row in selected),
                    expected[target_id]["selected_verified"],
                )
                self.assertTrue(
                    any(
                        set(row["safety_reasons"])
                        & {
                            "FULL_DOCUMENT_CACHE_MISS",
                            "SOURCE_PROXY_WITHOUT_FULL_DOCUMENT",
                        }
                        for row in selected
                    )
                )
                for document in documents:
                    if document["full_document_verified"]:
                        self.assertEqual(len(document["content_sha256"]), 64)
                        self.assertGreater(document["content_char_count"], 0)
                        self.assertFalse(document["safety_reasons"])
                    self.assertFalse(document["production_score_eligible"])

    def test_all_four_fact_classes_and_counterfacts_are_explicit(self) -> None:
        observed: Counter[str] = Counter()
        counter_count = 0
        for target in self.targets.values():
            facts = target["fact_comparisons"]
            classes = Counter(row["classification"] for row in facts)
            observed.update(classes)
            counter_count += sum(
                row["direction_candidate"] == "COUNTER" for row in facts
            )
            self.assertTrue(all(classes[name] > 0 for name in LEGACY_FACT_CLASSIFICATIONS))
            self.assertTrue(
                all(
                    row["duplicate_of_fact_id"]
                    for row in facts
                    if row["classification"] == "LEGACY_DUPLICATE_NOISE"
                )
            )
            self.assertTrue(
                all(
                    row["canonical_retrieval_status"]
                    == "AVAILABLE_AFTER_SAFE_APERTURE_TRANSFER"
                    for row in facts
                    if row["classification"]
                    == "LEGACY_VALID_FACT_MISSED_BY_CANONICAL"
                )
            )
        self.assertEqual(set(observed), set(LEGACY_FACT_CLASSIFICATIONS))
        self.assertGreater(counter_count, 0)

    def test_valid_facts_are_target_date_and_full_source_safe(self) -> None:
        for target_id, target in self.targets.items():
            documents = {
                row["document_id"]: row for row in target["documents"]
            }
            valid = [
                row
                for row in target["fact_comparisons"]
                if row["classification"]
                == "LEGACY_VALID_FACT_MISSED_BY_CANONICAL"
            ]
            self.assertTrue(valid)
            for fact in valid:
                with self.subTest(target_id=target_id, fact_id=fact["fact_id"]):
                    self.assertEqual(fact["target_id"], target_id)
                    self.assertFalse(fact["safety_reasons"])
                    self.assertTrue(
                        documents[fact["document_id"]]["full_document_verified"]
                    )
                    self.assertLessEqual(
                        fact["available_date"], target["as_of_date"]
                    )
                    self.assertFalse(fact["production_score_eligible"])
                    self.assertFalse(fact["legacy_mapping_authority"])

    def test_unsafe_facts_receive_exactly_zero_score_credit(self) -> None:
        for target in self.targets.values():
            unsafe = [
                row
                for row in target["fact_comparisons"]
                if row["classification"] == "LEGACY_UNSAFE_FACT"
            ]
            self.assertTrue(unsafe)
            self.assertTrue(all(row["safety_reasons"] for row in unsafe))
            self.assertTrue(all(row["legacy_score_credit"] == 0.0 for row in unsafe))
            self.assertTrue(
                all(row["canonical_retrieval_status"] == "QUARANTINED" for row in unsafe)
            )
        self.assertEqual(
            self.audit["metric_values"]["legacy_unsafe_fact_score_credit"], 0.0
        )

    def test_legacy_score_stage_and_mapping_fields_are_actually_stripped(self) -> None:
        self.assertGreater(
            sum(
                row["legacy_score_stage_or_mapping_field_count_seen_and_stripped"]
                for row in self.targets.values()
            ),
            0,
        )
        self.assertEqual(legacy_score_authority_leakage_paths(self.snapshot), ())
        self.assertFalse(self.snapshot["legacy_score_or_stage_authority"])
        self.assertFalse(self.snapshot["canonical_stage_authority"])
        self.assertFalse(
            self.audit["safe_legacy_facts_are_production_score_evidence"]
        )
        self.assertTrue(
            self.audit["canonical_semantic_revalidation_required"]
        )
        self.assertFalse(
            self.snapshot["frozen_observation_is_production_readiness_evidence"]
        )
        self.assertTrue(
            self.snapshot[
                "canonical_baseline_is_retrospective_as_of_filtered"
            ]
        )

    def test_canonical_shadow_graph_preserves_retrieval_and_no_score_authority(self) -> None:
        for target_id, target in self.targets.items():
            with self.subTest(target_id=target_id):
                graph = build_legacy_shadow_source_graph(target)
                node_counts = Counter(row.node_type for row in graph.nodes)
                self.assertEqual(
                    node_counts["SHADOW_QUERY"], len(target["generated_queries"])
                )
                self.assertEqual(
                    node_counts["SEARCH_CANDIDATE"],
                    len(target["search_result_observations"]),
                )
                self.assertEqual(
                    node_counts["DOCUMENT"],
                    sum(row["full_document_verified"] for row in target["documents"]),
                )
                self.assertFalse(graph.score_authority)
                for node in graph.nodes:
                    if node.node_type == "SHADOW_QUERY":
                        self.assertTrue(node.metadata["shadow_only"])
                        self.assertFalse(
                            node.metadata["production_execution_allowed"]
                        )
                        self.assertFalse(node.metadata["query_template_authority"])
                    if node.node_type == "SEARCH_CANDIDATE":
                        self.assertFalse(node.evidence_eligible)

    def test_six_capabilities_are_transferred_to_generic_canonical_paths(self) -> None:
        expected = {
            "QUERY_EXPANSION",
            "NAVER_DISCOVERY",
            "DOCUMENT_RANKER",
            "PAGE_FETCH",
            "THEME_BRIDGE",
            "SCORE_GAP_FEEDBACK",
        }
        self.assertEqual(
            {row["capability_id"] for row in PHASE92_CAPABILITY_TRANSFERS},
            expected,
        )
        proof = self.audit["capability_runtime_proof"]
        self.assertTrue(proof["query_expansion_llm_owned"])
        self.assertTrue(proof["theme_context_parameter_present"])
        self.assertTrue(proof["score_gap_context_parameter_present"])

    def test_acceptance_recall_is_above_threshold(self) -> None:
        metrics = self.audit["metric_values"]
        self.assertGreater(metrics["legacy_valid_material_fact_count"], 0)
        self.assertGreaterEqual(
            metrics["legacy_valid_material_fact_recall"],
            PHASE92_THRESHOLDS["legacy_valid_material_fact_recall_min"],
        )
        self.assertEqual(metrics["legacy_valid_material_fact_recall"], 1.0)

    def test_nonzero_unsafe_credit_makes_the_acceptance_fail(self) -> None:
        mutated = json.loads(json.dumps(self.snapshot, ensure_ascii=False))
        unsafe = next(
            row
            for target in mutated["targets"]
            for row in target["fact_comparisons"]
            if row["classification"] == "LEGACY_UNSAFE_FACT"
        )
        unsafe["legacy_score_credit"] = 0.1
        _refresh_snapshot_hash(mutated)
        audit = _compile_mutated_snapshot(self.ROOT, mutated)
        self.assertEqual(
            audit["critical_counts"]["legacy_unsafe_fact_score_credit_count"], 1
        )
        self.assertNotEqual(audit["status"], PHASE92_PASS)

    def test_missing_full_document_cannot_count_as_canonical_recall(self) -> None:
        mutated = json.loads(json.dumps(self.snapshot, ensure_ascii=False))
        target = mutated["targets"][0]
        valid = next(
            row
            for row in target["fact_comparisons"]
            if row["classification"]
            == "LEGACY_VALID_FACT_MISSED_BY_CANONICAL"
        )
        document = next(
            row
            for row in target["documents"]
            if row["document_id"] == valid["document_id"]
        )
        document["full_document_verified"] = False
        document["content_sha256"] = None
        document["safety_reasons"] = ["FULL_DOCUMENT_CACHE_MISS"]
        _refresh_snapshot_hash(mutated)
        audit = _compile_mutated_snapshot(self.ROOT, mutated)
        self.assertGreater(
            audit["critical_counts"]["valid_fact_without_full_document_count"],
            0,
        )
        self.assertGreater(
            audit["critical_counts"][
                "valid_fact_not_in_canonical_graph_count"
            ],
            0,
        )
        self.assertLess(
            audit["metric_values"]["legacy_valid_material_fact_recall"],
            1.0,
        )
        self.assertNotEqual(audit["status"], PHASE92_PASS)

    def test_raw_score_key_tamper_is_rejected_at_snapshot_boundary(self) -> None:
        mutated = json.loads(json.dumps(self.snapshot, ensure_ascii=False))
        mutated["targets"][0]["generated_queries"][0]["stage"] = "3-Green"
        _refresh_snapshot_hash(mutated)
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            path = root / "configs/e2r_v5_legacy_retrieval_shadow_snapshot_v1.json"
            path.parent.mkdir(parents=True)
            path.write_text(
                json.dumps(mutated, ensure_ascii=False, indent=2, sort_keys=True)
                + "\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "score/Stage/mapping"):
                load_legacy_retrieval_shadow_snapshot(root)

    def test_writer_emits_the_same_phase92_audit(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            path = write_phase92_legacy_retrieval_parity_audit(
                self.ROOT, output_path=Path(tmpdir) / "phase92.json"
            )
            written = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(written, self.audit)

    def test_production_module_contains_no_samsung_or_hynix_branch(self) -> None:
        text = (
            self.ROOT
            / "src/e2r/research_brain/researcher_mode/legacy_retrieval_aperture.py"
        ).read_text(encoding="utf-8")
        for token in ("005930", "000660", "삼성전자", "SK하이닉스"):
            self.assertNotIn(token, text)


def _refresh_snapshot_hash(snapshot: dict) -> None:
    snapshot.pop("snapshot_payload_sha256", None)
    encoded = json.dumps(
        snapshot,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    snapshot["snapshot_payload_sha256"] = hashlib.sha256(encoded).hexdigest()


def _compile_mutated_snapshot(
    source_root: Path, snapshot: dict
) -> dict:
    with tempfile.TemporaryDirectory() as tmpdir:
        root = Path(tmpdir)
        config_path = (
            root / "configs/e2r_v5_legacy_retrieval_shadow_sources_v1.json"
        )
        snapshot_path = (
            root / "configs/e2r_v5_legacy_retrieval_shadow_snapshot_v1.json"
        )
        config_path.parent.mkdir(parents=True)
        config_path.write_text(
            (
                source_root
                / "configs/e2r_v5_legacy_retrieval_shadow_sources_v1.json"
            ).read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        snapshot_path.write_text(
            json.dumps(snapshot, ensure_ascii=False, indent=2, sort_keys=True)
            + "\n",
            encoding="utf-8",
        )
        return dict(compile_phase92_legacy_retrieval_parity_audit(root))


if __name__ == "__main__":
    unittest.main()
