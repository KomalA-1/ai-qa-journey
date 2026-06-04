import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

print("=== GET REQUESTS ===")
for i in range(1,4):
    response = requests.get(f"{BASE_URL}/users/{i+1}") 
    data = response.json()
    print(f"\n === user{i} ===")
    
    print("User Name  :",data["name"])
    print("User Email :",data["email"])
    print("User City  :",data["address"]["city"])
    if(response.status_code == 200):
        print("User Found!")
    else:
        print("User Not Found!")

print("\n=== POST REQUEST ===")
new_user ={
    "name:"    : "Komal QA",
    "email"    : "komal@qa.com",
    "username" : "komalqa"
}

response = requests.post(f"{BASE_URL}/users",json = new_user)
print("Status Code :", response.status_code)
print("Created User :", response.json())

print("\n=== PUT REQUEST ===")
updated_user={
    "name"  : "Komal Senior QA",
    "email" : "komal.senior@qa.com"
} 

response = requests.put(f"{BASE_URL}/users/1", json = updated_user)
print("Status Code  :", response.status_code)
print("Updated User :", response.json())

print("\n === DELETE REQUEST ===")
response = requests.delete(f"{BASE_URL}/users/1")
print("Status Code  :", response.status_code)
print("Deleted Successful!"if response.status_code == 200 else "Delete Failed!")





