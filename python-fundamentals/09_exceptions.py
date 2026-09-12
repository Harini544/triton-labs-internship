# ==================================================
# EXCEPTION HANDLING
# ==================================================

# 1. CONCEPT
# An exception is an error that happens while the program is running.
# Exception handling lets the program respond instead of crashing immediately.

# 2. BASIC EXAMPLES
# Bad code example:
# number = int("abc")
# This gives ValueError because "abc" cannot become an integer.

try:
    number = int("123")
except ValueError:
    print("Could not convert text to number")
else:
    print("Converted number:", number)
finally:
    print("This always runs")

# 3. COMMON OPERATIONS
data = {"name": "Asha"}

try:
    print(data["email"])
except KeyError:
    print("The email key is missing")

numbers = [10, 20]

try:
    print(numbers[5])
except IndexError:
    print("That index does not exist")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

try:
    value = len(100)
except TypeError:
    print("This value does not have length")

def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return True

try:
    validate_age(-5)
except ValueError as error:
    print("Validation error:", error)

class InvalidRoleError(Exception):
    pass

def check_role(role):
    if role not in ["admin", "user"]:
        raise InvalidRoleError("Invalid role")

try:
    check_role("manager")
except InvalidRoleError as error:
    print("Custom error:", error)

# 4. WHEN TO USE IT
# Use exception handling around code that may fail.
# Backend examples: reading files, parsing input, checking request data, or database operations.

# 5. EXAMPLES
def parse_user_id(text):
    try:
        return int(text)
    except ValueError:
        return None

print("User ID:", parse_user_id("101"))
print("Bad User ID:", parse_user_id("abc"))

# 6. PRACTICE

# PRACTICE 1 - Easy:
# i handle error when abc cannot convert into int
try:
    practice_number = int("abc")
except ValueError:
    print("Cannot convert abc to number")
# --------------------------------------------------

# PRACTICE 2 - Easy:
# i handle divide by zero error
try:
    practice_result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
# --------------------------------------------------

# PRACTICE 3 - Medium:
# i handle missing key from dictionary
practice_data = {"name": "Asha"}
try:
    print(practice_data["email"])
except KeyError:
    print("Email key is not there")
# --------------------------------------------------

# PRACTICE 4 - Medium:
# i raise ValueError if age is negative
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be below zero")
    return "Age is valid"

try:
    print(check_age(-1))
except ValueError as error:
    print("Age error:", error)
# --------------------------------------------------

# PRACTICE 5 - Slightly challenging:
# i create custom error for wrong task status
class InvalidTaskStatusError(Exception):
    pass

def validate_task_status(status):
    if status not in ["todo", "in_progress", "done"]:
        raise InvalidTaskStatusError("Task status is invalid")
    return "Task status is valid"

try:
    print(validate_task_status("started"))
except InvalidTaskStatusError as error:
    print("Task status error:", error)
# --------------------------------------------------
