# functions typically cause some effect or returns a meaningful value or do both

my_string = 'Testing 123'

print(my_string) # causes an effect
print(len(my_string)) # returns a meaningful value
test = input('I do both! ') # does both!

# however, there is more going on with functions that don't return a meaningful value
print_return = print('Hello, world!')
print(print_return)

# you see that print is also returning a value of "None" - none is not true or false it is just null/nothing
x = None

if x:
	print('None is True.')
elif x is False:
	print('None is False.')
else:
	print('None is not True. None is not False. None is just None.')
	
x = None

if x is None:
	print('yes')
if x == None:
	print('also, yes')

# functions that we write that do not return a value will also automatically return None
def greet():
	print('something')
	
x = greet()
print(x)


