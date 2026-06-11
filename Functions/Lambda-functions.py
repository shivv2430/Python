# Python Lambda Functions (Anonymous Functions)
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Syntax: lambda arguments : expression

# Example 1: A lambda function that adds 10 to the number passed in as an argument
add_ten = lambda a : a + 10
print("Adding 10 to 5:", add_ten(5))

# Example 2: A lambda function that multiplies argument a with argument b
multiply = lambda a, b : a * b
print("Multiplying 5 and 6:", multiply(5, 6))

# Example 3: Using lambda functions inside another function
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print("Doubling 11:", mydoubler(11))
print("Tripling 11:", mytripler(11))
