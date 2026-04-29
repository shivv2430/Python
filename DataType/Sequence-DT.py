s = 'Welcome to the Geeks World'
print(s)

# check data type 
print(type(s))

# access string with index
print(s[1])
print(s[2])
print(s[-1])

# ----------------------What is String in Python?----------------------
# String is a sequence of characters enclosed in quotes.
# It is immutable, meaning it cannot be changed.

# ----------------------What is List in Python?----------------------
# Python has built-in support for lists which are ordered, mutable sequences of elements.
# Empty list
a = []
print(a)

# list with int values
a = [1, 2, 3]
print(a)

# list with mixed values int and String
b = ["Geeks", "For", "Geeks", 4, 5]
print(b)

# ----------------------What is Tuple in Python?----------------------
# Tuples are immutable, ordered sequences.
# initiate empty tuple
tup1 = ()
print(tup1)

tup2 = ('Geeks', 'For')
print("Tuple with the use of String: ", tup2)

tup1 = (1, 2, 3, 4, 5)

# access tuple items
print(tup1[0])
print(tup1[-1])
print(tup1[-3])

