from pages.login_page import LoginPage

def test_valid_login_with_screenshot(page):
    login = LoginPage(page)
    login.navigate()
    login.login("student", "Password123")

    login.take_screenshot("Valid _login_success")

    assert login.is_login_successful(), "Valid Login Failed!"
    print("Valid Login PASSED! Screenshot saved.")

def test_invalid_login_with_screenshot(page):
    login = LoginPage(page)
    login.navigate()
    login.login("wronguser", "wrongpass")

    login.take_screenshot("invalid_login_error")

    assert login.is_login_failed(), "Invalid Login Failed!"
    print("Invalid Login Passed! Screenshot saved.")