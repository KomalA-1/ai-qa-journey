from playwright.sync_api import sync_playwright

def test_locators():
     with sync_playwright() as p:
          browser = p.chromium.launch(headless=False)
          page = browser.new_page()

          page.goto("https://practicetestautomation.com/practice-test-login/")

          # Locate username fiels by label
          page.get_by_label("Username").fill("student")

          # Locate password field by label
          page.get_by_label("Password").fill("Password123")

          # Click Submit button by role
          page.get_by_role("button", name = "Submit").click()

          # Wait and get success message
          page.wait_for_timeout(2000)

          # Check Success
          success = page.get_by_text("Congratulations").is_visible()
          print(f"Login success visible: {success}")

          if success:
               print("Login Test PASSED!")
          else:
               print("Login Test Failed!")

          title = page.title()
          print(f"Page Title: {title}")

          url = page.url
          print(f"Page URL: {url}")

          if "logged-in" in url:
               print("URL verified!")
          else:
               print("URL wrong!")

          browser.close()

test_locators()
        
        
          
