# ==================================================
# DICTIONARIES
# ==================================================

# 1. CONCEPT
# A dictionary stores data as key-value pairs.
# A key is the label. A value is the data stored under that label.
# Dictionaries are very common in backend/API development because JSON looks similar.

# 2. BASIC EXAMPLES
user = {
    "name": "Asha",
    "role": "admin",
    "active": True
}

print("User:", user)
print("Name:", user["name"])
print("Role:", user.get("role"))

# 3. COMMON OPERATIONS
user["email"] = "asha@example.com"      # Add new key-value pair
user["role"] = "superadmin"            # Update existing value
print("Updated user:", user)

del user["active"]                     # Delete a key-value pair
print("After delete:", user)

print("Keys:", user.keys())
print("Values:", user.values())
print("Items:", user.items())

if "email" in user:
    print("Email exists")

for key, value in user.items():
    print(key, "=", value)

nested_user = {
    "id": 1,
    "profile": {
        "name": "Ravi",
        "city": "Chennai"
    }
}
print("Nested city:", nested_user["profile"]["city"])

project = {
    "name": "Task API",
    "tasks": ["create endpoint", "write tests"]
}
print("Project tasks:", project["tasks"])

# 4. WHEN TO USE IT
# Use dictionaries when each value needs a meaningful name.
# Example: user data, task data, API request body, or API response body.

# 5. EXAMPLES
task = {
    "id": 101,
    "title": "Build login API",
    "completed": False
}
print("Task title:", task["title"])

response = {
    "status": "success",
    "data": ["task 1", "task 2"]
}
print("API response:", response)

settings = {}
settings["debug"] = True
settings["port"] = 8000
print("Settings:", settings)

# 6. PRACTICE

# PRACTICE 1 - Easy:
# i created student dictionary with name and age
student = {"name": "Asha", "age": 21}
print("Student:", student)
# --------------------------------------------------

# PRACTICE 2 - Easy:
# i made task dictionary and printing title
practice_task = {"title": "Learn dictionaries", "completed": False}
print("Task title:", practice_task["title"])
# --------------------------------------------------

# PRACTICE 3 - Medium:
# i add email then update same email
practice_user = {"name": "Ravi"}
practice_user["email"] = "old@example.com"
practice_user["email"] = "new@example.com"
print("Practice user:", practice_user)
# --------------------------------------------------

# PRACTICE 4 - Medium:
# i loop dictionary and print key value
profile = {"name": "Meena", "role": "admin", "active": True}
for key, value in profile.items():
    print(key, value)
# --------------------------------------------------

# PRACTICE 5 - Slightly challenging:
# i created api response dictionary and print first user
api_response = {
    "status": "success",
    "users": ["Asha", "Ravi", "Meena"]
}
print("First API user:", api_response["users"][0])
# --------------------------------------------------
