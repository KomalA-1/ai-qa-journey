# Day 32 - AI-Native Testing Platforms

## Platforms Explored
- mabl: https://www.mabl.com
- Testsigma: https://testsigma.com

## Key Features vs What I Built

| Feature | Platform | My Implementation |
|---|---|---|
| Self-healing | mabl auto-heals locators | smart_locator.py |
| Bug reports | mabl generates reports | bug_reporter.py |
| Screenshots | mabl captures on failure | conftest.py hook |
| Cross-browser | mabl runs on all browsers | conftest.py params |
| CI/CD | mabl GitHub integration | playwright.yml |

## How These Platforms Differ from My Code
- They have UI dashboards (I have terminal output)
- They store historical test results (I have .txt reports)
- They use ML for healing (I use fallback strategies)
- They require no coding (I write Python)


## My Advantage
I understand WHAT these platforms do and HOW they work
because I built the same concepts from scratch.
This means I can:
1. Use these platforms immediately
2. Debug when they fail
3. Extend them with custom code
4. Evaluate which platform fits a project

## Interview Talking Points
- "I've used axe-playwright-python for accessibility"
- "I built a self-healing locator system from scratch"  
- "I understand how mabl's healing works under the hood"
- "I can work with both coded and codeless frameworks"

## Testsigma Natural Language vs My Playwright Code

### Testsigma (natural language):
Navigate to login page
Enter "student" in Username
Enter "Password123" in Password
Click Submit
Verify URL contains "logged-in-successfully"

### My Playwright code (Python):
login = LoginPage(page)
login.navigate()
login.login("student", "Password123")
assert "logged-in-successfully" in page.url

## My Reflection

1. Which platform would I recommend for a company with 
   no coding experience on the QA team, and why?
   - Testsigma because we can prompt in normal English language

2. Which platform would I recommend for a company with 
   experienced Python developers, and why?
   - For experienced Python developers I'd recommend our own Playwright framework because we have full control, can integrate with our existing CI/CD, and the team can review tests in code reviews like any other code.

3. What is one feature from mabl or Testsigma that I 
   would want to add to my own framework, and how would 
   I build it? 
   - I'd want to add mabl's historical test results dashboard. I'd build it by saving each test run's results to a JSON file with timestamp, test name, pass/fail, and duration — then use Python to generate an HTML report showing trends over time.