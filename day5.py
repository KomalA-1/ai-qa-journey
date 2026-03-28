test_cases = [
    {"name" : "Homepage Load", "expected" : "Home Page", "actual" : "Home Page"},
    {"name" : "Login Valid", "expected" : "Dashboard", "actual" : "Dashboard"},
    {"name" : "Login Invalid", "expected" : "Error Message", "actual" : "Dashboard"},
    {"name" : "Add to Cart", "expected" : "Cart Updated", "actual" : "Cart Updated"},
    {"name" : "Checkout", "expected" : "Order Confirmed", "actual" : "Page Not Found"},
]

passed = 0
failed = 0

for test in test_cases:
    name = test["name"]
    expected = test["expected"] 
    actual = test["actual"]

if actual == expected:
    print(f"{name}: PASS")
    passed +=1
else:
    print(f"{name}: FAIL")
    failed +=1


total = len(test_cases)
pass_rate = (passed/total) *100


print("======= FINAL REPORT =======")
print("Total Tests: {total}")
print("Passed: {passed}")
print("Failed: {failed}")
print("Pass Rate: {pass_rate.1f}%")


if(pass_rate >= 80):
    print("Status: TARGET MET")
else:
    print("Status: BELOW TARGET(target is 80%)")

print ("=============================")
