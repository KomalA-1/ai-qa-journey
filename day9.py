# print("============ WRITING TEST RESULTS =================")

# results = [
#     "TC-001 | Valud Login    | PASSED",
#     "TC-002 | Invalid Login  | FAILED",
#     "TC-003 | Search Product | PASSED",
#     "TC-004 | Add to Cart    | PASSED",
#     "TC-005 | CHeckout       | FAILED"
# ]


# with open("test_results.txt","w") as file:
#     file.write("======== TEST EXECUTION STARTED =======\n")
#     for result in results:
#         file.write(result + "\n")
#     file.write("======== TEST EXECUTION COMPLETED =========\n")

# print("test_results.txt created succesfully")

bugs = [
    "BUG-001,Login fails on Safari,High,Open",
    "BUG-002,Cart not updating,Medium,Fixed",
    "BUG-003,Payment crashes,Critical,Open",
    "BUG-004,Profile photo issue, Low,Fixed"
]

new_bugs =[
    "BUG-005,Profile name conflict,High,Open"
]

open_count = 0
fixed_count = 0

with open("bug_report.txt", "w") as file:
    for bug in bugs:
        file.write(bug + "\n")
        
with open("bug_report.txt", "a") as file:
    for bug in new_bugs:
        file.write(bug + "\n")

with open("bug_report.txt", "r") as file:
    lines = file.readlines() 

print(" =========== BUG REPORT ============")   

for line in lines:
    parts = line.strip().split(",")
    bug_id = parts[0]
    bug_name = parts[1]
    severity = parts[2]
    status = parts[3]

    if status == "Open":
        print(f"OPEN  | {bug_id} | {severity:<8} | {bug_name}")
        open_count += 1
    else:
        print(f"FIXED | {bug_id} | {severity:<8} | {bug_name}")
        fixed_count += 1

print(" =====================================")

print(f"Open : {open_count} | Fixed : {fixed_count}")
