# Day 25 - Data Driven Testing

import pytest
from pages.login_page import LoginPage

login_data = [
    ("student", "Password123", "success"),
    ("wronguser", "wrongpass", "failed"),
    ("student", "WrongPass999", "failed"),
    (""       , "Password123", "failed"),
    ("STUDENT", "Password123", "failed"),
    ("student", ""           , "failed"),
    ("student ", "Password123", "failed")
]

@pytest.mark.parametrize("username, password, expected", login_data)
def test_login_data_driven(page, username, password, expected):
    login = LoginPage(page)
    login.navigate()
    login.login(username, password)

    if expected == "success":
        assert login.is_login_successful(), \
            f"Expected success but failed for user: '{username}'"
        print(f"SUCCESS | user: '{username}'")

    elif expected == "failed":
        assert login.is_login_failed(), \
            f"Expected failure but passed for user: '{username}'"
        print(f"FAILED AS EXPECTED | user: '{username}'")