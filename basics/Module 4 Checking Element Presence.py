menu = ['Escargot', 'Calamari', 'Filet Mignon', 'Octopus']

selection = input('What would you like? ')
if selection in menu:
	print('Perfecto!')
else:
	print('We don\'t have that unfortunately.')

selection = input('What would you like? ')
if selection not in menu:
	print('We don\'t have that unfortunately.')
else:
	print('Perfecto!')
