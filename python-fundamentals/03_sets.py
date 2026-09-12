# ==================================================
# SETS
# ==================================================

# 1. CONCEPT
# A set stores unique values.
# Sets do not keep duplicate items.
# Sets are useful when you care about membership or uniqueness.

# 2. BASIC EXAMPLES
roles = {"admin", "user", "user", "editor"}
print("Unique roles:", roles)

# 3. COMMON OPERATIONS
roles.add("guest")
print("After add:", roles)

roles.remove("guest")      # Gives an error if the item does not exist
roles.discard("missing")   # Does not give an error if the item does not exist
print("After remove/discard:", roles)

frontend_skills = {"HTML", "CSS", "JavaScript"}
backend_skills = {"Python", "SQL", "JavaScript"}

print("Union:", frontend_skills.union(backend_skills))
print("Intersection:", frontend_skills.intersection(backend_skills))
print("Difference:", backend_skills.difference(frontend_skills))
print("Symmetric difference:", frontend_skills.symmetric_difference(backend_skills))

if "Python" in backend_skills:
    print("Python skill exists")

# 4. WHEN TO USE IT
# Use a set when duplicates should be removed automatically.
# Sets are better than lists for quick membership checks and uniqueness.

# 5. EXAMPLES
requested_ids = [1, 2, 2, 3, 3, 3]
unique_ids = set(requested_ids)
print("Unique IDs:", unique_ids)

allowed_roles = {"admin", "editor"}
user_roles = {"viewer", "editor"}
common_roles = allowed_roles.intersection(user_roles)
print("Matching roles:", common_roles)

seen_emails = set()
seen_emails.add("a@example.com")
seen_emails.add("a@example.com")
print("Seen emails:", seen_emails)

# 6. PRACTICE

# PRACTICE 1 - Easy:
# i created set of languages
languages = {"Python", "JavaScript", "SQL"}
print("Languages:", languages)
# --------------------------------------------------

# PRACTICE 2 - Easy:
# i add one more language in set
languages.add("Java")
print("After adding:", languages)
# --------------------------------------------------

# PRACTICE 3 - Medium:
# i remove duplicate number by converting list to set
duplicate_numbers = [1, 2, 2, 3, 3, 4]
unique_numbers = set(duplicate_numbers)
print("Unique numbers:", unique_numbers)
# --------------------------------------------------

# PRACTICE 4 - Medium:
# i find common items from two sets
team_a = {"Python", "Git", "SQL"}
team_b = {"Python", "Docker", "SQL"}
common_items = team_a.intersection(team_b)
print("Common items:", common_items)
# --------------------------------------------------

# PRACTICE 5 - Slightly challenging:
# i find ids in first set but not in second set
old_user_ids = {101, 102, 103, 104}
new_user_ids = {103, 104, 105}
missing_ids = old_user_ids.difference(new_user_ids)
print("Missing IDs:", missing_ids)
# --------------------------------------------------
