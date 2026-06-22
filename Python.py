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