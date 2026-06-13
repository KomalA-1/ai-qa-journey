from pages.login_page import LoginPage

def test_valid_login(page):
    login = LoginPage(page)
    login.navigate()
    login.login("student", "Password123")

    assert login.is_login_successful(), "Valid login failed - success message not found!"
    print("Valid Login PASSED!")

def test_invalid_username(page):
    login = LoginPage(page)
    login.navigate()
    login.login("wronguser", "wrongpass")

    assert login.is_login_failed(), "Invalid login test failed - error message not found!"
    print("Invalid Login test PASSED!")

def test_invalid_password(page):
    login = LoginPage(page)
    login.navigate()
    login.login("student", "password123")

    assert login.is_login_failed(), "Wrong password test failed - error message not found!"
    print("Invalid Password PASSED!")