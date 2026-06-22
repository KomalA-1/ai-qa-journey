# Month 1 Final Project _ API Suite

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
    assert data["name"] == "Leanne Graham"
    print(f"GET user PASSED: {data['name']}")

def test_create_post(api_request):
    new_post = {"title": "QA Final Project", "body": "Testing", "userID": 1}
    response = api_request.post("/posts", data = new_post)
    assert response.status == 201
    print(f"POST create PASSED")

def test_delete_post(api_request):
    response = api_request.delete("/posts/1")
    assert response.status == 200
    print("DELETE PASSED")

def test_todos_summary(api_request):
    response = api_request.get("/todos")
    assert response.status == 200
    todos = response.json()
    completed = sum(1 for t in todos if t["completed"])
    print(f"Todos: {len(todos)} total, {completed} completed")
    


