# Month 1 Final Project - Accessibility Suite

from axe_playwright_python.sync_playwright import Axe
from pages.login_page import LoginPage

def test_login_page_accessibility(page):
    login = LoginPage(page)
    login.navigate()
    page.wait_for_timeout(2000)

    axe = Axe()
    results = axe.run(page)
    violations = results.response.get("violations", [])

    critical = [v for v in violations if v['impact'] == 'critical']

    print(f"Total violations: {len(violations)} | Critical: {len(critical)}")
    for v in violations:
        print (f"{v['id']} ({v['impact']}): {v['description']}")

    assert len(critical) == 0, "Critical accesibility issues found!"
    print("No critical accesibility issues on login page")