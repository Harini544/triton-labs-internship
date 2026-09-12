# ==================================================
# CLASSES
# ==================================================

# 1. CONCEPT
# A class is a blueprint.
# An object is one real thing created from that blueprint.
# Classes group data and behavior together.

# 2. BASIC EXAMPLES
class User:
    app_name = "Task Management API"  # class attribute shared by all objects

    def __init__(self, name, role):
        self.name = name              # instance attribute
        self.role = role              # instance attribute

    def describe(self):
        return self.name + " is a " + self.role

asha = User("Asha", "admin")
ravi = User("Ravi", "user")

print(asha.describe())
print(ravi.describe())
print(User.app_name)

# 3. COMMON OPERATIONS
asha.role = "superadmin"
print("Updated role:", asha.role)

print("Asha app:", asha.app_name)
print("Ravi app:", ravi.app_name)

# 4. WHEN TO USE IT
# Use classes when data and actions belong together.
# Backend examples: User, Task, Product, Order, or Service classes.

# 5. EXAMPLES
class Task:
    default_status = "todo"

    def __init__(self, title):
        self.title = title
        self.status = Task.default_status

    def mark_done(self):
        self.status = "done"

    def summary(self):
        return self.title + " - " + self.status

task = Task("Write API tests")
print(task.summary())
task.mark_done()
print(task.summary())

# 6. PRACTICE

# PRACTICE 1 - Easy:
# i created empty Student class and one object
class Student:
    pass

student_one = Student()
print("Student object:", student_one)
# --------------------------------------------------

# PRACTICE 2 - Easy:
# i created PracticeUser class and store name in init
class PracticeUser:
    def __init__(self, name):
        self.name = name

practice_user_one = PracticeUser("Asha")
print("Practice user name:", practice_user_one.name)
# --------------------------------------------------

# PRACTICE 3 - Medium:
# i created PracticeTask and method for complete task
class PracticeTask:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_completed(self):
        self.completed = True

practice_task_one = PracticeTask("Learn classes")
practice_task_one.mark_completed()
print("Practice task completed:", practice_task_one.completed)
# --------------------------------------------------

# PRACTICE 4 - Medium:
# i use class attribute shared by two objects
class PracticeAppUser:
    app_name = "Python Fundamentals"

    def __init__(self, name):
        self.name = name

app_user_one = PracticeAppUser("Ravi")
app_user_two = PracticeAppUser("Meena")
print(app_user_one.app_name)
print(app_user_two.app_name)
# --------------------------------------------------

# PRACTICE 5 - Slightly challenging:
# i create many task objects and print summary
class SummaryTask:
    def __init__(self, title, status):
        self.title = title
        self.status = status

    def summary(self):
        return self.title + " - " + self.status

summary_tasks = [
    SummaryTask("Learn lists", "done"),
    SummaryTask("Learn classes", "in_progress"),
    SummaryTask("Learn Git", "todo")
]

for item in summary_tasks:
    print(item.summary())
# --------------------------------------------------
