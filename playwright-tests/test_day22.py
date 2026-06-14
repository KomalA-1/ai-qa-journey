import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture()
def api_request():
    with sync_playwright() as p:
        request_context = p.request.new_context(base_url = BASE_URL)
        yield request_context
        request_context.dispose()

def test_get_user(api_request):
    response = api_request.get("/users/1")
    assert response.status == 200

    data = response.json()
    assert data['name'] == "Leanne Graham"
    print(f"Get User data PASSED! User: {data['name']}")

def test_create_post(api_request):
    new_post = {
        "title": "QA Automation",
        "body": "Testing with Playwright API",
        "userID" : 1
    } 
    response = api_request.post("/posts", data = new_post)
    assert response.status == 201

    data = response.json()
    assert data["title"] == "QA Automation"
    print(f"Post test PASSED! Created post id: {data['id']}")

def test_delete_post(api_request):
    response = api_request.delete("/posts/1")
    assert response.status == 200
    print("DELETE test PASSED!")

def test_get_all_todos_count(api_request):
    response = api_request.get("/todos")
    assert response.status == 200

    todos = response.json()
    assert len(todos) == 200 # Check there are excatly 200 todos

    # Count how many are completed
    completed = sum(1 for todo in todos if todo["completed"] == True)
    print(f"Total todos: {len(todos)} | Completed: {completed}")