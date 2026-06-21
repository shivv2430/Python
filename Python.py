#Print Hello World
print("Hello, World!")

#Take Input from User
name = input("Enter your name: ")
print("Hello", name)

#Add Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a + b
print("Sum =", sum)

# Check if Number is Even or Odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#Check for Positive, Negative, or Zero
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#Find Largest of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is larger")
else:
    print(b, "is larger")