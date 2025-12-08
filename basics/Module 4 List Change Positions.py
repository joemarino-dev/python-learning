# Broken attempt at swap
print('''
###################
##  BROKEN SWAP  ##
###################
''')
first = input('Enter the first number: ')
second = input('Enter the second number: ')
print('Before swapping: ', first, second)
first = second
second = first
print('After swapping: ', first, second)

# Better attempt - works but not most efficient
print('''
###################
##   TEMP SWAP   ##
###################
''')
first = input('Enter the first number: ')
second = input('Enter the second number: ')
print('Before swapping: ', first, second)
temporary = first
first = second
second = temporary
print('After swapping: ', first, second)

# Even better attempt using a Python shortcut
print('''
###################
## SHORTCUT SWAP ##
###################
''')
first = input('Enter the first number: ')
second = input('Enter the second number: ')
print('Before swapping: ', first, second)
first, second = second, first
print('After swapping: ', first, second)

# Now using the shortcut and a list
print('''
###################
##   LIST SWAP   ##
###################
''')
guitar_brands = ['Fender', 'Charvel', 'Dean', 'Jackson', 'Gibson']
print('Before swapping: ', guitar_brands)
guitar_brands[0], guitar_brands[4] = guitar_brands[4], guitar_brands[0]
print('After swapping: ', guitar_brands)

# Now using a sort to swap elements
print('''
###################
##   SORT SWAP   ##
###################
''')
guitar_brands = ['Fender', 'Charvel', 'Dean', 'Jackson', 'Gibson']
print('Before swapping: ', guitar_brands)
guitar_brands.sort()
print('After swapping: ', guitar_brands)

# Now using a sort to swap numerical elements
print('''
###################
##  NUMBER SORT  ##
###################
''')
random_number = [3, 7, -9, 0, 1]
print('Before swapping: ', random_number)
random_number.sort()
print('After swapping: ', random_number)

# Now using a sort to swap numberical elements
print('''
###################
## REVERSE SORT ##
###################
''')
random_number = [3, 7, -9, 0, 1]
print('Before swapping: ', random_number)
random_number.sort(reverse=True)
print('After swapping: ', random_number)

# Sort without any actual list swapping - use a top level method
print('''
###################
##   TEMP SORT   ##
###################
''')
guitar_brands = ['Fender', 'Charvel', 'Dean', 'Jackson', 'Gibson']
print('Before sorting: ', guitar_brands)
print('Temp sorting: ', sorted(guitar_brands))
print('After sorting: ', guitar_brands)
