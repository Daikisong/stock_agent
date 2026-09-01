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

# Operational notices must be separate UI surfaces.  Searching the complete
# conversation body for words such as "error" is unsafe because a valid
# research report can quote or describe a provider/parser error.
OPERATIONAL_NOTICE_SELECTORS = (
    '[role="alert"]',
    '[aria-live="assertive"]',
    '[data-testid*="error" i]',
    '[data-testid*="toast" i]',
    '[data-testid*="quota" i]',
    '[data-sonner-toast]',
)

CHAT_HISTORY_SEARCH_CONTROL_SELECTORS = (
    'button[aria-label="검색"]',
    'button[aria-label*="채팅 검색"]',
    'button[aria-label*="Search chats" i]',
    'button[aria-label="Search"]',
)

CHAT_HISTORY_SEARCH_INPUT_SELECTORS = (
    'input[placeholder*="검색"]:visible',
    'input[placeholder*="Search" i]:visible',
    '[role="dialog"] input:visible',
)

CHAT_HISTORY_RESULT_LINK_SELECTORS = (
    'a[href*="/c/"]',
)

# Current ChatGPT Pro UI (2026-08): research runs from the ordinary composer
# with the reasoning level shown as ``Pro``.  Some deployments no longer
# render the former top-level ``Chat``/``Work`` radio group, so the visible
# prompt editor is the durable Chat surface.  If the older group is present,
# an active Work control still excludes the page from this path.
CHAT_MODE_ACTIVE_SELECTORS = (
    'button[role="radio"][data-state="on"]:has-text("Chat")',
    'button[role="radio"][aria-checked="true"]:has-text("Chat")',
)

CHAT_MODE_CONTROL_SELECTORS = (
    'button[role="radio"]:has-text("Chat")',
)

WORK_MODE_ACTIVE_SELECTORS = (
    'button[role="radio"][data-state="on"]:has-text("Work")',
    'button[role="radio"][aria-checked="true"]:has-text("Work")',
)

PRO_REASONING_ACTIVE_SELECTORS = (
    'form button:has-text("Pro")',
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
    'a[href*="/auth/signup"]',
    'a[href*="/log-in"]',
    'a[href*="/sign-up"]',
    'a[href*="auth.openai.com"]',
    'button[data-testid*="login"]',
    'button:has-text("Log in")',
    'a:has-text("Log in")',
    'button:has-text("Sign up")',
    'a:has-text("Sign up")',
    'button:has-text("로그인")',
    'a:has-text("로그인")',
    'button:has-text("가입")',
    'a:has-text("가입")',
)

MD_CANDIDATE_SELECTORS = (
    'button:has-text(".md")',
    'a:has-text(".md")',
    '[data-testid*="behavior-btn"]:has-text(".md")',
    '.entity-underline:has-text(".md")',
)

PDF_CANDIDATE_SELECTORS = (
    'button:has-text(".pdf")',
    'a:has-text(".pdf")',
    '[data-testid*="behavior-btn"]:has-text(".pdf")',
    '.entity-underline:has-text(".pdf")',
)

JSON_CANDIDATE_SELECTORS = (
    'button:has-text(".json")',
    'a:has-text(".json")',
    '[data-testid*="behavior-btn"]:has-text(".json")',
    '.entity-underline:has-text(".json")',
)

PREVIEW_ROOT_SELECTORS = (
    '[role="dialog"]',
    '[data-side-pane-shell-rail="true"]',
    '[data-side-pane-shell-surface="true"]',
    '[data-testid="stage-thread-flyout"]',
    '[data-testid="screen-threadFlyOut"]',
)

PREVIEW_CLOSE_SELECTORS = (
    '[role="dialog"][aria-label$=".md" i] button[data-testid="close-button"]',
    '[role="dialog"][aria-label$=".json" i] button[data-testid="close-button"]',
    '[role="dialog"][aria-label$=".pdf" i] button[data-testid="close-button"]',
    '[data-testid="stage-thread-flyout"] button[data-testid="close-button"]',
    '[data-testid="screen-threadFlyOut"] button[data-testid="close-button"]',
)

DOWNLOAD_SELECTORS = (
    'a[download]',
    'button[aria-label*="파일 다운로드"]',
    'a[aria-label*="파일 다운로드"]',
    'button[aria-label*="Download file" i]',
    'a[aria-label*="Download file" i]',
    'button[aria-label="다운로드"]',
    'button[aria-label="Download"]',
    'a[aria-label="다운로드"]',
    'a[aria-label="Download"]',
    'button:has-text("다운로드")',
    'button:has-text("Download")',
)

ASSISTANT_TURN_SELECTORS = (
    'section[data-turn="assistant"]',
    '[data-message-author-role="assistant"]',
    'article[data-turn="assistant"]',
    '[data-testid^="conversation-turn-"]:has([data-message-author-role="assistant"])',
    '[data-e2r-role="assistant"]',
)

USER_TURN_SELECTORS = (
    'section[data-turn="user"]',
    '[data-message-author-role="user"]',
    'article[data-turn="user"]',
    '[data-e2r-role="user"]',
)

CITATION_SELECTORS = (
    'a[href^="http://"]',
    'a[href^="https://"]',
    '[data-testid*="citation"]',
    '[data-testid*="source"]',
    'button:has-text("Sources")',
    'button:has-text("출처")',
)

__all__ = [name for name in globals() if name.endswith("_SELECTORS")]
