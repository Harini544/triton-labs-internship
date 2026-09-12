# ==================================================
# COMPREHENSIONS
# ==================================================

# 1. CONCEPT
# A comprehension is a shorter way to create a list, dictionary, or set.
# Learn the normal loop first. Then use comprehension when it is easy to read.

# 2. BASIC EXAMPLES
numbers = [1, 2, 3, 4]

squares = []
for number in numbers:
    squares.append(number * number)
print("Squares with loop:", squares)

squares_comp = [number * number for number in numbers]
print("Squares with comprehension:", squares_comp)

# 3. COMMON OPERATIONS
even_numbers = [number for number in numbers if number % 2 == 0]
print("Even numbers:", even_numbers)

labels = ["even" if number % 2 == 0 else "odd" for number in numbers]
print("Labels:", labels)

usernames = ["asha", "ravi", "meena"]
user_map = {name: len(name) for name in usernames}
print("Dictionary comprehension:", user_map)

unique_lengths = {len(name) for name in usernames}
print("Set comprehension:", unique_lengths)

pairs = []
for x in [1, 2]:
    for y in [10, 20]:
        pairs.append((x, y))
print("Nested loop:", pairs)

pairs_comp = [(x, y) for x in [1, 2] for y in [10, 20]]
print("Nested comprehension:", pairs_comp)

# 4. WHEN TO USE IT
# Use comprehensions for simple transformations and filters.
# Avoid them when the logic becomes hard to read.

# 5. EXAMPLES
api_names = ["login", "signup", "logout"]
endpoints = ["/api/" + name for name in api_names]
print("Endpoints:", endpoints)

scores = [45, 88, 92]
passed = [score for score in scores if score >= 50]
print("Passed:", passed)

users = ["Asha", "Ravi"]
default_roles = {user: "user" for user in users}
print("Default roles:", default_roles)

# 6. PRACTICE

# PRACTICE 1 - Easy:
# i double each number using list comprehension
practice_numbers = [1, 2, 3]
doubled_numbers = [number * 2 for number in practice_numbers]
print("Doubled:", doubled_numbers)
# --------------------------------------------------

# PRACTICE 2 - Easy:
# i keep names which length is more than 4
practice_names = ["Asha", "Ravikumar", "Meena", "Raj"]
long_names = [name for name in practice_names if len(name) > 4]
print("Long names:", long_names)
# --------------------------------------------------

# PRACTICE 3 - Medium:
# i create dictionary with number and square
square_map = {number: number * number for number in [1, 2, 3, 4]}
print("Square map:", square_map)
# --------------------------------------------------

# PRACTICE 4 - Medium:
# i create set of first letters so duplicate is removed
names_for_letters = ["Asha", "Arun", "Ravi", "Meena"]
first_letters = {name[0] for name in names_for_letters}
print("First letters:", first_letters)
# --------------------------------------------------

# PRACTICE 5 - Slightly challenging:
# i write nested loop first then same thing in comprehension
normal_pairs = []
for user_id in [1, 2]:
    for role in ["admin", "user"]:
        normal_pairs.append((user_id, role))

comp_pairs = [(user_id, role) for user_id in [1, 2] for role in ["admin", "user"]]
print("Normal pairs:", normal_pairs)
print("Comprehension pairs:", comp_pairs)
# --------------------------------------------------
