# Page Object for the Dashboard / Logged-in page

class DashboardPage:
    def __init__(self,page):
        self.page = page

    def get_welcome_message(self):
        return self.page.inner_text("body")
    
    def is_on_dashboard(self):
        return "logged-in-successfully" in self.page.url
    
    def get_current_url(self):
        return self.page.url
    
    def click_logout(self):
        # This site has a "Log out" link after login
        self.page.get_by_role("link", name = "Log out").click()

    def get_success_heading(self):
        return self.page.get_by_role("heading").inner_text()