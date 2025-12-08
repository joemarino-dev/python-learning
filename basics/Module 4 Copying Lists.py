# First let's do a copy for basic string variables, this will also work for other basic data types; note that you can independently change each variable after the copy
name_original = 'Mantas'
name_new = name_original
print(name_original, name_new)
name_original = 'Death'
print(name_original, name_new)

# Now let's do with a list and note that since lists are just pointers after copying - you cannot independently change them - what happens in one is reflected in the other
numbers_original = [1, 2, 3]
numbers_new = numbers_original
numbers_original[0] = -5
print('Original List: ', numbers_original, '\nNew List: ', numbers_new)

# However, it is as simple as slicing which will force two independent list references in memory
numbers_original = [1, 2, 3]
numbers_new = numbers_original[:]
numbers_original[0] = -5
print('Original List: ', numbers_original, '\nNew List: ', numbers_new)

# Similarly, you can slice but only portion of list
numbers_original = [1, 2, 3]
numbers_new = numbers_original[:2]
numbers_original[0] = -5
print('Original List: ', numbers_original, '\nNew List: ', numbers_new)
