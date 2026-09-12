# ==================================================
# FUNCTIONS
# ==================================================

# 1. CONCEPT
# A function is a reusable block of code.
# Functions help us avoid repeating the same code many times.

# 2. BASIC EXAMPLES
def greet():
    print("Hello")

greet()

def greet_user(name):
    print("Hello", name)

greet_user("Asha")

def add(a, b):
    return a + b

result = add(5, 3)
print("Result:", result)

# 3. COMMON OPERATIONS
def create_user(name, role="user"):
    return {
        "name": name,
        "role": role
    }

print(create_user("Ravi"))
print(create_user("Meena", "admin"))
print(create_user(role="editor", name="Kiran"))

def calculate_total(price, quantity):
    total = price * quantity
    return total

print("Total:", calculate_total(100, 3))

def is_admin(role):
    return role == "admin"

def check_access(role):
    if is_admin(role):
        return "Access allowed"
    return "Access denied"

print(check_access("admin"))

# 4. WHEN TO USE IT
# Use functions when code has a clear job.
# Backend examples: validate input, format a response, calculate totals, or check permissions.

# 5. EXAMPLES
def validate_email(email):
    if "@" in email:
        return True
    return False

print("Valid email:", validate_email("test@example.com"))

def build_response(status, data):
    return {
        "status": status,
        "data": data
    }

print(build_response("success", ["task 1", "task 2"]))

# 6. PRACTICE

# PRACTICE 1 - Easy:
# i created function for print my name
def print_my_name():
    print("My name is Asha")

print_my_name()
# --------------------------------------------------

# PRACTICE 2 - Easy:
# i pass name to function and print hello
def say_hello(name):
    print("Hello", name)

say_hello("Ravi")
# --------------------------------------------------

# PRACTICE 3 - Medium:
# i multiply two numbers and return answer
def multiply_numbers(a, b):
    return a * b

print("Product:", multiply_numbers(4, 5))
# --------------------------------------------------

# PRACTICE 4 - Medium:
# i use default role if role is not given
def make_user(name, role="user"):
    return {"name": name, "role": role}

print(make_user("Meena"))
print(make_user("Kiran", "admin"))
# --------------------------------------------------

# PRACTICE 5 - Slightly challenging:
# i check email then return response dictionary
def is_valid_email(email):
    return "@" in email

def email_response(email):
    if is_valid_email(email):
        return {"status": "success", "message": "valid email"}
    return {"status": "error", "message": "invalid email"}

print(email_response("test@example.com"))
print(email_response("wrongemail"))
# --------------------------------------------------
