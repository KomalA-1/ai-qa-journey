test_cases = [
    {"name": "Login Test",    "score": 95,  "max": 100},
    {"name": "Search Test",   "score": 80,  "max": 100},
    {"name": "Payment Test",  "score": 70,  "max": 0},    # max=0 will crash!
    {"name": "Logout Test",   "score": 88,  "max": 100},
    {"name": "Profile Test",  "score": None,"max": 100},  # None will crash!
]

completed = 0
skipped = 0

print("============ SAFE TEST RUNNER ===============")

for test in test_cases:
    try :
        pass_percent = (test["score"] / test["max"]) * 100
        print(f"{test['name']} : {pass_percent:.1f}% - PASSED")
        completed += 1
    except ZeroDivisionError:
        print(f"{test['name']}: SKIPPED - max score is zero")
        skipped += 1
    except TypeError:
        print(f"{test['name']} : SKIPPED - invalid score data")
        skipped += 1

print("==========================================")

print(f"Completed : {completed} | SKIPPED : {skipped}")






