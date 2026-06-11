# Python Variable Scope (Local vs Global Variables)
# Scope refers to the region of the code where a variable is accessible.

# 1. Global Variables
# Variables created outside of a function are known as global variables.
# Global variables can be used both inside and outside of functions.

global_var = "I am global"

def test_global():
    print("Inside function:", global_var)

test_global()
print("Outside function:", global_var)
print("-" * 30)

# 2. Local Variables
# Variables created inside a function are known as local variables.
# They can only be accessed inside that specific function.

def test_local():
    local_var = "I am local"
    print("Inside function:", local_var)

test_local()
# print(local_var) # This would cause an error because local_var is not accessible outside

print("-" * 30)

# 3. The global Keyword
# Normally, when you create a variable inside a function, it is local.
# To create a global variable inside a function, or to change a global variable inside a function, you use the 'global' keyword.

count = 0 # Global variable

def increment():
    global count # Declare that we want to use the global 'count' variable
    count += 1
    print("Count inside function:", count)

increment()
increment()
print("Count outside function:", count)
