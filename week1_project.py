test_suite = [
    {"id": 1, "name": "HomePageLoad", "expected": "Home Page", "actual": "Home Page"},
    {"id": 2, "name": "Valid Login", "expected": "Dashboard", "actual": "Dashboard"},
    {"id": 3, "name": "Invalid Login", "expected": "Error Message", "actual": "Dashboard"},
    {"id": 4, "name": "Search Page", "expected": "Results Found", "actual": "Results Found"},
    {"id": 5, "name": "Add to Cart", "expected": "Cart Updated", "actual": "Cart Updated"},
    {"id": 6, "name": "Checkout", "expected": "Order Confirmed", "actual": "Page Not Found"},
    {"id": 7, "name": "Payment", "expected": "Payment Successful", "actual": "Payment Successful"},
    {"id": 8, "name": "Logout", "expected": "Login Page", "actual": "Login Page"},
]  

def run_test(test):
    if test["actual"] == test["expected"]:
        print(f"PASSED | {test['id']} | {test['name']}")
        return "passed"
    else:
        print(f"FAILED | {test['id']} | {test['name']}")
        log_bug(test["name"], test["expected"], test["actual"])
        return "failed"
    
def log_bug(test_name, expected, actual):
    print("BUG LOGGED")
    print(f"Test    : {test_name}")
    print(f"Expected: {expected}")
    print(f"Actual  : {actual}")
    print(f"Severity : To be Assessed")

def calculate_pass_rate(passed, total):
    return round((passed/total) * 100, 1)


def get_release_status(pass_rate):
    if pass_rate >= 90:
        return "EXCELLENT - APPROVED FOR RELEASE"
    elif pass_rate >= 75:
        return "ACCEPTABLE - MINOR FIXES NEEDED"
    elif pass_rate >= 50:
        return "NEEDS IMPROVEMENT - DELAY RELEASE"
    else:
        return "CRITICAL - RELEASE BLOCKED"
    

def print_summary(passed, failed, bugs):
    total = passed + failed
    pass_rate = calculate_pass_rate(passed, total)
    status = get_release_status(pass_rate)

    print("\n==============================================")
    print(" ||          FINAL TEST REPORT                ||")
    print(" ===============================================")
    print(f"||     Total Tests : {total}                 ||")  
    print(f"||     Passed Tests: {passed}                ||")
    print(f"||     Failed Tests: {failed}                ||")
    print(f"||     Bugs Logged   : {bugs}                ||")
    print(f"||     Pass Rate     : {pass_rate}%          ||")
    print(" ||=============================================")
    print(f"||     Release Status: {status}              ||")
    print(" ===============================================")

print("===================================================")
print("||        KOMAL'S QA TEST RUNNER                 ||")
print("||         WEEK 1 FINAL PROJECT                  ||")
print("===================================================")
print("\n Executing Test Suite...\n")


passed = 0
failed = 0
bugs = 0

for test in test_suite:
    result = run_test(test)
    if result == "passed":
        passed += 1
    else:
        failed += 1
        bugs += 1

print_summary(passed, failed, bugs)