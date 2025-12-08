# many ways to create a tuple - parens optional but I think they are better for readability
# tuples (like strings, but unlike lists) are immutable - the object itself cannot be changed
empty_tuple = ()
tuple_a = (1, 2, 3)
tuple_b = 1, # note if you do it this way you must have trailing comma or Python won't know you are creating a tuple
tuple_c = 1, 2, 3
tuple_d = 1, 2, 3,

print(empty_tuple)
print(tuple_a)
print(tuple_b)
print(tuple_c)
print(tuple_d)

# this is ok
user_data = ('BBob', '123', '42')
print(user_data)
user_data = ('DDod', '789', '43')
print(user_data)

# but not this
# user_data.append('Test')

# you can do this
print(user_data[0])

# but not this
# user_data[0] = 'GGog'

# or this
# del user_data[0]

# but wondering if you can do this? You actually can
del user_data
# print(user_data)
