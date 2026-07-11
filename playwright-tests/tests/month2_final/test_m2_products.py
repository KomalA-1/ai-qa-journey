# tests/month2_final/test_m2_products.py
# Month 2 Final Project - Product Tests
# Website: automationexercise.com

import pytest
from pages.home_page import HomePage

# 
# 
# pytestmark = pytest.mark.chromium_only

search_terms = [
    ("dress",  True),   # should return results
    ("top",    True),   # should return results
    ("jeans",  True),   # should return results
]

@pytest.mark.parametrize("keyword, expect_results", search_terms)
def test_product_search_data_driven(page, keyword, expect_results):
    home = HomePage(page)
    home.navigate()
    home.search_product(keyword)

    count = home.get_search_results_count()
    print(f"🔍 '{keyword}' → {count} results")

    if expect_results:
        assert count > 0, f"❌ Expected results for '{keyword}' but got 0"
        print(f"✅ Search for '{keyword}' returned {count} results")
    else:
        assert count == 0, f"❌ Expected 0 results for '{keyword}'"
        print(f"✅ Search for '{keyword}' correctly returned 0 results")


def test_homepage_loads_correctly(page):
    home = HomePage(page)
    home.navigate()

    title = home.get_title()
    assert "Automation Exercise" in title
    print(f"✅ Homepage loaded: {title}")

    nav = home.is_nav_visible()
    assert nav, "❌ Navigation not visible"
    print("✅ Navigation visible")

    home.take_screenshot("m2_final_homepage")
    print("✅ Screenshot saved")