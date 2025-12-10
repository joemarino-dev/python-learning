# you can specify defaults for params and make them optional
def letter_counter(phrase='This is the default phrase to check', letter='a'):
	counter = 0
	for char in phrase:
		if char == letter:
			counter += 1
	print (letter, 'appears', counter, 'times in', phrase)
	
letter_counter()

letter_counter('How many letter a\'s are here?')

letter_counter(letter='e')

# but this one is no good because positional arguments CANNOT come after keyword
# letter_counter(phrase='New phrase', 'a')
