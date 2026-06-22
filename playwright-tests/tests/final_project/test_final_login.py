# Month 1 Final Project - Login and Dashboard Test Suite

import pytest
from pages.login_page import LoginPage

login_data = [
    ("student"  , "Password123", "success"),
    ("wronguser", "wrongpass", "failed"),
    ("student"  , "WrongPass999", "failed"),
    (""         , "Password123", "failed"),
]

@pytest.mark.parametrize("username, password, expected", login_data)
def test_login_scenarios(page, username, password, expected):
    login = LoginPage(page)
    login.navigate()
    login.login(username, password)

    if expected == "success":
        assert login.is_login_successful(), f"Expected success for '{username}'"
        print(f"Login success for user: '{username}")
    else:
        assert login.is_login_failed(), f"Expected failure for '{username}"
        print(f"Login failed for user: '{username}")

def test_full_user_journey(page):
    # End to end Login > Dashboard > Logout
    login = LoginPage(page)
    login.navigate()

    dashboard = login.login_and_go_to_dashboard("student","Password123")
    assert dashboard.is_on_dashboard(), "Did not reach dashboard"
    print(f"Reached Dashboard: {dashboard.get_current_url()}")

    heading = dashboard.get_success_heading()
    assert heading != ""
    print(f"Dashboard heading verified: {heading}")

    dashboard.click_logout()
    page.wait_for_timeout(2000)
    assert "practice-test-login" in page.url
    print("Full user journey PASSED: Login -> Dashboard -> Logout")