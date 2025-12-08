# strings can be treated much like list elements
fav_band = 'Devin Townsend'
print(fav_band[6])
print(fav_band[:5])

# with some exceptions
#fav_band[6] = 'Z'

# and there are a variety of functions
my_string = 'this should be all caps'
print(my_string.upper())
print(my_string) # note the above was not a permanent change
my_string_caps = my_string.upper() # but this will be
print(my_string_caps)


number = input('Enter your lucky number: ')
if number.isnumeric():
	print('Thanks. That\'s a number!')
else:
	print('Sorry but', number, 'is not a number...')
	
# islower checks if string has lower case only while isspace checks if string is only whitespace
