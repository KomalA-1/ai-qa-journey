# ======= STRING (text) =======

test_name = "Login Test"
test_status = "PASS"
browser = "Chrome"

# ===== INTEGER (whole number) =====
total_tests = 20
bugs_found = 3
test_duration_seconds = 45

# ===== FLOAT (decimal number) =====
response_time = 1.85
pass_percentage = 98.5

# ===== BOOLEAN (True or False) =====
is_passed = True
is_blocked = False
is_critical = True

# ===== PRIT EVERYTHING =====
print("===== Test Summary =====")
print(f"Test Name      : {test_name}")
print(f"Status         : {test_status}")
print(f"Browser        : {browser}")
print(f"Total Tests    : {total_tests}")
print(f"Bugs Found     : {bugs_found}")
print(f"Duration       : {test_duration_seconds} seconds")
print(f"Response Time  : {response_time} seconds")
print(f"Pass Rate      : {pass_percentage}%")
print(f"Is Passed      : {is_passed}")
print(f"Is Blocked     : {is_blocked}")
print(f"Is Critical    : {is_critical}")
print("=============================")

