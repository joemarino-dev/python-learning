# up until now we been writing functions that print to console - this is not good practice
def get_average(input_numbers):
	sum = 0.0
	for number in input_numbers:
		sum += number
	average = sum / len(input_numbers)
	print(average)
	
# rather we should return values to the caller and it is very easy
def get_average(input_numbers):
	sum = 0.0
	for number in input_numbers:
		sum += number
	average = sum / len(input_numbers)
	return average
	
print('The average is:', get_average([12.2, 7.3, 6.54, 10.2]))
	
x = get_average([20, 30, 40, 50, 60])
if x > 30:
	print('The average is too high.')

# note that anything after the return gets ignored - function is immediately exited
def get_average(input_numbers):
	sum = 0.0
	for number in input_numbers:
		sum += number
	average = sum / len(input_numbers)
	return average
	print('Prove it!')

x = get_average([2, 3])
print(x)

# though you can wrap returns in "if" to get different outcomes
def first_last_compare(some_list):
	if some_list[0] == some_list[-1]:
		return True
	else: 
		return False
		
print(first_last_compare([1, 3, 5, 1]))
print(first_last_compare([1, 3, 5, 2]))

# this will fail if an empty list sent in
# print(first_last_compare([]))
# but you can use a simple return with nothing to handle this case

def first_last_compare(some_list):
	if len(some_list) == 0:
		return
	if some_list[0] == some_list[-1]:
		return True
	else: 
		return False
		
print(first_last_compare([1, 3, 5, 1]))
print(first_last_compare([1, 3, 5, 2]))
print(first_last_compare([]))
