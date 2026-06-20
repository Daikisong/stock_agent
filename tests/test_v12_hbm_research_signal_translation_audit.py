from pathlib import Path
import tempfile
import unittest

from e2r.calibration.v12_hbm_research_signal_translation_audit import (
    build_v12_hbm_research_signal_translation_audit,
    render_v12_hbm_research_signal_translation_audit,
)


class V12HbmResearchSignalTranslationAuditTests(unittest.TestCase):
    def test_audit_flags_research_signals_that_stay_zero_in_runtime_fields(self) -> None:
        representative_rows = [
            {
                "symbol": "000660",
                "company_name": "SK하이닉스",
                "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "trigger_type": "Stage2-Actionable",
                "entry_date": "2024-03-20",
                "MFE_180D_pct": 60,
                "MAE_180D_pct": -5,
                "current_profile_verdict": "current_profile_correct",
                "evidence_available_at_that_date": "HBM3E shipments to Nvidia and 2024 capacity fully booked.",
            },
            {
                "symbol": "005930",
                "company_name": "삼성전자",
                "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "trigger_type": "Stage4C",
                "entry_date": "2024-05-23",
                "MFE_180D_pct": 5,
                "MAE_180D_pct": -20,
                "current_profile_verdict": "current_profile_4c",
                "evidence_available_at_that_date": "Samsung HBM qualification delay and heat/power issues.",
            },
        ]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "score_components_by_candidate.csv").write_text(
                "\n".join(
                    [
                        "symbol,company_name,as_of_date,current_stage,current_score,canonical_archetype_id,research_axis_bridge_customer,research_axis_bridge_backlog,research_axis_bridge_contract,capa_constraint,research_axis_bridge_margin,asp_pricing_power,revision_score,actual_profit_conversion_score,green_gate_deficit_summary",
                        "000660,SK하이닉스,2024-04-25,3-Yellow,76.0,C06_HBM_MEMORY_CUSTOMER_CAPACITY,100,0,0,0,100,20,100,80,total:76/87",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )
            payload = build_v12_hbm_research_signal_translation_audit(
                representative_rows=representative_rows,
                autopsy_directories=[root],
            )

        by_symbol = {row["symbol"]: row for row in payload["symbol_rows"]}
        self.assertEqual(by_symbol["000660"]["research_positive_or_green_worthy_count"], 1)
        self.assertIn("capacity_lock", by_symbol["000660"]["gap_signals"])
        self.assertIn("order_or_contract", by_symbol["000660"]["gap_signals"])
        self.assertEqual(by_symbol["005930"]["research_positive_or_green_worthy_count"], 0)

        report = render_v12_hbm_research_signal_translation_audit(payload)
        self.assertIn("삼전/하닉 전용 보너스가 아니라", report)
        self.assertIn("capacity_lock", report)
        self.assertIn("research_signal_present_but_runtime_field_zero", report)


if __name__ == "__main__":
    unittest.main()
