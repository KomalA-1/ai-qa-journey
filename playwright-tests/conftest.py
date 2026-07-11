# conftest.py
import pytest
from playwright.sync_api import sync_playwright
from bug_reporter import generate_bug_report
from datetime import datetime


@pytest.fixture(params=["chromium", "firefox", "webkit"])
def page(request):
    browser_name = request.param

    marker = request.node.get_closest_marker("chromium_only")
    if marker and browser_name != "chromium":
        pytest.skip(f"Skipped on {browser_name} — chromium only")

    with sync_playwright() as p:
        browser_type = getattr(p, browser_name)
        browser = browser_type.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1280, "height": 720}
        )
        page = context.new_page()
        page.set_default_timeout(60000)
        yield page
        context.close()
        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_path = f"screenshots/FAILED_{item.name}.png"
            page.screenshot(path=screenshot_path)
            generate_bug_report(
                test_name=item.name,
                status="FAILED",
                screenshot_path=screenshot_path,
                timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )