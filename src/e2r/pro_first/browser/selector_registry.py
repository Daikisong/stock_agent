"""Auditable ChatGPT DOM selector priorities."""

EDITOR_SELECTORS = (
    'div.ProseMirror[contenteditable="true"]',
    '[contenteditable="true"]',
    'textarea[name="prompt-textarea"]',
    '#prompt-textarea',
)

SEND_SELECTORS = (
    '#composer-submit-button',
    'button[data-testid="send-button"]',
    'button[aria-label*="프롬프트 보내기"]',
    'button[aria-label*="전송"]',
    'button[aria-label*="Send"]',
    'form button[type="submit"]',
)

STOP_SELECTORS = (
    'button[data-testid="stop-button"]',
    'button[aria-label*="중지"]',
    'button[aria-label*="Stop"]',
)

DEEP_RESEARCH_ACTIVE_SELECTORS = (
    '[data-testid*="deep-research"][aria-pressed="true"]',
    '[data-testid*="deep-research"][data-state="active"]',
    '[data-testid*="deep-research"][data-state="on"]',
    'button[aria-label*="Deep research"][aria-pressed="true"]',
    'button[aria-label*="심층 리서치"][aria-pressed="true"]',
)

DEEP_RESEARCH_CONTROL_SELECTORS = (
    'button[data-testid*="deep-research"]',
    'button[aria-label*="Deep research"]',
    'button[aria-label*="Deep Research"]',
    'button[aria-label*="심층 리서치"]',
    'button:has-text("Deep research")',
    'button:has-text("심층 리서치")',
)

DEEP_RESEARCH_OPTION_SELECTORS = (
    '[role="menuitem"]:has-text("Deep research")',
    '[role="menuitem"]:has-text("심층 리서치")',
    '[role="option"]:has-text("Deep research")',
    '[role="option"]:has-text("심층 리서치")',
)

TOOLS_BUTTON_SELECTORS = (
    'button[data-testid*="tools"]',
    'button[aria-label*="도구"]',
    'button[aria-label*="Tools"]',
)

ATTACH_BUTTON_SELECTORS = (
    'button[data-testid*="attach"]',
    'button[aria-label*="파일"]',
    'button[aria-label*="첨부"]',
    'button[aria-label*="Attach"]',
)

FILE_INPUT_SELECTORS = ('input[type="file"]',)

LOGIN_INDICATOR_SELECTORS = (
    'a[href*="/auth/login"]',
    'button:has-text("Log in")',
    'button:has-text("로그인")',
)

MD_CANDIDATE_SELECTORS = (
    'button:has-text(".md")',
    'a:has-text(".md")',
    '[data-testid*="behavior-btn"]:has-text(".md")',
    '.entity-underline:has-text(".md")',
)

PREVIEW_ROOT_SELECTORS = (
    '[role="dialog"]',
    '[data-side-pane-shell-rail="true"]',
    '[data-side-pane-shell-surface="true"]',
)

DOWNLOAD_SELECTORS = (
    'a[download]',
    'button[aria-label="다운로드"]',
    'button[aria-label="Download"]',
    'a[aria-label="다운로드"]',
    'a[aria-label="Download"]',
    'button:has-text("다운로드")',
    'button:has-text("Download")',
)

__all__ = [name for name in globals() if name.endswith("_SELECTORS")]
