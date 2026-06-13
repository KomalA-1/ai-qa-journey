from pages.login_page import LoginPage

def test_valid_login(page):
    login = LoginPage(page)
    login.navigate()
    login.login("student","Password123")

    if login.is_login_successful():
        print("Valid Login PASSED!")
    else:
        print("Valid Login FAILED")

def test_invalid_login(page):
    login = LoginPage(page)
    login.navigate()
    login.login("wronguser", "wrongpass")

    if login.is_login_failed():
        print("Invalid Login PASSED!")
    else:
        print("Invalid Login FAILED!")

def test_wrong_password(page):
    login = LoginPage(page)
    login.navigate()
    login.login("student", "password123")

    if login.is_login_failed():
        print("Wrong Password Test PASSED!")
    else:
        print("Wrong Password Test FAILED!")

