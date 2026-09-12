# ==================================================
# PYTHON COMMAND LINE
# ==================================================

# 1. CONCEPT
# The command line lets you run programs by typing commands.
# You can run a Python file from the terminal.

# 2. BASIC EXAMPLES
# To check Python version:
# python --version
#
# To run this file:
# python 10_command_line.py

print("This file is running from the command line.")

# 3. COMMON OPERATIONS
import sys

# sys.argv is a list of command-line arguments.
# The first item is always the file name.
print("All command-line arguments:", sys.argv)

if len(sys.argv) > 1:
    print("First extra argument:", sys.argv[1])
else:
    print("No extra argument was passed")

# Example command:
# python 10_command_line.py Asha
#
# In that command:
# sys.argv[0] is "10_command_line.py"
# sys.argv[1] is "Asha"

# 4. WHEN TO USE IT
# Command-line arguments are useful for small scripts.
# Backend developers use the terminal to run servers, tests, scripts, and Git commands.

# 5. EXAMPLES
if len(sys.argv) > 2:
    name = sys.argv[1]
    role = sys.argv[2]
    print("Name:", name)
    print("Role:", role)
else:
    print("Try: python 10_command_line.py Asha admin")

# 6. PRACTICE

# PRACTICE 1 - Easy:
# i run this file using this command
# python 10_command_line.py
# --------------------------------------------------

# PRACTICE 2 - Easy:
# i print sys argv and can pass one extra value
print("Practice argv:", sys.argv)
# example command: python 10_command_line.py Asha
# --------------------------------------------------

# PRACTICE 3 - Medium:
# i read name from command line if it is given
if len(sys.argv) > 1:
    command_name = sys.argv[1]
    print("Hello", command_name)
else:
    print("Please give name")
# --------------------------------------------------

# PRACTICE 4 - Medium:
# i read two numbers and convert string to int
if len(sys.argv) > 2:
    first_number = int(sys.argv[1])
    second_number = int(sys.argv[2])
    print("Sum:", first_number + second_number)
else:
    print("Please give two numbers")
# --------------------------------------------------

# PRACTICE 5 - Slightly challenging:
# i read task title and status then make dictionary
if len(sys.argv) > 2:
    command_task = {
        "title": sys.argv[1],
        "status": sys.argv[2]
    }
    print("Command task:", command_task)
else:
    print("Please give task title and status")
# --------------------------------------------------
