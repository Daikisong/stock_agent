from __future__ import annotations

from copy import deepcopy
from datetime import date, timedelta
import json
import unittest
from unittest import mock

from e2r.calibration.taxonomy import large_sector_for_archetype
from e2r.production.metadata import stable_hash
from e2r.production import v6_issuer_business_profile as profile_module
from e2r.production.v6_issuer_business_profile import (
    CANONICAL_COMPATIBILITY_PROVIDER,
    CompatibilityProviderCompletion,
    IssuerBusinessProfileConfig,
    PROFILE_PASS,
    PROFILE_PENDING,
    PROFILE_TEST_ONLY,
    REQUIRED_ARCHETYPES,
    V6IssuerBusinessProfileMaterializer,
    large_sector_for_industry_code,
    validate_forced_validation_profile_manifest,
    validate_issuer_business_profile,
    validate_issuer_business_profile_result,
)


AS_OF = "2026-08-09"


def _krx_row(symbol: str, company_name: str, market: str = "KOSPI") -> dict:
    endpoint = "stk_isu_base_info" if market == "KOSPI" else "ksq_isu_base_info"
    effective = "2026-08-07"
    return {
        "symbol": symbol,
        "company_name": company_name,
        "market": market,
        "eligible": True,
        "exclusion_reason": None,
        "listing_status": "LISTED",
        "source_mode": "LIVE",
        "source_effective_date": effective,
        "source_url": f"https://data-dbg.krx.co.kr/svc/apis/sto/{endpoint}?basDd=20260807",
        "source_request_id": "KRXREQ-"
        + stable_hash(
            {"market": market, "effective_date": effective, "endpoint": endpoint}
        )[:24],
        "source_content_hash": stable_hash(
            {"fixture": "official KRX response", "market": market}
        ),
        "raw_fields": {"ISU_SRT_CD": symbol, "ISU_NM": company_name},
    }


class FakeOpenDartFetcher:
    provider_name = "OpenDART"

    def __init__(
        self,
        industry_by_target: dict[str, str],
        *,
        fail_targets: set[str] | None = None,
        invalid_discovery_targets: set[str] | None = None,
        mutate_response_hash_for: set[str] | None = None,
        future_report_for: set[str] | None = None,
        stale_document_for: set[str] | None = None,
        document_padding: int = 0,
    ) -> None:
        self.industry_by_target = industry_by_target
        self.fail_targets = fail_targets or set()
        self.invalid_discovery_targets = invalid_discovery_targets or set()
        self.mutate_response_hash_for = mutate_response_hash_for or set()
        self.future_report_for = future_report_for or set()
        self.stale_document_for = stale_document_for or set()
        self.document_padding = document_padding
        self.calls: list[str] = []
        self.discovery_calls: list[str] = []
        self.full_documents: dict[str, str] = {}

    def discover_industry(
        self,
        *,
        target_id: str,
        company_name: str,
        as_of_date: date,
        credential: str,
        timeout_seconds: float,
    ) -> dict:
        del credential, timeout_seconds
        self.discovery_calls.append(target_id)
        if target_id in self.fail_targets:
            return {
                "status": "PENDING",
                "provider_name": "OpenDART",
                "target_id": target_id,
                "company_name": company_name,
                "request_count": 1,
                "error_category": "OPENDART_PROVIDER_FAILURE:fixture",
            }
        corp_code = "00" + target_id
        corp_xml = (
            "<result><list>"
            f"<corp_code>{corp_code}</corp_code>"
            f"<corp_name>{company_name}</corp_name>"
            f"<stock_code>{target_id}</stock_code>"
            "</list></result>"
        )
        company_payload = {
            "status": "000",
            "corp_code": corp_code,
            "corp_name": company_name,
            "stock_code": target_id,
            "induty_code": self.industry_by_target.get(target_id, "99999"),
        }
        if target_id in self.invalid_discovery_targets:
            company_payload["induty_code"] = ""
        company_text = json.dumps(
            company_payload,
            ensure_ascii=False,
            sort_keys=True,
        )
        return {
            "status": "DISCOVERED",
            "provider_name": "OpenDART",
            "target_id": target_id,
            "company_name": company_name,
            "request_count": 2,
            "corp_code_receipt": profile_module._source_receipt(
                role="CORP_CODE_IDENTITY",
                target_id=target_id,
                as_of_date=as_of_date,
                canonical_url=profile_module._CORP_CODE_URL,
                request_params={},
                response_text=corp_xml,
            ),
            "company_receipt": profile_module._source_receipt(
                role="COMPANY_IDENTITY",
                target_id=target_id,
                as_of_date=as_of_date,
                canonical_url=profile_module._COMPANY_URL,
                request_params={"corp_code": corp_code},
                response_text=company_text,
            ),
            "error_category": None,
        }

    def fetch(
        self,
        *,
        target_id: str,
        company_name: str,
        as_of_date: date,
        credential: str,
        max_list_pages: int,
        timeout_seconds: float,
    ) -> dict:
        del credential, max_list_pages, timeout_seconds
        self.calls.append(target_id)
        if target_id in self.fail_targets:
            return {
                "status": "PENDING",
                "provider_name": "OpenDART",
                "target_id": target_id,
                "company_name": company_name,
                "request_count": 1,
                "error_category": "OPENDART_PROVIDER_FAILURE:fixture",
            }
        corp_code = "00" + target_id
        corp_xml = (
            "<result><list>"
            f"<corp_code>{corp_code}</corp_code>"
            f"<corp_name>{company_name}</corp_name>"
            f"<stock_code>{target_id}</stock_code>"
            "</list></result>"
        )
        company_text = json.dumps(
            {
                "status": "000",
                "corp_code": corp_code,
                "corp_name": company_name,
                "stock_code": target_id,
                "induty_code": self.industry_by_target[target_id],
            },
            ensure_ascii=False,
            sort_keys=True,
        )
        day = "20260810" if target_id in self.future_report_for else "20260807"
        latest_rcept_no = f"20260807{target_id}"
        rows = [
            {
                "corp_code": corp_code,
                "report_nm": "사업보고서 (2025.12)",
                "rcept_dt": day,
                "rcept_no": latest_rcept_no,
            }
        ]
        if target_id in self.stale_document_for:
            rows.append(
                {
                    "corp_code": corp_code,
                    "report_nm": "분기보고서 (2026.06)",
                    "rcept_dt": "20260808",
                    "rcept_no": f"20260808{target_id}",
                }
            )
        list_text = json.dumps(
            {"status": "000", "total_page": 1, "list": rows},
            ensure_ascii=False,
            sort_keys=True,
        )
        quote = f"{target_id}의 공식 정기보고서에는 반복 가능한 사업 메커니즘과 고객 구조가 설명되어 있다."
        document_text = (
            "<DOCUMENT><BODY>"
            + quote
            + " 이 문장은 테스트용 공식 원문이며 이름 기반 분류를 사용하지 않는다."
            + ("가" * self.document_padding)
            + "</BODY></DOCUMENT>"
        )
        document_id = f"opendart:disclosure:{latest_rcept_no}"
        self.full_documents[document_id] = document_text
        corp_receipt = profile_module._source_receipt(
            role="CORP_CODE_IDENTITY",
            target_id=target_id,
            as_of_date=as_of_date,
            canonical_url=profile_module._CORP_CODE_URL,
            request_params={},
            response_text=corp_xml,
        )
        company_receipt = profile_module._source_receipt(
            role="COMPANY_IDENTITY",
            target_id=target_id,
            as_of_date=as_of_date,
            canonical_url=profile_module._COMPANY_URL,
            request_params={"corp_code": corp_code},
            response_text=company_text,
        )
        if target_id in self.mutate_response_hash_for:
            company_receipt = {**company_receipt, "response_hash": "0" * 64}
        list_receipt = profile_module._source_receipt(
            role="PERIODIC_REPORT_LIST",
            target_id=target_id,
            as_of_date=as_of_date,
            canonical_url=profile_module._LIST_URL,
            request_params={
                "corp_code": corp_code,
                "bgn_de": (as_of_date - timedelta(days=540)).strftime("%Y%m%d"),
                "end_de": as_of_date.strftime("%Y%m%d"),
                "page_no": 1,
                "page_count": 100,
            },
            response_text=list_text,
        )
        document_receipt = {
            **profile_module._source_receipt(
                role="PERIODIC_REPORT_DOCUMENT",
                target_id=target_id,
                as_of_date=as_of_date,
                canonical_url=profile_module._DOCUMENT_URL,
                request_params={"rcept_no": latest_rcept_no},
                response_text=document_text,
            ),
            "official_document_id": document_id,
            "viewer_url": f"{profile_module._DART_VIEWER_URL}?rcpNo={latest_rcept_no}",
            "rcept_no": latest_rcept_no,
            "available_date": "2026-08-07",
        }
        return {
            "status": "FETCHED",
            "provider_name": "OpenDART",
            "target_id": target_id,
            "company_name": company_name,
            "request_count": 4,
            "corp_code_receipt": corp_receipt,
            "company_receipt": company_receipt,
            "list_receipts": [list_receipt],
            "document_receipt": document_receipt,
            "error_category": None,
        }


class FakeCompatibilityProvider:
    def __init__(
        self,
        *,
        mode: str = "selected",
        real_provider: bool = True,
        fake_provider: bool = False,
        provider_name: str = CANONICAL_COMPATIBILITY_PROVIDER,
    ) -> None:
        self.mode = mode
        self.real_provider = real_provider
        self.fake_provider = fake_provider
        self.provider_name = provider_name
        self.calls = 0
        self.prompt_lengths: list[int] = []

    def complete(self, *, prompt: str, output_schema: dict) -> CompatibilityProviderCompletion:
        self.calls += 1
        self.prompt_lengths.append(len(prompt))
        self.output_schema = output_schema
        if self.mode == "provider_failure":
            raise RuntimeError("fixture provider unavailable")
        prompt_payload = json.loads(prompt)
        profiles = prompt_payload["profiles"]
        selected_targets: set[str] = set()
        decisions = []
        for archetype in tuple(prompt_payload["required_archetypes"]):
            expected_sector = large_sector_for_archetype(archetype)
            candidates = [
                row
                for row in profiles
                if row["large_sector_id"] == expected_sector
                and row["target_id"] not in selected_targets
            ]
            if self.mode == "duplicate_target" and archetype == REQUIRED_ARCHETYPES[2]:
                candidates = [
                    row
                    for row in profiles
                    if row["target_id"] in selected_targets
                    and row["large_sector_id"] == expected_sector
                ]
            tail_quote_absent = bool(
                self.mode == "tail_quote"
                and candidates
                and "</BODY></DOCUMENT>"
                not in str(candidates[0].get("periodic_report_full_text") or "")
            )
            if self.mode in {"abstain", "pending"} or tail_quote_absent:
                status = "PENDING" if self.mode == "pending" else "ABSTAIN"
                decisions.append(
                    {
                        "archetype_id": archetype,
                        "status": status,
                        "target_id": "",
                        "company_name": "",
                        "profile_id": "",
                        "large_sector_id": "",
                        "periodic_report_document_id": "",
                        "exact_quote": "",
                        "mechanism_rationale": "현재 공식 원문만으로 호환성을 확정할 수 없다.",
                        "confidence": 0.0,
                    }
                )
                continue
            row = candidates[0]
            selected_targets.add(row["target_id"])
            quote = (
                f"{row['target_id']}의 공식 정기보고서에는 반복 가능한 사업 메커니즘과 고객 구조가 설명되어 있다."
            )
            if self.mode in {"tail_quote", "unprompted_quote"}:
                quote = "</BODY></DOCUMENT>"
            decisions.append(
                {
                    "archetype_id": archetype,
                    "status": "SELECTED",
                    "target_id": row["target_id"],
                    "company_name": row["company_name"],
                    "profile_id": row["profile_id"],
                    "large_sector_id": (
                        "L10_POLICY_EVENT_CROSS_REDTEAM_MISC"
                        if self.mode == "cross_sector" and len(decisions) == 0
                        else row["large_sector_id"]
                    ),
                    "periodic_report_document_id": row["periodic_report_document_id"],
                    "exact_quote": quote + (" 변조" if self.mode == "quote_tamper" else ""),
                    "mechanism_rationale": "공식 정기보고서의 사업 메커니즘이 요청 아키타입과 호환된다.",
                    "confidence": 0.8,
                }
            )
        payload = {
            "decisions": decisions,
            "classification_complete": True,
            "unresolved_notes": [],
        }
        if self.mode == "missing_roster":
            payload["decisions"] = decisions[:-1]
        if self.mode == "forbidden_authority":
            payload["score"] = 99
        raw = json.dumps(payload, ensure_ascii=False, sort_keys=True)
        if self.mode == "raw_mismatch":
            raw = json.dumps({**payload, "unresolved_notes": ["변조"]}, ensure_ascii=False, sort_keys=True)
        return CompatibilityProviderCompletion(payload=payload, raw_response=raw)


def _five_rows() -> tuple[list[dict], dict[str, str]]:
    rows = [
        _krx_row("100001", "발행인 알파"),
        _krx_row("100002", "발행인 베타"),
        _krx_row("100003", "발행인 감마"),
        _krx_row("100004", "발행인 델타", "KOSDAQ"),
        _krx_row("100005", "발행인 엡실론", "KOSDAQ"),
    ]
    industries = {
        "100001": "26120",
        "100002": "20110",
        "100003": "20202",
        "100004": "21101",
        "100005": "62010",
    }
    return rows, industries


class V6IssuerBusinessProfileTest(unittest.TestCase):
    def _materialize(
        self,
        *,
        rows: list[dict] | None = None,
        fetcher: FakeOpenDartFetcher | None = None,
        provider: FakeCompatibilityProvider | None = None,
        credential: str | None = "official-fixture-key",
        test_mode: bool = False,
        max_fetches: int = 5,
        max_prompt_chars: int = 2_000_000,
    ) -> tuple[dict, FakeOpenDartFetcher, FakeCompatibilityProvider]:
        default_rows, industries = _five_rows()
        actual_fetcher = fetcher or FakeOpenDartFetcher(industries)
        actual_provider = provider or FakeCompatibilityProvider()
        result = V6IssuerBusinessProfileMaterializer().materialize(
            IssuerBusinessProfileConfig(
                as_of_date=AS_OF,
                max_profile_fetches=max_fetches,
                max_compatibility_prompt_chars=max_prompt_chars,
                test_mode=test_mode,
            ),
            universe_rows=rows or default_rows,
            credential=credential,
            fetcher=actual_fetcher,
            compatibility_provider=actual_provider,
        )
        return dict(result), actual_fetcher, actual_provider

    def test_corp_code_document_is_indexed_once_for_many_symbols(self) -> None:
        corp_xml = (
            "<result>"
            "<list><corp_code>001</corp_code><corp_name>첫째</corp_name>"
            "<stock_code>1</stock_code></list>"
            "<list><corp_code>002</corp_code><corp_name>둘째</corp_name>"
            "<stock_code>2</stock_code></list>"
            "<list><corp_code>003</corp_code><corp_name>중복A</corp_name>"
            "<stock_code>3</stock_code></list>"
            "<list><corp_code>004</corp_code><corp_name>중복B</corp_name>"
            "<stock_code>3</stock_code></list>"
            "</result>"
        )
        profile_module._corp_row_index.cache_clear()
        try:
            with mock.patch.object(
                profile_module.ET,
                "fromstring",
                wraps=profile_module.ET.fromstring,
            ) as parse:
                first = profile_module._corp_row(corp_xml, target_id="000001")
                second = profile_module._corp_row(corp_xml, target_id="000002")
                duplicate = profile_module._corp_row(corp_xml, target_id="000003")
                self.assertEqual(parse.call_count, 1)
            self.assertEqual(first["corp_name"], "첫째")
            self.assertEqual(second["corp_name"], "둘째")
            self.assertIsNone(duplicate)
            first["corp_name"] = "변경"
            self.assertEqual(
                profile_module._corp_row(corp_xml, target_id="000001")[
                    "corp_name"
                ],
                "첫째",
            )
        finally:
            profile_module._corp_row_index.cache_clear()

    def test_industry_21_is_pharma_not_materials(self) -> None:
        self.assertEqual(
            large_sector_for_industry_code("21101"),
            "L7_BIO_HEALTHCARE_MEDICAL",
        )
        self.assertNotEqual(
            large_sector_for_industry_code("21101"),
            "L4_MATERIALS_SPREAD_RESOURCE",
        )

    def test_forced_discovery_recovers_required_sector_outside_natural_roster(self) -> None:
        full_rows, industries = _five_rows()
        natural_rows = full_rows[1:]
        fetcher = FakeOpenDartFetcher(industries)
        provider = FakeCompatibilityProvider()

        result = V6IssuerBusinessProfileMaterializer().materialize(
            IssuerBusinessProfileConfig(
                as_of_date=AS_OF,
                max_profile_fetches=5,
                max_discovery_fetches=10,
                max_forced_candidates_per_required_slot=1,
            ),
            universe_rows=natural_rows,
            discovery_universe_rows=full_rows,
            credential="official-fixture-key",
            fetcher=fetcher,
            compatibility_provider=provider,
        )

        self.assertEqual(result["status"], PROFILE_PASS)
        expansion = result["candidate_expansion_receipt"]
        self.assertEqual(expansion["status"], "COMPLETE")
        self.assertEqual(expansion["selection_mode"], "FORCED_VALIDATION_CANARY")
        self.assertEqual(
            [row["target_id"] for row in expansion["expanded_candidates"]],
            [full_rows[0]["symbol"]],
        )
        self.assertEqual(
            expansion["natural_candidate_roster"],
            [row["symbol"] for row in natural_rows],
        )
        self.assertEqual(fetcher.calls[0], full_rows[0]["symbol"])
        self.assertEqual(
            tuple(row["archetype_id"] for row in result["selections"]),
            REQUIRED_ARCHETYPES,
        )
        self.assertFalse(expansion["score_or_stage_authority"])
        self.assertFalse(expansion["gold_authority"])

        drifted = deepcopy(result)
        drifted_discovery = drifted["candidate_expansion_receipt"][
            "expanded_candidates"
        ][0]
        drifted_discovery["company_profile_hash"] = "f" * 64
        discovery_core = {
            key: value
            for key, value in drifted_discovery.items()
            if key != "discovery_id"
        }
        drifted_discovery["discovery_id"] = (
            "PROFILEDISC-" + stable_hash(discovery_core)[:24]
        )
        drifted_expansion = drifted["candidate_expansion_receipt"]
        drifted_expansion["expanded_candidate_roster_hash"] = stable_hash(
            [
                row["discovery_id"]
                for row in drifted_expansion["expanded_candidates"]
            ]
        )
        expansion_core = {
            key: value
            for key, value in drifted_expansion.items()
            if key != "receipt_id"
        }
        drifted_expansion["receipt_id"] = (
            "PROFILEEXPAND-" + stable_hash(expansion_core)[:24]
        )
        with self.assertRaisesRegex(ValueError, "drifted from forced discovery"):
            validate_issuer_business_profile_result(drifted)

    def test_nonselected_ineligible_discovery_is_diagnostic(self) -> None:
        rows, industries = _five_rows()
        ineligible = _krx_row("100006", "발행인 비대상")
        industries[ineligible["symbol"]] = "99999"
        fetcher = FakeOpenDartFetcher(
            industries,
            invalid_discovery_targets={ineligible["symbol"]},
        )

        result = V6IssuerBusinessProfileMaterializer().materialize(
            IssuerBusinessProfileConfig(
                as_of_date=AS_OF,
                max_profile_fetches=5,
                max_discovery_fetches=10,
                max_forced_candidates_per_required_slot=1,
            ),
            universe_rows=rows,
            discovery_universe_rows=[*rows, ineligible],
            credential="official-fixture-key",
            fetcher=fetcher,
            compatibility_provider=FakeCompatibilityProvider(),
        )

        self.assertEqual(result["status"], PROFILE_PASS)
        expansion = result["candidate_expansion_receipt"]
        self.assertEqual(expansion["status"], "COMPLETE")
        self.assertEqual(expansion["stop_reason"], "FULL_KRX_EXHAUSTED")
        self.assertEqual(expansion["pending"], [])
        self.assertEqual(
            expansion["diagnostics"],
            [
                {
                    "code": "FORCED_DISCOVERY_CANDIDATE_INELIGIBLE",
                    "target_id": ineligible["symbol"],
                    "detail": (
                        "OpenDART discovery company identity or industry code "
                        "is invalid"
                    ),
                }
            ],
        )
        self.assertEqual(fetcher.discovery_calls, [ineligible["symbol"]])

    def test_forced_discovery_provider_failure_is_pending_before_full_profiles(self) -> None:
        full_rows, industries = _five_rows()
        natural_rows = full_rows[1:]
        fetcher = FakeOpenDartFetcher(
            industries,
            fail_targets={full_rows[0]["symbol"]},
        )
        provider = FakeCompatibilityProvider()

        result = V6IssuerBusinessProfileMaterializer().materialize(
            IssuerBusinessProfileConfig(
                as_of_date=AS_OF,
                max_profile_fetches=5,
                max_discovery_fetches=10,
                max_forced_candidates_per_required_slot=1,
            ),
            universe_rows=natural_rows,
            discovery_universe_rows=full_rows,
            credential="official-fixture-key",
            fetcher=fetcher,
            compatibility_provider=provider,
        )

        self.assertEqual(result["status"], PROFILE_PENDING)
        self.assertEqual(result["candidate_expansion_receipt"]["status"], "PENDING")
        self.assertEqual(
            result["candidate_expansion_receipt"]["stop_reason"],
            "PROVIDER_PENDING",
        )
        self.assertEqual(fetcher.calls, [])
        self.assertEqual(provider.calls, 0)

    def test_forced_discovery_budget_exhaustion_is_pending_and_bounded(self) -> None:
        full_rows, industries = _five_rows()
        natural_rows = full_rows[1:]
        irrelevant = _krx_row("100006", "발행인 비관련")
        industries[irrelevant["symbol"]] = "10799"
        discovery_rows = [irrelevant, *natural_rows, full_rows[0]]
        fetcher = FakeOpenDartFetcher(industries)
        provider = FakeCompatibilityProvider()

        result = V6IssuerBusinessProfileMaterializer().materialize(
            IssuerBusinessProfileConfig(
                as_of_date=AS_OF,
                max_profile_fetches=5,
                max_discovery_fetches=1,
                max_forced_candidates_per_required_slot=1,
            ),
            universe_rows=natural_rows,
            discovery_universe_rows=discovery_rows,
            credential="official-fixture-key",
            fetcher=fetcher,
            compatibility_provider=provider,
        )

        expansion = result["candidate_expansion_receipt"]
        self.assertEqual(result["status"], PROFILE_PENDING)
        self.assertEqual(expansion["status"], "PENDING")
        self.assertEqual(expansion["stop_reason"], "BUDGET_EXHAUSTED")
        self.assertEqual(expansion["discovery_fetch_count"], 1)
        self.assertEqual(fetcher.discovery_calls, [irrelevant["symbol"]])
        self.assertEqual(fetcher.calls, [])
        self.assertEqual(provider.calls, 0)

    def test_production_exact_five_is_complete_and_stops(self) -> None:
        rows, industries = _five_rows()
        rows.append(_krx_row("100006", "발행인 제타"))
        industries["100006"] = "62020"
        result, fetcher, provider = self._materialize(
            rows=rows,
            fetcher=FakeOpenDartFetcher(industries),
            max_fetches=6,
        )
        self.assertEqual(result["status"], PROFILE_PASS)
        self.assertEqual(
            tuple(row["archetype_id"] for row in result["selections"]),
            REQUIRED_ARCHETYPES,
        )
        self.assertEqual(len({row["target_id"] for row in result["selections"]}), 5)
        self.assertEqual(fetcher.calls, [row["symbol"] for row in rows[:5]])
        self.assertEqual(provider.calls, 1)
        self.assertLessEqual(provider.calls, result["audit"]["profile_fetch_count"])
        self.assertLessEqual(
            provider.prompt_lengths[0],
            result["audit"]["max_compatibility_prompt_chars"],
        )
        self.assertTrue(result["audit"]["stopped_on_five"])
        self.assertFalse(result["forced_validation_authority"])
        self.assertFalse(result["score_or_stage_authority"])
        self.assertFalse(result["gold_authority"])
        self.assertEqual(
            result["selections"][3]["large_sector_id"],
            "L7_BIO_HEALTHCARE_MEDICAL",
        )
        receipt = result["selections"][0]
        self.assertEqual(receipt["status"], "COMPLETE")
        self.assertEqual(receipt["as_of_date"], AS_OF)
        self.assertEqual(receipt["krx_row"]["symbol"], receipt["target_id"])
        self.assertEqual(receipt["corp_code"], "00" + receipt["target_id"])
        self.assertEqual(
            receipt["exact_quote_hash"],
            profile_module._sha256_text(receipt["exact_quote"]),
        )
        self.assertEqual(
            receipt["compatibility_response_envelope_hash"],
            result["compatibility_receipts"][0]["response_hash"],
        )
        self.assertIsInstance(receipt["confidence"], float)

    def test_nonselected_failed_candidate_is_diagnostic_not_permanent_blocker(self) -> None:
        rows, industries = _five_rows()
        failed = _krx_row("100000", "발행인 실패")
        industries["100000"] = "26110"
        fetcher = FakeOpenDartFetcher(industries, fail_targets={"100000"})
        result, _, _ = self._materialize(
            rows=[failed, *rows],
            fetcher=fetcher,
            max_fetches=6,
        )
        self.assertEqual(result["status"], PROFILE_PASS)
        self.assertEqual(result["audit"]["diagnostic_count"], 1)
        self.assertEqual(result["pending"][0]["target_id"], "100000")

    def test_missing_credential_is_pending_and_does_not_fetch(self) -> None:
        result, fetcher, provider = self._materialize(credential=None)
        self.assertEqual(result["status"], PROFILE_PENDING)
        self.assertEqual(fetcher.calls, [])
        self.assertEqual(provider.calls, 0)
        self.assertEqual(result["pending"], [{"code": "OPENDART_CREDENTIAL_MISSING"}])

    def test_source_hash_future_and_stale_latest_report_fail_closed(self) -> None:
        rows, industries = _five_rows()
        for fetcher in (
            FakeOpenDartFetcher(industries, mutate_response_hash_for={"100001"}),
            FakeOpenDartFetcher(industries, future_report_for={"100001"}),
            FakeOpenDartFetcher(industries, stale_document_for={"100001"}),
        ):
            with self.subTest(fetcher=fetcher):
                result, _, provider = self._materialize(
                    rows=rows,
                    fetcher=fetcher,
                    max_fetches=5,
                )
                self.assertEqual(result["status"], PROFILE_PENDING)
                self.assertEqual(provider.calls, 0)

    def test_krx_url_requires_the_exact_real_basdd_query(self) -> None:
        row = _krx_row("100001", "발행인 알파")
        self.assertEqual(
            profile_module._validate_krx_row(row, as_of_date=AS_OF)["source_url"],
            "https://data-dbg.krx.co.kr/svc/apis/sto/"
            "stk_isu_base_info?basDd=20260807",
        )
        for source_url in (
            row["source_url"].replace("basDd=20260807", "basDd=20260806"),
            row["source_url"] + "&page=1",
            row["source_url"].split("?", 1)[0],
        ):
            with self.subTest(source_url=source_url):
                tampered = deepcopy(row)
                tampered["source_url"] = source_url
                with self.assertRaisesRegex(ValueError, "current and canonical"):
                    profile_module._validate_krx_row(tampered, as_of_date=AS_OF)

    def test_provider_quote_sector_and_raw_hash_tamper_fail_closed(self) -> None:
        for mode in (
            "quote_tamper",
            "cross_sector",
            "duplicate_target",
            "missing_roster",
            "forbidden_authority",
            "raw_mismatch",
            "provider_failure",
        ):
            with self.subTest(mode=mode):
                result, _, provider = self._materialize(
                    provider=FakeCompatibilityProvider(mode=mode)
                )
                self.assertEqual(result["status"], PROFILE_PENDING)
                self.assertEqual(provider.calls, 1)
                self.assertEqual(result["selections"], [])

    def test_production_rejects_fake_provider_but_test_mode_never_passes(self) -> None:
        fake = FakeCompatibilityProvider(
            provider_name="fixture_provider",
            real_provider=False,
            fake_provider=True,
        )
        production, _, _ = self._materialize(provider=fake)
        self.assertEqual(production["status"], PROFILE_PENDING)
        test_result, _, _ = self._materialize(
            provider=FakeCompatibilityProvider(
                provider_name="fixture_provider",
                real_provider=False,
                fake_provider=True,
            ),
            test_mode=True,
        )
        self.assertEqual(test_result["status"], PROFILE_TEST_ONLY)
        self.assertFalse(test_result["audit"]["production_acceptance_pass"])

    def test_abstain_and_pending_never_become_complete(self) -> None:
        for mode in ("abstain", "pending"):
            with self.subTest(mode=mode):
                result, _, _ = self._materialize(
                    provider=FakeCompatibilityProvider(mode=mode)
                )
                self.assertNotEqual(result["status"], PROFILE_PASS)

    def test_provider_prompt_and_call_count_are_bounded(self) -> None:
        _, industries = _five_rows()
        fetcher = FakeOpenDartFetcher(industries, document_padding=3_000)
        provider = FakeCompatibilityProvider()
        result, _, _ = self._materialize(
            fetcher=fetcher,
            provider=provider,
            max_prompt_chars=10_000,
        )
        self.assertEqual(result["status"], PROFILE_PASS)
        self.assertEqual(provider.calls, 5)
        self.assertTrue(all(length <= 10_000 for length in provider.prompt_lengths))
        self.assertLessEqual(result["audit"]["profile_fetch_count"], 5)

    def test_oversized_full_reports_are_chunked_without_unprompted_quote_authority(self) -> None:
        _, industries = _five_rows()
        fetcher = FakeOpenDartFetcher(industries, document_padding=30_000)
        provider = FakeCompatibilityProvider()
        result, _, _ = self._materialize(
            fetcher=fetcher,
            provider=provider,
            max_prompt_chars=10_000,
        )
        self.assertEqual(result["status"], PROFILE_PASS)
        self.assertEqual(provider.calls, 5)
        self.assertTrue(all(length <= 10_000 for length in provider.prompt_lengths))

        unprompted, _, bad_provider = self._materialize(
            fetcher=FakeOpenDartFetcher(industries, document_padding=30_000),
            provider=FakeCompatibilityProvider(mode="unprompted_quote"),
            max_prompt_chars=10_000,
        )
        self.assertEqual(unprompted["status"], PROFILE_PENDING)
        self.assertEqual(bad_provider.calls, 1)
        self.assertEqual(unprompted["selections"], [])

    def test_chunking_reviews_the_report_tail_without_dropping_ranges(self) -> None:
        _, industries = _five_rows()
        provider = FakeCompatibilityProvider(mode="tail_quote")
        result, _, _ = self._materialize(
            fetcher=FakeOpenDartFetcher(industries, document_padding=30_000),
            provider=provider,
            max_prompt_chars=10_000,
            max_fetches=100,
        )
        self.assertEqual(result["status"], PROFILE_PASS)
        self.assertGreater(provider.calls, 5)
        self.assertLessEqual(provider.calls, 100)
        self.assertTrue(all(length <= 10_000 for length in provider.prompt_lengths))
        self.assertTrue(
            all(row["exact_quote"] == "</BODY></DOCUMENT>" for row in result["selections"])
        )

    def test_exported_validators_reject_quote_hash_or_orphan_tamper(self) -> None:
        result, fetcher, _ = self._materialize()
        self.assertEqual(
            validate_issuer_business_profile_result(
                result,
                full_documents_by_id=fetcher.full_documents,
            )["status"],
            PROFILE_PASS,
        )
        quote_tamper = deepcopy(result)
        quote_tamper["selections"][0]["exact_quote"] += " 변조"
        with self.assertRaisesRegex(ValueError, "quote"):
            validate_forced_validation_profile_manifest(quote_tamper)
        orphan = deepcopy(result)
        orphan["selections"][0]["compatibility_response_id"] = "PROFILECLASSRESP-orphan"
        with self.assertRaisesRegex(ValueError, "orphan"):
            validate_issuer_business_profile_result(orphan)
        response_hash_tamper = deepcopy(result)
        response_hash_tamper["compatibility_receipts"][0]["raw_response"] += " "
        with self.assertRaisesRegex(ValueError, "envelope/hash"):
            validate_issuer_business_profile_result(response_hash_tamper)
        request_hash_tamper = deepcopy(result)
        request_hash_tamper["compatibility_receipts"][0]["request_envelope"][
            "as_of_date"
        ] = "2026-08-08"
        with self.assertRaisesRegex(ValueError, "envelope/hash"):
            validate_issuer_business_profile_result(request_hash_tamper)
        expansion_hash_tamper = deepcopy(result)
        expansion_hash_tamper["candidate_expansion_receipt"][
            "natural_candidate_roster_hash"
        ] = "0" * 64
        with self.assertRaisesRegex(ValueError, "natural/full KRX roster"):
            validate_issuer_business_profile_result(expansion_hash_tamper)
        document_tamper = dict(fetcher.full_documents)
        first_doc = result["selections"][0]["periodic_report_document_id"]
        document_tamper[first_doc] += "변조"
        with self.assertRaisesRegex(ValueError, "full document"):
            validate_issuer_business_profile_result(
                result,
                full_documents_by_id=document_tamper,
            )

    def test_per_target_validator_recomputes_official_source_hashes(self) -> None:
        rows, industries = _five_rows()
        fetcher = FakeOpenDartFetcher(industries)
        bundle = fetcher.fetch(
            target_id=rows[0]["symbol"],
            company_name=rows[0]["company_name"],
            as_of_date=date.fromisoformat(AS_OF),
            credential="official-fixture-key",
            max_list_pages=3,
            timeout_seconds=30,
        )
        profile, full_text = validate_issuer_business_profile(
            krx_row=rows[0],
            opendart_bundle=bundle,
            as_of_date=AS_OF,
        )
        self.assertEqual(
            profile["source_hashes"]["document_full_text_hash"],
            profile_module._sha256_text(full_text),
        )
        tampered = deepcopy(bundle)
        tampered["document_receipt"]["response_text"] += "tampered"
        with self.assertRaisesRegex(ValueError, "hash mismatch"):
            validate_issuer_business_profile(
                krx_row=rows[0],
                opendart_bundle=tampered,
                as_of_date=AS_OF,
            )

    def test_non_opendart_fetcher_is_rejected(self) -> None:
        _, industries = _five_rows()
        fetcher = FakeOpenDartFetcher(industries)
        fetcher.provider_name = "general_web"
        with self.assertRaisesRegex(ValueError, "official-only"):
            self._materialize(fetcher=fetcher)


if __name__ == "__main__":
    unittest.main()
