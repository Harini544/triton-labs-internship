# ==================================================
# STACK TRACES
# ==================================================

# 1. CONCEPT
# A stack trace, also called a traceback, shows where an error happened.
# Read it from bottom to top:
# - Bottom line shows the error type and message.
# - Lines above show the file name and line number.
# - The line number points near the actual problem.

# 2. BASIC EXAMPLES
# Keep these examples commented first.
# Uncomment one broken example at a time, run the file, and read the traceback.

# 3. COMMON ERRORS

# NameError:
# Broken code:
# print(username)
#
# Error meaning:
# Python does not know what username is.
#
# How to fix:
# Define username before using it.
# username = "Asha"
# print(username)

# TypeError:
# Broken code:
# age = 20
# print(len(age))
#
# Error meaning:
# len() does not work on an integer.
#
# How to fix:
# Use len() only on values like strings, lists, tuples, dictionaries, or sets.

# IndexError:
# Broken code:
# users = ["Asha", "Ravi"]
# print(users[5])
#
# Error meaning:
# Index 5 does not exist in this list.
#
# How to fix:
# Use a valid index such as users[0] or users[1].

# KeyError:
# Broken code:
# user = {"name": "Asha"}
# print(user["email"])
#
# Error meaning:
# The dictionary does not have the key "email".
#
# How to fix:
# Use user.get("email") or add the key first.

# ValueError:
# Broken code:
# number = int("abc")
#
# Error meaning:
# "abc" cannot be converted into an integer.
#
# How to fix:
# Convert only valid number text, such as int("123").

# 4. WHEN TO USE IT
# Every Python developer must learn to read tracebacks.
# Tracebacks help you find bugs faster instead of guessing.

# 5. EXAMPLES
def divide(a, b):
    return a / b

# Broken code:
# divide(10, 0)
#
# Expected error:
# ZeroDivisionError: division by zero
#
# How to read:
# Find the line that called divide(10, 0).
# Then find the line inside divide where a / b happened.

print("Uncomment one broken example at a time to practice reading tracebacks.")

# 6. PRACTICE

# PRACTICE 1 - Easy:
# i got error type NameError when variable is not defined
# broken example:
# print(username)
# fixed example:
username = "Asha"
print("Username:", username)
# --------------------------------------------------

# PRACTICE 2 - Easy:
# i got TypeError because len not work on integer
# broken example:
# age = 20
# print(len(age))
# fixed example:
age_text = "20"
print("Age text length:", len(age_text))
# --------------------------------------------------

# PRACTICE 3 - Medium:
# i made IndexError then fixed using correct index
practice_users = ["Asha", "Ravi"]
# broken example:
# print(practice_users[5])
print("Correct user:", practice_users[1])
# --------------------------------------------------

# PRACTICE 4 - Medium:
# i made KeyError then fixed by get method
practice_user = {"name": "Meena"}
# broken example:
# print(practice_user["email"])
print("Email:", practice_user.get("email"))
# --------------------------------------------------

# PRACTICE 5 - Slightly challenging:
# i made function error and commented broken line
def get_first_task(tasks):
    return tasks[0]

empty_tasks = []
# broken example:
# print(get_first_task(empty_tasks))
# traceback show problem is return tasks[0] because list is empty
if len(empty_tasks) > 0:
    print(get_first_task(empty_tasks))
else:
    print("No task is available")
# --------------------------------------------------
