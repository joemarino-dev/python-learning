age = int(input('What is your age: '))
fav_band = input('What is your favorite band: ')
if age > 45 and fav_band == 'Devin Townsend':
	print('Hey we have a lot in common!')
else: 
	print('We are pretty different.')
	
new_band = input('Name one of your top 3 bands: ')
if new_band == 'Devin Townsend' or new_band == 'Death' or new_band == 'Anthrax':
	print('Hey I love', new_band, 'too.')
else:
	print('I\'m not a huge fan of', new_band, '.')
	
another_band = input('Name your favorite band: ')
if not another_band == 'Devin Townsend':
	print('We don\'t currently have the same favorite band but mine always changes!')
else: 
	print('Hey that\'s my favorite band too!')
	
age = int(input('What\'s your age? '))
top_band = input('Name your favorite band: ')
if not age > 40 and top_band == 'Devin Townsend' or \
	age > 45 and top_band == 'Devin Townsend':
		print('Matches logic.')
else: 
		print('No match.')
		
# more readable
age = int(input('What\'s your age? '))
top_band = input('Name your favorite band: ')
if ((not age > 40) and top_band == 'Devin Townsend') or \
	(age > 45 and top_band == 'Devin Townsend'):
		print('Matches logic.')
else: 
		print('No match.')
