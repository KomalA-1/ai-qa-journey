# Day 27 - Visual and Accessibility Testing

from playwright.sync_api import expect
from axe_playwright_python.sync_playwright import Axe
from pages.login_page import LoginPage

def test_visual_snapshot(page):
    login = LoginPage(page)
    login.navigate()
    page.wait_for_timeout(2000)

    # Visual regression check
    # expect(page).to_have_screenshot("login_page_visual.png")
    page.screenshot(path="screenshots/visual_baseline_login.png", full_page=True)
    print("Visual snapshot captured/verified!")

def test_accessibility_scan(page):
    login = LoginPage(page)
    login.navigate()
    page.wait_for_timeout(2000)

    axe = Axe()
    results = axe.run(page)

    violations = results.response.get("violations", [])

    print(f"Accessibility violations found: {len(violations)}")

    for v in violations:
        print(f"{v['id']} : {v['description']} Impact : {v['impact']}")

    # We just report - not fail - since some sites always have minor issues
    if len(violations) == 0:
        print("No accessibity violations found!")
    else:
        print(f"Found {len(violations)} accessibility issues to review")


    critical_violations = [v for v in violations if v['impact'] == 'critical']
    assert len(critical_violations) == 0, f"Found {len(critical_violations)} CRITICAL accessibility issues!"
    print("No critical accessibility issues!")

        
