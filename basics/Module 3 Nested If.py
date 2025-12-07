heavy_metal = input('Do you like heavy metal? y/n: ')
if heavy_metal == 'y':
	thrash_metal = input('How about thrash metal? y/n: ')
	if thrash_metal == 'y':
		print('You like heavy metal and thrash metal.')
	else: 
		print('You like heavy metal but not thrash metal.')
else:
		print('You don\'t like heavy metal. Too bad.')
