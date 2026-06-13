# Python Recursion (A function calling itself)
# Recursion happens when a function calls itself.
# It is useful for breaking down complex problems into smaller, simpler ones.
# Every recursive function must have a "base case" to stop the recursion, otherwise it will run forever!

# Example 1: A simple countdown timer using recursion
def countdown(n):
    # Base case: When n reaches 0, we stop.
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        # Recursive call: The function calls itself with a smaller number
        countdown(n - 1)

print("--- Countdown Example ---")
countdown(3)


# Example 2: Calculating Factorial
# The factorial of 5 (written as 5!) is 5 * 4 * 3 * 2 * 1 = 120
def factorial(x):
    # Base case: The factorial of 1 is 1
    if x == 1:
        return 1
    else:
        # Recursive call: Multiply x by the factorial of (x-1)
        return (x * factorial(x - 1))

print("\n--- Factorial Example ---")
print("Factorial of 5 is:", factorial(5))
print("Factorial of 3 is:", factorial(3))
