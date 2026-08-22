"""Local DOM-contract mock driven by the production Playwright adapter."""

from __future__ import annotations

from contextlib import AbstractContextManager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import threading
from urllib.parse import parse_qs, urlparse


def _mock_report(*, job_id: str, run_id: str, target_id: str, as_of_date: str) -> str:
    dossier = {
        "schema_version": "e2r_pro_research_dossier_v1",
        "job_id": job_id,
        "run_id": run_id,
        "target": {"target_id": target_id},
        "as_of_date": as_of_date,
        "research_status": "COMPLETE",
        "business_model": {},
        "candidate_archetypes": [],
        "material_facts": [],
        "counterfacts": [],
        "component_research": {
            "eps_fcf_explosion": {},
            "earnings_visibility": {},
            "bottleneck_pricing": {},
            "market_mispricing": {},
            "valuation_rerating": {},
            "capital_allocation": {},
            "information_confidence": {},
        },
        "structured_metrics": {},
        "unresolved_gaps": [],
        "sources": [],
        "research_saturation": {},
        "proposed_score_ranges": {},
        "score_authority": False,
        "stage_authority": False,
    }
    return "\n".join(
        (
            "# E2R Pro 독립 연구 결과",
            f"[[E2R_PRO_RUN_ID:{run_id}]]",
            f"[[E2R_PRO_JOB_ID:{job_id}]]",
            "검증 가능한 출처를 포함한 최종 보고서입니다.",
            "E2R_RESEARCH_DOSSIER_JSON_BEGIN",
            "```json",
            json.dumps(dossier, ensure_ascii=False, sort_keys=True),
            "```",
            "E2R_RESEARCH_DOSSIER_JSON_END",
        )
    )


def render_mock_chatgpt(
    state: str = "READY_FOR_INPUT",
    *,
    job_id: str = "PROJOB-mock",
    run_id: str = "PRORUN-mock",
    target_id: str = "123456",
    as_of_date: str = "2026-08-22",
    filename: str = "E2R_PRO_PROJOB-mock_123456_2026-08-22.md",
) -> str:
    login = state == "LOGIN_REQUIRED"
    composer = "" if login else """
      <main>
        <div data-message-id="old-turn"><button id="old-md" class="entity-underline">old_result.md</button></div>
        <button id="deep-research" data-testid="deep-research-toggle" aria-label="Deep research" aria-pressed="false">Deep research</button>
        <input id="packet-input" type="file" hidden>
        <div id="attachments"></div>
        <form id="composer-form">
          <div id="prompt-textarea" class="ProseMirror" contenteditable="true"></div>
          <button id="composer-submit-button" type="button" aria-label="Send">Send</button>
          <button data-testid="stop-button" type="button" hidden>Stop</button>
        </form>
        <section id="conversation-results"></section>
      </main>
    """
    login_markup = '<a href="/auth/login">Log in</a>' if login else ""
    return f"""<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>E2R Mock ChatGPT</title></head>
<body data-mock-state="{state}">
  {login_markup}
  {composer}
  <script>
    window.__submitCount = 0;
    window.__downloadClicks = [];
    const defaultContext = {json.dumps({"job_id": job_id, "run_id": run_id, "target_id": target_id, "as_of_date": as_of_date, "filename": filename})};
    function reportText(context) {{
      const dossier = {{
        schema_version: 'e2r_pro_research_dossier_v1', job_id: context.job_id,
        run_id: context.run_id, target: {{target_id: context.target_id}},
        as_of_date: context.as_of_date, research_status: 'COMPLETE', business_model: {{}},
        candidate_archetypes: [], material_facts: [], counterfacts: [],
        component_research: {{
          eps_fcf_explosion: {{}}, earnings_visibility: {{}}, bottleneck_pricing: {{}},
          market_mispricing: {{}}, valuation_rerating: {{}}, capital_allocation: {{}},
          information_confidence: {{}}
        }}, structured_metrics: {{}}, unresolved_gaps: [],
        sources: [], research_saturation: {{}}, proposed_score_ranges: {{}},
        score_authority: false, stage_authority: false
      }};
      return '# E2R Pro 독립 연구 결과\\n' +
        `[[E2R_PRO_RUN_ID:${{context.run_id}}]]\\n` +
        `[[E2R_PRO_JOB_ID:${{context.job_id}}]]\\n` +
        '검증 가능한 출처를 포함한 최종 보고서입니다.\\n' +
        'E2R_RESEARCH_DOSSIER_JSON_BEGIN\\n```json\\n' +
        JSON.stringify(dossier) + '\\n```\\nE2R_RESEARCH_DOSSIER_JSON_END';
    }}
    function openPreview(context, oldFile=false) {{
      document.querySelector('[role="dialog"]')?.remove();
      const dialog = document.createElement('div');
      dialog.setAttribute('role', 'dialog');
      const app = document.createElement('button');
      app.textContent = '앱 다운로드';
      dialog.appendChild(app);
      const link = document.createElement('a');
      link.setAttribute('aria-label', 'Download');
      link.textContent = 'Download';
      const selected = oldFile ? 'old_result.md' : context.filename;
      const params = new URLSearchParams({{...context, filename: selected}});
      link.href = '/download?' + params.toString();
      link.download = selected;
      link.addEventListener('click', () => window.__downloadClicks.push(selected));
      dialog.appendChild(link);
      document.body.appendChild(dialog);
    }}
    window.__setMockState = (nextState, supplied={{}}) => {{
      const context = {{...defaultContext, ...supplied}};
      document.body.dataset.mockState = nextState;
      const results = document.querySelector('#conversation-results');
      if (!results) return;
      results.replaceChildren();
      const stop = document.querySelector('[data-testid="stop-button"]');
      stop.hidden = nextState !== 'RUNNING';
      if (nextState === 'RUNNING') {{
        const partial = document.createElement('article');
        partial.dataset.turn = 'assistant';
        partial.dataset.messageId = 'running-turn';
        partial.textContent = 'Research in progress';
        results.appendChild(partial);
      }} else if (nextState === 'CLARIFICATION') {{
        const turn = document.createElement('article');
        turn.dataset.turn = 'assistant'; turn.dataset.messageId = 'clarification-turn';
        turn.textContent = 'Before I start, please clarify a new investment assumption?';
        results.appendChild(turn);
      }} else if (nextState === 'QUOTA') {{
        results.textContent = 'Usage limit reached. Quota pending.';
      }} else if (nextState === 'ERROR') {{
        results.textContent = 'Something went wrong. Please try again.';
      }} else if (nextState === 'COMPLETE_WITH_MD' || nextState === 'COMPLETE_WITH_MD_AND_PDF' || nextState === 'COMPLETE_WITH_DIRECT_REPORT') {{
        const turn = document.createElement('article');
        turn.dataset.turn = 'assistant'; turn.dataset.messageId = 'final-turn';
        turn.setAttribute('data-message-author-role', 'assistant');
        const pre = document.createElement('pre'); pre.textContent = reportText(context);
        turn.appendChild(pre);
        const citation = document.createElement('a'); citation.href = 'https://example.com/source';
        citation.textContent = 'Source'; turn.appendChild(citation);
        if (nextState === 'COMPLETE_WITH_MD' || nextState === 'COMPLETE_WITH_MD_AND_PDF') {{
          const file = document.createElement('button');
          file.className = 'entity-underline'; file.textContent = context.filename;
          file.addEventListener('click', () => openPreview(context));
          turn.appendChild(file);
        }}
        if (nextState === 'COMPLETE_WITH_MD_AND_PDF') {{
          const pdfContext = {{...context, filename: context.filename.replace(/\.md$/i, '.pdf')}};
          const pdf = document.createElement('button');
          pdf.className = 'entity-underline'; pdf.textContent = pdfContext.filename;
          pdf.addEventListener('click', () => openPreview(pdfContext));
          turn.appendChild(pdf);
        }}
        results.appendChild(turn);
      }}
    }};
    const deep = document.querySelector('#deep-research');
    if (deep) deep.addEventListener('click', () => deep.setAttribute('aria-pressed', 'true'));
    const input = document.querySelector('#packet-input');
    if (input) input.addEventListener('change', () => {{
      const button = document.createElement('button');
      button.type = 'button';
      button.dataset.testid = 'behavior-btn-attachment';
      button.textContent = input.files[0].name;
      document.querySelector('#attachments').appendChild(button);
    }});
    const send = document.querySelector('#composer-submit-button');
    if (send) send.addEventListener('click', () => {{
      window.__submitCount += 1;
      window.__setMockState('RUNNING');
    }});
    const oldMd = document.querySelector('#old-md');
    if (oldMd) oldMd.addEventListener('click', () => openPreview(defaultContext, true));
    window.__setMockState({json.dumps(state)}, defaultContext);
  </script>
</body>
</html>"""


class _MockHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802 - BaseHTTPRequestHandler API
        parsed = urlparse(self.path)
        query = parse_qs(parsed.query)
        if parsed.path == "/download":
            filename = query.get("filename", ["E2R_PRO_mock.md"])[0]
            if filename.lower().endswith(".pdf"):
                report = b"%PDF-1.4\n% E2R mock PDF\n1 0 obj<<>>endobj\n%%EOF\n"
                content_type = "application/pdf"
            else:
                report = _mock_report(
                    job_id=query.get("job_id", ["PROJOB-mock"])[0],
                    run_id=query.get("run_id", ["PRORUN-mock"])[0],
                    target_id=query.get("target_id", ["123456"])[0],
                    as_of_date=query.get("as_of_date", ["2026-08-22"])[0],
                ).encode("utf-8")
                content_type = "text/markdown; charset=utf-8"
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Disposition", f'attachment; filename="{filename}"')
            self.send_header("Content-Length", str(len(report)))
            self.end_headers()
            self.wfile.write(report)
            return
        state = query.get("state", ["READY_FOR_INPUT"])[0]
        body = render_mock_chatgpt(
            state,
            job_id=query.get("job_id", ["PROJOB-mock"])[0],
            run_id=query.get("run_id", ["PRORUN-mock"])[0],
            target_id=query.get("target_id", ["123456"])[0],
            as_of_date=query.get("as_of_date", ["2026-08-22"])[0],
            filename=query.get(
                "filename", ["E2R_PRO_PROJOB-mock_123456_2026-08-22.md"]
            )[0],
        ).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, _format: str, *_args: object) -> None:
        return


class MockChatGPTServer(AbstractContextManager["MockChatGPTServer"]):
    def __init__(self) -> None:
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), _MockHandler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)

    @property
    def base_url(self) -> str:
        return f"http://127.0.0.1:{self.server.server_port}"

    def __enter__(self) -> "MockChatGPTServer":
        self.thread.start()
        return self

    def __exit__(self, *_args: object) -> None:
        self.server.shutdown()
        self.thread.join(timeout=5)
        self.server.server_close()


__all__ = ["MockChatGPTServer", "render_mock_chatgpt"]
