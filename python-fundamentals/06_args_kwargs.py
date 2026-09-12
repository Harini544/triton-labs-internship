# ==================================================
# *ARGS AND **KWARGS
# ==================================================

# 1. CONCEPT
# *args collects extra positional arguments into a tuple.
# **kwargs collects extra keyword arguments into a dictionary.

# 2. BASIC EXAMPLES
def show_numbers(*args):
    print("Args:", args)

show_numbers(10, 20, 30)

def show_user(**kwargs):
    print("Kwargs:", kwargs)

show_user(name="Asha", role="admin")

# 3. COMMON OPERATIONS
def add_all(*args):
    total = 0
    for number in args:
        total = total + number
    return total

print("Total:", add_all(1, 2, 3, 4))

def create_profile(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)

create_profile(name="Ravi", city="Chennai", active=True)

def create_user(username, *roles, **details):
    print("Username:", username)
    print("Roles:", roles)
    print("Details:", details)

create_user("asha", "admin", "editor", email="asha@example.com")

# 4. WHEN TO USE IT
# Use *args when the number of values is flexible.
# Use **kwargs when you want flexible named values.
# In backend code, **kwargs can help build flexible filters or response data.

# 5. EXAMPLES
def log_event(event_name, **metadata):
    print("Event:", event_name)
    print("Metadata:", metadata)

log_event("user_login", user_id=101, success=True)

def check_any_role(*roles):
    if "admin" in roles:
        return "Admin found"
    return "Admin not found"

print(check_any_role("user", "editor", "admin"))

# 6. PRACTICE

# PRACTICE 1 - Easy:
# i accept many values by args and print it
def print_args(*args):
    print("Args values:", args)

print_args("Python", "Git", "SQL")
# --------------------------------------------------

# PRACTICE 2 - Easy:
# i accept named values by kwargs and print it
def print_kwargs(**kwargs):
    print("Kwargs values:", kwargs)

print_kwargs(name="Asha", role="admin")
# --------------------------------------------------

# PRACTICE 3 - Medium:
# i add all numbers using args
def sum_numbers(*args):
    total = 0
    for number in args:
        total = total + number
    return total

print("Sum:", sum_numbers(10, 20, 30))
# --------------------------------------------------

# PRACTICE 4 - Medium:
# i build user dictionary from kwargs
def build_user(**kwargs):
    return kwargs

print("Built user:", build_user(name="Ravi", email="ravi@example.com"))
# --------------------------------------------------

# PRACTICE 5 - Slightly challenging:
# i use normal parameter args and kwargs together
def show_everything(username, *roles, **details):
    print("Username:", username)
    print("Roles:", roles)
    print("Details:", details)

show_everything("meena", "admin", "editor", active=True, city="Chennai")
# --------------------------------------------------
