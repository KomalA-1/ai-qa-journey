from playwright.sync_api import sync_playwright, expect

def test_login_valid():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://practicetestautomation.com/practice-test-login/")

        page.get_by_label("Username").fill("student")
        page.get_by_label("Password").fill("Password123")
        page.get_by_role("button", name = "Submit").click()

        page.wait_for_timeout(3000)

        if "Congratulations" in page.inner_text("body"):
            print("Valid Login Test PASSED!")
        else:
            print("Valid Login Test FAIED!")
        #expect(page.get_by_text("Congratulations")).to_be_visible()
        #expect(page).to_have_url("https://practicetestautomation.com/logged-in-successfully/")

        #print("Valid Login Test PASSED!")
        browser.close()

def test_login_invalid():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://practicetestautomation.com/practice-test-login/")

        page.get_by_label("Username").fill("wronguser")
        page.get_by_label("Password").fill("wrongpass")
        page.get_by_role("button", name = "Submit").click()

        page.wait_for_timeout(3000)

        if "invalid" in page.inner_text("body"):
            print("Invalid Login Test PASSED!")
        else:
            print("Invalid Login Test FAILED!")

        #print("Page text:", page.inner_text("body"))

        #expect(page.get_by_text("Your password is invalid!")).to_be_visible()

        #print("Invalid login test PASSED!")
        browser.close()

def test_wrong_password():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://practicetestautomation.com/practice-test-login/")

        page.get_by_label("Username").fill("student")
        page.get_by_label("Password").fill("WrongPass99")
        page.get_by_role("button", name = "Submit").click()

        page.wait_for_timeout(3000)

        if "invalid" in page.inner_text("body"):
            print("Wrong password Test PASSED!")
        else:
            print("Wrong password Test FAILED!")

        #print("Page text:", page.inner_text("body"))

        #expect(page.get_by_text("Your password is invalid!")).to_be_visible()

        #print("Wrong password test PASSED!")
        browser.close()

test_login_valid()
test_login_invalid()
test_wrong_password()

     