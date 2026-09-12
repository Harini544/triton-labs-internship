# ==================================================
# LISTS
# ==================================================

# 1. CONCEPT
# A list stores many values in one variable.
# Lists keep order, allow duplicates, and can be changed after creation.
# In backend code, lists are often used for users, tasks, IDs, roles, or API results.

# 2. BASIC EXAMPLES
users = ["Asha", "Ravi", "Meena"]
print("Users:", users)

# Python starts counting from 0.
print("First user:", users[0])
print("Last user:", users[-1])

# Slicing gets part of a list.
print("First two users:", users[0:2])

# Lists are mutable, so this changes the second item.
users[1] = "Kiran"
print("Updated users:", users)

# 3. COMMON OPERATIONS
tasks = ["login API", "user API"]
tasks.append("payment API")          # Add to the end
tasks.insert(1, "auth middleware")   # Add at index 1
tasks.extend(["tests", "docs"])      # Add many items
print("Tasks:", tasks)

tasks.remove("docs")                 # Remove by value
last_task = tasks.pop()              # Remove and return last item
print("Removed:", last_task)
print("Task count:", len(tasks))

numbers = [5, 2, 9, 1]
numbers.sort()
print("Sorted:", numbers)
numbers.reverse()
print("Reversed:", numbers)

if "login API" in tasks:
    print("Login task exists")

for task in tasks:
    print("Task:", task)

nested_tasks = [["login", "signup"], ["create task", "delete task"]]
print("Nested item:", nested_tasks[0][1])

# Copying avoids changing the original list by accident.
original_roles = ["admin", "user"]
copied_roles = original_roles.copy()
copied_roles.append("guest")
print("Original roles:", original_roles)
print("Copied roles:", copied_roles)

# 4. WHEN TO USE IT
# Use a list when you need ordered data that may change.
# Example: a list of API response items, task names, or validation errors.

# 5. EXAMPLES
api_errors = []
api_errors.append("email is required")
api_errors.append("password is too short")
print("API errors:", api_errors)

task_statuses = ["todo", "in_progress", "done"]
for status in task_statuses:
    print("Allowed status:", status)

scores = [80, 95, 72]
total = 0
for score in scores:
    total = total + score
print("Total score:", total)

# 6. PRACTICE

# PRACTICE 1 - Easy:
# i created fruits list with 3 fruits
fruits = ["apple", "banana", "mango"]
print("Fruits:", fruits)
# --------------------------------------------------

# PRACTICE 2 - Easy:
# i made roles list and printing first role
roles = ["admin", "user", "guest"]
print("First role:", roles[0])
# --------------------------------------------------

# PRACTICE 3 - Medium:
# i add and remove task from list
my_tasks = ["login API", "user API"]
my_tasks.append("payment API")
my_tasks.remove("user API")
print("My tasks:", my_tasks)
# --------------------------------------------------

# PRACTICE 4 - Medium:
# i am printing only score bigger than 70
practice_scores = [45, 88, 92, 60]
for score in practice_scores:
    if score > 70:
        print("Passed score:", score)
# --------------------------------------------------

# PRACTICE 5 - Slightly challenging:
# i made nested list for two users and print second user role
practice_users = [["Asha", "admin"], ["Ravi", "user"]]
print("Second user role:", practice_users[1][1])
# --------------------------------------------------
