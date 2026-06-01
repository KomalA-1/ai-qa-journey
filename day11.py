import qa_utils

print("Test started at:",qa_utils.get_timestamp())

rate = qa_utils.calculate_pass_rate(88,100)
print(f"Pass Rate: {rate}%")

severity = qa_utils.get_severity(6)
print(f"Bug Severity: {severity}")

test_status = qa_utils.get_test_status(rate)
print(f"Status: {test_status}")