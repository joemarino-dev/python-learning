# finally the curtain drops on something I been wondering
# simple programs so far ask for input and just trust the user to follow the rules
# this is where exceptions come into play

try:
	value = int(input('Please enter a number: '))
	print('The inverse of', value, 'is', 1 / value)
except:
	print('You did not enter a number so I cannot compute.')
	
# this is great but even better is to tailor the graceful failure message for specific exception types
try:
	value = int(input('Please enter a number: '))
	print('The inverse of', value, 'is', 1 / value)
except ValueError:
	print('You did not enter a number so I cannot compute.')
except ZeroDivisionError:
	print('You entered 0 which is invalid for denominator.')

# lastly, you can finish with a general exception if anything else goes wrong
try:
	value = int(input('Please enter a number: '))
	print('The inverse of', value, 'is', 1 / value)
except ValueError:
	print('You did not enter a number so I cannot compute.')
except ZeroDivisionError:
	print('You entered 0 which is invalid for denominator.')
except:
	print('Something went wrong.')
