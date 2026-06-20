# Day 26 - Advanced POM (Multi-Page)

from pages.login_page import LoginPage

def test_login_then_check_dashboard(page):
    login = LoginPage(page)
    login.navigate()

    # This now returns a DashboardPage object!
    dashboard = login.login_and_go_to_dashboard("student", "Password123")

    assert dashboard.is_on_dashboard(), "Did not reached Dashboard!"
    print(f"Reached Dashboard! URL: {dashboard.get_current_url()}")

def test_login_then_logout(page):
    login = LoginPage(page)
    login.navigate()

    dashboard = login.login_and_go_to_dashboard("student", "Password123")
    assert dashboard.is_on_dashboard()
    print("On dashboard, now logging out...")

    dashboard.click_logout()
    page.wait_for_timeout(2000)

    # After logout we should be back on login page
    assert "practice-test-login" in page.url
    print("Successfully logged out and returned to login page!")

def test_dashboard_heading(page):
    login = LoginPage(page)
    login.navigate()

    dashboard = login.login_and_go_to_dashboard("student", "Password123")
    heading = dashboard.get_success_heading()
    print(f"Dashboard heading: {heading}")
    assert heading != ""