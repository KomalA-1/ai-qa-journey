from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login = LoginPage(page)
        login.navigate()
        login.login("student", "Password123")

        if login.is_login_successful():
            print("Valid Login PASSED!")
        else:
            print("Valid Login FAILED!")

        browser.close()

def test_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login = LoginPage(page)
        login.navigate()
        login.login("wronguser", "wrongpass")

        if login.is_login_failed():
            print("Invalid Login PASSED!")
        else:
            print("Invalid Login FAILED!")

        browser.close()

test_valid_login()
test_invalid_login()