# initialize empty dictionary
d = {}

d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)

# creating dictionary using dict() constructor
d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print(d1)

# Accessing elements of dictionary
d = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

# Accessing an element using key
print(d['name'])

# Accessing a element using get
print(d.get(3))

# Update value
d['name'] = 'Shivani'
print(d)

# add new key value pair
d['age'] = '20'
print(d)

# delete key value pair
d.pop('age')
print(d)
