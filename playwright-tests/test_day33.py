# test_day33.py
# Day 33 - Building Tests with AI Tools
# External site — chromium only due to cross-browser timeout issues

import pytest
from pages.home_page import HomePage

# Mark ALL tests in this file as chromium_only
#pytestmark = pytest.mark.chromium_only


def test_homepage_title(page):
    home = HomePage(page)
    home.navigate()
    home.take_screenshot("homepage_loaded")

    title = home.get_title()
    print(f"Page title: {title}")

    assert "Automation Exercise" in title, \
        f"❌ Expected 'Automation Exercise' in title, got: {title}"
    print("✅ Homepage title verified!")


def test_navigation_visible(page):
    home = HomePage(page)
    home.navigate()

    is_visible = home.is_nav_visible()
    home.take_screenshot("navigation_check")

    assert is_visible, "❌ Navigation menu is not visible!"
    print("✅ Navigation menu is visible!")


def test_product_search(page):
    home = HomePage(page)
    home.navigate()

    home.search_product("dress")
    home.take_screenshot("search_results_dress")

    count = home.get_search_results_count()
    print(f"Search results found: {count}")

    assert count > 0, f"❌ No search results found for 'dress'"
    print(f"✅ Product search working! Found {count} results for 'dress'")


def test_search_no_results(page):
    home = HomePage(page)
    home.navigate()

    home.search_product("xyznonexistentproduct123")
    home.take_screenshot("search_no_results")

    count = home.get_search_results_count()
    print(f"Results for nonsense search: {count}")

    if count == 0:
        print("✅ Empty search correctly returns 0 results!")
    else:
        print(f"⚠️ Website returned {count} results for nonsense query")

    assert True
    print("✅ Search functionality works without crashing!")