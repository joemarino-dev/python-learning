# you can create empty dictionaries then perform CRUD operations in various ways
grades = {}

grades['Joe'] = 'A+'
grades['Bob'] = 'F'

print(grades)

grades['Bob'] = 'B-'
print(grades)

grades.update({'Bob': 'A'})
print(grades)

print(len(grades))

if 'Joe' in grades:
	print('Joe got an', grades['Joe'])

# will produce a key error because there is no such key	
# del grades['Bobby']

del grades['Bob']
print(grades)

# up until Python 3.6 you could have a dictionary created one way but internally ordered another
# but post 3.6 dictionaries are ordered
grades = {}
grades['Jack'] = 'C+'
grades['George'] = 'A-'

print(grades)

# get keys
for element in grades:
	print(element)

# get keys, alternate more explicit version
for element in grades.keys():
	print(element)

# get values
for grade in grades.values():
	print(grade)

# get both
for person, grade in grades.items():
	print(person, "got", grade)

