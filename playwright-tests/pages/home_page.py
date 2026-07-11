# pages/home_page.py
# Page Object for automationexercise.com Home Page

import pytest


class HomePage:
    def __init__(self, page):
        self.page = page
        self.url = "https://automationexercise.com"

    def navigate(self):
        try:
            self.page.goto(
            self.url,
            wait_until="domcontentloaded",
            timeout=60000
        )
        except Exception as e:
            pytest.skip(f"External site unreachable on this browser: {e}")
        self.page.wait_for_timeout(3000)

    def get_title(self):
        return self.page.title()

    def is_nav_visible(self):
        nav_locators = [
            self.page.locator(".navbar-nav"),
            self.page.locator("#header"),
            self.page.locator("ul.nav"),
            self.page.get_by_role("navigation"),
        ]
        for locator in nav_locators:
            try:
                if locator.is_visible(timeout=5000):
                    print("✅ Nav found!")
                    return True
            except Exception:
                continue
        return False

    def search_product(self, keyword):
        self.page.evaluate("window.scrollTo(0, 0)")
        self.page.wait_for_timeout(2000)

        search_input = None
        locators_to_try = [
            self.page.locator("#search-product"),
            self.page.locator("input[id='search-product']"),
            self.page.get_by_placeholder("Search Product"),
        ]

        for locator in locators_to_try:
            try:
                locator.wait_for(timeout=10000, state="visible")
                search_input = locator
                print("✅ Found search input!")
                break
            except Exception:
                continue

        if search_input:
            search_input.clear()
            search_input.fill(keyword)
            self.page.wait_for_timeout(1000)
            self.page.locator("#submit_search").click()
            self.page.wait_for_timeout(5000)
        else:
            print("⚠️ Search input not found")

    def get_search_results_count(self):
        results = self.page.locator(".productinfo")
        return results.count()

    def take_screenshot(self, name):
        self.page.screenshot(
            path=f"screenshots/{name}.png",
            full_page=True
        )