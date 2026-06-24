# Test the bug reporter function

from bug_reporter import generate_bug_report
from datetime import datetime

def test_generate_bug_report():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_path = generate_bug_report(
        test_name = "test_valid_login",
        status = "FAILED",
        screenshot_path = "screenshots/FAILED_test_valid_login.png",
        timestamp = timestamp
    )

    # Verify the file was created
    import os
    assert os.path.exists(file_path), "Bug report file was not created!"
    print(f"Bug report exists at: {file_path}")

    # Read and print the report
    with open(file_path, "r") as f:
        content = f.read()
    print("\n", content)

