# pages/smart_locator.py
# Self-healing locator helper

def find_element_smart(page, locators, description="element"):
    """
    Tries multiple locator strategies until one works.
    locators = list of functions that return a locator
    """
    for i, locator_fn in enumerate(locators):
        try:
            element = locator_fn(page)
            if element.is_visible(timeout=3000):
                if i > 0:
                    print(f"⚠️ Primary locator failed for '{description}' — healed using strategy #{i+1}")
                else:
                    print(f"✅ Found '{description}' using primary locator")
                return element
        except Exception:
            continue

    raise Exception(f"❌ Could not find '{description}' using any of {len(locators)} strategies!")