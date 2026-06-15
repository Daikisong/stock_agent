from datetime import date
import unittest

from e2r.estimate_quality import build_estimate_quality_context
from e2r.features import FeatureEngineeringInput
from e2r.models import ConsensusRevision, ConsensusSnapshot


class EstimateQualityTests(unittest.TestCase):
    def test_structured_consensus_beats_newer_conflicting_report_proxy(self):
        as_of = date(2026, 6, 11)
        inputs = FeatureEngineeringInput(
            symbol="CASE",
            as_of_date=as_of,
            consensus=(
                ConsensusSnapshot(
                    symbol="CASE",
                    date=date(2026, 6, 10),
                    fiscal_year=2026,
                    as_of_date=as_of,
                    source="company_guide_snapshot",
                    eps_e=43833,
                    target_price=437500,
                    analyst_count=24,
                ),
                ConsensusSnapshot(
                    symbol="CASE",
                    date=date(2026, 6, 11),
                    fiscal_year=2026,
                    as_of_date=as_of,
                    source="report_proxy",
                    eps_e=5721,
                    target_price=110000,
                    parsed_fields={
                        "consensus_proxy_quality": "full_text_report",
                        "consensus_proxy_score_eligible": True,
                        "derived_from_source_type": "research_report",
                    },
                ),
            ),
        )

        context = build_estimate_quality_context(inputs)

        self.assertEqual(context.value("eps_e"), 43833)
        self.assertEqual(context.value("target_price"), 437500)
        self.assertEqual(context.source_fields["estimate_selected_eps_source"], "company_guide_snapshot")
        self.assertGreater(context.diagnostic_scores["estimate_conflict_count_capped"], 0)
        self.assertGreater(context.diagnostic_scores["estimate_proxy_quarantined_count_capped"], 0)

    def test_weak_report_proxy_remains_evidence_but_not_score_candidate(self):
        as_of = date(2026, 6, 11)
        inputs = FeatureEngineeringInput(
            symbol="CASE",
            as_of_date=as_of,
            consensus=(
                ConsensusSnapshot(
                    symbol="CASE",
                    date=as_of,
                    fiscal_year=2026,
                    as_of_date=as_of,
                    source="report_proxy",
                    eps_e=5721,
                    parsed_fields={
                        "consensus_proxy_quality": "weak",
                        "consensus_proxy_score_eligible": False,
                        "consensus_proxy_weak_reasons": ("short_raw_text",),
                    },
                ),
            ),
        )

        context = build_estimate_quality_context(inputs)

        self.assertIsNone(context.value("eps_e"))
        self.assertGreaterEqual(context.diagnostic_scores["estimate_proxy_quarantined_count_capped"], 1)
        self.assertEqual(context.diagnostic_scores["estimate_missing_eps_source"], 100.0)
        self.assertEqual(context.diagnostic_scores["estimate_missing_revision_source"], 100.0)
        self.assertNotIn("estimate_selected_eps_source", context.source_fields)

    def test_unknown_structured_source_is_low_quality_but_not_dropped(self):
        as_of = date(2026, 6, 11)
        inputs = FeatureEngineeringInput(
            symbol="CASE",
            as_of_date=as_of,
            consensus=(
                ConsensusSnapshot(
                    symbol="CASE",
                    date=as_of,
                    fiscal_year=2026,
                    as_of_date=as_of,
                    source="unknown",
                    eps_e=1000,
                ),
            ),
        )

        context = build_estimate_quality_context(inputs)

        self.assertEqual(context.value("eps_e"), 1000)
        self.assertEqual(context.diagnostic_scores["estimate_selected_eps_source_quality"], 55.0)

    def test_revision_outlier_is_quarantined_and_structured_revision_is_used(self):
        as_of = date(2026, 6, 11)
        inputs = FeatureEngineeringInput(
            symbol="CASE",
            as_of_date=as_of,
            consensus_revisions=(
                ConsensusRevision(
                    symbol="CASE",
                    date=date(2026, 6, 10),
                    fiscal_year=2026,
                    as_of_date=as_of,
                    source="consensus-csv",
                    eps_revision_1m=20,
                ),
                ConsensusRevision(
                    symbol="CASE",
                    date=as_of,
                    fiscal_year=2026,
                    as_of_date=as_of,
                    source="report_proxy",
                    target_price_revision_1m=1_374_900,
                    parsed_fields={
                        "consensus_proxy_quality": "full_text_report",
                        "consensus_proxy_score_eligible": True,
                        "target_price_revision_outlier": True,
                    },
                ),
            ),
        )

        context = build_estimate_quality_context(inputs)

        self.assertEqual(context.revision_selection.selected_value, 20)
        self.assertEqual(context.source_fields["estimate_selected_revision_source"], "consensus-csv")
        self.assertEqual(context.diagnostic_scores["estimate_revision_outlier_count_capped"], 1.0)
        self.assertEqual(context.diagnostic_scores["estimate_missing_fcf_source"], 100.0)


if __name__ == "__main__":
    unittest.main()
