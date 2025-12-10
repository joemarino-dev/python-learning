# top level has exception (which has many variationsunderneat), system exit, and keyboard interrupt

# system exit
import sys

name = input('Please enter your name: ')
if name == '':
	print('You didn\'t enter anything. Exiting.')
	sys.exit()
print('Hello', name, '!')

# keyboard interrupt is e.g., you create infinite loop and pressing the stop button to terminate

# exceptions: arithmetic error (many flavors), lookup error (index error, key error {dictionary}), type error, value error

