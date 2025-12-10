# generators are like stepping stones we can call in sequence for new values - python remembers prior return values
# to me this feels like pausing each iteration of the loop to grab something mid-flight
def get_number():
	for i in range(1, 4):
		yield i
		
generator = get_number()
print(next(generator))
print(next(generator))
print(next(generator)) # note if we do any more it will fail as generator function is finished

# python also allows you to run for loop against a generator which knows when to stop
for x in get_number():
	print(x)
	
# and yet another way to use a generator is to put values in a list using list function
numbers = list(get_number())
print(numbers)
