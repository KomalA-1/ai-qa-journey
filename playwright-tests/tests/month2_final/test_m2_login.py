# tests/month2_final/test_m2_login.py
# Month 2 Final Project - Login Tests
# Generated using AI prompt engineering + self-healing locators

import pytest
from pages.login_page import LoginPage
from pages.smart_locator import find_element_smart

login_data = [
    ("student",   "Password123",  "success"),
    ("wronguser", "wrongpass",    "failed"),
    ("student",   "WrongPass999", "failed"),
    ("",          "Password123",  "failed"),
    ("' OR '1'='1", "hack",      "failed"),  # SQL injection
]

@pytest.mark.parametrize("username, password, expected", login_data)
def test_login_data_driven(page, username, password, expected):
    login = LoginPage(page)
    login.navigate()
    login.login(username, password)

    if expected == "success":
        assert login.is_login_successful(), \
            f"❌ Expected success for '{username}'"
        print(f"✅ Login SUCCESS: '{username}'")
    else:
        assert login.is_login_failed(), \
            f"❌ Expected failure for '{username}'"
        print(f"✅ Login correctly FAILED: '{username}'")

# @pytest.mark.chromium_only
def test_self_healing_login(page):
    """Login test using self-healing locator strategy"""
    try:
        page.goto(
            "https://practicetestautomation.com/practice-test-login/",
            wait_until="domcontentloaded",
            timeout=60000
        )
    except Exception as e:
        pytest.skip(f"External site unreachable on this browser: {e}")

    submit_strategies = [
        lambda p: p.get_by_role("button", name="WRONG"),
        lambda p: p.get_by_role("button", name="Submit"),
    ]

    page.get_by_label("Username").fill("student")
    page.get_by_label("Password").fill("Password123")

    button = find_element_smart(page, submit_strategies, "Submit button")
    button.click()
    page.wait_for_timeout(2000)

    assert "logged-in-successfully" in page.url
    print("✅ Self-healing login test PASSED!")