# functions can take parameters as defined in function definition which are then passed in as arguments when function is called
# compare the first block of code to the functional-ized version

sprint_velocity = [43, 25, 51, 32, 17]

sum = 0.0

for velocity in sprint_velocity:
	sum += velocity

velocity_avg = sum / len(sprint_velocity)

print(velocity_avg)

def average_velocity(sprint_velocity):
	sum = 0.0
	for velocity in sprint_velocity:
		sum += velocity
	velocity_avg = sum / len(sprint_velocity)
	print(velocity_avg)
	
average_velocity([43, 25, 51, 32, 17])

# now this won't work because you haven't supplied required arguments
# average_velocity()

# similarly, not matching the data type with your argument will fail
# average_velocity(5)
# average_velocity('fruit')

# arguments can be positional, i.e., order matters, e.g., arg 1 to param 1, arg 2 to param 2 or they can be keyword arguments in which case order does not matter

def letter_counter(phrase, letter):
	counter = 0
	for char in phrase:
		if char == letter:
			counter += 1
	print (letter, 'appears', counter, 'times in', phrase)
	
letter_counter('Welcome', 'e')
letter_counter('The quick brown fox jumped over the lazy dog, sir', 'r')

# swap arguments - won't work - no error but based on the code the results will be bad
letter_counter('e', 'Welcome')

# but this will work - keyword arguments
letter_counter(letter='e', phrase='Welcome')
	
