from datetime import date
import unittest

from e2r.evidence_ids import stable_consensus_evidence_id, stable_revision_evidence_id
from e2r.models import ConsensusRevision, ConsensusSnapshot, Market, SourceTier
from e2r.pipeline.evidence_builder import evidence_from_feature_domains


class EvidenceBuilderTests(unittest.TestCase):
    def test_consensus_evidence_ids_are_source_aware_and_keep_legacy_id(self):
        as_of = date(2026, 6, 11)
        structured = ConsensusSnapshot(
            symbol="CASE",
            date=as_of,
            fiscal_year=2026,
            as_of_date=as_of,
            source="company_guide_snapshot",
            eps_e=43833,
        )
        proxy = ConsensusSnapshot(
            symbol="CASE",
            date=as_of,
            fiscal_year=2026,
            as_of_date=as_of,
            source="report_proxy",
            eps_e=5721,
            parsed_fields={
                "consensus_proxy_quality": "weak",
                "consensus_proxy_score_eligible": False,
            },
        )

        evidence = evidence_from_feature_domains(market=Market.KR, fallback_symbol="CASE", consensus=(structured, proxy))
        by_id = {item.evidence_id: item for item in evidence}

        structured_id = stable_consensus_evidence_id(
            symbol="CASE",
            estimate_date=as_of,
            fiscal_year=2026,
            source="company_guide_snapshot",
        )
        proxy_id = stable_consensus_evidence_id(
            symbol="CASE",
            estimate_date=as_of,
            fiscal_year=2026,
            source="report_proxy",
        )
        self.assertEqual(set(by_id), {structured_id, proxy_id})
        self.assertEqual(by_id[structured_id].source_tier, SourceTier.TIER_2)
        self.assertEqual(by_id[proxy_id].source_tier, SourceTier.TIER_4)
        self.assertEqual(by_id[proxy_id].parsed_fields["legacy_evidence_id"], "consensus:CASE:2026-06-11:2026")

    def test_consensus_revision_evidence_keeps_source_name_and_quality_tier(self):
        as_of = date(2026, 6, 11)
        revision = ConsensusRevision(
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
        )

        evidence = evidence_from_feature_domains(
            market=Market.KR,
            fallback_symbol="CASE",
            consensus_revisions=(revision,),
        )

        expected_id = stable_revision_evidence_id(
            symbol="CASE",
            estimate_date=as_of,
            fiscal_year=2026,
            source="report_proxy",
        )
        self.assertEqual(evidence[0].evidence_id, expected_id)
        self.assertEqual(evidence[0].source_name, "report_proxy")
        self.assertEqual(evidence[0].source_tier, SourceTier.TIER_3)
        self.assertTrue(evidence[0].parsed_fields["target_price_revision_outlier"])
        self.assertEqual(evidence[0].parsed_fields["legacy_evidence_id"], "revision:CASE:2026-06-11:2026")


if __name__ == "__main__":
    unittest.main()
