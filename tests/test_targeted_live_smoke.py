from __future__ import annotations

import json
import unittest
from datetime import date, datetime
from pathlib import Path
from types import SimpleNamespace

from e2r.research.search_provider import SearchResult
from e2r.research_brain.replay.source_backed import HistoricalHttpResponse
from e2r.research_brain.runtime.live_materialization import select_sector_samples
from e2r.research_brain.runtime.live_materialization.targeted_smoke import (
    IssuerNewsroomFeedSearchProvider,
    _full_thesis_status,
    _issuer_site_query_validation_error,
    _merge_evidence_documents,
    _pending_atomic_decision,
    _published_date_from_text,
    _search_and_fetch,
    _search_result_matches_llm_query,
    _select_claim_documents,
)


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "configs" / "e2r_targeted_live_smoke_v1.json"


class TargetedLiveSmokeTest(unittest.TestCase):
    def test_operational_phase35_report_passes_with_exact_pending_not_forced_green(self) -> None:
        report = json.loads(
            (
                ROOT
                / "docs/operational/e2r_live_targeted_smoke_report.json"
            ).read_text(encoding="utf-8")
        )

        self.assertEqual(report["status"], "TARGETED_LIVE_SMOKE_PASS")
        self.assertEqual(report["critical_count_sum"], 0)
        self.assertEqual(
            {item["symbol"] for item in report["mandatory_targets"]},
            {"005930", "000660"},
        )
        self.assertEqual(len(report["sector_samples"]), 9)
        self.assertTrue(report["safety"]["accepted_claim_provenance_contract_complete"])
        for target in report["mandatory_targets"]:
            self.assertEqual(
                target["daily_event_status"]["status"],
                "PARTIAL_OFFICIAL_EVENT_NOT_FULL_THESIS",
            )
            self.assertFalse(target["daily_event_status"]["called_hbm_full_thesis"])
            self.assertTrue(target["fetched_documents"])
            self.assertEqual(target["score_type"], "NO_SCORE")
            self.assertFalse(target["score_valid"])
            self.assertEqual(target["canonical_stage"], "0")
            self.assertTrue(target["full_thesis_status"]["status"].endswith("PENDING"))
    def test_current_krx_universe_yields_one_rule_sample_for_every_large_sector(self) -> None:
        config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        universe = _read_jsonl(
            ROOT / "output/live_materialization/2026-07-10/universe_eligible.jsonl"
        )

        selected = select_sector_samples(
            as_of_date="2026-07-10",
            universe=universe,
            candidate_pools=config["sector_candidate_pools"],
        )

        self.assertEqual([item["sector"] for item in selected], [f"L{i}" for i in range(1, 10)])
        self.assertEqual(len({item["symbol"] for item in selected}), 9)
        self.assertTrue(all(item["selection_hash"] for item in selected))

    def test_config_contains_questions_and_budgets_but_no_literal_search_queries(self) -> None:
        config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))

        self.assertNotIn("literal_queries", config)
        self.assertNotIn("queries", config)
        self.assertEqual(
            [item["symbol"] for item in config["mandatory_targets"]],
            ["005930", "000660"],
        )
        self.assertLessEqual(config["budgets"]["fetches_per_target"], 20)
        self.assertLessEqual(config["budgets"]["search_candidates_per_query"], 100)

    def test_search_snippet_is_never_evidence_and_only_official_full_text_is_fetched(self) -> None:
        config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        task = SimpleNamespace(
            target_id="005930",
            task_id="TASK-1",
            query_intent=SimpleNamespace(literal_queries=("Samsung Electronics 2026 HBM4 shipment",)),
        )
        text = (
            "Samsung Electronics\nFebruary 12, 2026\n"
            "Samsung Electronics shipped commercial HBM4 products after customer qualification. "
            "The full official release explains shipment, capacity, and current product lifecycle. "
        ) * 4
        provider = _SearchProvider(
            (
                SearchResult(
                    title="Samsung commercial HBM4 shipment",
                    url="https://news.samsung.com/global/example",
                    snippet="this snippet must never be evidence",
                    published_at=datetime(2026, 2, 12),
                    query="Samsung Electronics 2026 HBM4 shipment",
                    rank=1,
                ),
                SearchResult(
                    title="portal",
                    url="https://example.com/copied-story",
                    snippet="copied",
                    published_at=datetime(2026, 2, 12),
                    rank=2,
                ),
            )
        )

        search, fetch, documents = _search_and_fetch(
            config=config,
            targets=(config["mandatory_targets"][0],),
            tasks=(task,),
            as_of=date(2026, 7, 10),
            provider=provider,
            transport=_Transport(text),
        )

        self.assertEqual(len(search), 2)
        self.assertEqual(len(fetch), 1)
        self.assertEqual(len(documents), 1)
        self.assertEqual(documents[0]["content_text"], text.strip())
        self.assertNotIn("this snippet must never be evidence", documents[0]["content_text"])
        self.assertFalse(documents[0]["search_snippet_used_as_evidence"])
        self.assertEqual(documents[0]["published_at"], "2026-02-12")

    def test_future_official_result_is_filtered_before_fetch(self) -> None:
        config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        task = SimpleNamespace(
            target_id="005930",
            task_id="TASK-1",
            query_intent=SimpleNamespace(literal_queries=("Samsung Electronics 2026 HBM",)),
        )
        provider = _SearchProvider(
            (
                SearchResult(
                    title="future",
                    url="https://news.samsung.com/global/future",
                    published_at=datetime(2026, 7, 11),
                    rank=1,
                ),
            )
        )
        transport = _Transport("Samsung Electronics " * 30)

        _, fetch, documents = _search_and_fetch(
            config=config,
            targets=(config["mandatory_targets"][0],),
            tasks=(task,),
            as_of=date(2026, 7, 10),
            provider=provider,
            transport=transport,
        )

        self.assertFalse(fetch)
        self.assertFalse(documents)
        self.assertEqual(transport.call_count, 0)

    def test_partial_documents_keep_full_thesis_at_stage_zero_no_score(self) -> None:
        satisfaction = (
            SimpleNamespace(
                primitive_id="customer_preorder_or_allocation",
                original_gap_open=True,
            ),
        )
        status = _full_thesis_status(
            provider_pending=False,
            documents=({"document_id": "DOC-1"},),
            satisfaction=satisfaction,
        )
        decision = _pending_atomic_decision(
            as_of_date="2026-07-10",
            target_id="005930",
            satisfaction=satisfaction,
            provider_pending=False,
            source_pending=True,
        )

        self.assertEqual(status["status"], "FULL_THESIS_EVIDENCE_PENDING")
        self.assertFalse(status["score_finalized"])
        self.assertEqual(decision.score_type, "NO_SCORE")
        self.assertFalse(decision.score_valid)
        self.assertIsNone(decision.score_value)
        self.assertEqual(decision.canonical_stage, "0")
        self.assertEqual(decision.decision_status, "PENDING")

    def test_official_feed_executes_short_query_and_uses_verified_rss_date(self) -> None:
        rss = b"""<?xml version='1.0'?><rss><channel>
        <item><title>Current HBM4 shipment</title><link>https://news.example.com/current</link>
        <pubDate>Thu, 12 Feb 2026 15:00:00 +0000</pubDate></item>
        <item><title>Future item</title><link>https://news.example.com/future</link>
        <pubDate>Sat, 11 Jul 2026 00:00:00 +0000</pubDate></item>
        </channel></rss>"""
        transport = _BytesTransport(rss)
        provider = IssuerNewsroomFeedSearchProvider(
            feed_url="https://news.example.com/feed/",
            transport=transport,
            timeout_seconds=5,
        )

        results = provider.search("HBM4 shipment", date(2026, 7, 10), 10)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].url, "https://news.example.com/current")
        self.assertEqual(results[0].published_at.date().isoformat(), "2026-02-12")
        self.assertTrue(results[0].date_verified)
        self.assertIn("s=HBM4+shipment", transport.last_url)

    def test_native_site_query_validation_rejects_template_like_or_duplicate_query(self) -> None:
        base = {
            "input_id": "INPUT-1",
            "site_search_query": "HBM4 shipment",
            "rationale": "direct product and action terms",
        }
        self.assertIsNone(
            _issuer_site_query_validation_error(
                payload=base,
                expected_input_id="INPUT-1",
                query="HBM4 shipment",
                seen_queries=set(),
                as_of_date="2026-07-10",
            )
        )
        self.assertEqual(
            _issuer_site_query_validation_error(
                payload=base,
                expected_input_id="INPUT-1",
                query="HBM4 shipment",
                seen_queries={"hbm4 shipment"},
                as_of_date="2026-07-10",
            ),
            "DUPLICATE_ALREADY_EXECUTED_QUERY",
        )
        invalid = {**base, "site_search_query": "site:news.example.com HBM4"}
        self.assertEqual(
            _issuer_site_query_validation_error(
                payload=invalid,
                expected_input_id="INPUT-1",
                query=invalid["site_search_query"],
                seen_queries=set(),
                as_of_date="2026-07-10",
            ),
            "QUERY_CONTAINS_FORBIDDEN_SEARCH_SYNTAX",
        )

    def test_visible_article_date_uses_first_header_date_not_later_body_reference(self) -> None:
        text = "SK hynix\nJune 18, 2026\nThe article later compares July 1, 2026 guidance."
        self.assertEqual(
            _published_date_from_text(text, as_of=date(2026, 7, 10)),
            date(2026, 6, 18),
        )

    def test_resume_merges_task_lineage_and_selects_current_high_coverage_documents(self) -> None:
        base = {
            "target_id": "000660",
            "content_hash": "a" * 64,
            "published_at": "2026-04-22",
        }
        merged = _merge_evidence_documents(
            (
                {**base, "document_id": "DOC-A", "source_task_ids": ["TASK-1"]},
                {**base, "document_id": "DOC-A", "source_task_ids": ["TASK-2"]},
                {
                    **base,
                    "document_id": "DOC-B",
                    "content_hash": "b" * 64,
                    "published_at": "2024-10-24",
                    "source_task_ids": ["TASK-3", "TASK-4", "TASK-5"],
                },
            )
        )
        selected = _select_claim_documents(
            documents=merged,
            target_ids=("000660",),
            max_per_target=1,
            as_of_date="2026-07-10",
        )

        self.assertEqual(len(merged), 2)
        self.assertEqual(merged[0]["source_task_ids"], ["TASK-1", "TASK-2"])
        self.assertEqual(selected[0]["document_id"], "DOC-A")

    def test_official_result_still_requires_title_match_to_llm_query(self) -> None:
        self.assertTrue(
            _search_result_matches_llm_query(
                query="HBM capacity outlook",
                title="Samsung Ships Commercial HBM4 for AI Computing",
            )
        )
        self.assertFalse(
            _search_result_matches_llm_query(
                query="HBM capacity outlook",
                title="Samsung Electronics Ranks Fifth in Global Brands",
            )
        )


class _SearchProvider:
    def __init__(self, results):
        self.results = tuple(results)
        self.errors = []

    def search(self, query, as_of_date, max_results=100):
        del query, as_of_date
        return self.results[:max_results]


class _Transport:
    def __init__(self, text: str):
        self.text = text
        self.call_count = 0

    def fetch(self, *, url: str, timeout_seconds: int):
        del timeout_seconds
        self.call_count += 1
        return HistoricalHttpResponse(
            url=url,
            status_code=200,
            content_type="text/html; charset=utf-8",
            body=(f"<html><body><p>{self.text}</p></body></html>").encode("utf-8"),
        )


class _BytesTransport:
    def __init__(self, body: bytes):
        self.body = body
        self.last_url = ""

    def fetch(self, *, url: str, timeout_seconds: int):
        del timeout_seconds
        self.last_url = url
        return HistoricalHttpResponse(
            url=url,
            status_code=200,
            content_type="application/rss+xml",
            body=self.body,
        )


def _read_jsonl(path: Path):
    with path.open(encoding="utf-8") as handle:
        return tuple(json.loads(line) for line in handle if line.strip())


if __name__ == "__main__":
    unittest.main()
