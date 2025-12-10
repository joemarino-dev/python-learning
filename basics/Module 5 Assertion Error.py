# assertions are not meant for error handling - you can turn them off when publishing to users
# they are good for debugging and/or documenting assumptions to other devs

def get_inverse(number):
	assert (number != 0), '0 is not allowed!'
	return 1 / number
	
print(get_inverse(1))
print(get_inverse(0))


