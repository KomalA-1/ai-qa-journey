import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(params=["chromium", "firefox", "webkit"])
def page(request):
    browser_name =request.param
    with sync_playwright() as p:
        browser_type = getattr(p, browser_name)
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page       #give page to the test
        browser.close()  #closes after test finishes


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            page.screenshot(path=f"screenshots/FALED_{item.name}.png")

from bug_reporter import generate_bug_report
from datetime import datetime

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_path = f"screenshots/FAILED_{item.name}.png"
            page.screenshot(path = screenshot_path)

            generate_bug_report(
                test_name = item.name,
                status = "FAILED",
                screenshot_path = screenshot_path,
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )

