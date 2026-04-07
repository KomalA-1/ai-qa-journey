test_case = {
    "id"       : "TC-001",
    "name"     : "Valid Login Test",
    "priority" : "High",
    "expected" : "Dashboard Page",
    "actual"   : "Dashboard Page",
    "passed"   : "True"
}

bug_report = {
    "id"       : "BUG-001",
    "title"    : "Login button not working",
    "severity" : "High",
    "status"   : "Open"
}

print("======== TEST CASE DETAILS ========")
print(f"ID       : {test_case['id']}")
print(f"name     : {test_case['name']}")
print(f"Priority : {test_case['priority']}")
print(f"Expected : {test_case['expected']}")
print(f"Actual   : {test_case['actual']}")
print(f"Passed   : {test_case['passed']}")


print(f"Before : {bug_report['status']}")

bug_report['status'] = "In Progress"
print(f"After : {bug_report['status']}")

bug_report['assigned to'] = "Dev Team"
bug_report['fixed'] = "False"

print("\n======== UPDATED BUG REPORT ========")
for key, value in bug_report.items():
    print(f"{key} : {value}")





bugs = [
    {"id": "BUG-001", "title": "Login fails on Safari",      "severity": "High",     "status": "Open"},
    {"id": "BUG-002", "title": "Cart count not updating",    "severity": "Medium",   "status": "Fixed"},
    {"id": "BUG-003", "title": "Payment page crashes",       "severity": "Critical", "status": "Open"},
    {"id": "BUG-004", "title": "Profile photo not saving",   "severity": "Low",      "status": "Fixed"},
    {"id": "BUG-005", "title": "Search returns no results",  "severity": "High",     "status": "Open"},
]

open_count = 0
fixed_count = 0
critical_open = False

print ("============ BUG TRACKER =============")

for bugs in bugs:
    bug_id = bugs['id']
    title = bugs['title']
    severity = bugs['severity']
    status = bugs['status']

    if status == 'Open':
        print(f"OPEN  | {bug_id} | {severity:<8} | {title}")
        open_count += 1

        if severity == 'Critical':
            critical_open = True
    else:
        print(f"FIXED | {bug_id} | {severity:<8} | {title}")
        fixed_count += 1

print("=====================================")

print(f"Open : {open_count} Fixed : {fixed_count}")

if critical_open:
    print("WARNING: Critical bugs still open - BLOCK RELEASE!")




  


 

