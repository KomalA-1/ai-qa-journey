# test_day31.py
# Day 31 - Self-Healing Test Concepts

from pages.smart_locator import find_element_smart

def test_self_healing_submit_button(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")

    # Multiple strategies to find the submit button
    submit_strategies = [
        lambda p: p.get_by_role("button", name="Submit"),      # Strategy 1: correct
        lambda p: p.get_by_role("button", name="Login"),        # Strategy 2: wrong name (simulates site change)
        lambda p: p.locator("button[type='submit']"),           # Strategy 3: CSS fallback
        lambda p: p.locator("#submit"),                         # Strategy 4: ID fallback
    ]

    button = find_element_smart(page, submit_strategies, "Submit button")

    page.get_by_label("Username").fill("student")
    page.get_by_label("Password").fill("Password123")
    button.click()

    page.wait_for_timeout(2000)
    assert "logged-in-successfully" in page.url
    print("✅ Self-healing test PASSED!")


def test_self_healing_with_broken_primary(page):
    """Simulates what happens when the FIRST locator is wrong"""
    page.goto("https://practicetestautomation.com/practice-test-login/")

    # Intentionally put a WRONG locator first to prove healing works
    submit_strategies = [
        lambda p: p.get_by_role("button", name="WRONG_NAME_TEST"),  # This will fail!
        lambda p: p.get_by_role("button", name="Submit"),           # This heals it
    ]

    button = find_element_smart(page, submit_strategies, "Submit button (broken primary test)")

    page.get_by_label("Username").fill("student")
    page.get_by_label("Password").fill("Password123")
    button.click()

    page.wait_for_timeout(2000)
    assert "logged-in-successfully" in page.url
    print("✅ Healed test still PASSED despite broken primary locator!")


def test_self_healing_all_strategies_fail(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")

    bad_strategies = [
        lambda p: p.get_by_role("button", name="WRONG1"),
        lambda p: p.get_by_role("button", name="WRONG2"),
    ]

    try:
        find_element_smart(page, bad_strategies, "Submit button (all fail test)")
        print("❌ This should have raised an exception!")
    except Exception as e:
        print(f"✅ Correctly raised exception when all strategies failed: {e}")