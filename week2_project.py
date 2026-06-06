import requests
import qa_utils

BASE_URL = "https://jsonplaceholder.typicode.com"

results = []

def run_test(test_name,url, expected_status):
    try:
        response = requests.get(url)
        actual_status = response.status_code

        if actual_status == expected_status:
            status = "PASSED"
        else:
            status = "FAILED"

        results.append({
            "test"   : test_name,
            "status" : status,
            "code"   : actual_status
        })
    except Exception as e:
        results.append({
            "test"   : test_name,
            "status"   : "ERROR",
            "code"   : str(e)

        })

# === RUN TESTS ===
run_test("Get User 1",f"{BASE_URL}/users/1"      , 200)
run_test("Get All Posts",f"{BASE_URL}/posts"     , 200)
run_test("Get Comment 1",f"{BASE_URL}/comments/1", 200)
run_test("Get Invalid User",f"{BASE_URL}/invalid", 404)
run_test("Get Todos List",f"{BASE_URL}/todos/1"  , 200)
run_test("Get Photo 5",f"{BASE_URL}/photos/5"    , 200)

# === PRINT REPORT ===
passed = sum(1 for r in results if r["status"] == "PASSED")
failed = sum(1 for r in results if r["status"] == "FAILED")
error = sum(1 for r in results if r["status"] == "ERROR")
timestamp = qa_utils.get_timestamp()

print("=" * 45)
print("    API TEST SUITE REPORT")
print("=" * 45) 
print(f"Run at : {timestamp}")
print(f"Total  : {len(results)}")
print(f"Passed : {passed}")
print(f"Failed : {failed}")
print("=" * 45)

for r in results:
    icon = "Correct" if r["status"] == "PASSED" else "Wrong"
    print(f"{icon} {r['test']} | {r['status']} | {r['code']}")

print("=" * 45)

# === SAVE TO FILE ===
with open("week2_report.txt","w") as f:
    f.write(f"API Test Report  - {timestamp}\n")
    f.write("=" * 45 + "\n")
    for r in results:
        f.write(f"{r['test']} | {r['status']} | {r['code']} \n")
    f.write(f"\nPassed: {passed} | Failed: {failed}\n")

print("\n Report saved to week2_report.txt")