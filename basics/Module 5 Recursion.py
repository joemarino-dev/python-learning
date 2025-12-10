# contrast iterative functions vs using recursion
# iterative
def get_factorial(number):
	factorial = 1
	for x in range(1, number + 1):
		factorial *= x
	return factorial
	
test1 = get_factorial(3)
print(test1)

test2 = get_factorial(6)
print(test2)

# recursion - but theres a problem here you would hit max recursion depth - need stop function
# def get_factorial_recursion(number):
	# return number * get_factorial_recursion(number - 1)

# now with stop function
def get_factorial_recursion(number):
	if number <= 1:
		return 1
	return number * get_factorial_recursion(number -1)

test1 = get_factorial_recursion(3)
print(test1)

test2 = get_factorial_recursion(6)
print(test2)


