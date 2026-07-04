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

#Check if Number is Vowel or Consonant
char = input("Enter a character: ")

if char in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")

#Print Numbers 1 to 10
for i in range(1, 11):
    print(i)

#Find Sum of First N Numbers
n = int(input("Enter n: "))

total = 0
for i in range(1, n + 1):
    total += i

print("Sum =", total)

#Multiplication Table
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

#Factorial of a Number
n = int(input("Enter a number: "))

fact = 1
for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)

#Check Prime Number
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

#Reverse a String
text = input("Enter a string: ")

print(text[::-1])

#Check Palindrome
text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#Find Maximum in a List
numbers = [10, 25, 5, 40, 15]

print("Maximum =", max(numbers))

#Function Example
def greet(name):
    print("Hello", name)

greet("Shivani")

#Simple Calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)

#Find the Square of a Number
number = int(input("Enter a number: "))

square = number * number

print("Square =", square)

#Swap two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)


#Check Whether a Year is a Leap Year
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

#Check Whether a Number is an Armstrong Number
number = int(input("Enter a number: "))

original = number
sum = 0

while number > 0:
    digit = number % 10
    sum = sum + digit ** 3
    number = number // 10

if original == sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

#Count Positive and Negative Numbers in a List
numbers = [10, -2, 15, -8, 5, -1]

positive = 0
negative = 0

for num in numbers:
    if num >= 0:
        positive = positive + 1
    else:
        negative = negative + 1

print("Positive =", positive)
print("Negative =", negative)

#Print a Star (*) Pyramid
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print("*" * i)