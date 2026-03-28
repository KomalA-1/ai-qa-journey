test_cases = [
    {"name" : "Homepage Load", "expected" : "Home Page", "actual" : "Home Page"},
    {"name" : "Login Valid", "expected" : "Dashboard", "actual" : "Dashboard"},
    {"name" : "Login Invalid", "expected" : "Error Message", "actual" : "Dashboard"},
    {"name" : "Add to Cart", "expected" : "Cart Updated", "actual" : "Cart Updated"},
    {"name" : "Checkout", "expected" : "Order Confirmed", "actual" : "Page Not Found"},
]

def run_test(test):
    if test["actual"] == test["expected"]:
        print(f"PASSED | {test['name']}")
        return "passed"
    else:
        print(f"FAILED | {test['name']}")
        print(f"EXPECTED | {test['expected']}")
        print(f"ACTUAL | {test['actual']}")
        log_bug(test["name"], test["expected"], test["actual"])
        return "failed"
    
    
def print_summary(passed, failed):
    total = passed + failed
    pass_rate = round((passed/total) * 100,1)

    print("======= FINAL REPORT =======")
    print(f"Total     : {total}")
    print(f"Passed    : {passed}")
    print(f"Failed    : {failed}")
    print(f"Pass Rate : {pass_rate}%")

    if pass_rate >= 80:
        print("Status :  READY FOR RELEASE")
    else:
        print("Status : NOT READY - FIX FAILURES")
    print("=============================")


def log_bug(test_name, expected, actual):
    print(f"BUG LOGGED")
    print(f"Test     : {test_name}")
    print(f"Expected : {expected}")
    print(f"Actual   : {actual}")

print("==========  RUNNING TEST SUITE ==========")
passed = 0 
failed = 0

for test in test_cases:
    result  = run_test(test)
    if result == "passed":
        passed += 1
    else:
        failed += 1

print_summary(passed, failed)