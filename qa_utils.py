from datetime import datetime

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def calculate_pass_rate(score, max_score):
    if max_score == 0:
        return None
    return (score / max_score) * 100

def get_severity(bug_count):
    if bug_count > 5:
        return "High"
    elif bug_count > 2:
        return "Medium"
    else:
        return "Low"
    
def get_test_status(pass_rate):
    if pass_rate >= 90:
        return "Excellent"
    elif pass_rate >= 70:
        return "Acceptable"
    else:
        return "Needs Improvement"
