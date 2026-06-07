from playwright.sync_api import sync_playwright

def test_google_title():
    with sync_playwright() as p:
        # Open browser (headless = False meansyou see it open!)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Go to website
        page.goto("https://www.google.com")

        # Go to title
        title = page.title() 
        print(f"Page Title: {title}")

        # Check title contains Google
        assert "Google" in title
        print("Title test PASSED!")

        browser.close()

def test_wikipedia():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page() 

        page.goto("https://www.wikipedia.com")
        title =page.title()
        print(f"Page Title: {title}")

        assert "Wikipedia" in title
        print("Wikipedia test PASSED!")

        browser.close()

test_google_title()
test_wikipedia()