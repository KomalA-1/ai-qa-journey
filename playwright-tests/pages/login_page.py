# pages/login_page.py
# Page Object Model for Login Page

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://practicetestautomation.com/practice-test-login/"

    def navigate(self):
        self.page.goto(self.url)

    def enter_username(self, username):
        self.page.get_by_label("Username").fill(username)

    def enter_password(self, password):
        self.page.get_by_label("Password").fill(password)
    
    def click_submit(self):
        self.page.get_by_role("button", name="Submit").click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()
        self.page.wait_for_timeout(2000)

    def get_body_text(self):
        return self.page.inner_text("body")
    
    def is_login_successful(self):
        return "logged-in-successfully" in self.page.url

    def is_login_failed(self):
        return "invalid" in self.get_body_text() and "logged-in-successfully" not in self.page.url

    def take_screenshot(self, name):
        self.page.screenshot(path=f"screenshots/{name}.png")   
    