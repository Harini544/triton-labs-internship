# ==================================================
# TUPLES
# ==================================================

# 1. CONCEPT
# A tuple stores multiple values like a list, but it cannot be changed.
# This is called immutability.

# 2. BASIC EXAMPLES
point = (10, 20)
print("Point:", point)
print("X:", point[0])
print("Y:", point[1])

api_version = ("v1", "stable", 2026)
print("Slice:", api_version[0:2])

# Tuple unpacking puts tuple values into variables.
version, status, year = api_version
print(version, status, year)

# 3. COMMON OPERATIONS
roles = ("admin", "user", "guest")
print("Length:", len(roles))
print("Last role:", roles[-1])

for role in roles:
    print("Role:", role)

# 4. WHEN TO USE IT
# Use tuples when data should not change.
# Example: coordinates, fixed config values, or a database row returned as fixed data.

# 5. EXAMPLES
database_config = ("localhost", 5432)
host, port = database_config
print("Host:", host)
print("Port:", port)

status_codes = (200, 201, 404, 500)
if 200 in status_codes:
    print("Success code exists")

user_record = (1, "Asha", "admin")
user_id, name, role = user_record
print("User:", user_id, name, role)

# 6. PRACTICE

# PRACTICE 1 - Easy:
# i created tuple with colors
colors = ("red", "green", "blue")
print("Colors:", colors)
# --------------------------------------------------

# PRACTICE 2 - Easy:
# i print second item from tuple
print("Second color:", colors[1])
# --------------------------------------------------

# PRACTICE 3 - Medium:
# i unpack tuple into two variables
user_info = ("Asha", "admin")
practice_name, practice_role = user_info
print("Name:", practice_name)
print("Role:", practice_role)
# --------------------------------------------------

# PRACTICE 4 - Medium:
# i loop status codes tuple
practice_status_codes = (200, 201, 400, 404)
for code in practice_status_codes:
    print("Status code:", code)
# --------------------------------------------------

# PRACTICE 5 - Slightly challenging:
# i use tuple because api version should not change by mistake
fixed_api_version = ("v1", "stable")
print("Fixed API version:", fixed_api_version)
# --------------------------------------------------
