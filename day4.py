print("SCRIPT IS RUNNING")
page_loaded = True
cart_items = 3
button_visible = False
total_amount = 59.99
all_passed = True

print('======= Test Summary =======')

if page_loaded:
    print("Passed: Page loaded successfully")
else:
    print("Failed: Page failed to load")
    all_passed = False

if cart_items > 0:
    print("Passed: Items are more than 0")
else:
    print("Failed: Cart is empty")
    all_passed = False

if button_visible:
    print("Passed: Button is visible")
else:
    print("Failed: Button is not visible")
    all_passed = False

if total_amount < 100:
    print("Passed : Total amount is less than 100")
else:
    print("Failed : Total amount is greater than or equal to 100")
    all_passed = False

if all_passed:
    print("All checks passed!")
else:
    print("Some checks failed!")