import requests
from faker import Faker

fake = Faker()

print("===== Fake Test User =====")

for i in range(2):
    print(f"\n ==== Fake User {i+1} ====")
    print("Name    :", fake.name())
    print("Email   :", fake.email())
    #print("Phone   :", fake.phone_number())
    #print("Address :", fake.address())

print("\n=== LIVE API TEST ===")
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print("Status Code:", response.status_code)
if response.status_code == 200:
    print("API Test Passed")
else:
    print("API Test Failed")
print("Response   :", response.json())






